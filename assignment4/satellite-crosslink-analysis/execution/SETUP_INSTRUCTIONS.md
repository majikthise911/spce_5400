# SETUP INSTRUCTIONS
## How to Execute the Satellite Crosslink Trade Study

---

## Overview

You have a comprehensive prompt engineering framework and need to execute a satellite crosslink trade study. This guide shows you exactly how to organize files and run the analysis.

---

## Step 1: Organize Your Files

### Create Project Directory Structure

```
satellite-crosslink-analysis/
│
├── prompts/
│   ├── HYBRID_SATELLITE_TRADE_STUDY_PROMPT.md (your original)
│   ├── PATCH_DOCUMENT_Template_Integration.md
│   ├── PATCHES_9-17_CORRECTED.md
│   └── HYBRID_SATELLITE_TRADE_STUDY_PROMPT_AMENDED.md (after applying patches)
│
├── templates/
│   ├── Laser_Link_Calculations_template.xlsx (original from professor)
│   └── Laser_Link_Calculations_template_MODIFIED.xlsx (after changes)
│
├── execution/
│   ├── EXECUTE_TRADE_STUDY.md (created for you)
│   └── SETUP_INSTRUCTIONS.md (this file)
│
└── outputs/
    └── (Claude Code will generate files here)
```

### Required Files Checklist

Before starting, you must have:

- [ ] **HYBRID_SATELLITE_TRADE_STUDY_PROMPT.md** (original) OR  
- [ ] **HYBRID_SATELLITE_TRADE_STUDY_PROMPT_AMENDED.md** (patched version)
- [ ] **Laser_Link_Calculations_template.xlsx** (from professor)
- [ ] **EXECUTE_TRADE_STUDY.md** (execution wrapper)
- [ ] Claude Code CLI installed and working

---

## Step 2: Apply Patches (If Not Done Yet)

### Option A: Quick Patches (30 minutes)

If you want to patch manually:

1. Open `HYBRID_SATELLITE_TRADE_STUDY_PROMPT.md` in your text editor
2. Open `PATCH_DOCUMENT_Template_Integration.md` (patches 1-7)
3. Open `PATCHES_9-17_CORRECTED.md` (patches 8-18)
4. Apply patches sequentially (follow the patch documents)
5. Save as `HYBRID_SATELLITE_TRADE_STUDY_PROMPT_AMENDED.md`

**Critical patches to prioritize:**
- PATCH 1: Critical template instruction
- PATCH 7: Complete link budget restructure (THE BIG ONE)
- PATCH 12: Add Appendix D

### Option B: Use Original + Point Claude to Patches

If you don't want to manually patch:

1. Keep original `HYBRID_SATELLITE_TRADE_STUDY_PROMPT.md`
2. Also provide the patch documents to Claude Code
3. Tell it: "Apply patches from PATCH_DOCUMENT_Template_Integration.md and PATCHES_9-17_CORRECTED.md to the original prompt as you execute"

**This is easier but slightly less clean.**

---

## Step 3: Prepare Excel Template

### Manual Method (Recommended - 2 minutes)

1. Open `Laser_Link_Calculations_template.xlsx` in Excel
2. Find the cell with intersatellite distance (currently 1000000 m or 1000 km)
   - Change to: **250000 m** or **250 km**
3. Find the cell with data rate (currently 1.00E+10 bps or 10 Gbps)
   - Change to: **1.00E+09 bps** or **1 Gbps**
4. Save as: `Laser_Link_Calculations_template_MODIFIED.xlsx`
5. Keep both files (original and modified)

### Programmatic Method (If Claude Code Prefers)

Let Claude Code read the template and note the values need changing:
- It should handle the modifications in its calculations
- But you'll need to manually update the actual Excel file for submission

---

## Step 4: Run Claude Code CLI

### Method 1: Direct Execution (Simple)

From your project directory:

```bash
cd satellite-crosslink-analysis/execution/

claude-code "Read and execute EXECUTE_TRADE_STUDY.md. The comprehensive methodology is in ../prompts/HYBRID_SATELLITE_TRADE_STUDY_PROMPT_AMENDED.md and the Excel template is in ../templates/Laser_Link_Calculations_template.xlsx. Modify template parameters (250km range, 1Gbps rate) and generate complete trade study report."
```

### Method 2: Interactive Session (Recommended for Large Tasks)

```bash
cd satellite-crosslink-analysis/execution/

claude-code
```

Then in the Claude Code session:

```
> Read EXECUTE_TRADE_STUDY.md
> Confirm you understand the 5-phase execution plan
> Begin Phase 1: Read the comprehensive prompt and examine Excel template
```

Let it work through phases, checking in between phases.

### Method 3: Chunked Execution (Most Control)

Execute in smaller pieces:

