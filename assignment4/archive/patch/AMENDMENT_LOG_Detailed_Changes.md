# AMENDMENT LOG: Changes Made to HYBRID_SATELLITE_TRADE_STUDY_PROMPT

## Document Version Control
- **Original Document:** HYBRID_SATELLITE_TRADE_STUDY_PROMPT.md
- **Amended Document:** HYBRID_SATELLITE_TRADE_STUDY_PROMPT_AMENDED.md
- **Amendment Date:** November 12, 2025
- **Reason for Amendment:** Incorporate Excel template ("Laser_Link_Calculations_template.xlsx") structure and requirements

---

## SUMMARY OF MAJOR CHANGES

### 1. Added Critical Template Reference in Executive Instructions
**Location:** Top of document, Executive Instructions section

**Change Added:**
```
**CRITICAL: You have been provided with an Excel template ("Laser_Link_Calculations_template.xlsx") 
for laser link calculations. Follow its structure and methodology for the optical analysis, and create 
an equivalent template structure for the RF analysis.**
```

**Rationale:** Establishes template as authoritative reference that must be followed, not optional guidance.

---

### 2. Updated Mission Parameters with Template Corrections
**Location:** Mission Parameters section

**Changes:**
- **Data Rate:** Added explicit note "**(UPDATE from 10 Gbps in template)**" after 1 Gbit/sec requirement
- **Range:** Added note "**(UPDATE from 1000 km in template)**" for 250 km specification

**Rationale:** Template has different default values (1000 km range, 10 Gbps rate) that must be changed for this assignment.

---

### 3. Enhanced Optical Communications Engineer Role
**Location:** Engineering Analysis Team, Section 2

**Major Additions:**

