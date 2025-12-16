# Phase 1: Requirements Analysis Complete

**Project**: RAD-AI Final Paper
**Date**: 2025-12-15
**Author**: Jordan Clayton

---

## File Verification Results (Gate 0)

**Files Found in `./final_paper/source_material/`:**
```
├── CubeSat__FinalReport2023 (example).pdf    ✓ PRIMARY STYLE REFERENCE
├── CubeSat__FinalReport2023 (example).md     ✓ Markdown version for parsing
├── problem_statement                          ✓ PRIMARY REQUIREMENTS
├── Ch1-3_Summary.md                          ✓ NASA CubeSat 101 summary
├── ch1-3 from nasa_csli_cubesat_101.md       ✓ Full NASA training material
├── CubeSat_Design_Specifications_Rev.14.1.md ✓ Official CubeSat standard
├── gsfc-hdbk-8007_mission_success_handbook_cubesat_missions.md ✓ NASA handbook
├── Building_Satellites_in_18_Months.md       ✓ Project management reference
```

**Assignment 3 Outline**: `./assignment3/submission/Jordan_Clayton_Project1_Draft_Outline r1.pdf` ✓ ACCESSIBLE

**GATE 0 STATUS**: ✓ ALL CRITICAL FILES FOUND → PROCEED

---

## Problem Statement Distillation

**Core Requirements (from problem_statement file):**

• **Design a CubeSat mission paper** that extends the Assignment 3 outline (RAD-AI: Radiation-Mitigated Edge AI for Autonomous Space Operations) into a complete final report following the example paper structure

• **Follow CubeSat 101 process** covering all sections from the NASA training material (Intro, Process, Mission Models) with sufficient detail to attract funding

• **Deliver 150-point final paper** (total project worth 200 pts including the 50-pt outline) by Dec 31, 2025

• **Match example paper depth and quality** — instructor feedback: "your outline is quite complete. Press forward with a design and provide as much detail as possible"

• **Success criteria**: Complete design paper with requirements, conceptual design alternatives, testing methodology, final design specifications, and supporting appendices

---

## Rubric Mapping Matrix

**Note**: No explicit rubric provided. Deriving grading criteria from:
1. Example paper structure (16 required sections)
2. Instructor feedback ("provide as much detail as possible")
3. CubeSat 101 process requirements
4. Standard engineering design paper expectations

| Rubric Criterion | Target Section(s) | Source Material | Completion Phase |
|------------------|-------------------|-----------------|------------------|
| Executive Summary (mission overview) | §1 | Outline p.3 | Batch 1 |
| Clear Objective & Problem Statement | §2.1, §2.2 | Outline p.3-5 | Batch 1 |
| Project Planning/Management | §3 | Outline p.5, CubeSat 101 Ch.2 | Batch 1 |
| Requirements Lists (5 categories) | §4.1.1-4.1.5 | Outline p.5-6, Example p.6-7 | Batch 1 |
| Conceptual Design Alternatives | §5.1-5.3 | Outline p.5-6, Example p.8-15 | Batch 2 |
| Testing Methods (Electrical) | §6 | Example p.16-20, NASA GEVS | Batch 2 |
| Testing Methods (Structural) | §7 | Example p.21-24, NASA GEVS | Batch 2 |
| Final Design Specifications | §8.1-8.3 | Outline p.5-6, Example p.25-33 | Batch 3 |
| Concept of Operations | §9 | Outline p.6-7, Example p.34 | Batch 3 |
| System Block Diagrams | §10 | Example p.35-37 | Batch 3 |
| Flight/Expected Results | §11 | Outline p.4, Example p.38-41 | Batch 3 |
| Conclusion | §12 | Outline p.8, Example p.42 | Batch 3 |
| Sponsor/Team Interactions | §13, §14 | Example p.43 (adapt for individual) | Batch 4 |
| References (properly formatted) | §15 | Outline p.8-11 (51 refs) | Batch 4 |
| Appendices A-D | §16 | Example p.44-63 | Batch 4 |
| Technical depth & citations | Throughout | All sources | All Batches |
| Professional tone/formatting | Throughout | Example paper style | All Batches |

---

## Content Allocation Strategy

