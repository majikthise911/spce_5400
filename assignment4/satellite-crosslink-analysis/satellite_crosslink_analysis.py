"""
Satellite Crosslink Trade Study: Optical vs. RF (Ka-band)
Following HYBRID_SATELLITE_TRADE_STUDY_PROMPT_AMENDED.md methodology
Modified from Laser_Link_Calculations_template.xlsx
"""

import numpy as np
import pandas as pd
from typing import Dict, Tuple
import os

# Physical constants
c = 2.998e8  # Speed of light (m/s)
h = 6.626e-34  # Planck's constant (J·s)
k_B = 1.38e-23  # Boltzmann's constant (J/K)

class OpticalLinkBudget:
    """Optical link budget calculator following Excel template methodology"""

    def __init__(self, range_m: float, bit_rate_bps: float):
        """Initialize with mission parameters"""
        self.range_m = range_m
        self.bit_rate_bps = bit_rate_bps

        # Template detector parameters
        self.Q_photoelectrons = 40  # photoelectrons/bit (from template)
        self.eta_quantum_eff = 0.3  # quantum efficiency (from template)
        self.wavelength_m = 1.55e-6  # 1550 nm (from template)

        # Template loss parameters
        self.L_pointing_dB = -3.0  # pointing error loss (from template)
        self.L_line_dB = -6.0  # line in/out losses (from template)
        self.L_atm_dB = 0.0  # atmospheric loss (vacuum)

        # Design parameters (to be optimized)
        self.P_tx_W = None
        self.D_tx_m = None
        self.D_rx_m = None

    def calculate_detector_requirements(self) -> Dict:
        """
        Step 1: Detector-first calculation (template methodology)
        Returns required power at receiver based on photoelectron requirements
        """
        # Template calculation flow
        n_photons_per_bit = self.Q_photoelectrons / self.eta_quantum_eff  # 133.33

        # Photon energy
        f_Hz = c / self.wavelength_m  # frequency
        E_photon_J = h * f_Hz  # energy per photon

        # Energy per bit
        J_per_bit = n_photons_per_bit * E_photon_J

        # Required power at receiver
        P_req_W = J_per_bit * self.bit_rate_bps
        P_req_dBW = 10 * np.log10(P_req_W)

        return {
            'Q_photoelectrons': self.Q_photoelectrons,
            'Q_dB': 10 * np.log10(self.Q_photoelectrons),
            'eta_quantum_eff': self.eta_quantum_eff,
            'eta_dB': 10 * np.log10(self.eta_quantum_eff),
            'n_photons_per_bit': n_photons_per_bit,
            'n_dB': 10 * np.log10(n_photons_per_bit),
            'wavelength_m': self.wavelength_m,
            'wavelength_um': self.wavelength_m * 1e6,
            'frequency_Hz': f_Hz,
            'E_photon_J': E_photon_J,
            'E_photon_dB': 10 * np.log10(E_photon_J),
            'J_per_bit': J_per_bit,
            'J_per_bit_dB': 10 * np.log10(J_per_bit),
            'bit_rate_bps': self.bit_rate_bps,
            'P_req_W': P_req_W,
            'P_req_dBW': P_req_dBW
        }

    def calculate_link_budget(self, P_tx_W: float, D_tx_m: float, D_rx_m: float) -> Dict:
        """
        Step 2: Link budget calculation using template formulas
        """
        self.P_tx_W = P_tx_W
        self.D_tx_m = D_tx_m
        self.D_rx_m = D_rx_m

        # Free space loss (template formula)
        L_fs = (self.wavelength_m / (4 * np.pi * self.range_m))**2
        L_fs_dB = 10 * np.log10(L_fs)

        # Gains using template formula: G = (π×D/λ)²
        G_tx = (np.pi * D_tx_m / self.wavelength_m)**2
        G_tx_dBi = 10 * np.log10(G_tx)

        G_rx = (np.pi * D_rx_m / self.wavelength_m)**2
        G_rx_dBi = 10 * np.log10(G_rx)

        # Received power (template methodology)
        P_rx_W = (P_tx_W * L_fs * G_tx * G_rx *
                  10**(self.L_pointing_dB/10) * 10**(self.L_line_dB/10) *
                  10**(self.L_atm_dB/10))
        P_rx_dBW = 10 * np.log10(P_rx_W)

        # Get detector requirements
        detector = self.calculate_detector_requirements()

        # Margin
        margin_dB = P_rx_dBW - detector['P_req_dBW']

        # Beam divergence (calculate for reference)
        theta_div_rad = 1.22 * self.wavelength_m / D_tx_m
        theta_div_urad = theta_div_rad * 1e6

        # Spot size at range
        spot_diameter_m = theta_div_rad * self.range_m

        return {
            'P_tx_W': P_tx_W,
            'P_tx_dBW': 10 * np.log10(P_tx_W),
            'range_m': self.range_m,
            'range_km': self.range_m / 1000,
            'L_fs': L_fs,
            'L_fs_dB': L_fs_dB,
            'D_tx_m': D_tx_m,
            'D_tx_cm': D_tx_m * 100,
            'D_rx_m': D_rx_m,
            'D_rx_cm': D_rx_m * 100,
            'G_tx': G_tx,
            'G_tx_dBi': G_tx_dBi,
            'G_rx': G_rx,
            'G_rx_dBi': G_rx_dBi,
            'L_pointing_dB': self.L_pointing_dB,
            'L_line_dB': self.L_line_dB,
            'L_atm_dB': self.L_atm_dB,
            'P_rx_W': P_rx_W,
            'P_rx_dBW': P_rx_dBW,
            'P_req_W': detector['P_req_W'],
            'P_req_dBW': detector['P_req_dBW'],
            'margin_dB': margin_dB,
            'theta_div_rad': theta_div_rad,
            'theta_div_urad': theta_div_urad,
            'spot_diameter_m': spot_diameter_m,
            'detector': detector
        }

    def optimize_design(self, target_margin_dB: float = 3.0,
                       max_power_W: float = 5.0,
                       max_aperture_m: float = 0.2) -> Dict:
        """
        Optimize aperture sizes and power to achieve target margin
        """
        detector = self.calculate_detector_requirements()
        P_req_W = detector['P_req_W']

        # Start with conservative initial guess
        D_tx = 0.1  # 10 cm
        D_rx = 0.1  # 10 cm
        P_tx = 1.0  # 1 W

        # Iteratively adjust to hit target margin
        for iteration in range(20):
            result = self.calculate_link_budget(P_tx, D_tx, D_rx)
            current_margin = result['margin_dB']

            if abs(current_margin - target_margin_dB) < 0.1:
                break

            # Adjust parameters
            if current_margin < target_margin_dB:
                # Need more link budget - increase apertures first, then power
                if D_tx < max_aperture_m:
                    D_tx *= 1.1
                    D_rx *= 1.1
                elif P_tx < max_power_W:
                    P_tx *= 1.2
                else:
                    break  # Can't meet target
            else:
                # Have excess margin - can reduce size/power
                if P_tx > 0.1:
                    P_tx *= 0.9
                elif D_tx > 0.05:
                    D_tx *= 0.95
                    D_rx *= 0.95

        return self.calculate_link_budget(P_tx, D_tx, D_rx)


