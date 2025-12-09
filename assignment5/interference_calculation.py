import numpy as np

# Step 1 (Box [2]): Input Parameters (from Fig. 9.11 top box; book example scaled to L-band)
f_x = 1598e6  # Hz; external intruder (e.g., nearby tx)
f_t = 1500e6  # Hz; uplink transmit freq
f_r = 1540e6  # Hz; downlink receive freq
B = 100e3     # Hz; downlink bandwidth (narrow for IF example)
f_IF = 140e6  # Hz; fixed intermediate frequency (Box [3])

# Step 2 (Box [5]): Compute Δf (after f_IF; half-bandwidth for edges)
delta_f = B / 2  # Hz; e.g., 50 kHz, so IF band = 139.95–140.05 MHz (Eq. 9.13)

# Step 3 (Box [4]): Compute f_LO (downconversion mixer; book example LO for disturbance)
f_LO = 237e6  # Hz; per p. 365: 237 MHz offset for mirroring into IF (adjusted for demo)

# Step 4 (Box [6]): First IM Product f1 = 2*f_x - f_t (3rd-order mix; parallel path 1)
f1 = 2 * f_x - f_t  # Hz; e.g., ~1696 MHz ghost

# Step 5 (Boxes [7]/[9]): Downconvert f1 to IF and check band (decision diamonds: upper/lower bounds)
f1_IF = np.abs(f1 - f_LO)  # Hz; shifted to IF frame
in_band_f1_upper = (f1_IF <= f_IF + delta_f)  # Upper: <= 140.05 MHz (Box [7])
in_band_f1_lower = (f1_IF >= f_IF - delta_f)  # Lower: >= 139.95 MHz (Box [9])
in_band_f1 = in_band_f1_upper and in_band_f1_lower  # Both true for full in-band (to [10])

# Step 6 (Box [11]): Second IM Product f2 = 2*f_r - f_x (symmetric mix; parallel path 2)
f2 = 2 * f_r - f_x  # Hz; e.g., ~1680 MHz ghost (adjusted for demo)

# Step 7 (Boxes [12]/[14]): Downconvert f2 to IF and check band (symmetric decisions)
f2_IF = np.abs(f2 - f_LO)  # Hz
in_band_f2_upper = (f2_IF <= f_IF + delta_f)  # Box [12]
in_band_f2_lower = (f2_IF >= f_IF - delta_f)  # Box [14]
in_band_f2 = in_band_f2_upper and in_band_f2_lower  # to [15]

# Step 8 (Box [16]): If either in-band, compute powers at IF (merge to S/N box)
S_fIF_dBm = -10  # dBm; desired signal power at IF (defined outside for prints)
N_thermal_dBm = -174 + 10 * np.log10(B) + 10  # dBm; kTB noise + NF=10 dB
N_IM_dBm = -8 if in_band_f1 or in_band_f2 else -np.inf  # dBm; ghost adds ~ -8 dBm (strong for demo)
N_fIF_dBm = 10 * np.log10(10**(N_thermal_dBm/10) + 10**(N_IM_dBm/10))  # dBm; total noise
S_minus_N_dB = S_fIF_dBm - N_fIF_dBm  # dB

# Step 9 (Box [17]): Final Threshold (decision diamond; >20 dB safe)
disturbance = S_minus_N_dB < 20  # Boolean; why: 20 dB margin for robust SNR

# Outputs (mimic Fig. 9.12 form: statuses + verdict; end at [20])
print(f"Inputs: f_x={f_x/1e6:.0f} MHz, f_t={f_t/1e6:.0f} MHz, f_r={f_r/1e6:.0f} MHz, B={B/1e3:.0f} kHz")
print(f"f_IF={f_IF/1e6:.0f} MHz, Δf={delta_f/1e3:.0f} kHz, f_LO={f_LO/1e6:.0f} MHz")
print(f"\nf1 = {f1/1e6:.0f} MHz → f1_IF = {f1_IF/1e6:.3f} MHz → In-band: {in_band_f1}")
print(f"f2 = {f2/1e6:.0f} MHz → f2_IF = {f2_IF/1e6:.3f} MHz → In-band: {in_band_f2}")
print(f"\nS(f_IF) = {S_fIF_dBm} dBm, N(f_IF) = {N_fIF_dBm:.1f} dBm")
print(f"S - N = {S_minus_N_dB:.1f} dB")
print(f"Final Status: {'Disturbance - TAKE ACTION!' if disturbance else 'No Disturbance'}")