```bash
# Phase 1 & 2: Optical Analysis
claude-code "Read EXECUTE_TRADE_STUDY.md Phase 2. Perform optical link budget analysis following the Excel template structure. Modify range to 250km and rate to 1Gbps."

# Phase 3: RF Analysis  
claude-code "Read EXECUTE_TRADE_STUDY.md Phase 3. Perform RF link budget analysis with analogous structure to optical template."

# Phase 4: Trade Analysis
claude-code "Read EXECUTE_TRADE_STUDY.md Phase 4. Compare optical vs RF, perform sensitivity analysis and scenario analysis."

# Phase 5: Final Report
claude-code "Read EXECUTE_TRADE_STUDY.md Phase 5. Generate complete trade study report with all sections and appendices."
```

---

## Step 5: Monitor Execution

### What to Watch For

**Phase 1 (Setup) - Should take ~5 min:**
- ✅ Claude reads comprehensive prompt
- ✅ Claude examines Excel template
- ✅ Claude notes parameter changes needed (250km, 1Gbps)
- ✅ Claude creates execution plan

**Phase 2 (Optical) - Should take ~20 min:**
- ✅ Starts with detector calculations (Q=40, η=0.3, n=133.33)
- ✅ Uses template formula G = (πD/λ)²
- ✅ Separates losses (pointing, line, atmospheric)
- ✅ Achieves ≥3 dB margin

**Phase 3 (RF) - Should take ~20 min:**
- ✅ Creates analogous structure to optical
- ✅ Uses Ka-band parameters (32 GHz)
- ✅ Parallel table format for comparison
- ✅ Achieves ≥3 dB margin

**Phase 4 (Trade) - Should take ~15 min:**
- ✅ Generates comparison matrices
- ✅ Performs sensitivity analysis
- ✅ Analyzes all 5 scenarios
- ✅ Creates weighted decision matrix

**Phase 5 (Documentation) - Should take ~20-30 min:**
- ✅ Generates all 6 sections
- ✅ Creates all 4 appendices
- ✅ Includes Appendix D (template modifications)
- ✅ Performs self-consistency validation

### Red Flags (Stop and Correct)

🚨 **Claude is NOT following template structure:**
- Optical link budget doesn't start with photoelectrons/bit
- Using gain approximations instead of (πD/λ)²
- Combining losses instead of separating them
→ **Stop and remind it to follow Excel template exactly**

🚨 **Claude forgot parameter changes:**
- Using 1000 km range instead of 250 km
- Using 10 Gbps rate instead of 1 Gbps
→ **Stop and correct the parameters**

🚨 **Link margins are negative or unrealistic:**
- Margins should be ≥3 dB for at least one technology
- If both are negative, apertures/power need adjustment
→ **Review calculations, may need design iteration**

---

## Step 6: Review Outputs

### Expected Output Files

Claude Code should generate (in `/mnt/user-data/outputs/`):

1. **Satellite_Crosslink_Trade_Study_Report.md**
   - 3000+ words
   - 6 main sections
   - 4 appendices
   - Complete trade study

2. **Optical_Link_Budget.csv**
   - Detector requirements table
   - Link budget table
   - All calculations with formulas

3. **RF_Link_Budget.csv**
   - System parameters
   - Link budget table
   - Parallel structure to optical

4. **Comparison_Matrices.csv**
   - Side-by-side comparison
   - Weighted decision matrix
   - Scenario analysis results

5. **Modified_Laser_Link_Template.xlsx** (if automated)
   - Updated range: 250 km
   - Updated rate: 1 Gbps

### Quality Verification Checklist

Review the main report and verify:

#### Template Compliance:
- [ ] Optical analysis starts with photoelectrons/bit (Q=40)
- [ ] Uses quantum efficiency η=0.3
- [ ] Calculates photons/bit (n=133.33)
- [ ] Uses photon energy (h×f) approach
- [ ] Gain formula is G = (πD/λ)²
- [ ] Losses separated: pointing (-3dB), line (-6dB), atm (0dB)

#### Parameter Correctness:
- [ ] Range is 250 km (NOT 1000 km)
- [ ] Data rate is 1 Gbps (NOT 10 Gbps)
- [ ] These changes are documented in Appendix D

#### Completeness:
- [ ] All 6 sections present
- [ ] All 4 appendices present (especially Appendix D)
- [ ] Both link budgets complete with ≥3 dB margin
- [ ] 5 scenarios analyzed
- [ ] Self-consistency validation performed
- [ ] Clear recommendation with confidence level

#### Technical Quality:
- [ ] Calculations are traceable
- [ ] Assumptions documented
- [ ] Formulas provided
- [ ] Units included everywhere
- [ ] Numbers are realistic (not absurd values)

---

## Step 7: Post-Processing

### If Everything Looks Good:

1. **Export to PDF:**
   - Convert main report to PDF for submission
   - Include supporting CSV files as appendices

2. **Update Excel Template:**
   - If not done automatically, manually update original template
   - Document changes in worksheet
   - Include modified version in submission

3. **Create Summary Slide:**
   - One-page summary of recommendation
   - Key comparison table
   - Decision rationale

### If Issues Found:

**Issue: Calculations seem wrong**
→ Review link budget formulas
→ Check parameter values (250km, 1Gbps)
→ Verify template formula usage

**Issue: Missing sections**
→ Identify which sections missing
→ Re-run specific phases
→ Merge outputs

