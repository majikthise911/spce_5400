# Complete Formulas, Sources, and Trade Study Logic Flow
## Assignment 4: Optical vs. RF Crosslinks Trade Study

**Document #23**
**Date:** November 2025
**Purpose:** Comprehensive reference of all formulas, calculations, sources, and decision logic used in the trade study

---

## TABLE OF CONTENTS

1. [Trade Study Logic Flow](#trade-study-logic-flow)
2. [Optical (Laser) Link Formulas](#optical-laser-link-formulas)
3. [RF (Ka-Band) Link Formulas](#rf-ka-band-link-formulas)
4. [Physical Constants](#physical-constants)
5. [Parameter Sources](#parameter-sources)
6. [References](#references)

---

## TRADE STUDY LOGIC FLOW

### High-Level Decision Tree

```
ASSIGNMENT REQUIREMENTS
├── Range: 250 km (Given)
├── Data Rate: 1 Gbps (Given)
└── Platform: Small satellites (Given)
    │
    ├─────────────────────────┬─────────────────────────┐
    │                         │                         │
OPTICAL ANALYSIS         RF ANALYSIS            COMPARISON
    │                         │                         │
    ▼                         ▼                         ▼
[STEP 1]                 [STEP 1]               Link Margin
Excel Template           Design Choices         Power
Detector-First           Select frequency       Aperture Size
    │                         │                  Data Rate
    ▼                         ▼                  Pointing
Q = 40 (template)        f = 32 GHz             │
η = 0.3 (template)       Ka-band ISL            ▼
λ = 1550 nm (choice)         │                  RECOMMENDATION
    │                         ▼                      │
    ▼                    [STEP 2]                   ▼
[STEP 2]                 Calculate λ            OPTICAL PREFERRED
n = Q/η = 133.33         λ = c/f                (25.66 dB margin)
    │                         │                  vs RF (2.8 dB)
    ▼                         ▼
[STEP 3]                 [STEP 3]
E_photon = hc/λ          Choose aperture
    │                    D = 30 cm
    ▼                         │
[STEP 4]                      ▼
E_bit = n × E_photon     [STEP 4]
    │                    G = η_ant(πD/λ)²
    ▼                         │
[STEP 5]                      ▼
P_req = E_bit × R_b      [STEP 5]
    │                    FSPL = 20log(4πR/λ)
    ▼                         │
[STEP 6]                      ▼
Choose aperture          [STEP 6]
D = 10 cm                N_0 = k_B × T_sys
    │                         │
    ▼                         ▼
[STEP 7]                 [STEP 7]
G = (πD/λ)²              Choose Tx power
    │                    P_t = 1.2 W
    ▼                         │
[STEP 8]                      ▼
L_s = (λ/4πR)²           [STEP 8]
    │                    P_rx = EIRP - FSPL + G_rx - Losses
    ▼                         │
[STEP 9]                      ▼
Choose Tx power          [STEP 9]
P_tx = 0.122 W           C/N_0 = P_rx - N_0
    │                         │
    ▼                         ▼
[STEP 10]                [STEP 10]
P_rx = P_tx×L_s×G²×L     (C/N_0)_req = E_b/N_0 + 10log(R_b)
    │                         │
    ▼                         ▼
[STEP 11]                [STEP 11]
Margin = P_rx - P_req    Margin = C/N_0 - (C/N_0)_req
    │                         │
    ▼                         ▼
RESULT:                  RESULT:
25.66 dB margin          2.8 dB margin
θ = 18.9 μrad            θ = 2.19°
P = 0.122 W              P = 1.2 W
D = 10 cm                D = 30 cm
```

### Detailed Logic Flow Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                     MISSION REQUIREMENTS                        │
│  • Range: 250 km LEO-to-LEO                                    │
│  • Data Rate: 1 Gbps minimum                                   │
│  • Platform: Small satellites (SWaP constrained)               │
│  • Requirement: Compare Optical vs RF crosslinks              │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│              TEMPLATE & DESIGN FOUNDATION                       │
│  Excel Template Provides:                                      │
│  • Q = 40 photoelectrons/bit (BER 10⁻⁹)                       │
│  • η = 0.3 quantum efficiency                                  │
│  • Pointing loss = -3.0 dB                                     │
│  • Line losses = -6.0 dB                                       │
│  • Detector-first methodology                                  │
└────────────┬───────────────────────┬────────────────────────────┘
             │                       │
    ┌────────┴─────────┐    ┌───────┴──────────┐
    │                  │    │                  │
    ▼                  ▼    ▼                  ▼
┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐
│  OPTICAL PATH   │  │   RF PATH       │  │ DESIGN CHOICES  │
└─────────────────┘  └─────────────────┘  └─────────────────┘

═══════════════════════════════════════════════════════════════════
                        OPTICAL LINK FLOW
═══════════════════════════════════════════════════════════════════

[1] DESIGN CHOICE: Wavelength Selection
    ├─ Option A: Nd:YAG 1064 nm (template laser)
    ├─ Option B: 850 nm (VCSEL, low cost)
    └─ ✓ SELECTED: 1550 nm
        Rationale: • Telecom C-band standard (mature)
                   • Eye-safe (Class 1M)
                   • InGaAs detector optimized at this λ
                   • Heritage: NASA LCRD, ESA EDRS

[2] DETECTOR REQUIREMENTS (Template-Driven)
    Input:  Q = 40 photoelectrons/bit (from template)
            η = 0.3 (from template, matches InGaAs APD @ 1550nm)
    ────────────────────────────────────────────────────
    Formula: n = Q / η
    Calc:    n = 40 / 0.3 = 133.33 photons/bit
    Source:  Excel template Row 6

[3] PHOTON ENERGY (Fundamental Physics)
    Input:  λ = 1550 nm = 1.55 × 10⁻⁶ m
            c = 3 × 10⁸ m/s
            h = 6.626 × 10⁻³⁴ J·s
    ────────────────────────────────────────────────────
    Formula: f = c / λ
    Calc:    f = 1.935 × 10¹⁴ Hz
    ────────────────────────────────────────────────────
    Formula: E_photon = h × f
    Calc:    E = 1.282 × 10⁻¹⁹ J/photon
    Source:  Planck's equation (1900)

[4] ENERGY PER BIT
    Input:  n = 133.33 photons/bit
            E_photon = 1.282 × 10⁻¹⁹ J
    ────────────────────────────────────────────────────
    Formula: E_bit = n × E_photon
    Calc:    E_bit = 1.709 × 10⁻¹⁷ J/bit
    Source:  Excel template Row 10

[5] REQUIRED RECEIVER POWER
    Input:  E_bit = 1.709 × 10⁻¹⁷ J/bit
            R_b = 1 Gbps = 1 × 10⁹ bps
    ────────────────────────────────────────────────────
    Formula: P_req = E_bit × R_b
    Calc:    P_req = 1.709 × 10⁻⁸ W = -77.67 dBW
    Source:  Excel template Row 12, P = E/t

[6] DESIGN CHOICE: Aperture Size
    ├─ Constraint: Small satellite compatible (<15 cm)
    ├─ Trade: Larger D → Higher gain, but heavier
    └─ ✓ SELECTED: D = 10 cm
        Rationale: • Fits 1U face (10×10 cm)
                   • Provides high gain at 1550 nm
                   • Commercial availability

[7] TELESCOPE GAIN
    Input:  D = 0.10 m
            λ = 1.55 × 10⁻⁶ m
    ────────────────────────────────────────────────────
    Formula: G = (π × D / λ)²
    Calc:    G = 4.108 × 10¹⁰ = 106.1 dBi
    Source:  Excel template Rows 19-20
             Diffraction-limited aperture theory
    Note:    Both Tx and Rx use same size

[8] FREE SPACE LOSS
    Input:  R = 250 km = 250,000 m
            λ = 1.55 × 10⁻⁶ m
    ────────────────────────────────────────────────────
    Formula: L_s = (λ / (4πR))²
    Calc:    L_s = 2.434 × 10⁻²⁵ = -246.1 dB
    Source:  Excel template Row 16
             Friis transmission equation (1946)

[9] ADDITIONAL LOSSES (Template Values)
    • Pointing loss:  -3.0 dB  (achievable with FSM)
    • Line losses:    -6.0 dB  (total from template)
      Estimated breakdown: Tx coupling (~2 dB) + Tx optics (~1 dB) +
                          Rx optics (~1 dB) + Rx coupling (~1.5 dB) +
                          Detector packaging (~0.5 dB)
    • Atmospheric:     0.0 dB  (vacuum path)
    Source: Excel template Rows 21-23 (total values only)

[10] DESIGN CHOICE: Transmit Power
     ├─ Method: Work backwards from desired margin
     └─ ✓ SELECTED: P_tx = 0.122 W (-9.1 dBW)

     How this was chosen:

     Step 1: Required receiver power (from detector requirements)
             P_req = -77.67 dBW

     Step 2: Choose desired margin (design goal)
             Margin = 25 dB (provides robustness)

     Step 3: Required received power
             P_rx = P_req + Margin
             P_rx = -77.67 + 25 = -52.67 dBW (target)

     Step 4: Use link equation to solve for P_tx
             P_rx = P_tx + G_tx + G_rx + L_s + L_pt + L_o
             -52.67 = P_tx + 106.1 + 106.1 - 246.1 - 3.0 - 6.0
             -52.67 = P_tx - 42.9
             P_tx = -9.77 dBW ≈ -9.1 dBW
             P_tx = 0.122 W

     Rationale: • Provides 25.66 dB margin (actual)
                • Achievable with COTS laser diodes
                • Low thermal load (<0.5 W total with driver)

[11] RECEIVED POWER (Link Budget)
     Input (all in dB):
             P_tx = -9.1 dBW
             G_tx = +106.1 dBi
             G_rx = +106.1 dBi
             L_s = -246.1 dB
             L_pt = -3.0 dB
             L_o = -6.0 dB
     ────────────────────────────────────────────────────
     Formula (dB addition):
             P_rx = P_tx + G_tx + G_rx + L_s + L_pt + L_o

     Calculation:
             P_rx = -9.1 + 106.1 + 106.1 - 246.1 - 3.0 - 6.0

             Combine gains:  -9.1 + 106.1 + 106.1 = 203.1 dBW
             Combine losses: -246.1 - 3.0 - 6.0 = -255.1 dB
             Total:          203.1 - 255.1 = -52.0 dBW

             P_rx = -52.01 dBW

     In linear: P_rx = 10^(-52.01/10) = 6.303 × 10⁻⁶ W = 6.303 μW

     Source: Friis equation (dB form), Excel template Row 24 =SUM(F14:F23)

[12] LINK MARGIN
     Input:  P_rx = -52.01 dBW
             P_req = -77.67 dBW
     ────────────────────────────────────────────────────
     Formula: Margin = P_rx - P_req
     Calc:    Margin = 25.66 dB (369× in linear)
     Source:  Excel template Row 26

[13] BEAM DIVERGENCE AND POINTING (Analysis)
     Input:  λ = 1.55 × 10⁻⁶ m
             D = 0.10 m
     ────────────────────────────────────────────────────
     Formula (divergence to first null):
             θ_null = 1.22 × λ / D

     Calc:   θ_null = 18.91 μrad (radius to first zero)
             Spot diameter at 250 km = 4.73 m

     Source: Airy disk formula (first zero of Bessel J₁)
             Born & Wolf "Principles of Optics" (1959)

     ────────────────────────────────────────────────────
     Formula (half-power beamwidth, -3 dB point):
             θ_3dB ≈ 0.514 × λ / D
             Or: θ_3dB ≈ 0.42 × θ_null

     Calc:   θ_3dB = 0.514 × 1.55×10⁻⁶ / 0.10
             θ_3dB ≈ 8.0 μrad (where intensity = 50%)

     Source: Numerical solution of Airy pattern

     ────────────────────────────────────────────────────
     POINTING REQUIREMENT:

     Template specifies: -3.0 dB pointing loss budget

     This corresponds to pointing error = half-power beamwidth
     Maximum error: ±8.0 μrad (3σ) → gives -3 dB loss
     Conservative target: ±5.0 μrad (3σ) → gives ~-1.5 dB loss

     Achievability: Star tracker (±24 μrad) + FSM (±1 μrad)
                    = ±5 μrad achievable ✓
                    Heritage: ESA EDRS <5 μrad

     In angle units:
     - 18.91 μrad = 0.0011° = 3.9 arcsec (beam divergence)
     - 8.0 μrad = 0.00046° = 1.6 arcsec (half-power)
     - 5.0 μrad = 0.00029° = 1.0 arcsec (target)

═══════════════════════════════════════════════════════════════════
                          RF LINK FLOW
═══════════════════════════════════════════════════════════════════

[1] DESIGN CHOICE: Frequency Selection
    ├─ Option A: X-band 8 GHz (lower FSPL, bigger antenna)
    ├─ Option B: Ku-band 14 GHz (moderate)
    └─ ✓ SELECTED: Ka-band 32 GHz
        Rationale: • ITU Ka-band ISL allocation
                   • High data rate capability
                   • Heritage: Starlink, Iridium NEXT

[2] WAVELENGTH FROM FREQUENCY
    Input:  f = 32 GHz = 32 × 10⁹ Hz
            c = 3 × 10⁸ m/s
    ────────────────────────────────────────────────────
    Formula: λ = c / f
    Calc:    λ = 9.375 × 10⁻³ m = 9.375 mm
    Source:  Wave equation (fundamental)

[3] FREE SPACE PATH LOSS
    Input:  R = 250 km = 250,000 m
            λ = 0.009375 m
    ────────────────────────────────────────────────────
    Formula: FSPL(dB) = 20 × log₁₀(4πR/λ)
    Calc:    FSPL = 170.5 dB
    Source:  Friis equation, ITU-R P.525 standard

[4] DESIGN CHOICE: Antenna Size
    ├─ Constraint: Deployable mesh antenna for smallsat
    ├─ Trade: Larger D → Higher gain, but deployment complexity
    └─ ✓ SELECTED: D = 30 cm
        Rationale: • Provides adequate gain at Ka-band
                   • Deployable from 3U volume
                   • Commercial heritage (Viasat)

[5] ANTENNA GAIN (with efficiency)
    Input:  D = 0.30 m
            λ = 0.009375 m
            η_ant = 0.6 (typical deployable mesh)
    ────────────────────────────────────────────────────
    Formula: G = η_ant × (π × D / λ)²
    Calc:    G = 6,064 = 37.8 dBi
    Source:  Antenna theory
             Kraus & Marhefka "Antennas" (2002)
    Note:    Both Tx and Rx use same size

[6] SYSTEM NOISE TEMPERATURE (Design Parameter)
    ├─ LNA noise figure: ~3 dB at Ka-band
    ├─ Feed/waveguide losses: 1-2 dB
    ├─ Sky noise at LEO: ~10 K
    └─ ✓ SELECTED: T_sys = 650 K
        Rationale: • Typical for Ka-band smallsat receiver
                   • LNA + losses contribution

[7] NOISE POWER DENSITY
    Input:  k_B = 1.38 × 10⁻²³ J/K
            T_sys = 650 K
    ────────────────────────────────────────────────────
    Formula: N_0 = k_B × T_sys
    Calc:    N_0 = 8.97 × 10⁻²¹ W/Hz = -200.5 dBW/Hz
    Source:  Johnson-Nyquist noise (1928)

[8] REQUIRED E_b/N_0 (Design Parameter)
    ├─ Uncoded BPSK: ~9.6 dB for BER 10⁻⁹
    ├─ With LDPC coding: 9.6 dB (6 dB coding gain)
    └─ ✓ SELECTED: 9.6 dB
        Rationale: • Achievable with modern FEC
                   • 16-APSK modulation with coding

[9] DESIGN CHOICE: Transmit Power
    ├─ Iterate to achieve positive margin
    └─ ✓ SELECTED: P_t = 1.2 W
        Rationale: • Provides 2.8 dB margin
                   • Typical Ka-band SSPA capability

[10] EIRP (Effective Isotropic Radiated Power)
     Input:  P_t = 1.2 W = 0.8 dBW
             G_t = 37.8 dBi
     ────────────────────────────────────────────────────
     Formula: EIRP = P_t + G_t
     Calc:    EIRP = 38.6 dBW
     Source:  FCC 47 CFR §2.1, standard RF practice

[11] ADDITIONAL LOSSES
     • Pointing loss:  -1.0 dB  (body pointing)
     • Feed loss:      -1.0 dB  (waveguide)
     • Misc losses:    -2.0 dB  (polarization, etc.)
     Source: RF link budget standard practice

[12] RECEIVED POWER
     Input:  EIRP = 38.6 dBW
             FSPL = -170.5 dB
             G_rx = 37.8 dBi
             Losses = -4.0 dB
     ────────────────────────────────────────────────────
     Formula: P_rx = EIRP - FSPL + G_rx - Losses
     Calc:    P_rx = -98.1 dBW
     Source:  Friis equation

[13] CARRIER-TO-NOISE DENSITY
     Input:  P_rx = -98.1 dBW
             N_0 = -200.5 dBW/Hz
     ────────────────────────────────────────────────────
     Formula: C/N_0 = P_rx - N_0
     Calc:    C/N_0 = 102.4 dB-Hz
     Source:  Standard communications theory
              Sklar "Digital Communications" (2001)

[14] REQUIRED C/N_0
     Input:  E_b/N_0 = 9.6 dB
             R_b = 1 Gbps = 1 × 10⁹ bps
     ────────────────────────────────────────────────────
     Formula: (C/N_0)_req = E_b/N_0 + 10×log₁₀(R_b)
     Calc:    (C/N_0)_req = 9.6 + 90.0 = 99.6 dB-Hz
     Source:  Shannon-Hartley theorem

[15] LINK MARGIN
     Input:  C/N_0 = 102.4 dB-Hz
             (C/N_0)_req = 99.6 dB-Hz
     ────────────────────────────────────────────────────
     Formula: Margin = C/N_0 - (C/N_0)_req
     Calc:    Margin = 2.8 dB (1.91× in linear)
     Source:  Standard RF link budget practice

[16] BEAMWIDTH (Pointing Analysis)
     Input:  λ = 0.009375 m
             D = 0.30 m
     ────────────────────────────────────────────────────
     Formula: θ_3dB ≈ 70 × λ / D  (degrees)
     Calc:    θ = 2.19° = 7,884 arcsec
     Source:  Antenna beamwidth approximation
              Stutzman & Thiele (2012)

     Pointing requirement: <0.73° for 1 dB loss

═══════════════════════════════════════════════════════════════════
                      COMPARISON & DECISION
═══════════════════════════════════════════════════════════════════

┌─────────────────────────────────────────────────────────────────┐
│              FIVE KEY PARAMETERS COMPARISON                     │
└─────────────────────────────────────────────────────────────────┘

[1] APERTURE SIZE
    Optical: 10 cm → Winner (3× smaller)
    RF:      30 cm

    Impact: • Launch volume savings
            • Simpler mechanical design
            • Lower mass

[2] TRANSMIT POWER
    Optical: 0.122 W → Winner (10× lower)
    RF:      1.2 W

    Impact: • Lower power budget
            • Smaller thermal load
            • Longer mission life

[3] DATA RATE CAPABILITY
    Optical: 10+ Gbps scalable (calculated: 15.66 dB margin @ 10 Gbps)
    RF:      ~1.5 Gbps max (calculated: fails at 2 Gbps)

    Impact: • Future-proof design
            • Mission flexibility
            • Science data return

[4] LINK MARGIN
    Optical: 25.66 dB → Winner (8.9× better)
    RF:      2.8 dB

    Impact: • Robustness to degradation
            • Weather margin (if ground segment)
            • Component aging tolerance

[5] POINTING ACCURACY
    Optical: 18.9 μrad (0.0011°)
    RF:      2.19° → Winner (2,000× easier)

    Impact: • FSM required for optical
            • Development cost
            • Acquisition time

┌─────────────────────────────────────────────────────────────────┐
│                    DECISION MATRIX                              │
└─────────────────────────────────────────────────────────────────┘

                              Optical Wins: 4 of 5 parameters
                              RF Wins:      1 of 5 parameters

Key Insight: Optical's 25.66 dB margin provides flexibility to:
             • Trade margin for simpler pointing (reduce FSM cost)
             • Scale data rate to 10 Gbps (still 15.66 dB margin)
             • Tolerate component degradation over mission life
             • Extend range to 500 km (19.64 dB margin remains)

RF's advantage: Pointing is 2,000× easier, BUT:
                • Only 2.8 dB margin = no degradation tolerance
                • Cannot scale data rate (fails at 2 Gbps)
                • Cannot extend range (fails at 500 km)
                • Limited future flexibility

┌─────────────────────────────────────────────────────────────────┐
│                  FINAL RECOMMENDATION                           │
│                                                                 │
│  ✓ OPTICAL (LASER) CROSSLINKS RECOMMENDED                      │
│                                                                 │
│  Confidence: HIGH                                               │
│                                                                 │
│  Rationale: Superior performance on 4 of 5 key parameters.     │
│  The enormous link margin (25.66 dB vs 2.8 dB) provides        │
│  transformational advantages that outweigh the pointing         │
│  complexity. Heritage FSM technology (EDRS, LCRD) mitigates    │
│  pointing risk.                                                 │
└─────────────────────────────────────────────────────────────────┘

```

---

## OPTICAL (LASER) LINK FORMULAS

### 1. Detector Requirements

| Formula | Variables | Source |
|---------|-----------|--------|
| `n = Q / η` | n = photons/bit<br>Q = photoelectrons/bit<br>η = quantum efficiency | **Excel template Row 6**<br>Basic photon counting |
| **Values:** | Q = 40 (template)<br>η = 0.3 (template)<br>n = 133.33 | BER 10⁻⁹ requirement |

**Modulation Note:** OOK (On-Off Keying) inferred from Q = 40, which is standard for OOK direct detection at BER 10⁻⁹.

### 2. Photon Energy

| Formula | Variables | Source |
|---------|-----------|--------|
| `f = c / λ` | f = frequency (Hz)<br>c = speed of light (m/s)<br>λ = wavelength (m) | **Fundamental physics**<br>Wave equation |
| `E_photon = h × f` | h = Planck's constant (J·s)<br>E = energy per photon (J) | **Planck (1900)**<br>Quantum mechanics |
| **Combined:** `E = h × c / λ` | | |

**Example Calculation:**
```
λ = 1550 nm = 1.55 × 10⁻⁶ m (design choice: telecom standard)
f = (3 × 10⁸) / (1.55 × 10⁻⁶) = 1.935 × 10¹⁴ Hz
E = (6.626 × 10⁻³⁴) × (1.935 × 10¹⁴) = 1.282 × 10⁻¹⁹ J
```

### 3. Energy and Power

| Formula | Variables | Source |
|---------|-----------|--------|
| `E_bit = n × E_photon` | E_bit = energy per bit (J) | **Excel template Row 10** |
| `P_req = E_bit × R_b` | P_req = required power (W)<br>R_b = bit rate (bps) | **Excel template Row 12**<br>Power = Energy/Time |

**Example Calculation:**
```
E_bit = 133.33 × 1.282×10⁻¹⁹ = 1.709 × 10⁻¹⁷ J/bit
P_req = 1.709×10⁻¹⁷ × 1×10⁹ = 1.709×10⁻⁸ W = -77.67 dBW
```

### 4. Free Space Loss

| Formula | Variables | Source |
|---------|-----------|--------|
| `L_s = (λ / (4πR))²` | L_s = free space loss (linear)<br>R = range (m) | **Excel template Row 16**<br>**Friis (1946)** |
| **In dB:** `-10 × log₁₀(L_s)` | | |

**Example Calculation:**
```
R = 250 km = 250,000 m (given)
L_s = (1.55×10⁻⁶ / (4π × 250,000))² = 2.434 × 10⁻²⁵
L_s(dB) = -246.1 dB
```

**Derivation:** From Friis transmission equation for isotropic radiators.

### 5. Telescope Gain

| Formula | Variables | Source |
|---------|-----------|--------|
| `G = (π × D / λ)²` | G = gain (linear)<br>D = aperture diameter (m) | **Excel template Rows 19-20**<br>**Diffraction-limited aperture** |
| **In dB:** `10 × log₁₀(G)` | | |

**Example Calculation:**
```
D = 10 cm = 0.10 m (design choice)
G = (π × 0.10 / 1.55×10⁻⁶)² = 4.108 × 10¹⁰ = 106.1 dBi
```

**Note:** This is the **exact formula from Excel template**, not an approximation. For optical systems, efficiency is implicit in the Q and η values.

### 6. Link Budget Equation

| Formula | Variables | Source |
|---------|-----------|--------|
| `P_rx = P_tx × L_s × G_tx × G_rx × L_pt × L_o` | All losses in linear<br>All gains in linear | **Friis equation**<br>**Excel template Row 24** |
| **In dB:** `P_rx = P_tx + G_tx + G_rx + L_s + L_pt + L_o` | All in dB | Addition form |

**Example Calculation:**
```
P_tx = 0.122 W = -9.1 dBW (design choice)
G_tx = G_rx = 106.1 dBi
L_s = -246.1 dB
L_pt = -3.0 dB (template)
L_o = -6.0 dB (template)

P_rx = -9.1 + 106.1 + 106.1 - 246.1 - 3.0 - 6.0 = -52.0 dBW
```

### 7. Link Margin

| Formula | Variables | Source |
|---------|-----------|--------|
| `Margin = P_rx - P_req` | In dB | **Excel template Row 26**<br>Standard practice |

**Example Calculation:**
```
Margin = -52.01 - (-77.67) = 25.66 dB
Linear: 10^(25.66/10) = 369× more power than required
```

### 8. Beam Divergence and Pointing

#### 8.1 Beam Divergence (to first null)

| Formula | Variables | Source |
|---------|-----------|--------|
| `θ_null = 1.22 × λ / D` | θ_null = angle to first zero (rad)<br>Factor 1.22 = first zero of J₁ Bessel function | **Airy disk formula**<br>**Born & Wolf (1959)** |

**Example Calculation:**
```
θ_null = 1.22 × 1.55×10⁻⁶ / 0.10 = 1.891×10⁻⁵ rad = 18.91 μrad

Spot size at 250 km = 18.91 μrad × 250 km = 4.73 m diameter
```

**Physical Meaning:** First zero of Airy pattern defines diffraction-limited beam.

#### 8.2 Half-Power Beamwidth (-3 dB point)

| Formula | Variables | Source |
|---------|-----------|--------|
| `θ_3dB ≈ 0.514 × λ / D` | θ_3dB = half-power angle (rad)<br>Where intensity = 50% of peak | **Numerical solution**<br>Airy pattern analysis |
| **Alternative:** `θ_3dB ≈ 0.42 × θ_null` | Ratio: 0.514/1.22 ≈ 0.42 | Relationship from Bessel function |

**Example Calculation:**
```
θ_3dB = 0.514 × 1.55×10⁻⁶ / 0.10 = 7.97×10⁻⁶ rad ≈ 8.0 μrad

Or: θ_3dB = 0.42 × 18.91 = 7.94 μrad
```

**Physical Meaning:** At this angle, beam intensity drops to 50% (−3 dB from peak).

#### 8.3 Pointing Requirement

**Relationship between pointing error and loss:**

For -3 dB pointing loss (from template):
- Pointing error = θ_3dB = 8.0 μrad
- This places receiver at half-power point of transmit beam

**Pointing accuracy requirement:**
```
Maximum error: ±8.0 μrad (3σ) → achieves -3 dB loss
Conservative: ±5.0 μrad (3σ) → achieves ~-1.5 dB loss (margin)
```

**Achievability with heritage technology:**
- Star tracker: ±24 μrad (coarse)
- Fine Steering Mirror (FSM): ±1 μrad (fine)
- **Combined: ±5 μrad achievable**
- **Heritage: ESA EDRS <5 μrad demonstrated**

**Important:** The pointing requirement (8 μrad) is NOT the beam divergence (18.91 μrad). It's the half-power beamwidth, which is approximately 0.42× the beam divergence for Airy disk patterns.

---

## RF (Ka-BAND) LINK FORMULAS

### 1. Wavelength from Frequency

| Formula | Variables | Source |
|---------|-----------|--------|
| `λ = c / f` | λ = wavelength (m)<br>f = frequency (Hz)<br>c = speed of light | **Fundamental physics** |

**Example Calculation:**
```
f = 32 GHz = 32 × 10⁹ Hz (Ka-band ISL allocation)
λ = 3×10⁸ / 32×10⁹ = 9.375×10⁻³ m = 9.375 mm
```

### 2. Free Space Path Loss

| Formula | Variables | Source |
|---------|-----------|--------|
| `FSPL(dB) = 20 × log₁₀(4πR/λ)` | R = range (m)<br>λ = wavelength (m) | **Friis equation**<br>**ITU-R P.525** |
| **Alternate:** `32.45 + 20log(f_MHz) + 20log(R_km)` | Frequency and range version | ITU-R standard |

**Example Calculation:**
```
FSPL = 20 × log₁₀((4π × 250,000) / 0.009375)
     = 20 × log₁₀(335,103,253)
     = 20 × 8.525 = 170.5 dB
```

### 3. Antenna Gain (with efficiency)

| Formula | Variables | Source |
|---------|-----------|--------|
| `G = η_ant × (π × D / λ)²` | η_ant = antenna efficiency<br>D = diameter (m) | **Kraus & Marhefka (2002)**<br>Antenna theory |

**Example Calculation:**
```
D = 30 cm = 0.30 m (design choice)
η_ant = 0.6 (typical deployable mesh)
G = 0.6 × (π × 0.30 / 0.009375)² = 6,064 = 37.8 dBi
```

**Note:** Efficiency factor accounts for surface errors, blockage, spillover losses.

### 4. EIRP

| Formula | Variables | Source |
|---------|-----------|--------|
| `EIRP = P_t + G_t` | In dB<br>EIRP = Effective Isotropic Radiated Power | **FCC 47 CFR §2.1**<br>Standard RF practice |

**Example Calculation:**
```
P_t = 1.2 W = 0.8 dBW (design choice)
G_t = 37.8 dBi
EIRP = 0.8 + 37.8 = 38.6 dBW
```

### 5. Received Power

| Formula | Variables | Source |
|---------|-----------|--------|
| `P_rx = EIRP - FSPL + G_rx - ΣLosses` | All in dB | **Friis equation**<br>Standard RF link budget |

**Example Calculation:**
```
P_rx = 38.6 - 170.5 + 37.8 - 1.0 - 1.0 - 2.0
     = -98.1 dBW
```

### 6. Noise Power Density

| Formula | Variables | Source |
|---------|-----------|--------|
| `N_0 = k_B × T_sys` | N_0 = noise density (W/Hz)<br>k_B = Boltzmann constant<br>T_sys = system noise temp (K) | **Johnson-Nyquist (1928)**<br>Thermodynamics |

**Example Calculation:**
```
k_B = 1.38 × 10⁻²³ J/K
T_sys = 650 K (Ka-band LNA + losses)
N_0 = 1.38×10⁻²³ × 650 = 8.97×10⁻²¹ W/Hz = -200.5 dBW/Hz
```

### 7. Carrier-to-Noise Density

| Formula | Variables | Source |
|---------|-----------|--------|
| `C/N_0 = P_rx - N_0` | In dB-Hz<br>C/N_0 = Carrier to Noise Density | **Sklar (2001)**<br>Digital Communications |

**Example Calculation:**
```
C/N_0 = -98.1 - (-200.5) = 102.4 dB-Hz
```

### 8. Required C/N_0

| Formula | Variables | Source |
|---------|-----------|--------|
| `(C/N_0)_req = E_b/N_0 + 10×log₁₀(R_b)` | E_b/N_0 = energy per bit to noise<br>R_b = bit rate (bps) | **Shannon-Hartley**<br>Information theory |

**Example Calculation:**
```
E_b/N_0 = 9.6 dB (BER 10⁻⁹ with LDPC coding)
R_b = 1 Gbps
(C/N_0)_req = 9.6 + 10×log₁₀(10⁹) = 9.6 + 90.0 = 99.6 dB-Hz
```

### 9. Link Margin

| Formula | Variables | Source |
|---------|-----------|--------|
| `Margin = C/N_0 - (C/N_0)_req` | In dB | Standard RF practice |

**Example Calculation:**
```
Margin = 102.4 - 99.6 = 2.8 dB
Linear: 10^(2.8/10) = 1.91× safety factor
```

### 10. Antenna Beamwidth

| Formula | Variables | Source |
|---------|-----------|--------|
| `θ_3dB ≈ 70 × λ / D` | In degrees<br>θ_3dB = half-power beamwidth | **Stutzman & Thiele (2012)**<br>Approximation |
| **Exact:** `1.22 × λ / D` | In radians | Same as optical (Airy disk) |

**Example Calculation:**
```
θ_3dB = 70 × 0.009375 / 0.30 = 2.19 degrees
      = 2.19° × 3600"/° = 7,884 arcseconds
```

**Note:** 70 ≈ 1.22 × 57.3 (radian to degree conversion)

---

## PHYSICAL CONSTANTS

| Constant | Symbol | Value | Source |
|----------|--------|-------|--------|
| Speed of light | c | 2.998 × 10⁸ m/s | **CODATA 2018**<br>Exact by SI definition |
| Planck's constant | h | 6.626 × 10⁻³⁴ J·s | **CODATA 2018**<br>±0.000040×10⁻³⁴ |
| Boltzmann constant | k_B | 1.38 × 10⁻²³ J/K | **CODATA 2018**<br>Exact by 2019 SI redefinition |

**Source:** Committee on Data for Science and Technology (CODATA)
**Reference:** https://physics.nist.gov/cuu/Constants/

---

## PARAMETER SOURCES

### Given in Problem Statement

| Parameter | Value | Source |
|-----------|-------|--------|
| Range | 250 km | Assignment requirement |
| Data rate | 1 Gbps | Assignment requirement |
| Orbit altitude | 500 km | Assignment (informational) |
| Platform | Small satellites | Assignment |

### From Excel Template

| Parameter | Value | Location | Rationale |
|-----------|-------|----------|-----------|
| Q (photoelectrons/bit) | 40 | Row 4 | BER 10⁻⁹ requirement |
| η (quantum efficiency) | 0.3 | Row 5 | Typical detector |
| Pointing loss | -3.0 dB | Row 21 | Achievable with FSM |
| Line losses | -6.0 dB | Row 22 | Optics budget |

**Note:** Template used Nd:YAG laser (~3.7 μm), but methodology is wavelength-independent.

### Design Choices (Justified)

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| **Optical wavelength** | 1550 nm | Telecom C-band standard, eye-safe, InGaAs detector optimized, NASA LCRD heritage |
| **Optical modulation** | OOK (inferred) | Q = 40 corresponds to OOK direct detection at BER 10⁻⁹ |
| **Optical aperture** | 10 cm | Fits 1U face, provides 106.1 dBi gain at 1550 nm |
| **Optical Tx power** | 0.122 W | Calculated from link equation to achieve 25 dB margin goal |
| **RF frequency** | 32 GHz | Ka-band ISL allocation (ITU) |
| **RF modulation** | 16-APSK | High spectral efficiency for Ka-band |
| **RF antenna** | 30 cm | Provides 37.8 dBi gain, deployable from 3U |
| **RF Tx power** | 1.2 W | Calculated from link equation to achieve ~3 dB margin |
| **RF antenna efficiency** | 0.6 | Typical deployable mesh antenna |
| **RF noise temp** | 650 K | Ka-band LNA + losses typical |
| **RF E_b/N_0** | 9.6 dB | BER 10⁻⁹ with LDPC coding |

---

## REFERENCES

### Primary Sources

1. **Excel Template:** "Laser_Link_Calculations_template.xlsx"
   - Provided with assignment
   - Detector-first methodology
   - Q, η, loss values

2. **Problem Statement:** Assignment #4 description
   - Range: 250 km
   - Data rate: 1 Gbps
   - Comparison requirement

### Textbooks & Theory

3. **Born, M., & Wolf, E. (1959).** *Principles of Optics.*
   - Airy disk diffraction formula
   - Beam divergence: θ = 1.22λ/D

4. **Friis, H.T. (1946).** "A Note on a Simple Transmission Formula." *Proc. IRE*, 34(5), 254-256.
   - Free space loss formula
   - Foundation of link budgets

5. **Kraus, J.D., & Marhefka, R.J. (2002).** *Antennas: For All Applications* (3rd ed.).
   - Antenna gain with efficiency
   - Beamwidth formulas

6. **Sklar, B. (2001).** *Digital Communications: Fundamentals and Applications* (2nd ed.).
   - C/N₀ calculations
   - BER vs E_b/N_0 relationships

7. **Stutzman, W.L., & Thiele, G.A. (2012).** *Antenna Theory and Design* (3rd ed.).
   - RF antenna beamwidth
   - Pattern analysis

### Standards

8. **ITU-R P.525-4.** "Calculation of free-space attenuation."
   - FSPL formula standardization
   - International Telecommunication Union

9. **FCC 47 CFR §2.1.** Definitions (EIRP)
   - Federal Communications Commission
   - US regulatory definition

10. **CODATA 2018.** Fundamental Physical Constants
    - c, h, k_B values
    - NIST reference: https://physics.nist.gov/cuu/Constants/

### Heritage Missions (for parameter justification)

11. **NASA LCRD** (Laser Communications Relay Demonstration, 2021)
    - 1550 nm wavelength
    - 1.2 Gbps demonstrated
    - LEO-GEO optical relay

12. **ESA EDRS** (European Data Relay System, 2016)
    - 1.8 Gbps optical ISL
    - <5 μrad pointing accuracy
    - Operational heritage

13. **SpaceX Starlink** (2019-present)
    - Ka-band ISL at 32 GHz
    - 5,000+ satellites
    - Operational constellation

14. **Iridium NEXT** (2018)
    - Ka-band ISL
    - 66-satellite constellation
    - Proven crosslink technology

### Component Datasheets (for typical values)

15. **Hamamatsu G8931 Series** InGaAs APD
    - η = 0.3-0.5 at 1550 nm
    - Used for quantum efficiency justification

16. **Tesat CubeLCT** specifications
    - 1.8 Gbps capability
    - 7.3 kg mass, <25W power
    - Optical terminal heritage

17. **Viasat ArcLight Ka-band Terminals**
    - 30-40 cm deployable antennas
    - Smallsat RF heritage

---

**END OF DOCUMENT #23**

**Document Control:**
- Version: 1.0
- Date: November 2025
- Author: Trade Study Analysis
- Purpose: Complete reference for Assignment 4 formulas, sources, and logic flow