### Section 1 - Executive Summary
```
├── Source: Outline p.3
├── Key technical content:
│   • RAD-AI 6U CubeSat mission overview
│   • Problem: COTS AI fails in radiation; rad-hard too slow
│   • Solution: RISC-V + AI accelerator with TMR/shielding
│   • Unique contribution: Real-time radiation-aware autonomous computing
│   • Cost/timeline: $100-120k, 3 years, free CSLI launch
├── Required citations: 3-5
├── Figures/tables needed: None
└── Target length: 300-400 words
```

### Section 2 - Introduction
```
├── Source: Outline p.3-5
├── 2.1 Objective
│   • Primary: Demonstrate AI-driven autonomous computing with radiation-aware operation in LEO for 12 months
│   • Secondary objectives (4 items from outline)
│   • Success criteria (minimum/baseline/full)
├── 2.2 Problem Statement
│   • Autonomy critical for Artemis/Mars Sample Return (6-44 min delays)
│   • Capability gap: RAD750 too slow, NVIDIA Jetson fails in radiation
│   • HPSC timeline creates 2025-2027 gap
│   • Market validation (Cosmic Shielding, AFRL partnerships)
├── Required citations: 10-15
├── Figures/tables needed: None
└── Target length: 800-1000 words
```

### Section 3 - Project Planning and Management
```
├── Source: Outline p.5, 7-8, CubeSat 101 Ch.2
├── Key technical content:
│   • Three-phase development approach
│   • Timeline: PDR (7-10 mo) → CDR (11-16) → Integration/Test (17-24) → FRR (25-30) → Ops (31-42)
│   • Hybrid strategy: COTS bus + custom AI payload
│   • Three units: ETU, FlatSat, two Flight Units
│   • Budget management with 20% reserve
│   • CSLI compliance requirements
├── Required citations: 5-8
├── Figures/tables needed: Gantt chart or timeline table
└── Target length: 600-800 words
```

### Section 4 - Problem Specifications
```
├── Source: Outline p.5-6, Example p.6-7 (structure), CubeSat specs
├── 4.1 Project Requirements
│   4.1.1 Communications Requirements List
│       • UHF transceiver specs (8W, 9600 bps)
│       • Amateur radio compatibility
│       • Ground segment (university UHF, SatNOGS backup)
│       • Data rates (target 100 MB/day)
│   4.1.2 Power Requirements List
│       • ~36W average, 15-30W AI peaks
│       • GaAs solar ~45W BOL
│       • 60 Wh Li-ion battery
│       • 20% margin
│   4.1.3 Telemetry and Control Requirements List
│       • Sensor data: RADFETs, cosmic ray telescope, temp/voltage
│       • Autonomous mode switching (<1 min latency)
│       • Data logging for post-mission analysis
│   4.1.4 Mechanical Requirements List
│       • 6U form factor (20×10×34 cm, <14 kg)
│       • 1.5U AI payload, 1.5U power, 3U bus allocation
│       • CDS Rev 14 compliance
│   4.1.5 Thermal Requirements List
│       • -40°C to +60°C operational range
│       • AI processor thermal management
│       • Battery temperature maintenance
├── Required citations: 8-12
├── Figures/tables needed: Requirements tables (5)
└── Target length: 1200-1500 words
```

### Section 5 - Conceptual Design
```
├── Source: Outline p.3-6, Example p.8-15
├── 5.1 Missions (evaluate alternatives like example)
│   • Mission Concept 1: Cloud detection (like Phi-Sat-1)
│   • Mission Concept 2: Radiation-aware autonomous computing (SELECTED)
│   • Mission Concept 3: Pure radiation monitoring
│   • Mission Concept 4: Star-field tracking only
│   • Selection rationale
├── 5.2 Electrical
│   • Main computer options (RISC-V vs ARM vs x86)
│   • AI accelerator options (FPGA vs GPU vs dedicated)
│   • Communications options (UHF vs S-band)
│   • Power system options
├── 5.3 Structure
│   • 6U configuration options
│   • Shielding approaches (selective vs full)
│   • Thermal management approaches
├── Required citations: 15-20
├── Figures/tables needed: Trade tables, block diagrams
└── Target length: 2000-2500 words
```

### Section 6 - Electrical Testing Methods and Results
```
├── Source: Example p.16-20, NASA GEVS [45], Outline p.6
├── Key technical content:
│   • Sensor integration & calibration methodology
│   • Radiation testing at LBNL (proton beam, TID, SEU)
│   • TMR validation testing
│   • Power system testing
│   • Communications range testing
│   • Software HIL simulation with radiation injection
│   • Monte Carlo TMR analysis
├── Required citations: 8-12
├── Figures/tables needed: Test setup photos/diagrams, results tables
└── Target length: 1500-2000 words
```

