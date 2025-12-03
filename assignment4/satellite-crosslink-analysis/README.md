# Optical vs. RF Crosslinks Trade Study
## SpCE 5400 - Assignment 4

**Author:** Jordan Clayton
**Course:** SpCE 5400 - Small Satellite Engineering & Operations
**Date:** November 2025

---

## 📋 Project Overview

This repository contains a comprehensive trade study analyzing **optical (laser)** versus **RF (Ka-band)** crosslink technologies for a Low Earth Orbit (LEO) satellite constellation.

**Mission Scenario:**
- Two small satellites at 500 km altitude
- Inter-satellite separation: 250 km
- Required data rate: 1 Gbps
- Environment: LEO-to-LEO (vacuum path)

**Analysis Scope:**
- Complete link budget calculations for both technologies
- Comparison of 5 key parameters: aperture size, transmit power, data rate capability, link margin, and pointing accuracy
- Quantitative recommendation with engineering justification

---

## 📁 Repository Structure

```
satellite-crosslink-analysis/
├── README.md                           # This file
├── build_pdf_file24.sh                 # Script to generate PDF from submission
├── build_pdf_simple.sh                 # Alternative PDF build script
├── generate_plots.py                   # Script to generate all visualization plots
├── PDF_BUILD_README.md                 # Documentation for PDF generation
├── pdf_metadata.yaml                   # Metadata for PDF generation
│
├── outputs/                            # Main outputs directory
│   ├── 24_Assignment4_Submission_With_Calculations_Concise.md  # MAIN SUBMISSION
│   ├── Assignment4_Concise_FINAL.pdf                           # PDF VERSION
│   ├── 11_Assignment4_Tutorial_Guide.md                        # Educational walkthrough
│   ├── 12_Assignment4_Submission_With_Calculations.md          # Detailed version
│   ├── 23_Complete_Formulas_Sources_and_Logic_Flow.md          # Formula reference
│   └── figures/                        # All visualization plots (8 PNG files)
│       ├── 01_link_margin_comparison.png
│       ├── 02_pointing_comparison.png
│       ├── 03_beam_divergence.png
│       ├── 04_data_rate_scalability.png
│       ├── 05_range_sensitivity.png
│       ├── 06_size_comparison.png
│       ├── 07_trade_space.png
│       ├── 08_summary_scorecard.png
│       └── Gaussian_Beam_FWHM.gif     # Beam divergence diagram
│
├── templates/                          # Template files
│   └── problem_statement.md            # Original assignment requirements
│
├── prompts/                            # Analysis prompts used
│
├── execution/                          # Execution logs
│
└── archive/                            # Archived old versions
    ├── old_outputs/                    # Previous analysis versions
    └── old_scripts/                    # Deprecated scripts
```

---

## 🎯 Key Results

### Quantitative Comparison

| Parameter | Optical (Laser) | RF (Ka-band) | Winner | Advantage |
|-----------|----------------|--------------|---------|-----------|
| **Aperture Size** | **10 cm** | 30 cm | Optical | **3× smaller** |
| **Transmit Power** | **0.122 W** | 1.2 W | Optical | **10× lower** |
| **Data Rate** | **10+ Gbps** | ~2 Gbps max | Optical | **5× scalability** |
| **Link Margin** | **25.66 dB** | 2.8 dB | Optical | **9× better** |
| **Pointing Accuracy** | ±8.0 μrad | **2.19°** | RF | **4,800× easier** |

### Recommendation

**OPTICAL (LASER) CROSSLINKS** - High Confidence

**Rationale:**
- **Superior link margin:** 25.66 dB vs 2.8 dB (9× better)
- **Compact design:** 10 cm aperture vs 30 cm (3× smaller, fits cubesat)
- **Low power:** 0.122 W vs 1.2 W (10× lower power consumption)
- **Future-proof:** Scales to 10+ Gbps vs RF's ~2 Gbps limit
- **Pointing challenge manageable:** Heritage FSM technology exists (EDRS, LCRD)

Despite requiring 4,800× more precise pointing (8 μrad vs 2.19°), optical's massive link margin and SWaP advantages make it the superior choice for performance-driven small satellite missions.

---

## 🚀 Quick Start

### View the Submission

**Markdown version:**
```bash
open outputs/24_Assignment4_Submission_With_Calculations_Concise.md
```

**PDF version (with sidebar navigation):**
```bash
open outputs/Assignment4_Concise_FINAL.pdf
```

### Generate Plots

```bash
python3 generate_plots.py
```

This creates 8 publication-quality plots in `outputs/figures/`:
1. Link margin comparison (bar chart)
2. Pointing requirement comparison (log scale)
3. Beam divergence illustration (side view)
4. Data rate scalability (margin vs data rate)
5. Range sensitivity (margin vs distance)
6. Size comparison (physical apertures)
7. Trade space plot (margin vs pointing difficulty)
8. Summary scorecard (decision table)

### Build PDF from Markdown

```bash
./build_pdf_file24.sh
```

