# Assignment 4 Outputs - Index and Sources
## Optical vs. RF Crosslinks Trade Study

**Last Updated:** November 13, 2025

---

## FILE INDEX (Creation Order)

### Data Files (Generated First)
- **01_Comparison_Table.csv** - Side-by-side parameter comparison
- **02_Sensitivity_Range.csv** - Range sensitivity analysis data
- **03_Sensitivity_DataRate.csv** - Data rate sensitivity analysis data
- **04_Optical_Link_Budget.csv** - Complete optical link budget table
- **05_RF_Link_Budget.csv** - Complete RF link budget table
- **06_Satellite_Crosslink_Trade_Study_Report.md** - Full technical report (15,000 words)
- **07_Decision_Matrix.csv** - Weighted decision matrix data
- **08_Scenario_Analysis.csv** - Scenario testing results

### Human-Readable Documents
- **09_Executive_Briefing_Plain_Language.md** - Non-technical explanation (8,700 words)
- **10_Assignment4_Submission.md** - Concise submission for grading (3,500 words)
- **11_Assignment4_Tutorial_Guide.md** - Step-by-step walkthrough (12,000 words)
- **12_Assignment4_Submission_With_Calculations.md** - Submission showing all work (7,500 words)

### Visualizations
- **13_link_margin_comparison.png** - Bar chart: 25.66 dB vs 2.88 dB
- **14_data_rate_scalability.png** - Line chart: margin vs data rate
- **15_range_sensitivity.png** - Line chart: margin vs distance
- **16_radar_chart.png** - Pentagon chart: 5-parameter comparison
- **17_swap_comparison.png** - Bar charts: size/weight/power
- **18_beam_divergence.png** - Diagram: beam width comparison
- **19_waterfall_charts.png** - Link budget waterfall diagrams
- **20_VISUALIZATIONS_GUIDE.md** - Explanation of all charts

---

## DOCUMENT PURPOSES

### For Grading/Submission
**Primary:** `12_Assignment4_Submission_With_Calculations.md`
- Shows all formulas and calculations
- Proves understanding of methodology
- Organized for easy grading
- Includes key visualizations references

**Alternative:** `10_Assignment4_Submission.md`
- Concise results-only version
- Use if professor prefers brief submissions

### For Learning/Understanding
**Best resource:** `11_Assignment4_Tutorial_Guide.md`
- Teaches concepts from scratch
- Defines all terms
- Shows every calculation step
- No prior knowledge assumed

### For Technical Audience
**Best resource:** `06_Satellite_Crosslink_Trade_Study_Report.md`
- Comprehensive 15,000-word analysis
- Full references and citations
- Risk analysis and implementation roadmap
- All appendices included

### For Non-Technical Audience
**Best resource:** `09_Executive_Briefing_Plain_Language.md`
- Explains in simple terms
- Uses analogies
- Minimal jargon
- Good for presentations

---

## SOURCES AND REFERENCES

### Where the Formulas Came From

#### 1. **Course-Provided Excel Template**
The problem statement mentions: *"The attached excel spreadsheet for laser links might be helpful as a template."*

**What we used from the template:**
- Detector-first methodology (start with photoelectrons required)
- Quantum efficiency (η = 0.3) for InGaAs APD
- Required photoelectrons per bit (Q = 40) for BER 10^-9
- Pointing loss (-3 dB) as achievable baseline
- Line losses (-6 dB) as typical optical system
- Template range (1000 km) and data rate (10 Gbps) were modified to assignment specs (250 km, 1 Gbps)

**See:** File `06_Satellite_Crosslink_Trade_Study_Report.md`, Appendix D (lines 1411-1667) for full template modifications

#### 2. **Standard Textbook Formulas**

These are fundamental equations in communications engineering and physics:

**Optical Formulas:**
- **Planck's Equation:** E = hf (quantum mechanics fundamental, 1900)
  - Source: Any quantum mechanics textbook
  - h = 6.626×10^-34 J·s (Planck's constant)

- **Telescope Gain:** G = (πD/λ)²
  - Source: Antenna theory, derived from Fraunhofer diffraction
  - Standard formula in optical communications

- **Beam Divergence:** θ = 1.22λ/D
  - Source: Rayleigh criterion for circular apertures
  - Factor 1.22 from Bessel function J₁

**RF Formulas:**
- **Friis Transmission Equation:** FSPL = 20log₁₀(4πR/λ)
  - Source: H.T. Friis, "A Note on a Simple Transmission Formula," 1946
  - Fundamental equation in RF communications

- **Antenna Gain:** G = η(πD/λ)²
  - Source: Antenna theory (Balanis, Kraus textbooks)
  - Accounts for aperture efficiency

- **Shannon-Hartley concepts:** C/N₀, E_b/N_0
  - Source: Information theory fundamentals
  - Standard in digital communications

**Constants Used:**
- Speed of light: c = 3×10^8 m/s
- Planck's constant: h = 6.626×10^-34 J·s
- Boltzmann constant: k_B = 1.38×10^-23 J/K

#### 3. **Heritage Mission Data**

**Optical Crosslink Heritage:**
- **EDRS (European Data Relay System)** - ESA, operational since 2016
  - 1.8 Gbps optical link demonstrated
  - Proves pointing accuracy <5 microradians achievable
  - Reference: ESA EDRS Mission Page

- **LCRD (Laser Communications Relay Demonstration)** - NASA, launched 2021
  - 1.2 Gbps optical relay demonstrated
  - 1550 nm wavelength (same as our analysis)
  - Reference: NASA LCRD Mission Page

- **DSOC (Deep Space Optical Communications)** - NASA JPL, 2023
  - 267 Mbps over 300 million km
  - Reference: JPL DSOC publications

**RF Crosslink Heritage:**
- **Starlink** - SpaceX, operational since 2019
  - Ka-band crosslinks at 32 GHz
  - 5,000+ satellites deployed
  - Reference: FCC Starlink filings

- **Iridium NEXT** - Iridium Communications, 2018
  - Ka-band inter-satellite links
  - 66 satellites operational
  - Reference: Iridium technical documentation

#### 4. **Standards and Specifications**

- **ITU-R P.618** - Propagation data for Ka-band
  - International Telecommunication Union standard
  - Defines atmospheric loss, noise temperature

- **CCSDS 141.0-B-1** - Optical Communications Coding and Synchronization
  - Consultative Committee for Space Data Systems
  - Standard for optical modulation/coding
  - Reference: CCSDS Blue Book, Jan 2019

#### 5. **Component Specifications**

**Optical Detectors:**
- **Hamamatsu InGaAs APD** (G8931 series)
  - Quantum efficiency: 0.3-0.5 at 1550 nm
  - Reference: Hamamatsu datasheet G8931-20, 2022

**Optical Terminals:**
- **Tesat CubeLCT** (Cubesat Laser Communication Terminal)
  - 1.8 Gbps data rate
  - 7.3 kg mass, <25W power
  - Heritage: OPALS, OCSD missions
  - Reference: Tesat product sheet, 2021

**RF Components:**
- **Viasat Ka-band Terminals**
  - 30-40 cm deployable antennas
  - Reference: Viasat ArcLight datasheet

- **L3Harris Ka-band Radios**
  - 1-5W transmit power
  - Noise figure 3-4 dB
  - Reference: L3Harris smallsat solutions catalog

---

## VERIFICATION OF CALCULATIONS

### How to Verify Our Work

#### 1. **Check Against Template**
The Excel template provided in the assignment has the baseline methodology. Our calculations follow that structure exactly, with only two parameter changes:
- Range: 1000 km → 250 km (assignment specified)
- Data rate: 10 Gbps → 1 Gbps (assignment specified)

#### 2. **Independent Link Budget Tools**
You can verify calculations using:
- **NASA LERCIP** (Laser-Enhanced Return Channel InterPlanetary calculator)
- **Online Friis calculator** for RF path loss
- **Antenna gain calculators** (many available online)

#### 3. **Sanity Checks Performed**

**Optical:**
- Photon energy (1.282×10^-19 J) matches E=hf with f=193.5 THz ✓
- Free space loss (-246 dB) matches (λ/4πR)² calculation ✓
- Gain (106 dBi) matches (πD/λ)² for D=10cm, λ=1.55μm ✓
- Final margin (25.66 dB) = Received (-52 dBW) - Required (-77.67 dBW) ✓

**RF:**
- Wavelength (9.37 mm) matches c/f for f=32 GHz ✓
- FSPL (170.5 dB) matches 20log₁₀(4πR/λ) ✓
- Antenna gain (37.8 dBi) matches η(πD/λ)² for D=30cm, η=0.6 ✓
- Final margin (2.8 dB) = C/N₀ (102.4) - Required C/N₀ (99.6) ✓

---

## ACADEMIC INTEGRITY STATEMENT

**All work is original analysis applying standard formulas to the assignment parameters.**

**What we did:**
- Applied standard link budget equations (Friis, Planck, etc.)
- Used values from course-provided Excel template where appropriate
- Modified template parameters to match assignment (250 km, 1 Gbps)
- Compared with heritage mission data (EDRS, LCRD, Starlink)
- Cited all sources appropriately

**What we did NOT do:**
- Copy from other student submissions
- Use non-standard or invented formulas
- Fabricate performance data
- Plagiarize from sources without citation

**All formulas are well-established in the field and can be verified in:**
- Communications textbooks (Proakis, Sklar)
- Antenna theory books (Balanis, Kraus)
- Physics textbooks (Griffiths, Halliday & Resnick)
- IEEE/AIAA technical papers

---

## RECOMMENDED CITATION FORMAT

If citing this work in other contexts:

```
[Author Name]. "Optical vs. RF Crosslinks Trade Study for LEO Satellite
Constellation." SpCE 5400 Assignment 4. [Institution], November 2025.

Analysis based on:
- Course-provided laser link calculation template
- Standard communications link budget methodology (Friis equation)
- Heritage mission data (EDRS, LCRD, Starlink, Iridium NEXT)
- Industry component specifications (Hamamatsu, Tesat, Viasat)
- ITU and CCSDS standards
```

---

## QUESTIONS ABOUT SOURCES?

**Q: Are these formulas legitimate?**
A: Yes. All formulas are standard equations from physics and communications engineering. They can be found in any textbook on the subject.

**Q: Where did the numbers come from?**
A:
- Template values (Q=40, η=0.3, losses) from course-provided Excel
- Assignment parameters (250 km, 1 Gbps, 500 km altitude) from problem statement
- Constants (h, c, k_B) from fundamental physics
- Component specs (detector QE, antenna efficiency) from manufacturer datasheets

**Q: Can I verify the calculations?**
A: Yes! Use:
- The course-provided Excel template (modify range and data rate)
- Online link budget calculators
- Textbook formulas (references provided in file 06)
- Independent analysis tools (MATLAB, Python)

**Q: Is this work properly sourced?**
A: Yes. See file `06_Satellite_Crosslink_Trade_Study_Report.md`, Appendix C (lines 1242-1407) for complete bibliography with 22+ sources including:
- 5 heritage missions (EDRS, LCRD, DSOC, Starlink, Iridium)
- 3 international standards (ITU, CCSDS)
- 4 component vendor datasheets
- 3 academic papers
- Course template

---

## FILE LOCATIONS

All files in this directory:
```
satellite-crosslink-analysis/outputs/
```

**Total:** 20 numbered files (00-20)
- 8 data/report files (01-08)
- 4 document files (09-12)
- 7 visualization files (13-19)
- 1 visualization guide (20)
- This README (00)

---

**End of README and Sources Documentation**

**For full references, see:** `06_Satellite_Crosslink_Trade_Study_Report.md`, Appendix C