class RFLinkBudget:
    """RF Ka-band link budget calculator with analogous structure to optical"""

    def __init__(self, range_m: float, bit_rate_bps: float):
        """Initialize with mission parameters"""
        self.range_m = range_m
        self.bit_rate_bps = bit_rate_bps

        # RF parameters
        self.f_Hz = 32e9  # 32 GHz Ka-band
        self.wavelength_m = c / self.f_Hz  # ~9.37 mm

        # Antenna efficiency (includes losses)
        self.eta_ant = 0.6

        # System noise temperature
        self.T_sys_K = 650  # typical Ka-band

        # Required Eb/N0 for BER 10^-9 with coding
        self.Eb_N0_req_dB = 9.6

        # Loss parameters
        self.L_pointing_dB = -1.0  # RF has wider beamwidth
        self.L_feed_dB = -1.0  # feed losses
        self.L_misc_dB = -2.0  # miscellaneous
        self.L_atm_dB = 0.0  # vacuum

    def calculate_receiver_requirements(self) -> Dict:
        """
        Calculate required C/N0 based on data rate and Eb/N0
        """
        # Required Eb/N0 in linear
        Eb_N0_req = 10**(self.Eb_N0_req_dB / 10)

        # Required C/N0
        C_N0_req_dBHz = self.Eb_N0_req_dB + 10 * np.log10(self.bit_rate_bps)
        C_N0_req_Hz = 10**(C_N0_req_dBHz / 10)

        # Required received power
        N0 = k_B * self.T_sys_K
        N0_dBW_Hz = 10 * np.log10(N0)

        P_req_dBW = C_N0_req_dBHz + N0_dBW_Hz
        P_req_W = 10**(P_req_dBW / 10)

        return {
            'T_sys_K': self.T_sys_K,
            'Eb_N0_req_dB': self.Eb_N0_req_dB,
            'bit_rate_bps': self.bit_rate_bps,
            'C_N0_req_dBHz': C_N0_req_dBHz,
            'N0': N0,
            'N0_dBW_Hz': N0_dBW_Hz,
            'P_req_W': P_req_W,
            'P_req_dBW': P_req_dBW
        }

    def calculate_link_budget(self, P_tx_W: float, D_tx_m: float, D_rx_m: float) -> Dict:
        """
        RF link budget calculation
        """
        # Antenna gains (with efficiency)
        G_tx = self.eta_ant * (np.pi * D_tx_m / self.wavelength_m)**2
        G_tx_dBi = 10 * np.log10(G_tx)

        G_rx = self.eta_ant * (np.pi * D_rx_m / self.wavelength_m)**2
        G_rx_dBi = 10 * np.log10(G_rx)

        # EIRP
        EIRP_dBW = 10 * np.log10(P_tx_W) + G_tx_dBi

        # Free space path loss
        FSPL_dB = 20 * np.log10(4 * np.pi * self.range_m / self.wavelength_m)

        # Received power
        P_rx_dBW = (10 * np.log10(P_tx_W) + G_tx_dBi - FSPL_dB + G_rx_dBi +
                    self.L_pointing_dB + self.L_feed_dB + self.L_misc_dB + self.L_atm_dB)
        P_rx_W = 10**(P_rx_dBW / 10)

        # C/N0
        N0 = k_B * self.T_sys_K
        C_N0_dBHz = P_rx_dBW - 10 * np.log10(N0)

        # Margin
        rx_req = self.calculate_receiver_requirements()
        margin_dB = C_N0_dBHz - rx_req['C_N0_req_dBHz']

        # Beamwidth (3dB)
        theta_3dB_rad = 1.22 * self.wavelength_m / D_tx_m
        theta_3dB_deg = np.degrees(theta_3dB_rad)

        # G/T figure of merit
        G_over_T_dB_K = G_rx_dBi - 10 * np.log10(self.T_sys_K)

        return {
            'P_tx_W': P_tx_W,
            'P_tx_dBW': 10 * np.log10(P_tx_W),
            'frequency_GHz': self.f_Hz / 1e9,
            'wavelength_m': self.wavelength_m,
            'wavelength_mm': self.wavelength_m * 1000,
            'range_m': self.range_m,
            'range_km': self.range_m / 1000,
            'D_tx_m': D_tx_m,
            'D_tx_cm': D_tx_m * 100,
            'D_rx_m': D_rx_m,
            'D_rx_cm': D_rx_m * 100,
            'eta_ant': self.eta_ant,
            'G_tx': G_tx,
            'G_tx_dBi': G_tx_dBi,
            'G_rx': G_rx,
            'G_rx_dBi': G_rx_dBi,
            'EIRP_dBW': EIRP_dBW,
            'FSPL_dB': FSPL_dB,
            'L_pointing_dB': self.L_pointing_dB,
            'L_feed_dB': self.L_feed_dB,
            'L_misc_dB': self.L_misc_dB,
            'L_atm_dB': self.L_atm_dB,
            'P_rx_W': P_rx_W,
            'P_rx_dBW': P_rx_dBW,
            'T_sys_K': self.T_sys_K,
            'G_over_T_dB_K': G_over_T_dB_K,
            'C_N0_dBHz': C_N0_dBHz,
            'C_N0_req_dBHz': rx_req['C_N0_req_dBHz'],
            'margin_dB': margin_dB,
            'theta_3dB_rad': theta_3dB_rad,
            'theta_3dB_deg': theta_3dB_deg,
            'receiver': rx_req
        }

    def optimize_design(self, target_margin_dB: float = 3.0,
                       max_power_W: float = 20.0,
                       max_aperture_m: float = 0.5) -> Dict:
        """
        Optimize antenna sizes and power to achieve target margin
        """
        # Start with initial guess
        D_tx = 0.3  # 30 cm
        D_rx = 0.3  # 30 cm
        P_tx = 10.0  # 10 W

        # Iteratively adjust
        for iteration in range(20):
            result = self.calculate_link_budget(P_tx, D_tx, D_rx)
            current_margin = result['margin_dB']

            if abs(current_margin - target_margin_dB) < 0.1:
                break

            if current_margin < target_margin_dB:
                # Need more link budget
                if D_tx < max_aperture_m:
                    D_tx *= 1.1
                    D_rx *= 1.1
                elif P_tx < max_power_W:
                    P_tx *= 1.2
                else:
                    break
            else:
                # Have excess margin
                if P_tx > 1.0:
                    P_tx *= 0.9
                elif D_tx > 0.1:
                    D_tx *= 0.95
                    D_rx *= 0.95

        return self.calculate_link_budget(P_tx, D_tx, D_rx)