### Section 7 - Structural Testing Methods and Results
```
├── Source: Example p.21-24, NASA GEVS [45]
├── Key technical content:
│   • Vibration testing (14.1 Grms per GEVS)
│   • Thermal-vacuum testing (-40°C to +60°C)
│   • EMI/EMC testing
│   • Mechanical fit checks
│   • Shielding effectiveness verification
├── Required citations: 5-8
├── Figures/tables needed: Test setup, results graphs
└── Target length: 1000-1200 words
```

### Section 8 - Final Design
```
├── Source: Outline p.5-6, Example p.25-33
├── 8.1 Mission
│   • Selected mission: Radiation-aware autonomous AI computing
│   • 12-month operational timeline
│   • Three operational phases
├── 8.2 Electrical
│   • SiFive U74 RISC-V quad-core (1.5 GHz)
│   • Lattice CrossLink-NX FPGA AI accelerator
│   • TMR software implementation
│   • 2mm tantalum selective shielding
│   • Watchdog timers, EDAC
│   • Complete sensor package
│   • Power system design
│   • Communications system design
├── 8.3 Structure
│   • 6U allocation diagram
│   • Shielding placement
│   • Thermal design
│   • Mass budget
├── Required citations: 15-20
├── Figures/tables needed: Circuit diagrams, CAD renders, mass/power budgets
└── Target length: 2500-3000 words
```

### Section 9 - Concept of Operations
```
├── Source: Outline p.6-7, Example p.34
├── Key technical content:
│   • CONOPS diagram with operational phases
│   • Phase 1: Commissioning (Weeks 1-4)
│   • Phase 2: Characterization (Months 2-4)
│   • Phase 3: Science ops (Months 5-12)
│   • Autonomous mode transitions (Normal, Protected, Safe)
│   • Data flow from sensors to ground
├── Required citations: 3-5
├── Figures/tables needed: CONOPS diagram
└── Target length: 600-800 words
```

### Section 10 - System Block Definitions Diagram
```
├── Source: Example p.35-37
├── Key technical content:
│   • External system diagram (mission environment hierarchy)
│   • Internal system diagram (subsystem connections)
│   • Functional system diagram (data/power flow)
├── Required citations: 2-3
├── Figures/tables needed: 3 block diagrams
└── Target length: 600-800 words
```

### Section 11 - Flight Results (Expected/Simulated)
```
├── Source: Outline p.4, 6-7
├── Key technical content:
│   • Expected orbital parameters (400-600 km, 6-10 SAA passes daily)
│   • Predicted radiation environment (5-10 krad TID/year)
│   • Expected AI performance metrics
│   • Predicted mode transition behavior
│   • Simulated degradation curves
│   • Success criteria verification approach
├── Required citations: 5-8
├── Figures/tables needed: Simulation results, predicted curves
└── Target length: 1000-1200 words
```

### Section 12 - Conclusion
```
├── Source: Outline p.8
├── Key technical content:
│   • Summary of design achievements
│   • How RAD-AI addresses the 2025-2027 gap
│   • Contribution to NASA autonomy technology
│   • Lessons learned from design process
│   • Recommendations for future work
├── Required citations: 3-5
├── Figures/tables needed: None
└── Target length: 500-700 words
```

### Section 13 - Sponsor Interactions
```
├── Source: Adapt from Example p.43
├── Key technical content:
│   • Potential sponsors identified (SiFive, Cosmic Shielding, AFRL)
│   • University support structure
│   • Faculty advisor interactions
│   • Industry partnership approach
├── Required citations: 1-2
├── Figures/tables needed: None
└── Target length: 300-400 words
```

### Section 14 - Team Interactions
```
├── Source: Adapt from Example p.43
├── Key technical content:
│   • Individual project (single author)
│   • Course collaboration with instructor
│   • External consultation approach
│   • Resource utilization
├── Required citations: 0-1
├── Figures/tables needed: None
└── Target length: 200-300 words
```

### Section 15 - References
```
├── Source: Outline p.8-11 (51 references already)
├── Key technical content:
│   • Maintain numbered citation format [N]
│   • Verify all in-text citations have entries
│   • Add new citations for expanded content
│   • Follow example paper formatting
├── Required citations: N/A
├── Figures/tables needed: None
└── Target length: ~2-3 pages
```

