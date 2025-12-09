#!/usr/bin/env python3
"""
=====================================================================
INTERMODULATION INTERFERENCE ANALYSIS - EDUCATIONAL VERSION
=====================================================================

This program implements the intermodulation interference modeling
flowchart from Figure 9.11 in the textbook. It analyzes whether
third-order intermodulation products will cause interference in a
satellite communication receiver system.

EDUCATIONAL PURPOSE:
This version includes extensive comments explaining every concept,
acronym, calculation, and decision point to serve as a learning
resource for understanding interference analysis.

Author: Jordan Clayton
Date: December 8, 2025
=====================================================================
"""

import numpy as np
import matplotlib.pyplot as plt
import os

print("="*80)
print("INTERMODULATION INTERFERENCE ANALYSIS - EDUCATIONAL VERSION")
print("Following Figure 9.11 Flowchart")
print("="*80)

# ==============================================================================
# SECTION 1: INPUT PARAMETERS
# ==============================================================================
# This section defines all the input frequencies and system parameters
# that will be analyzed for potential interference issues.
# ==============================================================================

print("\nINPUT PARAMETERS:")
print("-" * 80)

# FREQUENCY DEFINITIONS:
# -----------------------
# f_x: External intruder/disturbance frequency (Hz)
#      This is an unwanted signal from another transmitter or interference
#      source that is present in the environment. It could be from another
#      satellite, ground station, or any RF emitter.
#
# f_t: Transmit (uplink) frequency (Hz)
#      This is the frequency at which the ground station transmits signals
#      UP to the satellite. Also called the "uplink" frequency.
#
# f_r: Receive (downlink) frequency (Hz)
#      This is the frequency at which the satellite transmits signals
#      DOWN to the ground receiver. Also called the "downlink" frequency.
#
# B: IF Bandwidth (Hz)
#    IF stands for "Intermediate Frequency" - this is the bandwidth of
#    the filter in the IF stage of the receiver. Only signals within
#    this bandwidth around the IF center frequency will pass through.
#
# f_IF: Target IF frequency (Hz)
#       After the receiver mixes the incoming RF signal with a local
#       oscillator, it converts to this intermediate frequency for
#       easier filtering and processing.

f_x = 1598e6  # Hz = 1598 MHz; L-band frequency (1-2 GHz range common for satellites)
f_t = 1500e6  # Hz = 1500 MHz; uplink transmit frequency
f_r = 1540e6  # Hz = 1540 MHz; downlink receive frequency
B = 100e3     # Hz = 100 kHz; relatively narrow bandwidth for a single channel
f_IF = 140e6  # Hz = 140 MHz; standard IF frequency used in many receivers

print(f"f_x (intruder)     = {f_x/1e6:.0f} MHz")
print(f"f_t (transmit)     = {f_t/1e6:.0f} MHz")
print(f"f_r (receive)      = {f_r/1e6:.0f} MHz")
print(f"f_IF (target)      = {f_IF/1e6:.0f} MHz")
print(f"B (IF bandwidth)   = {B/1e3:.0f} kHz")

# CONTEXT: Why these specific values?
# ------------------------------------
# L-band (1-2 GHz) is commonly used for satellite communications because:
# 1. Good penetration through atmosphere
# 2. Reasonable antenna sizes
# 3. Less rain attenuation than higher frequencies
# 4. GPS, Iridium, and other satellite systems use this band

# ==============================================================================
# SECTION 2: IF PASSBAND CALCULATION
# ==============================================================================
# The IF (Intermediate Frequency) filter only allows signals within a specific
# frequency range to pass through. We need to calculate the upper and lower
# bounds of this passband to determine if interference will be accepted.
# ==============================================================================

print("\nCALCULATIONS:")
print("-" * 80)

