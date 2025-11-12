# PATCH DOCUMENT: Excel Template Integration
## For HYBRID_SATELLITE_TRADE_STUDY_PROMPT.md

---

## HOW TO USE THIS PATCH DOCUMENT

### Method 1: Manual Application (Recommended)
1. Open your original `HYBRID_SATELLITE_TRADE_STUDY_PROMPT.md` in a text editor
2. Work through patches sequentially (PATCH 1 → PATCH 2 → etc.)
3. For each patch:
   - Find the location (use section headers or line numbers as guides)
   - Apply the change (INSERT, REPLACE, or MODIFY as indicated)
   - Mark the patch as ✅ complete
4. Save as `HYBRID_SATELLITE_TRADE_STUDY_PROMPT_v2.md`

### Method 2: Find & Replace
- For simple text modifications, use Find & Replace in your editor
- Search for the "FIND:" text
- Replace with the "REPLACE WITH:" text

### Patch Format Legend:
- 📍 **LOCATION:** Where to make the change
- ➕ **INSERT:** Add new text at this location
- 🔄 **REPLACE:** Replace existing text with new text
- ✏️ **MODIFY:** Edit existing text (small change)
- 📝 **NOTE:** Important context or rationale

---

## PATCHES IN ORDER OF APPLICATION

---

### PATCH 1: Critical Template Instruction (Executive Instructions)
**Priority:** 🔴 CRITICAL  
**Difficulty:** 🟢 Easy

📍 **LOCATION:** After line "This trade study will use a **Multi-Agent + Tree-of-Thoughts + Self-Consistency** approach..."

➕ **INSERT THIS NEW PARAGRAPH:**
```
**CRITICAL: You have been provided with an Excel template ("Laser_Link_Calculations_template.xlsx") for laser link calculations. Follow its structure and methodology for the optical analysis, and create an equivalent template structure for the RF analysis.**
```

📝 **NOTE:** This goes right after the methodology statement, before the "---" separator

---

### PATCH 2: Mission Parameters - Range Update
**Priority:** 🔴 CRITICAL  
**Difficulty:** 🟢 Easy

📍 **LOCATION:** Mission Parameters section, line with "Inter-satellite separation: 250 km"

✏️ **MODIFY:**
```
FIND:
- Inter-satellite separation: 250 km

REPLACE WITH:
- Inter-satellite separation: 250 km (**UPDATE from 1000 km in template**)
```

---

### PATCH 3: Mission Parameters - Data Rate Update
**Priority:** 🔴 CRITICAL  
**Difficulty:** 🟢 Easy

📍 **LOCATION:** Mission Parameters section, line with "Required data rate: 1 Gbit/sec minimum"

✏️ **MODIFY:**
```
FIND:
- Required data rate: 1 Gbit/sec minimum

REPLACE WITH:
- Required data rate: 1 Gbit/sec minimum (**UPDATE from 10 Gbps in template**)
```

---

### PATCH 4: RF Engineer Role Enhancement
**Priority:** 🟡 MEDIUM  
**Difficulty:** 🟢 Easy

📍 **LOCATION:** Section "### 1. RF/Ka-Band Link Engineer", under "Analysis Responsibilities:" (end of list)

➕ **ADD THIS BULLET (at end of responsibilities list):**
```
- **Create RF link budget template analogous to provided optical template**
```

➕ **ADD THIS BULLET (at end of deliverables list):**
```
- **Excel-format RF link budget following same structure as optical template**
```

---

### PATCH 5: Optical Engineer Role Enhancement
**Priority:** 🔴 CRITICAL  
**Difficulty:** 🟢 Easy

📍 **LOCATION:** Section "### 2. Optical Communications Engineer"

