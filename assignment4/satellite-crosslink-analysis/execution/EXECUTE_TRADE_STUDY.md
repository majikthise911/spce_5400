# EXECUTE SATELLITE CROSSLINK TRADE STUDY

## Mission
Perform comprehensive optical vs. RF (Ka-band) crosslink trade study for LEO satellite constellation following the methodology in `HYBRID_SATELLITE_TRADE_STUDY_PROMPT_AMENDED.md` (or apply patches to original if not yet amended).

---

## Required Files

Verify these files are in your working directory:

1. **HYBRID_SATELLITE_TRADE_STUDY_PROMPT_AMENDED.md** (or original + patches)
2. **Laser_Link_Calculations_template.xlsx**
3. This execution file

---

## System Parameters (From Assignment)

**Orbital Configuration:**
- Altitude: 500 km LEO
- Inter-satellite separation: 250 km
- Required data rate: 1 Gbps
- Platform: Small satellites

**Excel Template Modifications Required:**
- Range: 1000 km → **250 km**
- Data rate: 10 Gbps → **1 Gbps**

---

## Execution Instructions for Claude Code

### Phase 1: Setup & Planning (5 minutes)

1. **Read the comprehensive prompt:**
   - Open and thoroughly read `HYBRID_SATELLITE_TRADE_STUDY_PROMPT_AMENDED.md`
   - Understand the multi-agent coordination framework
   - Note all requirements and deliverables

2. **Examine the Excel template:**
   - Open `Laser_Link_Calculations_template.xlsx`
   - Identify current parameters (1000 km range, 10 Gbps rate)
   - Understand the detector-first calculation methodology
   - Note: Q=40 photoelectrons/bit, η=0.3 quantum efficiency, n=133.33 photons/bit

3. **Create work plan:**
   - Identify which calculations to do first
   - Determine file structure for outputs
   - Plan code/spreadsheet approach

---

### Phase 2: Optical Link Budget (Following Template) (20 minutes)

**CRITICAL: Follow the Excel template structure exactly**

#### Step 1: Detector Requirements Calculation
```python
# Template approach: Start with detector
Q = 40                          # photoelectrons/bit
eta = 0.3                       # quantum efficiency
n = Q / eta                     # photons/bit = 133.33
wavelength = 1.55e-6            # meters
c = 2.998e8                     # speed of light
f = c / wavelength              # frequency
h = 6.626e-34                   # Planck's constant
E_photon = h * f                # energy per photon
J_per_bit = n * E_photon        # joules per bit
bit_rate = 1e9                  # 1 Gbps (MODIFIED from template)
P_req = J_per_bit * bit_rate    # required power at receiver
```

#### Step 2: Link Budget Calculation
```python
# Modified from template values
R = 250e3                       # range in meters (MODIFIED from 1000 km)

# Design parameters to optimize
P_tx = [CALCULATE]              # transmit power
D_tx = [CALCULATE]              # transmit aperture
D_rx = [CALCULATE]              # receive aperture

# Template formulas (USE THESE EXACTLY)
import numpy as np
wavelength = 1.55e-6
G_tx = (np.pi * D_tx / wavelength)**2     # Gain formula from template
G_rx = (np.pi * D_rx / wavelength)**2     # Gain formula from template
L_fs = (wavelength / (4 * np.pi * R))**2  # Free space loss

# Template loss values
L_pointing = -3.0               # dB (verify achievable)
L_line = -6.0                   # dB (template default)
L_atm = 0.0                     # dB (vacuum)

# Calculate received power
P_rx = P_tx * L_fs * G_tx * G_rx * 10**(L_pointing/10) * 10**(L_line/10)

# Margin
Margin_dB = 10*np.log10(P_rx / P_req)    # Target >= 3 dB
```

**Deliverable:** Complete optical link budget table following template structure

---

### Phase 3: RF Link Budget (Analogous Structure) (20 minutes)

Create RF link budget with parallel structure to optical template:

```python
# RF parameters
f_rf = 32e9                     # 32 GHz Ka-band
wavelength_rf = c / f_rf        # ~9.37 mm
R = 250e3                       # same range
bit_rate = 1e9                  # 1 Gbps

# Design parameters
P_tx_rf = [CALCULATE]
D_tx_rf = [CALCULATE]
D_rx_rf = [CALCULATE]
eta_ant = 0.6                   # antenna efficiency

# Gain calculations (with efficiency)
G_tx_rf = eta_ant * (np.pi * D_tx_rf / wavelength_rf)**2
G_rx_rf = eta_ant * (np.pi * D_rx_rf / wavelength_rf)**2

# Path loss
FSPL_dB = 20*np.log10(4*np.pi*R/wavelength_rf)

# Receiver
T_sys = 650                     # K (system noise temp)
k = 1.38e-23                    # Boltzmann constant
C_over_N0 = [CALCULATE]         # carrier to noise density
Eb_N0_req = 9.6                 # dB (for BER 10^-9 with coding)

# Margin
Margin_dB = C_over_N0 - 10*np.log10(bit_rate) - Eb_N0_req
```

**Deliverable:** Complete RF link budget table in analogous format

---

### Phase 4: Trade Analysis & Comparison (15 minutes)