def perform_sensitivity_analysis():
    """
    Perform sensitivity analysis for both technologies
    """
    print("\n" + "="*80)
    print("PHASE 4: SENSITIVITY ANALYSIS")
    print("="*80)

    # Baseline parameters
    range_baseline = 250e3  # 250 km
    bit_rate_baseline = 1e9  # 1 Gbps

    # Initialize calculators
    optical = OpticalLinkBudget(range_baseline, bit_rate_baseline)
    rf = RFLinkBudget(range_baseline, bit_rate_baseline)

    # Get baseline designs
    optical_baseline = optical.optimize_design(target_margin_dB=3.0)
    rf_baseline = rf.optimize_design(target_margin_dB=3.0)

    print(f"\nOptical Baseline: Margin = {optical_baseline['margin_dB']:.2f} dB")
    print(f"  Tx/Rx Apertures: {optical_baseline['D_tx_cm']:.1f}/{optical_baseline['D_rx_cm']:.1f} cm")
    print(f"  Tx Power: {optical_baseline['P_tx_W']:.3f} W")

    print(f"\nRF Baseline: Margin = {rf_baseline['margin_dB']:.2f} dB")
    print(f"  Tx/Rx Antennas: {rf_baseline['D_tx_cm']:.1f}/{rf_baseline['D_rx_cm']:.1f} cm")
    print(f"  Tx Power: {rf_baseline['P_tx_W']:.1f} W")

    # Sensitivity sweeps
    sensitivities = {
        'optical': {},
        'rf': {}
    }

    # Range sensitivity (150, 250, 500 km)
    ranges_km = [150, 250, 500]
    optical_margins_range = []
    rf_margins_range = []

    for R_km in ranges_km:
        R_m = R_km * 1000

        # Optical
        opt_temp = OpticalLinkBudget(R_m, bit_rate_baseline)
        opt_result = opt_temp.calculate_link_budget(
            optical_baseline['P_tx_W'],
            optical_baseline['D_tx_m'],
            optical_baseline['D_rx_m']
        )
        optical_margins_range.append(opt_result['margin_dB'])

        # RF
        rf_temp = RFLinkBudget(R_m, bit_rate_baseline)
        rf_result = rf_temp.calculate_link_budget(
            rf_baseline['P_tx_W'],
            rf_baseline['D_tx_m'],
            rf_baseline['D_rx_m']
        )
        rf_margins_range.append(rf_result['margin_dB'])

    sensitivities['optical']['range'] = {'ranges_km': ranges_km, 'margins_dB': optical_margins_range}
    sensitivities['rf']['range'] = {'ranges_km': ranges_km, 'margins_dB': rf_margins_range}

    # Data rate sensitivity (0.5, 1, 2, 5 Gbps)
    data_rates_Gbps = [0.5, 1, 2, 5]
    optical_margins_rate = []
    rf_margins_rate = []

    for rate_Gbps in data_rates_Gbps:
        rate_bps = rate_Gbps * 1e9

        # Optical
        opt_temp = OpticalLinkBudget(range_baseline, rate_bps)
        opt_result = opt_temp.calculate_link_budget(
            optical_baseline['P_tx_W'],
            optical_baseline['D_tx_m'],
            optical_baseline['D_rx_m']
        )
        optical_margins_rate.append(opt_result['margin_dB'])

        # RF
        rf_temp = RFLinkBudget(range_baseline, rate_bps)
        rf_result = rf_temp.calculate_link_budget(
            rf_baseline['P_tx_W'],
            rf_baseline['D_tx_m'],
            rf_baseline['D_rx_m']
        )
        rf_margins_rate.append(rf_result['margin_dB'])

    sensitivities['optical']['data_rate'] = {'rates_Gbps': data_rates_Gbps, 'margins_dB': optical_margins_rate}
    sensitivities['rf']['data_rate'] = {'rates_Gbps': data_rates_Gbps, 'margins_dB': rf_margins_rate}

    return sensitivities, optical_baseline, rf_baseline