# CALCULATION: IF Passband Limits
# --------------------------------
# The IF filter has a center frequency (f_IF) and a bandwidth (B).
# The filter passes frequencies in the range: [f_IF - B/2, f_IF + B/2]
#
# Example:
# If f_IF = 140 MHz and B = 100 kHz:
# - Lower edge = 140 MHz - 50 kHz = 139.95 MHz
# - Upper edge = 140 MHz + 50 kHz = 140.05 MHz
#
# Any signal that falls within [139.95, 140.05] MHz will PASS THROUGH
# Any signal outside this range will be BLOCKED

delta_f = B / 2  # Half-bandwidth: dividing by 2 gives us the ± range
IF_lower = f_IF - delta_f  # Lower edge of the passband
IF_upper = f_IF + delta_f  # Upper edge of the passband

print(f"IF passband        = [{IF_lower/1e6:.4f}, {IF_upper/1e6:.4f}] MHz")

# PHYSICAL INTERPRETATION:
# ------------------------
# Think of this filter like a very narrow window. Only signals at exactly
# the right frequency can pass through. This is crucial for:
# 1. Selecting the desired channel
# 2. Rejecting adjacent channel interference
# 3. Improving signal-to-noise ratio

# ==============================================================================
# SECTION 3: THIRD-ORDER INTERMODULATION PRODUCTS
# ==============================================================================
# When multiple signals pass through a NONLINEAR device (like an amplifier),
# they mix together and create new "phantom" frequencies called intermodulation
# products. These are unwanted signals that weren't present in the original
# transmission!
# ==============================================================================

# THEORY: Why do intermodulation products occur?
# -----------------------------------------------
# Real-world amplifiers are NOT perfectly linear. Their transfer function
# can be approximated by a Taylor series:
#
#   V_out = g₁·V_in + g₂·V_in² + g₃·V_in³ + ...
#
# Where:
# - g₁ is the linear gain (desired)
# - g₂ causes second-order distortion
# - g₃ causes third-order distortion (most problematic)
#
# When you have two input frequencies f_a and f_b, the cubic term (g₃·V_in³)
# produces intermodulation products at frequencies:
#   - 2·f_a ± f_b  (third-order)
#   - 2·f_b ± f_a  (third-order)
#
# These are called "third-order" because they arise from the cubic (³) term.

# CALCULATION: Third-Order IM Products
# -------------------------------------
# Following the flowchart Box [6] and Box [11], we calculate two primary
# third-order intermodulation frequencies:
#
# f1 = 2·f_x - f_t  (mixing: 2 times intruder minus transmit)
# f2 = 2·f_r - f_x  (mixing: 2 times receive minus intruder)
#
# These specific combinations are chosen because they are the most likely
# to fall near the IF frequency and cause interference.

f1 = 2 * f_x - f_t  # First intermodulation product (Hz)
f2 = 2 * f_r - f_x  # Second intermodulation product (Hz)

print(f"f1 (IM product)    = 2*{f_x/1e6:.0f} - {f_t/1e6:.0f} = {f1/1e6:.0f} MHz")
print(f"f2 (IM product)    = 2*{f_r/1e6:.0f} - {f_x/1e6:.0f} = {f2/1e6:.0f} MHz")

# NUMERICAL EXAMPLE:
# ------------------
# f1 = 2·(1598) - 1500 = 3196 - 1500 = 1696 MHz
# f2 = 2·(1540) - 1598 = 3080 - 1598 = 1482 MHz
#
# These are "ghost" frequencies that didn't exist in the original signals!
# They are created by the nonlinearity in the receiver's front-end amplifier.

# WHY ARE THESE DANGEROUS?
# -------------------------
# Even though these frequencies are created at very low power levels
# (typically 20-40 dB below the main signals), they can still cause
# interference if they happen to fall within the IF passband after
# frequency conversion.

# ==============================================================================
# SECTION 4: LOCAL OSCILLATOR FREQUENCY CALCULATION
# ==============================================================================
# The receiver uses a technique called "heterodyning" to convert the incoming
# high-frequency RF signal down to a lower intermediate frequency (IF).
# This is done by mixing (multiplying) the RF signal with a locally-generated
# sine wave called the "Local Oscillator" (LO).
# ==============================================================================