Execute the following analyses:

1. **Side-by-side comparison:**
   - Aperture sizes (optical vs RF)
   - Transmit powers (optical vs RF)
   - Link margins (optical vs RF)
   - Pointing requirements (μrad vs degrees)
   - System mass and power estimates

2. **Sensitivity analysis:**
   - Optical: Vary pointing loss (-1 to -6 dB), QE (0.2-0.5), apertures (±50%)
   - RF: Vary pointing loss, transmit power (±3dB), antenna diameter (±50%)

3. **Scenario analysis:**
   - Baseline: 250 km, 1 Gbps
   - Extended range: 500 km
   - Higher rate: 10 Gbps  
   - SWaP constrained: <5kg, <20W
   - Hybrid approach

4. **Weighted decision matrix:**
   - Performance (25%)
   - SWaP (20%)
   - Pointing complexity (15%)
   - TRL (15%)
   - Scalability (10%)
   - Cost (10%)
   - Operations (5%)

**Deliverable:** Complete comparison matrices and trade analysis

---

### Phase 5: Recommendation & Documentation (20 minutes)

1. **Self-consistency validation:**
   - Reasoning path 1: Link budget optimization
   - Reasoning path 2: SWaP-constrained analysis
   - Reasoning path 3: Technology risk assessment
   - Check for 2-of-3 or 3-of-3 agreement

2. **Generate final recommendation:**
   - Primary technology choice
   - Confidence level (High/Medium/Low)
   - Justification with quantitative support
   - Alternative/fallback option
   - Implementation roadmap

3. **Create all deliverables:**
   - Executive summary (1-2 pages)
   - Section 1: Assumptions & Parameters
   - Section 2: RF Link Analysis
   - Section 3: Optical Link Analysis (with detector subsection & loss breakdown)
   - Section 4: System-Level Comparison
   - Section 5: Trade-Off Analysis
   - Section 6: Recommendation & Rationale
   - Appendix A: Formulas
   - Appendix B: Assumptions
   - Appendix C: References
   - Appendix D: Template Modifications

---

## Output Structure

Create these files in `/mnt/user-data/outputs/`:

1. **Satellite_Crosslink_Trade_Study_Report.md** - Main report (all sections)
2. **Optical_Link_Budget.csv** - Detailed optical calculations
3. **RF_Link_Budget.csv** - Detailed RF calculations
4. **Comparison_Matrices.csv** - All comparison data
5. **Sensitivity_Analysis_Plots.png** - Key sensitivity charts (if possible)
6. **Modified_Laser_Link_Template.xlsx** - Updated Excel template with 250km, 1Gbps

---

## Quality Checks

Before finalizing, verify:

✅ Optical link budget follows Excel template structure (detector-first)  
✅ Used template formula G = (πD/λ)² for optical gains  
✅ Separated losses: pointing (-3dB), line (-6dB), atmospheric (0dB)  
✅ RF link budget uses analogous structure  
✅ Template parameters modified: 250 km range, 1 Gbps rate  
✅ Detector analysis included (photoelectrons→photons→energy→power)  
✅ All scenarios analyzed (baseline + 4 variations)  
✅ Self-consistency validation performed  
✅ Link margin ≥3 dB for recommended technology  
✅ Appendix D documents all template changes  
✅ All assumptions documented with rationale  
✅ Calculations traceable and reproducible  

---

## Expected Runtime

**Total: ~80-90 minutes of computation**
- Phase 1 (Setup): 5 min
- Phase 2 (Optical): 20 min
- Phase 3 (RF): 20 min
- Phase 4 (Trade): 15 min
- Phase 5 (Documentation): 20-30 min

---

## Execution Command

**From project directory, run:**

```bash
claude-code "Execute the satellite crosslink trade study following EXECUTE_TRADE_STUDY.md. Read the comprehensive prompt methodology, modify the Excel template parameters, perform all calculations, and generate the complete trade study report with all sections and appendices."
```

**Or interactive mode:**

```bash
claude-code
> Read EXECUTE_TRADE_STUDY.md and begin the analysis
```

---

## Troubleshooting

**If Claude Code asks for clarification:**
- Point it to the comprehensive prompt for detailed methodology
- Remind it to follow the Excel template structure for optical
- Emphasize the two critical parameter changes (250km, 1Gbps)

**If calculations seem off:**
- Verify template formulas are being used: G = (πD/λ)²
- Check that detector-first approach is being followed
- Confirm range is 250km (not 1000km) and rate is 1Gbps (not 10Gbps)

**If Excel template can't be modified programmatically:**
- Manually change the two parameters in Excel
- Provide the modified file to Claude Code
- Have it read the modified values

---

## Success Criteria

You'll know it worked when you have:

📄 **Main Report** - Complete trade study (3000+ words, all 6 sections + appendices)  
📊 **Link Budgets** - Both optical (template-based) and RF with ≥3dB margin  
📈 **Comparison Data** - Quantitative comparison matrices  
🎯 **Clear Recommendation** - Justified choice with confidence level  
📋 **Template Documentation** - Appendix D showing modifications  

---

**Ready to execute! Good luck with your assignment! 🚀**