def generate_comparison_table(optical_result: Dict, rf_result: Dict) -> pd.DataFrame:
    """
    Generate side-by-side comparison table
    """
    comparison_data = {
        'Parameter': [
            'Transmit Power (W)',
            'Transmit Power (dBW)',
            'Tx Aperture/Antenna (cm)',
            'Rx Aperture/Antenna (cm)',
            'Tx Gain (dBi)',
            'Rx Gain (dBi)',
            'Frequency/Wavelength',
            'Range (km)',
            'Free Space Loss (dB)',
            'Pointing Loss (dB)',
            'Other Losses (dB)',
            'Received Power (dBW)',
            'Required Power (dBW)',
            'Link Margin (dB)',
            'Pointing Accuracy Required',
            'Beamwidth/Divergence'
        ],
        'Optical': [
            f"{optical_result['P_tx_W']:.3f}",
            f"{optical_result['P_tx_dBW']:.1f}",
            f"{optical_result['D_tx_cm']:.1f}",
            f"{optical_result['D_rx_cm']:.1f}",
            f"{optical_result['G_tx_dBi']:.1f}",
            f"{optical_result['G_rx_dBi']:.1f}",
            f"193.5 THz / 1.55 um",
            f"{optical_result['range_km']:.0f}",
            f"{optical_result['L_fs_dB']:.1f}",
            f"{optical_result['L_pointing_dB']:.1f}",
            f"{optical_result['L_line_dB']:.1f}",
            f"{optical_result['P_rx_dBW']:.1f}",
            f"{optical_result['P_req_dBW']:.1f}",
            f"{optical_result['margin_dB']:.2f}",
            f"{optical_result['theta_div_urad']:.1f} urad",
            f"{optical_result['theta_div_urad']:.1f} urad"
        ],
        'RF (Ka-band)': [
            f"{rf_result['P_tx_W']:.1f}",
            f"{rf_result['P_tx_dBW']:.1f}",
            f"{rf_result['D_tx_cm']:.1f}",
            f"{rf_result['D_rx_cm']:.1f}",
            f"{rf_result['G_tx_dBi']:.1f}",
            f"{rf_result['G_rx_dBi']:.1f}",
            f"32 GHz / 9.37 mm",
            f"{rf_result['range_km']:.0f}",
            f"-{rf_result['FSPL_dB']:.1f}",
            f"{rf_result['L_pointing_dB']:.1f}",
            f"{rf_result['L_feed_dB'] + rf_result['L_misc_dB']:.1f}",
            f"{rf_result['P_rx_dBW']:.1f}",
            f"{rf_result['receiver']['P_req_dBW']:.1f}",
            f"{rf_result['margin_dB']:.2f}",
            f"{rf_result['theta_3dB_deg']:.3f} deg",
            f"{rf_result['theta_3dB_deg']:.3f} deg"
        ]
    }

    return pd.DataFrame(comparison_data)