# THEORY: Heterodyning and Frequency Conversion
# ----------------------------------------------
# When you multiply two sine waves at frequencies f_RF and f_LO, you get
# sum and difference frequencies:
#
#   cos(2π·f_RF·t) × cos(2π·f_LO·t) = ½[cos(2π·(f_RF + f_LO)·t) + cos(2π·(f_RF - f_LO)·t)]
#
# This creates two new frequencies:
# - f_RF + f_LO  (sum frequency - usually filtered out)
# - |f_RF - f_LO| (difference frequency - this is the IF we want!)
#
# The receiver then filters to keep only the difference frequency.

# CALCULATION: LO Frequency
# --------------------------
# We want the difference |f2 - f_LO| to equal f_IF (140 MHz)
# Therefore: f_LO = f2 - f_IF
#
# This ensures that when f2 (our second IM product) mixes with the LO,
# it produces a signal at the IF frequency.

f_LO = f2 - f_IF  # Local Oscillator frequency (Hz)

print(f"f_LO (heterodyne)  = {f_LO/1e6:.0f} MHz")

# NUMERICAL VERIFICATION:
# -----------------------
# f_LO = 1482 - 140 = 1342 MHz
#
# This means the receiver's local oscillator generates a 1342 MHz sine wave
# that mixes with the incoming signals to produce the IF output.

# WHY THIS SPECIFIC VALUE?
# -------------------------
# The LO frequency is chosen to downconvert the desired receive frequency
# (f_r = 1540 MHz) to the IF frequency (140 MHz):
#   |1540 - 1342| = 198 MHz... wait, that's not 140 MHz!
#
# Actually, we calculated f_LO based on f2 (the IM product), which is 1482 MHz:
#   |1482 - 1342| = 140 MHz ✓
#
# This demonstrates a key point: the LO will downconvert ANY signal that is
# 140 MHz away from f_LO, including both desired signals AND IM products!

# ==============================================================================
# SECTION 5: DOWNCONVERSION TO IF - CHECKING FOR IN-BAND INTERFERENCE
# ==============================================================================
# Now we need to determine if the intermodulation products f1 and f2 will
# fall within the IF passband after being downconverted by the LO.
# If they do, they will cause interference!
# ==============================================================================

# CALCULATION: Downconvert f1 to IF
# ----------------------------------
# When f1 passes through the mixer (multiplier with LO), it produces:
#   f1_IF = |f1 - f_LO|
#
# We take the absolute value because the mixer produces both sum and difference,
# but we only care about the difference frequency (the IF).

f1_IF = np.abs(f1 - f_LO)  # f1 downconverted to IF domain (Hz)

print(f"f1_IF              = {f1_IF/1e6:.3f} MHz")

# NUMERICAL EXAMPLE:
# ------------------
# f1_IF = |1696 - 1342| = 354 MHz
#
# This is the frequency that f1 will appear at after downconversion.

# CALCULATION: Downconvert f2 to IF
# ----------------------------------
# Same process for f2:

f2_IF = np.abs(f2 - f_LO)  # f2 downconverted to IF domain (Hz)

print(f"f2_IF              = {f2_IF/1e6:.3f} MHz")

# NUMERICAL EXAMPLE:
# ------------------
# f2_IF = |1482 - 1342| = 140 MHz
#
# Notice that f2_IF = 140 MHz, which is EXACTLY the IF center frequency!
# This is by design, since we calculated f_LO = f2 - f_IF.

# IN-BAND CHECK: Does f1 fall within the IF passband?
# ----------------------------------------------------
# We compare f1_IF to the IF passband limits:
#   IF_lower ≤ f1_IF ≤ IF_upper ?
#
# If TRUE: f1 will pass through the IF filter → INTERFERENCE!
# If FALSE: f1 will be blocked by the IF filter → NO INTERFERENCE

in_band_f1 = (IF_lower <= f1_IF <= IF_upper)

print(f"f1 in-band?        = {in_band_f1}")