🔄 **REPLACE "Analysis Responsibilities:" SECTION WITH:**
```
**Analysis Responsibilities:**
- Laser link budget calculation at 1550 nm **following provided Excel template structure**
- **Detector-level analysis:** photoelectrons/BIT, quantum efficiency, photons/BIT
- **Photon energy calculation:** h×f (Planck's constant × frequency)
- Telescope aperture sizing (transmit and receive optics)
- Beam divergence and spot size at 250 km range
- Laser transmitter power requirements
- **Gain calculations using template formula:** Gt = (π×Dt/λ)², Gr = (π×Dr/λ)²
- Detector sensitivity (APD/PMT selection, quantum efficiency)
- Background noise sources (solar, lunar, earth albedo)
- Acquisition, Tracking, and Pointing (ATP) system complexity
- Pointing jitter and bias budget (microradians)
- **Detailed loss breakdown:** pointing error loss, line in/out losses, atmospheric loss
- Modulation schemes (OOK, PPM, DPIM) and coding gain
```

🔄 **REPLACE "Deliverables:" SECTION WITH:**
```
**Deliverables:**
- Complete optical link budget **using provided Excel template structure**
- Modified Excel template with correct parameters (250 km range, 1 Gbps rate)
- Telescope aperture specifications (Tx/Rx diameters in meters)
- Laser transmitter specifications (power, wavelength, divergence)
- Pointing accuracy requirements (microradians or arcseconds)
- ATP system architecture and acquisition time estimates
- System mass estimate (kg) and power budget (W)
- Technology Readiness Level (TRL) assessment
- **Detector analysis:** quantum efficiency requirements, photoelectron calculations
```

---

### PATCH 6: PAT Engineer Role Enhancement
**Priority:** 🟡 MEDIUM  
**Difficulty:** 🟢 Easy

📍 **LOCATION:** Section "### 3. Pointing, Acquisition & Tracking (PAT) Engineer", under "Analysis Responsibilities:" (end of list)

➕ **ADD THESE BULLETS:**
```
- **Pointing error loss analysis:** quantify -3 dB loss assumption from template
```

➕ **ADD TO DELIVERABLES:**
```
- **Pointing loss budget breakdown:** static bias, dynamic jitter, tracking errors
```

---

### PATCH 7: Complete Link Budget Restructure (LARGEST CHANGE)
**Priority:** 🔴 CRITICAL - MOST IMPORTANT PATCH  
**Difficulty:** 🔴 Complex (but just copy-paste)

📍 **LOCATION:** Section "### Phase 2: Individual Link Budget Analysis"

🔄 **REPLACE THE ENTIRE SUBSECTION "#### **Link Equation Components**" THROUGH THE END OF "#### **Required Information Table**" WITH THE FOLLOWING:**

```markdown
#### **Link Equation Components**

### **OPTICAL Link Budget (Following Excel Template Structure):**

**Step 1: Detector Requirements**

The Excel template uses a detector-first approach. Follow this structure:

```
Symbol | Parameter | Calculation | Linear | Log Value
-------|-----------|-------------|--------|----------
Q      | Req Photoelectrons/BIT | [Specify based on BER] | 40 | 16.0 dB
η      | Detector Quantum Efficiency | [APD or PMT selection] | 0.3 | -5.23 dB
n      | Req. Photons/BIT | Q/η | 133.33 | 21.25 dB
λ      | Wavelength (micron) | Given | 1.55 | -
f      | Frequency (Hz) | c/λ | 1.935E+14 | -
hν     | h*freq (W-s/photon) | Planck's constant × f | [Calculate] | [dB]
J/b    | Joules/BIT | n × h × f | [Calculate] | [dB]
Rb     | BIT rate (1/s) | Given | 1.00E+09 | - (UPDATE from 1E+10)
Preq   | Power required at receiver (W) | (J/b) × Rb | [Calculate] | [dBW]
```

**Key Template Values:**
- **Q = 40 photoelectrons/bit** (typical for BER ~10⁻⁹)
- **η = 0.3** (typical for InGaAs APD at 1550nm)
- **n = Q/η = 133.33 photons/bit**
- **Preq** is calculated from photon energy × photon rate

**Step 2: Link Budget Calculation**

```
Symbol | Parameter | Linear | Log Value | Notes
-------|-----------|--------|-----------|-------
Pt     | Tx Power (W) | [Calculate] | [dBW] | Design parameter
R      | Intersatellite distance (m) | 250000 | - | UPDATE from 1000000 in template
Ls     | Free Space Loss | 1/(4πR/λ)² | [dB] | Geometric spreading
Dt     | Tx aperture diameter (m) | [Calculate] | - | Design parameter
Dr     | Rx aperture diameter (m) | [Calculate] | - | Design parameter
Gt     | Tx Gain | (π×Dt/λ)² | [dBi] | Template formula - USE THIS
Gr     | Rx Gain | (π×Dr/λ)² | [dBi] | Template formula - USE THIS
Lpt    | Pointing error Loss | [Calculate] | -3.00 dB | Template default (verify achievable)
Lo     | Other Losses (line in/out) | [Calculate] | -6.00 dB | Template default
       | Atmospheric loss | 1.0 | 0.00 dB | Vacuum path (LEO-LEO)