**Issue: Recommendation unclear**
→ Check self-consistency validation
→ Review comparison matrix scores
→ Ensure quantitative justification

**Issue: Template not followed**
→ Highlight specific deviations
→ Point Claude to template structure
→ Re-run optical analysis (Phase 2)

---

## Step 8: Submission Preparation

### Final Deliverables Package

Your submission should include:

1. **Main Report (PDF)**
   - Satellite_Crosslink_Trade_Study_Report.pdf
   - ~10-15 pages with appendices

2. **Supporting Calculations**
   - Optical_Link_Budget.csv or .xlsx
   - RF_Link_Budget.csv or .xlsx

3. **Modified Excel Template**
   - Laser_Link_Calculations_template_MODIFIED.xlsx
   - With highlighted changes

4. **Optional: Source Prompt**
   - HYBRID_SATELLITE_TRADE_STUDY_PROMPT_AMENDED.md
   - Shows your methodology framework

### Quality Final Check

Before submitting:

✅ Read through entire report (does it make sense?)  
✅ Check all tables have data (no blank cells)  
✅ Verify calculations (spot-check a few key values)  
✅ Confirm template modifications documented  
✅ Ensure recommendation is clear and justified  
✅ Proofread for typos and formatting  

---

## Troubleshooting Guide

### Problem: Claude Code won't start

**Solution:**
```bash
# Check Claude Code is installed
which claude-code

# If not installed, install it
# [Follow Claude Code installation instructions]

# Check you're in right directory
pwd
ls -la

# Try verbose mode
claude-code --verbose
```

### Problem: Claude Code can't find files

**Solution:**
```bash
# Use absolute paths
claude-code "Read /full/path/to/EXECUTE_TRADE_STUDY.md"

# Or ensure files are in current directory
cp ../prompts/*.md .
cp ../templates/*.xlsx .
claude-code "Read EXECUTE_TRADE_STUDY.md"
```

### Problem: Excel template errors

**Solution:**
- Manually modify Excel file before running
- Provide modified file directly
- Or let Claude work with CSV version of data

### Problem: Output is incomplete

**Solution:**
- Run phases individually (Method 3)
- Check for error messages
- Increase token/time limits if available
- Break into smaller chunks

### Problem: Calculations don't match expectations

**Solution:**
- Verify input parameters (250km, 1Gbps)
- Check formula implementation
- Compare to Excel template manually
- Review assumptions in Appendix B

---

## Tips for Success

### Do's ✅
- Apply patches before execution (saves confusion)
- Modify Excel template manually (2 min vs. debugging)
- Monitor execution (catch errors early)
- Use interactive mode for large tasks
- Check outputs after each phase
- Keep original files for reference

### Don'ts ❌
- Don't skip reading the comprehensive prompt
- Don't forget to modify template parameters
- Don't ignore red flags during execution
- Don't submit without verification
- Don't panic if first attempt isn't perfect (iterate!)

---

## Time Estimates

**Preparation:** 30-45 minutes
- Apply patches: 30 min (or skip if using original + patches)
- Modify Excel: 2 min
- Setup files: 3 min

**Execution:** 80-90 minutes
- Claude Code runtime: 60-80 min
- Monitoring/corrections: 10-20 min

**Review & Polish:** 30-45 minutes
- Quality check: 15 min
- Fix issues: 10-15 min
- Format for submission: 15 min

**Total:** 2.5 - 3 hours end-to-end

---

## Getting Help

**If you get stuck:**

1. **Check the execution file:** EXECUTE_TRADE_STUDY.md has phase-by-phase instructions
2. **Review patch documents:** Ensure template requirements are clear
3. **Verify file structure:** All required files in right locations
4. **Try simplified command:** Start with just Phase 1-2
5. **Manual intervention:** If automation struggles, do calculations in Python/Excel yourself using the prompt as guide

**Remember:** The comprehensive prompt is a framework for HOW to think about the problem. Even if automation doesn't work perfectly, you can use it as a detailed guide for manual analysis.

---

## Final Checklist Before Execution

Run through this before starting:

- [ ] All files organized in project directory
- [ ] Patches applied (or ready to reference)
- [ ] Excel template modified (250km, 1Gbps)
- [ ] Claude Code CLI working
- [ ] EXECUTE_TRADE_STUDY.md ready
- [ ] You understand the 5-phase execution plan
- [ ] You know how to monitor progress
- [ ] You have 3 hours available
- [ ] You're ready to troubleshoot if needed

**If all checked → You're ready to execute! 🚀**

---

## Quick Start Command

Once everything is set up:

```bash
cd satellite-crosslink-analysis/execution/

claude-code "Execute EXECUTE_TRADE_STUDY.md completely. Read the comprehensive methodology from ../prompts/HYBRID_SATELLITE_TRADE_STUDY_PROMPT_AMENDED.md, analyze ../templates/Laser_Link_Calculations_template.xlsx (modify to 250km range and 1Gbps rate), perform complete optical and RF link budgets, conduct trade analysis, and generate full report with all sections and appendices in ../outputs/"
```

**Good luck with your assignment! 📡🛰️**