# INTERPRETATION:
# ---------------
# f1_IF = 354 MHz
# IF passband = [139.95, 140.05] MHz
# Is 354 MHz in [139.95, 140.05]? NO → f1 is OUT-OF-BAND ✓
#
# This means f1 will be rejected by the IF filter and won't cause interference.

# IN-BAND CHECK: Does f2 fall within the IF passband?
# ----------------------------------------------------
# Same check for f2:

in_band_f2 = (IF_lower <= f2_IF <= IF_upper)

print(f"f2 in-band?        = {in_band_f2}")

# INTERPRETATION:
# ---------------
# f2_IF = 140.000 MHz
# IF passband = [139.95, 140.05] MHz
# Is 140.000 MHz in [139.95, 140.05]? YES → f2 is IN-BAND ⚠️
#
# This means f2 WILL pass through the IF filter and WILL cause interference!

# ==============================================================================
# SECTION 6: SIGNAL-TO-NOISE RATIO ANALYSIS
# ==============================================================================
# Now that we know f2 is in-band, we need to quantify HOW MUCH interference
# it will cause. We do this by calculating the Signal-to-Noise Ratio (S/N).
# ==============================================================================

print("\nSIGNAL-TO-NOISE ANALYSIS:")
print("-" * 80)

# DEFINITION: Signal-to-Noise Ratio (S/N or SNR)
# -----------------------------------------------
# S/N is the ratio of the desired signal power to the total noise power:
#
#   S/N = P_signal / P_noise (linear ratio)
#   S/N = 10·log₁₀(P_signal / P_noise) dB (logarithmic)
#   S/N = P_signal(dBm) - P_noise(dBm) dB (in decibels)
#
# A higher S/N means the signal is stronger relative to the noise,
# which results in better quality and lower bit error rate (BER).

# PARAMETER: Desired Signal Power
# --------------------------------
# S(f_IF) is the power of the desired signal at the IF output.
# Typical values for satellite receivers after the LNA (Low Noise Amplifier):
# - Strong signal: -70 to -80 dBm
# - Moderate signal: -90 to -100 dBm
# - Weak signal: -110 to -120 dBm
#
# We use -2 dBm as a representative value after amplification.

S_fIF_dBm = -2  # dBm (decibels relative to 1 milliwatt)

print(f"S(f_IF)            = {S_fIF_dBm} dBm")

# UNIT EXPLANATION: dBm
# ----------------------
# dBm = decibels relative to 1 milliwatt
# Formula: P(dBm) = 10·log₁₀(P(mW) / 1 mW)
#
# Examples:
# - 0 dBm = 1 mW
# - 10 dBm = 10 mW
# - -10 dBm = 0.1 mW
# - -2 dBm ≈ 0.63 mW

# CALCULATION: Thermal Noise Power
# ---------------------------------
# All electronic systems generate thermal noise due to random motion of
# electrons at non-zero temperature. The noise power is given by:
#
#   N_thermal = k · T · B  (Watts)
#
# Where:
# - k = Boltzmann's constant = 1.38 × 10⁻²³ J/K
# - T = Temperature in Kelvin (typically 290K for room temperature)
# - B = Bandwidth in Hz
#
# In dBm, this is often expressed as:
#   N_thermal(dBm) = -174 dBm/Hz + 10·log₁₀(B) + NF(dB)
#
# Where:
# - -174 dBm/Hz is the thermal noise density at 290K
# - NF is the Noise Figure of the receiver (how much it degrades S/N)

k_T_dBm_Hz = -174  # dBm/Hz; thermal noise density at room temp (290K)
NF_dB = 3          # dB; typical LNA noise figure (2-5 dB is good)
N_thermal_dBm = k_T_dBm_Hz + 10 * np.log10(B) + NF_dB

print(f"N_thermal          = {N_thermal_dBm:.1f} dBm")

# NUMERICAL EXAMPLE:
# ------------------
# N_thermal = -174 + 10·log₁₀(100,000) + 3
#           = -174 + 50 + 3
#           = -121 dBm
#
# This is the noise power in a 100 kHz bandwidth with a 3 dB noise figure.