Pr     | Rx power | Pt × Ls × Gt × Gr × Lpt × Lo | [dBW] | Received power
M      | Margin (Pr-Preq) | Pr - Preq | [dB] | Target ≥3 dB
```

**Critical Notes:**
- **MUST use template gain formula:** G = (π×D/λ)², NOT approximations
- **MUST separate losses:** pointing (-3dB), line (-6dB), atmospheric (0dB)
- **Margin = Pr - Preq** (where Preq comes from detector calculation)
- **Update range:** 250 km (not 1000 km from template)
- **Update rate:** 1 Gbps (not 10 Gbps from template)

---

### **RF Link Budget (Ka-band):**

Create analogous structure to optical template for direct comparison.

**Step 1: System Parameters**
```
Symbol | Parameter | Value | Units
-------|-----------|-------|------
f      | Frequency | 32 GHz | Hz
λ      | Wavelength | 0.00937 m | m
R      | Range | 250 km | m
Rb     | Data Rate | 1 Gbps | bps
```

**Step 2: Transmitter Section**
```
Symbol | Parameter | Value | Units | Notes
-------|-----------|-------|-------|-------
Pt     | Tx Power | [Calculate] | W (dBW) | Design parameter
Dt     | Tx Antenna Diameter | [Calculate] | m | Design parameter
ηt     | Tx Antenna Efficiency | 0.55-0.65 | - | Typical for small sat
Gt     | Tx Antenna Gain | ηt(πDt/λ)² | dBi | Note: includes efficiency
EIRP   | EIRP | Pt + Gt | dBW | Equivalent isotropic radiated power
Lpt    | Pointing Loss | [Calculate] | dB | From beamwidth
Lf     | Feed losses | -0.5 to -1.0 | dB | Typical
```

**Step 3: Path Loss Section**
```
Symbol | Parameter | Value | Units
-------|-----------|-------|------
FSPL   | Free Space Path Loss | 20log₁₀(4πR/λ) | dB
Latm   | Atmospheric Loss | 0.00 | dB (vacuum)
Lmisc  | Miscellaneous Losses | -2 to -3 | dB
```

**Step 4: Receiver Section**
```
Symbol | Parameter | Value | Units
-------|-----------|-------|------
Dr     | Rx Antenna Diameter | [Calculate] | m
ηr     | Rx Antenna Efficiency | 0.55-0.65 | -
Gr     | Rx Antenna Gain | ηr(πDr/λ)² | dBi
Ts     | System Noise Temperature | 500-800 | K (typical Ka-band)
G/T    | Figure of Merit | Gr - 10log₁₀(Ts) | dB/K
```

**Step 5: Link Performance**
```
Symbol | Parameter | Calculation | Units
-------|-----------|-------------|------
Pr     | Received Power | EIRP - FSPL - Losses + Gr | dBW
k      | Boltzmann's constant | -228.6 | dBW/K/Hz
C/N₀   | Carrier-to-Noise Density | Pr - k - 10log₁₀(Ts) | dB-Hz
Eb/N₀  | Required for BER 10⁻⁹ | ~9.6 dB (with coding) | dB
M      | Margin | C/N₀ - 10log₁₀(Rb) - Eb/N₀ | dB
```

---

#### **Required Information Table**

This table enables direct comparison between technologies:

| Parameter | RF (Ka-band) | Optical (Template-Based) | Units | Notes |
|-----------|--------------|--------------------------|-------|-------|
| **Transmitter** | | | | |
| Power output | [Calculate] | [Calculate] | W or dBW | Template uses dBW |
| Frequency/Wavelength | 32 GHz / 0.0094m | 193.5 THz / 1.55μm | - | - |
| Aperture diameter | [Calculate] | [Calculate] | m | Template uses meters |
| Gain formula | ηt(πDt/λ)² | (πDt/λ)² | - | Template formula |
| Gain value | [Calculate] | [Calculate] | dBi | - |
| Beamwidth/Divergence | [Calculate] | [Calculate] | deg / μrad | - |
| **Path** | | | | |
| Range | 250 | 250 | km | **UPDATE from 1000km** |
| Free-space loss | [Calculate] | [Calculate] | dB | - |
| Pointing loss | [Calculate] | -3.00 (typical) | dB | Template default |
| Line/Feed losses | -0.5 to -1.0 | -6.00 | dB | Template shows -6dB |
| Atmospheric loss | 0.00 (vacuum) | 0.00 (vacuum) | dB | LEO-to-LEO |
| **Receiver** | | | | |
| Aperture diameter | [Calculate] | [Calculate] | m | - |
| Gain formula | ηr(πDr/λ)² | (πDr/λ)² | - | Template formula |
| Gain value | [Calculate] | [Calculate] | dBi | - |
| Noise metric | Ts = 500-800 K | η = 0.3 | K / - | Different approaches |
| Detector requirement | - | Q = 40 photoelec/bit | - | Template parameter |
| Req. photons/BIT | - | n = 133.33 | - | Template: Q/η |
| Required C/N₀ or Preq | [Calculate] | [Calculate] | dB-Hz / dBW | Different metrics |
| **Performance** | | | | |
| BIT rate | 1.00E+09 | 1.00E+09 | bps | **UPDATE from 10 Gbps** |
| Link margin | [Calculate] | [Calculate] | dB | Target ≥3 dB |
| Spectral efficiency | [Calculate] | [Calculate] | bps/Hz | - |
| Modulation/Coding | 16-APSK/LDPC | OOK or PPM | - | - |
```

