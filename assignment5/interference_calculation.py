#!/usr/bin/env python3
"""
Intermodulation Interference Analysis 
Following Figure 9.11 flowchart from textbook



Author: Jordan Clayton 
Date: December 8, 2025
"""

import numpy as np
import matplotlib.pyplot as plt
import os

print("="*80)
print("INTERMODULATION INTERFERENCE ANALYSIS")
print("Following Figure 9.11 Flowchart")
print("="*80)

# ==============================================================================
# INPUT PARAMETERS
# ==============================================================================
print("\nINPUT PARAMETERS:")
print("-" * 80)

f_x = 1598e6  # Hz; external intruder/disturbance frequency
f_t = 1500e6  # Hz; uplink transmit frequency
f_r = 1540e6  # Hz; downlink receive frequency
B = 100e3     # Hz; IF bandwidth (narrow channel)
f_IF = 140e6  # Hz; standard intermediate frequency

print(f"f_x (intruder)     = {f_x/1e6:.0f} MHz")
print(f"f_t (transmit)     = {f_t/1e6:.0f} MHz")
print(f"f_r (receive)      = {f_r/1e6:.0f} MHz")
print(f"f_IF (target)      = {f_IF/1e6:.0f} MHz")
print(f"B (IF bandwidth)   = {B/1e3:.0f} kHz")

# ==============================================================================
# CALCULATIONS
# ==============================================================================
print("\nCALCULATIONS:")
print("-" * 80)

# IF passband limits
delta_f = B / 2
IF_lower = f_IF - delta_f
IF_upper = f_IF + delta_f
print(f"IF passband        = [{IF_lower/1e6:.4f}, {IF_upper/1e6:.4f}] MHz")

# Third-order IM products
f1 = 2 * f_x - f_t
f2 = 2 * f_r - f_x
print(f"f1 (IM product)    = 2*{f_x/1e6:.0f} - {f_t/1e6:.0f} = {f1/1e6:.0f} MHz")
print(f"f2 (IM product)    = 2*{f_r/1e6:.0f} - {f_x/1e6:.0f} = {f2/1e6:.0f} MHz")

# Local oscillator frequency
f_LO = f2 - f_IF
print(f"f_LO (heterodyne)  = {f_LO/1e6:.0f} MHz")

# Downconvert to IF
f1_IF = np.abs(f1 - f_LO)
f2_IF = np.abs(f2 - f_LO)
print(f"f1_IF              = {f1_IF/1e6:.3f} MHz")
print(f"f2_IF              = {f2_IF/1e6:.3f} MHz")

# In-band checks
in_band_f1 = (IF_lower <= f1_IF <= IF_upper)
in_band_f2 = (IF_lower <= f2_IF <= IF_upper)
print(f"f1 in-band?        = {in_band_f1}")
print(f"f2 in-band?        = {in_band_f2}")

# ==============================================================================
# SIGNAL-TO-NOISE ANALYSIS
# ==============================================================================
print("\nSIGNAL-TO-NOISE ANALYSIS:")
print("-" * 80)

S_fIF_dBm = -2  # dBm
k_T_dBm_Hz = -174  # dBm/Hz
NF_dB = 3
N_thermal_dBm = k_T_dBm_Hz + 10 * np.log10(B) + NF_dB

print(f"S(f_IF)            = {S_fIF_dBm} dBm")
print(f"N_thermal          = {N_thermal_dBm:.1f} dBm")

if in_band_f1 or in_band_f2:
    IM_suppression_dB = 25
    N_IM_dBm = S_fIF_dBm - IM_suppression_dB
    N_thermal_linear = 10**(N_thermal_dBm/10)
    N_IM_linear = 10**(N_IM_dBm/10)
    N_total_linear = N_thermal_linear + N_IM_linear
    N_fIF_dBm = 10 * np.log10(N_total_linear)
    print(f"N_IM               = {N_IM_dBm} dBm")
    print(f"N_total            = {N_fIF_dBm:.1f} dBm")
else:
    N_fIF_dBm = N_thermal_dBm
    print(f"N_total            = {N_fIF_dBm:.1f} dBm (no IM interference)")

S_minus_N_dB = S_fIF_dBm - N_fIF_dBm
print(f"S/N                = {S_minus_N_dB:.1f} dB")

# ==============================================================================
# VERDICT
# ==============================================================================
print("\nVERDICT:")
print("-" * 80)

threshold_dB = 20
disturbance = S_minus_N_dB < threshold_dB

print(f"S/N threshold      = {threshold_dB} dB")
print(f"Actual S/N         = {S_minus_N_dB:.1f} dB")

if disturbance:
    print(f"Status             = DISTURBANCE DETECTED")
else:
    print(f"Status             = UNDISTURBED")

# ==============================================================================
# VISUALIZATION
# ==============================================================================
print("\n" + "="*80)
print("Generating frequency spectrum plot...")
print("="*80)

fig, ax = plt.subplots(figsize=(12, 6))

# Plot input frequencies
ax.stem([f_t/1e6, f_r/1e6, f_x/1e6], [5, 5, 3],
        linefmt='b-', markerfmt='bo', basefmt=' ', label='Input Frequencies')

# Plot IM products
ax.stem([f1/1e6, f2/1e6], [-10, -10],
        linefmt='r-', markerfmt='r^', basefmt=' ', label='IM Products')

# Plot LO and IF
ax.stem([f_LO/1e6], [10], linefmt='g-', markerfmt='gs', basefmt=' ', label='Local Oscillator')
ax.axvspan(IF_lower/1e6, IF_upper/1e6, alpha=0.3, color='yellow', label='IF Passband')

# Add labels
ax.text(f_t/1e6, 5.5, 'f_t', ha='center', fontsize=10, fontweight='bold')
ax.text(f_r/1e6, 5.5, 'f_r', ha='center', fontsize=10, fontweight='bold')
ax.text(f_x/1e6, 3.5, 'f_x', ha='center', fontsize=10, fontweight='bold')
ax.text(f1/1e6, -9, 'f1 (IM)', ha='center', fontsize=9, color='red')
ax.text(f2/1e6, -9, 'f2 (IM)', ha='center', fontsize=9, color='red')
ax.text(f_LO/1e6, 11, 'f_LO', ha='center', fontsize=10, fontweight='bold')

ax.set_xlabel('Frequency (MHz)', fontsize=12, fontweight='bold')
ax.set_ylabel('Relative Power (dBm)', fontsize=12, fontweight='bold')
ax.set_title('Intermodulation Interference - Frequency Spectrum', fontsize=14, fontweight='bold')
ax.legend(loc='upper right', fontsize=10)
ax.grid(True, alpha=0.3)
ax.set_xlim(100, 1700)

plt.tight_layout()
output_filename = 'intermod_spectrum.png'
plt.savefig(output_filename, dpi=150, bbox_inches='tight')
print(f"Plot saved: {output_filename}")
print("="*80)