# EXPLANATION: Noise Figure (NF)
# -------------------------------
# The noise figure quantifies how much noise the receiver adds to the signal.
#
#   NF = (S/N)_input / (S/N)_output  (linear ratio)
#   NF(dB) = 10·log₁₀(NF)
#
# - NF = 1 (0 dB): Ideal noiseless receiver (impossible in practice)
# - NF = 2 (3 dB): Good low-noise amplifier
# - NF = 10 (10 dB): Poor, noisy receiver
#
# A 3 dB noise figure means the receiver degrades the S/N by 3 dB.

# CALCULATION: Intermodulation Noise Power
# -----------------------------------------
# If an intermodulation product falls in-band, it acts like additional noise.
# The IM product is weaker than the main signal because it's generated by
# the third-order nonlinearity (g₃ coefficient), which is small.
#
# The power of the IM product relative to the desired signal depends on
# the amplifier's OIP3 (Output Third-Order Intercept Point).

if in_band_f1 or in_band_f2:
    # PARAMETER: IM Suppression
    # --------------------------
    # The IM product is typically 20-40 dB weaker than the desired signal,
    # depending on the amplifier's linearity (OIP3).
    #
    # Higher OIP3 → More linear amplifier → Greater IM suppression
    #
    # We use 25 dB as a typical value.

    IM_suppression_dB = 25  # dB below the desired signal
    N_IM_dBm = S_fIF_dBm - IM_suppression_dB

    print(f"N_IM               = {N_IM_dBm} dBm")

    # NUMERICAL EXAMPLE:
    # ------------------
    # N_IM = -2 - 25 = -27 dBm
    #
    # This is the power of the intermodulation interference.

    # CALCULATION: Total Noise Power
    # -------------------------------
    # Total noise = Thermal noise + IM noise
    #
    # We CANNOT simply add dBm values! We must convert to linear (mW),
    # add, then convert back to dBm:
    #
    #   P_total(mW) = P₁(mW) + P₂(mW)
    #   P_total(dBm) = 10·log₁₀(P_total(mW))

    N_thermal_linear = 10**(N_thermal_dBm/10)  # Convert dBm → mW
    N_IM_linear = 10**(N_IM_dBm/10)            # Convert dBm → mW
    N_total_linear = N_thermal_linear + N_IM_linear  # Add in linear scale
    N_fIF_dBm = 10 * np.log10(N_total_linear)  # Convert back to dBm

    print(f"N_total            = {N_fIF_dBm:.1f} dBm")

    # NUMERICAL EXAMPLE:
    # ------------------
    # N_thermal = -121 dBm → 10^(-121/10) = 7.94 × 10⁻¹³ mW
    # N_IM = -27 dBm → 10^(-27/10) = 1.995 × 10⁻³ mW
    # N_total = 7.94×10⁻¹³ + 1.995×10⁻³ ≈ 1.995×10⁻³ mW
    # N_total(dBm) = 10·log₁₀(1.995×10⁻³) ≈ -27 dBm
    #
    # Notice that the IM noise dominates! The thermal noise is negligible
    # compared to the IM interference.

else:
    # NO INTERMODULATION INTERFERENCE
    # --------------------------------
    # If no IM products fall in-band, the total noise is just thermal noise.

    N_fIF_dBm = N_thermal_dBm
    print(f"N_total            = {N_fIF_dBm:.1f} dBm (no IM interference)")

# CALCULATION: Signal-to-Noise Ratio
# -----------------------------------
# In dB, we subtract: S/N(dB) = S(dBm) - N(dBm)

S_minus_N_dB = S_fIF_dBm - N_fIF_dBm

print(f"S/N                = {S_minus_N_dB:.1f} dB")

# NUMERICAL EXAMPLE:
# ------------------
# S/N = -2 - (-27) = -2 + 27 = 25 dB
#
# This is actually a pretty good S/N ratio!