📝 **NOTE:** This is the largest and most important patch. The new structure follows the Excel template methodology exactly.

---

### PATCH 8: Enhanced Sensitivity Analysis
**Priority:** 🟡 MEDIUM  
**Difficulty:** 🟢 Easy

📍 **LOCATION:** Section "#### **Sensitivity Analysis (Per Technology)**", under "**For Optical:**"

➕ **ADD THESE BULLETS TO THE OPTICAL SENSITIVITY LIST:**
```
- Quantum efficiency: 0.2 to 0.5
- Required photoelectrons/BIT: 30 to 50
- Line losses: -3 dB to -10 dB (template uses -6 dB)
```

---

### PATCH 9: Section 2 - Add New Detector Analysis Subsection
**Priority:** 🟡 MEDIUM  
**Difficulty:** 🟢 Easy

📍 **LOCATION:** Section 2 (Optical Link Analysis), AFTER subsection "2.1 Link Budget..."

➕ **INSERT NEW SUBSECTION:**
```markdown
#### 2.2 Detector Analysis (Following Template Methodology)

**Detector Requirements:**
- **Photoelectron requirements justification:** Explain why Q=40 photoelectrons/bit is needed for target BER (typically 10⁻⁹)
- **Quantum efficiency selection:** Justify choice of detector (InGaAs APD typical η=0.3 at 1550nm, or consider PMT with different η)
- **Photons per bit calculation:** n = Q/η (template shows 133.33 photons/bit for Q=40, η=0.3)
- **Photon energy calculation:** E_photon = h×f where h = 6.626×10⁻³⁴ J·s (Planck's constant)
- **Energy per bit:** J/b = n × E_photon
- **Power required at receiver:** P_req = (J/b) × R_b where R_b = bit rate

**Detector Technology Trade:**
- **InGaAs APD:** η ≈ 0.3-0.5, good for 1550nm, moderate gain, lower noise
- **PMT (Photomultiplier Tube):** η ≈ 0.1-0.2, very high gain, higher noise
- **PIN Photodiode:** η ≈ 0.6-0.8, no internal gain, needs more laser power

**Template Calculation Flow:**
```
Q (photoelec/bit) → η (quantum efficiency) → n (photons/bit) → 
E_photon (J) → J/b (joules/bit) → P_req (W)
```

This detector-first approach is fundamental to the template methodology and differs from traditional power-based link budgets.
```