#### 3a. Detector-Level Analysis Requirements
**Added:**
- **Detector-level analysis:** photoelectrons/BIT, quantum efficiency, photons/BIT
- **Photon energy calculation:** h×f (Planck's constant × frequency)

**Rationale:** Template uses photon-counting approach starting from photoelectrons/bit, not just power levels.

#### 3b. Template Formula Specification
**Added:**
- **Gain calculations using template formula:** Gt = (π×Dt/λ)², Gr = (π×Dr/λ)²

**Rationale:** Template uses specific gain formula (π×D/λ)² rather than approximations or other formulations.

#### 3c. Detailed Loss Breakdown
**Added:**
- **Detailed loss breakdown:** pointing error loss, line in/out losses, atmospheric loss

**Rationale:** Template explicitly separates these losses rather than combining into generic "implementation loss."

#### 3d. New Deliverables
**Added:**
- Complete optical link budget **using provided Excel template structure**
- Modified Excel template with correct parameters (250 km range, 1 Gbps rate)
- **Detector analysis:** quantum efficiency requirements, photoelectron calculations

**Rationale:** Ensures optical analysis follows template structure exactly.

---

### 4. Enhanced RF Engineer Role
**Location:** Engineering Analysis Team, Section 1

**Major Additions:**

#### 4a. Template Creation Requirement
**Added:**
- **Create RF link budget template analogous to provided optical template**
- **Excel-format RF link budget following same structure as optical template**

**Rationale:** RF analysis should mirror optical template structure for direct comparison.

---

### 5. Enhanced PAT Engineer Role
**Location:** Engineering Analysis Team, Section 3

**Addition:**
- **Pointing error loss analysis:** quantify -3 dB loss assumption from template
- **Pointing loss budget breakdown:** static bias, dynamic jitter, tracking errors

**Rationale:** Template uses -3 dB pointing loss default; PAT engineer must validate this is achievable.

---

### 6. Complete Restructuring of Link Budget Section
**Location:** Phase 2: Individual Link Budget Analysis

This is the most extensive change. The entire section was restructured to follow template format.

### 6a. NEW Optical Link Budget Structure

**Replaced previous optical link budget format with two-step template-based approach:**

**STEP 1: Detector Requirements Table** (NEW)
```
Symbol | Parameter | Calculation | Linear | Log Value
Q      | Req Photoelectrons/BIT | 40 | 16.0 dB
η      | Detector Quantum Efficiency | 0.3 | -5.23 dB
n      | Req. Photons/BIT | Q/η | 133.33 | 21.25 dB
λ      | Wavelength (micron) | 1.55
f      | Frequency (Hz) | c/λ | 1.935E+14
hν     | h*freq (W-s/photon) | h×f
J/b    | Joules/BIT | n×h×f
f      | BIT rate (1/s) | 1.00E+09 (UPDATE from 1E+10)
Preq   | Power required at receiver | (J/b)×f
```

**Rationale:** Template begins with detector-level requirements and builds up to system level. This is fundamentally different from typical power-based link budgets.

**STEP 2: Link Budget Calculation Table** (RESTRUCTURED)
```
Symbol | Parameter | Linear | Log Value
Pt     | Tx Power (W)
R      | Intersatellite distance (m) | 250000 (UPDATE from 1000000)
Ls     | Free Space Loss
Dt     | Tx aperture diameter (m)
Dr     | Rx aperture diameter (m)
Gt     | Tx Gain (π²Dt/λ)² | (π×Dt/λ)²
Gr     | Rx Gain (π²Dr/λ)² | (π×Dr/λ)²
Lpt    | Pointing error Loss | -3.00 dB (typical)
Lo     | Other Losses (line in/out) | -6 dB (typical)
       | atmospheric loss | 0.00 dB (vacuum)
Pr     | Rx power
M      | Margin (Pr-Preq) | Pr - Preq
```

**Key Changes from Original:**
1. Uses template symbols (Pt, R, Ls, Dt, Dr, Gt, Gr, Lpt, Lo, Pr, M)
2. Explicit gain formula: (π×Dt/λ)²
3. Separate line loss (-6 dB) from pointing loss (-3 dB)
4. Margin calculation as Pr - Preq (not arbitrary target)
5. All parameters in template format (Linear | Log Value columns)

### 6b. NEW Critical Template Parameters Section

**Added entirely new section:**
```
**Critical Excel Template Parameters to Adjust:**
- Change intersatellite distance from 1000 km to **250 km**
- Change BIT rate from 10 Gbps to **1 Gbps** (1.00E+09)
- Verify/adjust quantum efficiency (0.3 is typical for InGaAs APD at 1550nm)
- Verify/adjust required photoelectrons/BIT (40 is typical for BER ~10⁻⁹)
```

**Rationale:** Critical instructions for modifying template to match assignment requirements.

---

### 7. Updated Required Information Table
**Location:** Phase 2, after link budget formulas

**Major Changes:**

#### 7a. Added Notes Column
**Added:** "Notes" column with template-specific comments

**Examples:**
- "Template uses meters" for aperture diameter
- "Template uses dBW" for power
- "Template formula" for gain calculations
- "**UPDATE from 1000km in template**" for range
- "**UPDATE from 10 Gbps**" for bit rate

#### 7b. Added Template-Specific Parameters
**New rows added:**
- Detector req: 40 photoelec/bit (from template)
- Req. photons/BIT: 133.33 (from template calculation)
- Line/Feed losses: Separate row showing -6 dB for optical (from template)

#### 7c. Modified Gain Formula Row
**Changed:** 
- From: "Beamwidth/Divergence"
- To: "Gain formula: (πD/λ)²" with explicit note "Template formula"

**Rationale:** Emphasizes using template's specific formula, not approximations.

---

### 8. Enhanced Sensitivity Analysis Section
**Location:** Phase 2, Sensitivity Analysis

**Added for Optical:**
- **Pointing error loss:** -1 dB to -6 dB (template uses -3 dB) - NEW
- **Quantum efficiency:** 0.2 to 0.5 - NEW
- **Required photoelectrons/BIT:** 30 to 50 - NEW
- **Line losses:** -3 dB to -10 dB (template uses -6 dB) - NEW

**Rationale:** These are template-specific parameters that should be sensitivity-tested.

---

### 9. Added Section-Level Template References Throughout

**Locations:** Multiple sections throughout document

**Pattern of additions:**
- Section 2 (Optical Link Analysis): "#### 2.1 Link Budget (Following Excel Template)"
- Section 2: NEW subsection "#### 2.2 Detector Analysis"
- Section 2: NEW subsection "#### 2.4 Loss Budget Breakdown"
- Output format instructions updated with template references

**Rationale:** Constant reminders that template structure must be followed.

---

### 10. NEW Detector Analysis Subsection
**Location:** Section 2 (Optical Link Analysis), NEW subsection 2.2

**Entirely new content added:**
```
#### 2.2 Detector Analysis
- Photoelectron requirements justification (BER target)
- Quantum efficiency selection (InGaAs APD vs PMT)
- Photon energy calculations (h×f methodology)
- Power required at receiver derivation
```

**Rationale:** Template's detector-level approach requires dedicated analysis section.

---

### 11. Expanded Loss Budget Breakdown
**Location:** Section 2 (Optical), Section 3 (RF)

**For Optical (NEW structure):**
```
#### 2.4 Loss Budget Breakdown
- **Free space loss:** calculation and value
- **Pointing error loss:** -3 dB assumption and sensitivity
- **Line in/out losses:** -6 dB breakdown (coupling, filters, detectors)
- **Atmospheric loss:** 0 dB (vacuum path)
- **Total losses:** sum and impact on margin
```

**Original had:** Generic "loss budget" without template-specific breakdowns.

**Rationale:** Template explicitly separates these losses; analysis must address each.

---

### 12. Modified Comparison Matrix Structure
**Location:** Section 4, Comparison Tables

**Changes to main comparison table:**

#### 12a. Changed Header
**From:** "Optical (Laser)" 
**To:** "Optical (Template-Based)"

**Rationale:** Emphasizes that optical analysis follows template structure.

#### 12b. Added Template-Specific Rows
**New rows:**
- Detector/Noise Metric: "η=[X], n=[X] photons/bit" vs "Ts=[X] K"
- Required Power/C/N₀: "[X] dBW" vs "[X] dB-Hz" with note "Different"

**Rationale:** Highlights fundamental difference in optical vs RF metrics.

#### 12c. Loss Breakdown Detail
**Changed:**
- From single "Total Path Loss" row
- To: Separate rows for "Pointing Loss", "Other Losses", "Total Path Loss"

**Rationale:** Matches template's explicit loss separation.

---

### 13. NEW Appendix Sections

### 13a. NEW Appendix A: Optical Formulas (Template Format)
**Location:** Appendices, NEW section A.1

**Added complete formula set matching template:**
```
// Detector Requirements
Q_photoelectrons_per_bit = 40
eta_quantum_efficiency = 0.3
n_photons_per_bit = Q / eta
[... etc following template structure ...]
```

**Rationale:** Provides exact template formulas for reproducibility.

### 13b. NEW Appendix D: Excel Template Modifications
**Location:** Appendices, entirely NEW appendix

**Contents:**
```
#### **Appendix D: Excel Template Modifications**

**Required Changes to Provided Optical Template:**

1. **Range (Cell location TBD):**
   - Current value: 1000000 m (1000 km)
   - **Change to: 250000 m (250 km)**
   - Impact: -6 dB improvement in free space loss

2. **Data Rate (Cell location TBD):**
   - Current value: 1.00E+10 bps (10 Gbps)
   - **Change to: 1.00E+09 bps (1 Gbps)**
   - Impact: -10 dB reduction in required receiver power

[... continues with verification items ...]
```

**Rationale:** Provides clear instructions for modifying the actual Excel file.

---

### 14. Updated Constraints & Quality Standards
**Location:** Near end of document

**Additions:**
- ✅ **Follow Excel template structure for optical link budget**
- ✅ **Create equivalent template for RF link budget**
- ✅ **Modify template parameters: 250 km range, 1 Gbps rate**
- ✅ **Template-Consistent:** Optical analysis follows provided Excel structure
- ✅ **Template-Modified:** Document changes made to Excel template

**Rationale:** Adds template compliance to quality criteria.

---

### 15. Enhanced Usage Instructions
**Location:** Usage Instructions section

**NEW subsection added:**
```
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
```

**Rationale:** Explicit instructions on how to use and follow the template.

---

### 16. Updated Final Deliverable Checklist
**Location:** Final Deliverable Checklist section

**Added checklist items:**
- [ ] **Excel template reviewed and modifications documented**
- [ ] **Optical link budget follows template structure exactly**
- [ ] **RF link budget uses analogous template format**
- [ ] **Template parameters updated:** 250 km range, 1 Gbps rate
- [ ] **Detector analysis complete:** photoelectrons/bit, quantum efficiency, photons/bit
- [ ] **Loss breakdown matches template structure:** pointing, line, atmospheric
- [ ] **Template modification log included in Appendix D**
- [ ] Formulas provided in appendix **(matching template format)**

**Rationale:** Ensures template requirements are verified before submission.

---

### 17. Updated Success Criteria
**Location:** Success Criteria section

**Added criteria:**
- 🎯 **Follow Template Structure:** Optical analysis exactly matches Excel template methodology
- 🎯 **Create RF Equivalent:** RF link budget uses analogous template format
- 🎯 **Document Modifications:** Clear log of changes made to template parameters
- 🎯 **Include Detector Physics:** Photon-level calculations following template approach
- 🎯 **Maintain Consistency:** RF and optical analyses comparable and directly comparable

**Rationale:** Template compliance is now a success criterion.

---

### 18. Updated Technique Citation
**Location:** End of document, technique citation

**Changed from:**
```
<source>Liu et al. (2021); Schulhoff et al. (2024); Claude Code Best Practices (2024)</source>
```

**To:**
```
<source>Liu et al. (2021); Schulhoff et al. (2024); Claude Code Best Practices (2024); 
Course-Provided Excel Template (2024)</source>
```

**Rationale:** Acknowledges template as authoritative source material.

---

## QUANTITATIVE SUMMARY OF CHANGES

### Lines/Sections Added:
- **Major new sections:** 3 (Detector Analysis, Loss Breakdown Detail, Template Modifications Appendix)
- **New subsections:** ~12 across document
- **New table rows:** ~8 in comparison matrices
- **New checklist items:** 8
- **New formula sections:** 1 complete section
- **New instructions:** 2 major instruction blocks

### Lines/Sections Modified:
- **Mission Parameters:** 2 parameters with UPDATE notes
- **Engineer roles:** All 4 roles enhanced
- **Link budget structure:** Complete restructure (~200 lines)
- **Comparison tables:** Restructured with new rows
- **All major sections:** Added template references

### Text Added Approximately:
- **New content:** ~3,000 words
- **Modified content:** ~1,500 words
- **Total document growth:** ~40% larger than original

---

## KEY PHILOSOPHICAL CHANGES

### 1. From "Optional Reference" to "Mandatory Structure"
**Before:** Template mentioned as "might be helpful"
**After:** Template is authoritative structure that MUST be followed

### 2. From Power-Based to Detector-Based (Optical)
**Before:** Traditional power budget approach
**After:** Photon-counting detector-first approach (photoelectrons → photons → energy → power)

### 3. From Generic Loss Terms to Explicit Breakdown
**Before:** Combined "implementation losses"
**After:** Separated pointing (-3 dB), line (-6 dB), atmospheric (0 dB)

### 4. From Approximations to Template Formulas
**Before:** Various gain formulas acceptable
**After:** Must use template formula G = (πD/λ)²

### 5. From Any Structure to Parallel Structure
**Before:** RF and optical could use different formats
**After:** RF must mirror optical template structure for comparison

---

## RATIONALE FOR CHANGES

### Primary Drivers:
1. **Template Consistency:** Assignment provides specific template → must follow it
2. **Reproducibility:** Using template ensures grading consistency
3. **Learning Objectives:** Template teaches specific methodology (detector-based approach)
4. **Parameter Alignment:** Template has wrong defaults that must be corrected
5. **Comparison Fairness:** Parallel structures enable apples-to-apples comparison

### Expected Impact:
- **Clarity:** Explicit template instructions reduce ambiguity
- **Quality:** Template provides validated formulas and structure
- **Completeness:** Detector analysis was missing from original prompt
- **Professionalism:** Following provided templates demonstrates attention to requirements

---

## VALIDATION CHECKLIST

Before using amended prompt, verify:

✅ Template file is available for reference
✅ Template modifications (250 km, 1 Gbps) are clearly documented
✅ Optical link budget follows template structure exactly
✅ RF link budget uses analogous structure
✅ Detector analysis (photoelectrons, QE, photons) is included
✅ Loss breakdown (pointing, line, atmospheric) matches template
✅ Gain formula (πD/λ)² matches template
✅ All template parameters are explicitly called out
✅ Margin calculation (Pr - Preq) matches template approach
✅ Appendix D documents template modifications

---

## CONCLUSION

The amended prompt transforms the template from supplementary reference material into the primary structural framework for the optical analysis. This ensures:

1. **Compliance** with assignment expectations
2. **Consistency** with provided materials
3. **Completeness** of detector-level analysis
4. **Comparability** through parallel RF structure
5. **Reproducibility** through explicit formulas and modifications

The ~40% expansion in content ensures every template-specific requirement is explicitly addressed while maintaining the original prompt's multi-agent, tree-of-thoughts, and self-consistency framework.

---

**Document prepared by:** AI Assistant (Claude)  
**Date:** November 12, 2025  
**Original prompt credit:** User synthesis from multiple AI outputs  
**Template source:** Course instructor (SPCE 5085)