### Section 16 - Appendices
```
├── Source: Example p.44-63
├── Appendix A – 3D CAD Drawings/Renders
│   • 6U configuration views
│   • Component placement diagrams
│   • Shielding layout
├── Appendix B – Complete System Circuit
│   • AI payload circuit diagram
│   • Power distribution diagram
│   • Communications system diagram
├── Appendix C – Requirements and Verification
│   • Full requirements table with verification methods
│   • Traceability matrix
├── Appendix D – Management
│   • Detailed Gantt chart
│   • Budget breakdown
│   • Risk register
├── Required citations: 0
├── Figures/tables needed: Multiple diagrams and tables
└── Target length: 2000-2500 words + figures
```

---

## Conflicts Documented

### CONFLICT 1: Document Type Mismatch
```
CONFLICT DETECTED:
- Example paper documents: Completed mission with actual flight results (April 2023 flight)
- Assignment 3 outline presents: Proposed mission design (not yet built/flown)

RESOLUTION: Following problem statement + instructor feedback
- This is a DESIGN paper for a proposed CubeSat mission
- "Flight Results" section becomes "Expected Flight Results" with simulations/predictions
- Testing sections describe proposed methodology + any preliminary/theoretical analysis
- This approach is valid for graduate design courses

Rationale: Problem statement says "Press forward with a design and provide as much detail as possible" - confirming this is a design exercise, not a post-flight report.
```

### CONFLICT 2: Structure Mapping
```
CONFLICT DETECTED:
- Example paper structure: 16 sections following DemoSat report format
- Outline structure: 4 main sections + conclusion following proposal format

RESOLUTION: Following example paper structure (higher priority as STYLE REFERENCE)
- Reorganize outline content into example's 16-section structure
- Expand technical depth significantly
- Add missing sections (testing, CONOPS, block diagrams, appendices)
- Maintain outline's technical content and citations

Rationale: Example paper structure is the PRIMARY STYLE REFERENCE per methodology.
```

### CONFLICT 3: Sponsor/Team Sections
```
CONFLICT DETECTED:
- Example paper: Multi-student team with industry sponsor (AMERGINT)
- Assignment 3 outline: Individual student project with potential future sponsors

RESOLUTION: Adapt sections for individual project context
- Section 13: Focus on potential sponsor relationships and industry outreach
- Section 14: Describe individual work with course/instructor collaboration
- Maintain professional tone, acknowledge individual scope

Rationale: Problem statement doesn't require team project; adapt to actual circumstances.
```

---

## VALIDATION GATE 1

```
☑ All 4+ required files read completely (not just skimmed)
  - start_here.md: Full methodology read
  - problem_statement: Requirements extracted
  - CubeSat__FinalReport2023 (example).md: Full 63-page document analyzed
  - Jordan_Clayton_Project1_Draft_Outline r1.pdf: All 11 pages with 51 references

☑ Problem statement captured in ≤5 clear bullets
  - 5 core requirements identified

☑ Rubric matrix complete with ALL grading criteria mapped
  - 17 criteria mapped to sections and completion phases

☑ Content allocation covers all 16 required sections
  - Each section has source mapping, content bullets, citation estimates, figure needs, word targets

☑ No critical gaps identified (or gaps documented with mitigation)
  - 3 conflicts documented with resolutions
  - All sections have sufficient source material

Status: PASS → Proceed to Phase 2
```

---

**GATE 1 STATUS**: PASS

**PROCEED TO PHASE 2**: YES

**Estimated Final Paper Length**: ~15,000-17,000 words (~55-65 pages with figures)

**Batch Execution Plan**:
- **Batch 1**: Sections 1-4 (Executive Summary, Introduction, Planning, Requirements) ~3,500-4,000 words
- **Batch 2**: Sections 5-7 (Conceptual Design, Electrical Testing, Structural Testing) ~4,500-5,500 words
- **Batch 3**: Sections 8-12 (Final Design, CONOPS, Block Diagrams, Flight Results, Conclusion) ~5,000-6,000 words
- **Batch 4**: Sections 13-16 (Sponsor, Team, References, Appendices) ~2,500-3,500 words

---

*Phase 1 completed: 2025-12-15*
*Ready for user approval to proceed to Phase 2: Batched Drafting*