---

### PATCH 10: Section 2 - Enhance Loss Budget Breakdown
**Priority:** 🟡 MEDIUM  
**Difficulty:** 🟢 Easy

📍 **LOCATION:** Section 2 (Optical Link Analysis), find subsection about losses (may be 2.4 or similar)

🔄 **IF THERE'S A GENERIC "LOSS BUDGET" SUBSECTION, REPLACE IT WITH:**
```markdown
#### 2.4 Loss Budget Breakdown (Per Template Structure)

The template explicitly separates losses. Analyze each:

**Free Space Loss:**
- Formula: L_s = (λ/4πR)² 
- For λ=1.55μm, R=250km: Calculate specific value
- Physical meaning: Geometric spreading of beam

**Pointing Error Loss (Template default: -3.00 dB):**
- Breakdown:
  - Static pointing bias: [X] μrad
  - Dynamic jitter: [X] μrad RMS
  - Tracking error: [X] μrad
- Total pointing loss: [Calculate based on beam divergence]
- **Verify -3 dB is achievable** with spacecraft ACS + FSM
- If not achievable, adjust to realistic value (may be -4 or -5 dB)

**Line In/Out Losses (Template default: -6.00 dB):**
- Breakdown:
  - Transmit coupling loss: ~2 dB (laser to telescope)
  - Optical train losses: ~1 dB (mirrors, filters)
  - Receive coupling loss: ~2 dB (telescope to detector)
  - Detector insertion loss: ~1 dB
- Total: ~6 dB (matches template)
- Adjust if using different optical design

**Atmospheric Loss (Vacuum path: 0.00 dB):**
- LEO-to-LEO crosslink passes through vacuum
- No atmospheric absorption or scattering
- Only applies if path crosses atmosphere (not this scenario)

**Total Link Loss Budget:**
- Free space loss: [X] dB
- Pointing error: -3 dB (or adjusted value)
- Line losses: -6 dB (or adjusted value)  
- Atmospheric: 0 dB
- **Total:** [Sum] dB

**Sensitivity:** Show how margin changes if pointing loss varies from -1 to -6 dB
```

---

### PATCH 11: Section 4 - Update Comparison Table
**Priority:** 🟡 MEDIUM  
**Difficulty:** 🟡 Moderate

📍 **LOCATION:** Section 4 (Direct Comparison), main comparison table "#### 4.1 Side-by-Side Link Budget Comparison"

✏️ **MODIFY TABLE HEADER:**
```
FIND:
| Parameter | Optical (Laser) | RF (Ka-band) |

REPLACE WITH:
| Parameter | Optical (Template-Based) | RF (Ka-band) |
```

➕ **ADD THESE ROWS TO THE TABLE (after "Receiver" section):**
```
| Noise/Detector Metric | η=0.3, Q=40, n=133.33 | Ts=[X] K | Different approaches |
| Detector/Receiver Type | InGaAs APD | LNA + Mixer | - |
```