# ==============================================================================
# SECTION 7: THRESHOLD DECISION - IS THE SYSTEM DISTURBED?
# ==============================================================================
# We compare the actual S/N to a minimum threshold required for acceptable
# performance. If S/N falls below the threshold, the system is "disturbed"
# and will experience errors.
# ==============================================================================

print("\nVERDICT:")
print("-" * 80)

# PARAMETER: S/N Threshold
# -------------------------
# The required S/N depends on the modulation scheme and desired BER
# (Bit Error Rate):
#
# Modulation       | Required S/N | Typical BER
# -----------------|--------------|-------------
# BPSK             | 10-12 dB     | 10⁻⁶
# QPSK             | 13-15 dB     | 10⁻⁶
# 16-QAM           | 18-20 dB     | 10⁻⁶
# 64-QAM           | 24-26 dB     | 10⁻⁶
#
# BER = Bit Error Rate (e.g., 10⁻⁶ means 1 error per million bits)
#
# We use 20 dB as a threshold for robust operation with low BER.

threshold_dB = 20  # dB; minimum S/N for BER < 10⁻⁶

print(f"S/N threshold      = {threshold_dB} dB")
print(f"Actual S/N         = {S_minus_N_dB:.1f} dB")

# DECISION LOGIC: Compare S/N to Threshold
# -----------------------------------------
# If S/N < Threshold:
#   → System is DISTURBED (interference is causing problems)
#   → BER will be high, communication quality poor
#   → Action required (Box 19 in flowchart)
#
# If S/N ≥ Threshold:
#   → System is UNDISTURBED (operating normally)
#   → BER is acceptable, good communication quality
#   → No action needed (Box 18 in flowchart)

disturbance = S_minus_N_dB < threshold_dB

if disturbance:
    print(f"Status             = DISTURBANCE DETECTED")
    print("\nREASON: S/N ratio has fallen below the minimum threshold.")
    print("IMPACT: High bit error rate, degraded communication quality.")
    print("ACTION REQUIRED: Implement mitigation strategies (see textbook Box 19).")
else:
    print(f"Status             = UNDISTURBED")
    print("\nREASON: S/N ratio meets or exceeds the minimum threshold.")
    print("IMPACT: Acceptable bit error rate, good communication quality.")
    print("ACTION: Continue normal operation (no changes needed).")

# INTERPRETATION FOR THIS EXAMPLE:
# ---------------------------------
# S/N = 25 dB, Threshold = 20 dB
# 25 > 20 → UNDISTURBED ✓
#
# Even though the f2 intermodulation product falls in-band, it is weak
# enough (25 dB suppression) that it doesn't significantly degrade
# the signal quality. The system can still operate with acceptable BER.

# ==============================================================================
# SECTION 8: VISUALIZATION - FREQUENCY SPECTRUM DIAGRAM
# ==============================================================================
# Create a visual representation of all the frequencies involved in this
# analysis to help understand the relationships between signals.
# ==============================================================================

print("\n" + "="*80)
print("Generating frequency spectrum plot...")
print("="*80)

# Create a figure with one subplot
# figsize=(12, 6) means 12 inches wide × 6 inches tall
fig, ax = plt.subplots(figsize=(12, 6))

# PLOT: Input Frequencies (f_t, f_r, f_x)
# ----------------------------------------
# These are the original signals present in the system.
# We use blue circles ('bo') to represent them.
# The height represents relative power (arbitrary units for visualization).

ax.stem([f_t/1e6, f_r/1e6, f_x/1e6], [5, 5, 3],
        linefmt='b-',           # Blue line
        markerfmt='bo',         # Blue circle marker
        basefmt=' ',            # No baseline
        label='Input Frequencies')

# PLOT: Intermodulation Products (f1, f2)
# ----------------------------------------
# These are the "ghost" frequencies created by nonlinearity.
# We use red triangles ('r^') to represent them.
# They are shown at lower power (-10 dB) because they are weaker.