def main():
    """
    Main execution function
    """
    print("="*80)
    print("SATELLITE CROSSLINK TRADE STUDY: OPTICAL vs. RF (Ka-band)")
    print("="*80)
    print("\nMission Parameters:")
    print("  - Altitude: 500 km LEO")
    print("  - Inter-satellite separation: 250 km")
    print("  - Required data rate: 1 Gbps")
    print("  - Platform: Small satellites")
    print()

    # Create output directory
    output_dir = 'outputs'
    os.makedirs(output_dir, exist_ok=True)

    # PHASE 2: Optical Link Budget
    print("\n" + "="*80)
    print("PHASE 2: OPTICAL LINK BUDGET (Following Template Methodology)")
    print("="*80)

    range_m = 250e3  # 250 km (modified from 1000 km template)
    bit_rate_bps = 1e9  # 1 Gbps (modified from 10 Gbps template)

    optical = OpticalLinkBudget(range_m, bit_rate_bps)

    # Calculate detector requirements
    detector = optical.calculate_detector_requirements()
    print("\nDetector Requirements (Template Methodology):")
    print(f"  Q (photoelectrons/bit): {detector['Q_photoelectrons']} ({detector['Q_dB']:.2f} dB)")
    print(f"  eta (quantum efficiency): {detector['eta_quantum_eff']} ({detector['eta_dB']:.2f} dB)")
    print(f"  n (photons/bit): {detector['n_photons_per_bit']:.2f} ({detector['n_dB']:.2f} dB)")
    print(f"  Wavelength: {detector['wavelength_um']:.2f} um")
    print(f"  Frequency: {detector['frequency_Hz']:.3e} Hz")
    print(f"  Photon energy (h*nu): {detector['E_photon_J']:.3e} J ({detector['E_photon_dB']:.2f} dB)")
    print(f"  Energy per bit: {detector['J_per_bit']:.3e} J ({detector['J_per_bit_dB']:.2f} dB)")
    print(f"  Required power at receiver: {detector['P_req_W']:.3e} W ({detector['P_req_dBW']:.2f} dBW)")

    # Optimize design
    print("\nOptimizing optical link design for 3 dB margin...")
    optical_result = optical.optimize_design(target_margin_dB=3.0)

    print(f"\nOptimized Optical Link Budget:")
    print(f"  Tx Power: {optical_result['P_tx_W']:.3f} W ({optical_result['P_tx_dBW']:.1f} dBW)")
    print(f"  Tx Aperture: {optical_result['D_tx_cm']:.1f} cm")
    print(f"  Rx Aperture: {optical_result['D_rx_cm']:.1f} cm")
    print(f"  Tx Gain: {optical_result['G_tx_dBi']:.1f} dBi")
    print(f"  Rx Gain: {optical_result['G_rx_dBi']:.1f} dBi")
    print(f"  Free Space Loss: {optical_result['L_fs_dB']:.1f} dB")
    print(f"  Pointing Loss: {optical_result['L_pointing_dB']:.1f} dB")
    print(f"  Line Losses: {optical_result['L_line_dB']:.1f} dB")
    print(f"  Received Power: {optical_result['P_rx_dBW']:.1f} dBW")
    print(f"  Required Power: {optical_result['P_req_dBW']:.1f} dBW")
    print(f"  LINK MARGIN: {optical_result['margin_dB']:.2f} dB")
    print(f"  Beam Divergence: {optical_result['theta_div_urad']:.1f} urad")
    print(f"  Spot Diameter at Range: {optical_result['spot_diameter_m']:.2f} m")

    # PHASE 3: RF Link Budget
    print("\n" + "="*80)
    print("PHASE 3: RF (Ka-BAND) LINK BUDGET (Analogous Structure)")
    print("="*80)

    rf = RFLinkBudget(range_m, bit_rate_bps)

    # Calculate receiver requirements
    rx_req = rf.calculate_receiver_requirements()
    print("\nReceiver Requirements:")
    print(f"  System Noise Temperature: {rx_req['T_sys_K']} K")
    print(f"  Required Eb/N0: {rx_req['Eb_N0_req_dB']} dB")
    print(f"  Bit Rate: {rx_req['bit_rate_bps']:.3e} bps")
    print(f"  Required C/N0: {rx_req['C_N0_req_dBHz']:.1f} dB-Hz")
    print(f"  Noise Spectral Density (N0): {rx_req['N0_dBW_Hz']:.1f} dBW/Hz")
    print(f"  Required power at receiver: {rx_req['P_req_W']:.3e} W ({rx_req['P_req_dBW']:.1f} dBW)")

    # Optimize design
    print("\nOptimizing RF link design for 3 dB margin...")
    rf_result = rf.optimize_design(target_margin_dB=3.0)

    print(f"\nOptimized RF Link Budget:")
    print(f"  Tx Power: {rf_result['P_tx_W']:.1f} W ({rf_result['P_tx_dBW']:.1f} dBW)")
    print(f"  Tx Antenna Diameter: {rf_result['D_tx_cm']:.1f} cm")
    print(f"  Rx Antenna Diameter: {rf_result['D_rx_cm']:.1f} cm")
    print(f"  Antenna Efficiency: {rf_result['eta_ant']}")
    print(f"  Tx Gain: {rf_result['G_tx_dBi']:.1f} dBi")
    print(f"  Rx Gain: {rf_result['G_rx_dBi']:.1f} dBi")
    print(f"  EIRP: {rf_result['EIRP_dBW']:.1f} dBW")
    print(f"  Free Space Path Loss: {rf_result['FSPL_dB']:.1f} dB")
    print(f"  Total Losses: {rf_result['L_pointing_dB'] + rf_result['L_feed_dB'] + rf_result['L_misc_dB']:.1f} dB")
    print(f"  G/T: {rf_result['G_over_T_dB_K']:.1f} dB/K")
    print(f"  C/N0: {rf_result['C_N0_dBHz']:.1f} dB-Hz")
    print(f"  Required C/N0: {rf_result['C_N0_req_dBHz']:.1f} dB-Hz")
    print(f"  LINK MARGIN: {rf_result['margin_dB']:.2f} dB")
    print(f"  3dB Beamwidth: {rf_result['theta_3dB_deg']:.3f} deg")

    # Generate comparison table
    print("\n" + "="*80)
    print("SIDE-BY-SIDE COMPARISON")
    print("="*80)
    comparison_df = generate_comparison_table(optical_result, rf_result)
    print("\n", comparison_df.to_string(index=False))

    # Save comparison to CSV
    comparison_df.to_csv(f'{output_dir}/Comparison_Table.csv', index=False)
    print(f"\n[OK] Saved comparison table to {output_dir}/Comparison_Table.csv")

    # PHASE 4: Sensitivity Analysis
    sensitivities, opt_base, rf_base = perform_sensitivity_analysis()

    # Save sensitivity data
    sens_df = pd.DataFrame({
        'Range_km': sensitivities['optical']['range']['ranges_km'],
        'Optical_Margin_dB': sensitivities['optical']['range']['margins_dB'],
        'RF_Margin_dB': sensitivities['rf']['range']['margins_dB']
    })
    sens_df.to_csv(f'{output_dir}/Sensitivity_Range.csv', index=False)

    sens_rate_df = pd.DataFrame({
        'DataRate_Gbps': sensitivities['optical']['data_rate']['rates_Gbps'],
        'Optical_Margin_dB': sensitivities['optical']['data_rate']['margins_dB'],
        'RF_Margin_dB': sensitivities['rf']['data_rate']['margins_dB']
    })
    sens_rate_df.to_csv(f'{output_dir}/Sensitivity_DataRate.csv', index=False)

    print(f"\n[OK] Saved sensitivity analysis to {output_dir}/Sensitivity_*.csv")

    # Save detailed link budgets
    optical_budget_df = pd.DataFrame([optical_result])
    optical_budget_df.to_csv(f'{output_dir}/Optical_Link_Budget.csv', index=False)

    rf_budget_df = pd.DataFrame([rf_result])
    rf_budget_df.to_csv(f'{output_dir}/RF_Link_Budget.csv', index=False)

    print(f"[OK] Saved optical link budget to {output_dir}/Optical_Link_Budget.csv")
    print(f"[OK] Saved RF link budget to {output_dir}/RF_Link_Budget.csv")

    print("\n" + "="*80)
    print("ANALYSIS COMPLETE")
    print("="*80)
    print("\nNext: Generate comprehensive trade study report with all sections")

    return optical_result, rf_result, sensitivities


if __name__ == "__main__":
    optical_result, rf_result, sensitivities = main()