➕ **MODIFY LOSS ROWS TO SHOW BREAKDOWN:**
```
REPLACE:
| Total Path Loss | [X] dB | [X] dB | [X] dB |

WITH THREE SEPARATE ROWS:
| Pointing Loss | -3.00 dB (template) | [X] dB | [X] dB |
| Line/Feed Losses | -6.00 dB (template) | [X] dB | [X] dB |
| Total Path Loss | [X] dB | [X] dB | [X] dB |
```

---

### PATCH 12: Add New Appendix D
**Priority:** 🟡 MEDIUM  
**Difficulty:** 🟢 Easy

📍 **LOCATION:** After Appendix C (References), before final sections

➕ **INSERT ENTIRE NEW APPENDIX:**
```markdown
#### **Appendix D: Excel Template Modifications**

This appendix documents all changes made to the provided "Laser_Link_Calculations_template.xlsx" file.

**Required Parameter Changes:**

**1. Intersatellite Distance**
- **Template Value:** 1,000,000 m (1000 km)
- **Assignment Value:** 250,000 m (250 km)
- **Cell Location:** [Specify after examining template]
- **Impact on Link Budget:** 
  - Free space loss improves by ~6 dB (factor of 4 reduction in range)
  - Formula: ΔL = 20×log₁₀(R₁/R₂) = 20×log₁₀(1000/250) = 12 dB improvement in path
  - But geometric dilution is squared, so net effect is 6 dB

**2. Data Rate (Bit Rate)**
- **Template Value:** 1.00E+10 bps (10 Gbps)
- **Assignment Value:** 1.00E+09 bps (1 Gbps)  
- **Cell Location:** [Specify after examining template]
- **Impact on Link Budget:**
  - Required power at receiver decreases by 10 dB (factor of 10 reduction)
  - P_req = (Joules/bit) × (bits/second), so 10× reduction in rate = -10 dB
  - This creates +10 dB improvement in margin (or allows reducing transmit power/apertures)

**Verified Parameters (Keep Template Defaults):**

**3. Quantum Efficiency (η)**
- **Template Value:** 0.3 (-5.23 dB)
- **Status:** ✅ Keep - appropriate for InGaAs APD at 1550nm
- **Rationale:** Typical commercial APDs achieve η = 0.3-0.5, template uses conservative value

**4. Required Photoelectrons/BIT (Q)**
- **Template Value:** 40 (16.0 dB)
- **Status:** ✅ Keep - appropriate for BER target of 10⁻⁹
- **Rationale:** Standard requirement for acceptable bit error rate in communications

**5. Pointing Error Loss**
- **Template Value:** -3.00 dB
- **Status:** ⚠️ Verify achievable with spacecraft ACS + FSM
- **Rationale:** Aggressive but feasible with fine steering mirror; may need to increase to -4 or -5 dB if pointing capability is limited
- **Recommendation:** Perform pointing accuracy analysis to confirm

**6. Line In/Out Losses**
- **Template Value:** -6.00 dB
- **Status:** ✅ Keep - reasonable for optical system
- **Rationale:** Typical breakdown: coupling (-2dB), optics (-1dB), coupling (-2dB), detector (-1dB)

**Summary of Changes:**

| Parameter | Template | Assignment | Change | Impact |
|-----------|----------|------------|--------|--------|
| Range | 1000 km | 250 km | -75% | +6 dB margin improvement |
| Data Rate | 10 Gbps | 1 Gbps | -90% | +10 dB margin improvement |
| QE (η) | 0.3 | 0.3 | None | Verified appropriate |
| Q (photoelec) | 40 | 40 | None | Verified appropriate |
| Pointing Loss | -3 dB | -3 dB | None | Verify achievable |
| Line Losses | -6 dB | -6 dB | None | Verified appropriate |

**Net Impact:** 
- Reducing range (1000→250 km) and data rate (10→1 Gbps) provides ~16 dB of improvement
- This allows either: (1) smaller apertures, (2) lower power, (3) larger margin, or (4) combination
- Design optimization should explore these trades

**Modified Template Filename:** `Laser_Link_Calculations_template_MODIFIED.xlsx`

**Verification Checklist:**
- [ ] Range changed to 250 km
- [ ] Data rate changed to 1 Gbps  
- [ ] All other parameters verified as appropriate
- [ ] Formulas and cell references checked (no broken links)
- [ ] Link margin calculated and documented
- [ ] Template modifications documented in this appendix
```