ax.stem([f1/1e6, f2/1e6], [-10, -10],
        linefmt='r-',           # Red line
        markerfmt='r^',         # Red triangle marker
        basefmt=' ',            # No baseline
        label='IM Products')

# PLOT: Local Oscillator (f_LO)
# ------------------------------
# The LO is the frequency generated by the receiver for downconversion.
# We use a green square ('gs') to represent it.

ax.stem([f_LO/1e6], [10],
        linefmt='g-',           # Green line
        markerfmt='gs',         # Green square marker
        basefmt=' ',            # No baseline
        label='Local Oscillator')

# PLOT: IF Passband (shaded region)
# ----------------------------------
# This is the narrow frequency range that the IF filter allows through.
# We use a yellow shaded region (axvspan = vertical span) to show it.
# alpha=0.3 makes it semi-transparent.

ax.axvspan(IF_lower/1e6, IF_upper/1e6,
          alpha=0.3,             # 30% opacity (70% transparent)
          color='yellow',
          label='IF Passband')

# ADD LABELS: Text annotations for each frequency
# ------------------------------------------------
# This helps identify what each point represents.
# ha='center' means horizontally align text at center.

ax.text(f_t/1e6, 5.5, 'f_t', ha='center', fontsize=10, fontweight='bold')
ax.text(f_r/1e6, 5.5, 'f_r', ha='center', fontsize=10, fontweight='bold')
ax.text(f_x/1e6, 3.5, 'f_x', ha='center', fontsize=10, fontweight='bold')
ax.text(f1/1e6, -9, 'f1 (IM)', ha='center', fontsize=9, color='red')
ax.text(f2/1e6, -9, 'f2 (IM)', ha='center', fontsize=9, color='red')
ax.text(f_LO/1e6, 11, 'f_LO', ha='center', fontsize=10, fontweight='bold')

# FORMATTING: Axis labels and title
# ----------------------------------
ax.set_xlabel('Frequency (MHz)', fontsize=12, fontweight='bold')
ax.set_ylabel('Relative Power (dBm)', fontsize=12, fontweight='bold')
ax.set_title('Intermodulation Interference - Frequency Spectrum', fontsize=14, fontweight='bold')

# Add legend to identify what each symbol means
ax.legend(loc='upper right', fontsize=10)

# Add grid for easier reading
ax.grid(True, alpha=0.3)  # Light grid lines

# Set x-axis limits to show all relevant frequencies
ax.set_xlim(100, 1700)  # MHz

# SAVE: Export plot to image file
# --------------------------------
plt.tight_layout()  # Automatically adjust spacing to prevent label cutoff
output_filename = 'intermod_spectrum_educational.png'
plt.savefig(output_filename, dpi=150, bbox_inches='tight')

print(f"Plot saved: {output_filename}")
print("="*80)

# ==============================================================================
# SUMMARY OF KEY CONCEPTS
# ==============================================================================
#
# 1. INTERMODULATION:
#    - Unwanted frequencies created when signals mix in nonlinear devices
#    - Third-order products (2f₁ ± f₂) are most problematic
#    - Can interfere even when original signals are separated in frequency
#
# 2. HETERODYNING:
#    - Frequency conversion technique using mixing with local oscillator
#    - Produces sum and difference frequencies: f_RF ± f_LO
#    - Allows high-frequency RF to be processed at lower IF frequency
#
# 3. IF FILTERING:
#    - Narrow bandpass filter centered at IF frequency
#    - Rejects out-of-band signals and noise
#    - Critical for selecting desired channel
#
# 4. SIGNAL-TO-NOISE RATIO:
#    - Ratio of desired signal power to total noise/interference power
#    - Higher S/N → Better quality, lower bit error rate
#    - Must exceed threshold for acceptable performance
#
# 5. INTERFERENCE MITIGATION:
#    - Change frequencies to move IM products out-of-band
#    - Use more linear amplifiers (higher OIP3)
#    - Employ sharper filters to reject interference
#
# ==============================================================================
# END OF EDUCATIONAL VERSION
# ==============================================================================