Creates professional PDF with:
- PDF bookmarks (sidebar navigation)
- Clickable table of contents
- Numbered sections
- Embedded figures
- Blue hyperlinks

**Requirements:**
- Pandoc 3.8+
- XeLaTeX (from MacTeX)

See `PDF_BUILD_README.md` for detailed instructions.

---

## 📊 Analysis Highlights

### Optical Link Budget
- **Methodology:** Detector-first approach using quantum efficiency
- **Transmit power:** 0.122 W (iteratively selected for 25.66 dB margin)
- **Aperture:** 10 cm diameter telescopes (Tx and Rx)
- **Wavelength:** 1550 nm (telecom standard, eye-safe)
- **Key advantage:** Enormous link margin provides robustness buffer

### RF Link Budget
- **Methodology:** Standard Friis equation approach
- **Transmit power:** 1.2 W (selected for 2.8 dB margin)
- **Aperture:** 30 cm diameter antennas (Tx and Rx)
- **Frequency:** 32 GHz (Ka-band ISL allocation)
- **Key limitation:** Minimal margin leaves no degradation buffer

### Critical Insight: Pointing Requirement
- **Optical:** ±8.0 μrad (half-power beamwidth, NOT 18.9 μrad beam divergence to first null)
- **RF:** 2.19° beamwidth
- **Ratio:** RF is 4,800× easier to point in linear angle
- **Resolution:** Optical's 25.66 dB margin can trade for relaxed pointing if needed

---

## 📚 Supporting Documents

### Main Documents
1. **24_Assignment4_Submission_With_Calculations_Concise.md** - Primary submission with all calculations
2. **Assignment4_Concise_FINAL.pdf** - Formatted PDF version
3. **11_Assignment4_Tutorial_Guide.md** - Step-by-step educational walkthrough
4. **23_Complete_Formulas_Sources_and_Logic_Flow.md** - Comprehensive formula reference

### Visualizations
- All plots in `outputs/figures/` (300 DPI PNG format)
- Gaussian beam FWHM diagram explaining pointing requirement

---

## 🔧 Technical Details

### Link Budget Formulas

**Optical:**
```
n = Q / η                                [photons/bit]
E_photon = h × c / λ                     [J/photon]
P_req = E_bit × R_b                      [W]
L_s = (λ / (4πR))²                       [linear]
G = (πD / λ)²                            [linear]
Margin = 10 × log₁₀(P_rx / P_req)       [dB]
θ_3dB = 0.514 × λ / D                    [radians, half-power beamwidth]
```

**RF:**
```
FSPL = 20 × log₁₀(4πR/λ)                [dB]
G = η_ant × (πD/λ)²                      [linear]
N_0 = k_B × T_sys                        [W/Hz]
C/N_0 = P_rx - N_0                       [dB-Hz]
Margin = C/N_0 - (C/N_0)_req             [dB]
θ_3dB ≈ 70 × λ / D                       [degrees]
```

### Design Parameters

**Optical:**
- Wavelength: 1550 nm (design choice - telecom standard)
- Quantum efficiency: 0.3 (InGaAs APD detector)
- Required photoelectrons/bit: 40 (for BER 10⁻⁹)
- Modulation: OOK (On-Off Keying)

**RF:**
- Frequency: 32 GHz (design choice - Ka-band ISL)
- Antenna efficiency: 0.6 (deployable mesh)
- System noise temperature: 650 K (Ka-band LNA typical)
- Required E_b/N_0: 9.6 dB (with LDPC coding)

---

## 📖 References

Key sources cited:
- ITU-R Recommendations (P.618-13, S.1328)
- Born & Wolf "Principles of Optics" (Airy disk formula)
- Friis transmission equation (1946)
- NASA LCRD and ESA EDRS mission data
- Excel template (modified from JPL OLSG baseline)

Complete references list available in submission document.

---

## 🛠️ Tools & Dependencies

**Required:**
- Python 3.8+ (for plot generation)
- Matplotlib, NumPy (for visualizations)
- Pandoc 3.8+ (for PDF generation)
- XeLaTeX (from MacTeX, for PDF generation)

**Optional:**
- SciPy (for Airy disk plot - currently skipped if not installed)

**Install dependencies:**
```bash
pip install matplotlib numpy
brew install pandoc
brew install --cask mactex-no-gui  # or full mactex
```

---

## 📝 Notes

- **Pointing accuracy correction:** Earlier versions incorrectly used 18.9 μrad (beam divergence to first null). The actual pointing requirement is 8.0 μrad (half-power beamwidth for -3 dB loss).

- **Link margin units:** Optical margin is in dB (power ratio), RF margin is also in dB (C/N₀ ratio). Both are directly comparable.

- **Scalability:** Optical maintains 15.66 dB margin at 10 Gbps; RF fails at 2 Gbps (-0.21 dB margin).

---

## 📧 Contact

**Jordan Clayton**
SpCE 5400 - Small Satellite Engineering & Operations
November 2025

---

## 📜 License

This is coursework for SpCE 5400. All analysis, calculations, and visualizations are original work unless otherwise cited.

---

**Last Updated:** November 17, 2025