---

### PATCH 13: Update Constraints & Quality Standards
**Priority:** 🟢 LOW  
**Difficulty:** 🟢 Easy

📍 **LOCATION:** Section "## Constraints & Quality Standards"

➕ **ADD TO CONSTRAINTS LIST:**
```
✅ **Follow Excel template structure for optical link budget**  
✅ **Create equivalent template for RF link budget**  
✅ **Modify template parameters: 250 km range, 1 Gbps rate**
```

➕ **ADD TO QUALITY CRITERIA LIST:**
```
✅ **Template-Consistent:** Optical analysis follows provided Excel structure  
✅ **Template-Modified:** Document changes made to Excel template
```

---

### PATCH 14: Update Usage Instructions
**Priority:** 🟢 LOW  
**Difficulty:** 🟢 Easy

📍 **LOCATION:** Section "## Usage Instructions", after the existing instructions

➕ **INSERT NEW SUBSECTION:**
```markdown
### **Critical Template Instructions:**

**For Optical Link Budget:**
- Start by reading the provided Excel template structure
- Follow the template's calculation methodology exactly
- Modify only the specified parameters (range, data rate)
- Preserve the template's loss breakdown structure
- Use template formulas: G = (πD/λ)², not approximations

**For RF Link Budget:**
- Create an analogous template structure
- Use similar row/column organization
- Include equivalent loss breakdown
- Enable direct side-by-side comparison
- Maintain same margin calculation format (dB)

**Template Parameter Modifications:**
1. Open "Laser_Link_Calculations_template.xlsx"
2. Change intersatellite distance: 1000 km → 250 km
3. Change data rate: 10 Gbps → 1 Gbps
4. Verify all other parameters are appropriate
5. Document changes in Appendix D of your report
```

---

### PATCH 15: Update Final Deliverable Checklist
**Priority:** 🟢 LOW  
**Difficulty:** 🟢 Easy

📍 **LOCATION:** Section "## Final Deliverable Checklist"

➕ **ADD THESE ITEMS TO THE CHECKLIST (insert near the top):**
```
- [ ] **Excel template reviewed and modifications documented**
- [ ] **Optical link budget follows template structure exactly**
- [ ] **RF link budget uses analogous template format**
- [ ] **Template parameters updated:** 250 km range, 1 Gbps rate
- [ ] **Detector analysis complete:** photoelectrons/bit, quantum efficiency, photons/bit
- [ ] **Loss breakdown matches template structure:** pointing, line, atmospheric
- [ ] **Template modification log included in Appendix D**
```

---

### PATCH 16: Update Success Criteria
**Priority:** 🟢 LOW  
**Difficulty:** 🟢 Easy

📍 **LOCATION:** Section "## Success Criteria"

➕ **ADD THESE ITEMS TO THE LIST:**
```
🎯 **Follow Template Structure:** Optical analysis exactly matches Excel template methodology  
🎯 **Create RF Equivalent:** RF link budget uses analogous template format  
🎯 **Document Modifications:** Clear log of changes made to template parameters  
🎯 **Include Detector Physics:** Photon-level calculations following template approach
```

---

### PATCH 17: Update Technique Citation
**Priority:** 🟢 LOW  
**Difficulty:** 🟢 Easy

📍 **LOCATION:** Very end of document, in the `<source>` tag

