# QUICK REFERENCE: Key Amendments to Hybrid Prompt

## Files Created
1. **HYBRID_SATELLITE_TRADE_STUDY_PROMPT_AMENDED.md** - Full amended prompt (use this for your assignment)
2. **AMENDMENT_LOG_Detailed_Changes.md** - Complete list of all changes (18 major categories)
3. **This file** - Quick reference summary

---

## Top 10 Most Important Changes

### 1. ✅ TEMPLATE IS NOW MANDATORY
**Critical instruction added at top of prompt:**
"You have been provided with an Excel template for laser link calculations. Follow its structure and methodology."

### 2. ✅ DETECTOR-LEVEL ANALYSIS REQUIRED
**NEW calculation step for optical:**
- Start with photoelectrons/BIT (Q = 40)
- Calculate quantum efficiency (η = 0.3)
- Derive photons/BIT (n = Q/η = 133.33)
- Calculate photon energy (h×f)
- Derive required power (Preq)

### 3. ✅ TEMPLATE PARAMETERS MUST BE UPDATED
**Two critical corrections needed:**
- Range: 1000 km → **250 km** (affects free space loss by -6 dB)
- Data rate: 10 Gbps → **1 Gbps** (affects required power by -10 dB)

### 4. ✅ SPECIFIC GAIN FORMULA REQUIRED
**Must use template formula:**
- G = (π × D / λ)²
- NOT approximations or other formulas