✏️ **MODIFY:**
```
FIND:
<source>Liu et al. (2021); Schulhoff et al. (2024); Claude Code Best Practices (2024)</source>

REPLACE WITH:
<source>Liu et al. (2021); Schulhoff et al. (2024); Claude Code Best Practices (2024); Course-Provided Excel Template (2024)</source>
```

---

## PATCH APPLICATION CHECKLIST

Use this to track your progress:

### Critical Patches (Do First):
- [ ] PATCH 1: Critical template instruction (Executive)
- [ ] PATCH 2: Range update (Mission Parameters)
- [ ] PATCH 3: Data rate update (Mission Parameters)
- [ ] PATCH 5: Optical engineer role (MOST DETAILED)
- [ ] PATCH 7: Complete link budget restructure (**LARGEST CHANGE**)

### Medium Priority Patches:
- [ ] PATCH 4: RF engineer role
- [ ] PATCH 6: PAT engineer role
- [ ] PATCH 8: Sensitivity analysis additions
- [ ] PATCH 9: New detector analysis subsection
- [ ] PATCH 10: Loss budget breakdown enhancement
- [ ] PATCH 11: Comparison table updates
- [ ] PATCH 12: New Appendix D

### Low Priority Patches (Polish):
- [ ] PATCH 13: Constraints & quality standards
- [ ] PATCH 14: Usage instructions
- [ ] PATCH 15: Deliverable checklist
- [ ] PATCH 16: Success criteria
- [ ] PATCH 17: Technique citation

---

## VERIFICATION STEPS

After applying all patches:

1. **Search for template-related terms:**
   - Search document for "template" - should appear ~20-30 times
   - Search for "photoelectron" - should appear in detector analysis
   - Search for "(πD/λ)²" - should appear in gain formulas
   - Search for "250 km" - should have UPDATE note
   - Search for "1 Gbps" - should have UPDATE note

2. **Check structural completeness:**
   - Executive instructions mention template ✅
   - Phase 2 has detector-first approach ✅
   - Section 2 has detector analysis subsection ✅
   - Appendix D exists ✅
   - Comparison tables show template-based optical ✅

3. **Verify formula consistency:**
   - Optical gain uses (πD/λ)² not approximations ✅
   - Losses are separated (pointing, line, atmospheric) ✅
   - Margin = Pr - Preq (not arbitrary target) ✅

---

## TROUBLESHOOTING

### If you can't find a section:
- Use your text editor's Find function (Ctrl+F / Cmd+F)
- Search for the section header or unique text
- Line numbers are approximate - use section names as primary guide

### If a patch doesn't fit exactly:
- Context is more important than exact line numbers
- Adapt the patch to your document structure
- Maintain the intent of the change

### If patches seem to overlap:
- Apply in the order listed
- Later patches may refine earlier ones
- Some patches add to the same section - that's intentional

---

## FINAL NOTES

**Most Critical Changes:**
1. PATCH 7 (Link Budget) - This is 90% of the technical work
2. PATCH 5 (Optical Engineer Role) - Defines new responsibilities
3. PATCH 12 (Appendix D) - Documents template modifications

**Time Estimate:**
- Critical patches: 30-45 minutes
- Medium patches: 15-20 minutes
- Low patches: 5-10 minutes
- **Total: ~60-75 minutes**

**Save Your Work:**
- Save as new filename: `HYBRID_SATELLITE_TRADE_STUDY_PROMPT_v2.md`
- Keep original for reference
- Consider version control (Git) if available

---

## QUICK START GUIDE

If you want to start immediately:

1. Open your original `HYBRID_SATELLITE_TRADE_STUDY_PROMPT.md`
2. Apply PATCH 1 (add critical template instruction at top)
3. Apply PATCH 7 (replace entire link budget section) ← **THIS IS THE BIG ONE**
4. Apply PATCH 12 (add Appendix D at end)
5. Apply remaining patches as time permits

Those three patches give you ~80% of the value. The rest are refinements and completeness.

---

**Ready to begin? Start with PATCH 1 and work your way down! ✅**