### 5. ✅ LOSS BREAKDOWN MUST BE EXPLICIT
**Separate these losses (don't combine):**
- Pointing error: -3 dB (template default)
- Line losses (in/out): -6 dB (template default)
- Atmospheric: 0 dB (vacuum)

### 6. ✅ RF MUST MIRROR OPTICAL STRUCTURE
**Create RF link budget that:**
- Uses same table format as optical template
- Has equivalent loss breakdown
- Enables direct side-by-side comparison

### 7. ✅ NEW SECTION REQUIRED: Detector Analysis
**Must include for optical:**
- Photoelectron requirements justification
- Quantum efficiency selection (APD vs PMT)
- Photon energy calculations (h×f)
- Power required at receiver derivation

### 8. ✅ NEW APPENDIX REQUIRED: Template Modifications
**Appendix D must document:**
- What you changed in the template
- Why you changed it
- Impact of changes on link budget

### 9. ✅ MARGIN CALCULATION CHANGED
**Optical margin now:**
- M = Pr - Preq (received power minus required power)
- NOT arbitrary "achieve 3 dB" target
- Preq comes from detector calculation

### 10. ✅ ENHANCED COMPARISON TABLE
**New rows added:**
- Detector requirements (photoelec/bit, QE, photons/bit)
- Separate loss breakdowns (pointing, line, atmospheric)
- Different metrics (dBW for optical, dB-Hz for RF)

---

## What Stays the Same

✅ Multi-Agent Coordination approach (4 engineers)
✅ Tree-of-Thoughts (3 branches per technology)
✅ Self-Consistency validation (3 reasoning paths)
✅ 5 scenario analysis (baseline, range, rate, SWaP, hybrid)
✅ Output structure (6 main sections + appendices)
✅ Quality standards and success criteria
✅ Usage instructions framework

---

## Critical Template Values from Screenshot

From the Excel template image you provided:

**Detector Parameters:**
- Req Photoelectrons/BIT: **40** (16.0 dB)
- Detector Quantum Efficiency: **0.3** (-5.23 dB)
- Req. Photons/BIT: **133.33** (21.25 dB) [calculated as 40/0.3]

**System Parameters (NEED TO CHANGE):**
- Wavelength: 1.55 μm (correct, keep this)
- Intersatellite distance: 1000000 m → **change to 250000 m**
- BIT rate: 1.00E+10 → **change to 1.00E+09**

**Loss Parameters:**
- Pointing error loss: **-3.00 dB** (verify achievable)
- Other losses (line in/out): **-6.00 dB** (typical)
- Atmospheric loss: **0.00 dB** (vacuum, correct)

**Aperture Examples from Template:**
- Tx aperture: 0.1 m (10 cm) - shown in template
- Rx aperture: 0.07 m (7 cm) - shown in template
- These are examples; you'll calculate actual sizes needed

---

## Step-by-Step Usage

### Step 1: Open Excel Template
- Locate "Laser_Link_Calculations_template.xlsx"
- Review current structure and values

### Step 2: Modify Template
- Change intersatellite distance: 1000 km → 250 km
- Change BIT rate: 10 Gbps → 1 Gbps
- Document these changes in your report (Appendix D)

### Step 3: Use Amended Prompt
- Copy "HYBRID_SATELLITE_TRADE_STUDY_PROMPT_AMENDED.md"
- Paste into AI (Claude, GPT-4, etc.)
- Attach modified Excel template if possible

### Step 4: Follow Template Structure
For optical analysis:
1. Start with detector requirements (photoelectrons → photons)
2. Calculate photon energy and required power
3. Build link budget using template formula G = (πD/λ)²
4. Separate losses (pointing, line, atmospheric)
5. Calculate margin as M = Pr - Preq

### Step 5: Create RF Equivalent
- Mirror optical template structure
- Use analogous table format
- Enable direct comparison

### Step 6: Complete Analysis
- Follow all other prompt instructions (agents, branches, scenarios)
- Document template modifications in Appendix D
- Verify all template requirements in final checklist

---

## Common Mistakes to Avoid

❌ **Don't** ignore the template structure
✅ **Do** follow it exactly for optical

❌ **Don't** use approximations for gain
✅ **Do** use template formula G = (πD/λ)²

❌ **Don't** combine losses into generic term
✅ **Do** separate pointing, line, and atmospheric

❌ **Don't** skip detector analysis
✅ **Do** include photoelectron/photon calculations

❌ **Don't** forget to update template parameters
✅ **Do** change range to 250km and rate to 1 Gbps

❌ **Don't** use different structures for optical vs RF
✅ **Do** create parallel template formats

❌ **Don't** forget to document template changes
✅ **Do** include Appendix D with modification log

---

## Quick Checklist Before Submitting

Analysis must include:
- [ ] Detector requirements table (Q, η, n, h×f)
- [ ] Template formula for gain: G = (πD/λ)²
- [ ] Separate loss terms: pointing (-3 dB), line (-6 dB), atm (0 dB)
- [ ] Modified template parameters: 250 km, 1 Gbps
- [ ] Margin calculation: M = Pr - Preq
- [ ] RF link budget in analogous template format
- [ ] Appendix D documenting template modifications
- [ ] All template values explained/justified

---

## Why These Changes Matter

1. **Grade Protection:** Following provided template shows you understood assignment requirements

2. **Methodology Accuracy:** Template uses validated detector-based approach for optical links

3. **Reproducibility:** Grader can verify your work against same template

4. **Learning Objectives:** Assignment designed to teach specific template methodology

5. **Professional Practice:** Real engineers use and modify provided analysis tools

---

## Questions to Ask Your AI

When using the amended prompt, you might ask:

1. "Have you reviewed the Excel template structure?"
2. "Are you using the template formula G = (πD/λ)² for optical gain?"
3. "Did you start with photoelectrons/bit for the optical detector analysis?"
4. "Have you separated pointing loss, line loss, and atmospheric loss?"
5. "Did you document the template parameter changes (1000km→250km, 10Gbps→1Gbps)?"
6. "Is your RF link budget using a parallel structure to the optical template?"

---

## Final Notes

- **Template is authoritative** - when in doubt, follow template structure
- **Document everything** - especially template modifications
- **Parallel structure** - RF should mirror optical format
- **Detector-first** - optical analysis starts with photoelectrons, not power
- **Explicit losses** - separate pointing, line, and atmospheric
- **Formula specific** - use G = (πD/λ)², not approximations

---

**Files Location:**
- Full amended prompt: `/mnt/user-data/outputs/HYBRID_SATELLITE_TRADE_STUDY_PROMPT_AMENDED.md`
- Detailed changes: `/mnt/user-data/outputs/AMENDMENT_LOG_Detailed_Changes.md`
- This quick reference: `/mnt/user-data/outputs/QUICK_REFERENCE_Amendments.md`

**Use the amended prompt (file #1) for your assignment!**
