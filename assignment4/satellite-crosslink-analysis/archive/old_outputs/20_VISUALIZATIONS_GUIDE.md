# Visualization Guide
## Optical vs RF Crosslinks Trade Study

All visualizations are saved as high-resolution PNG files (300 DPI) suitable for reports and presentations.

---

## 1. Link Margin Comparison (`1_link_margin_comparison.png`)

**What it shows:**
- Side-by-side bar chart comparing link margins
- Optical: 25.66 dB
- RF: 2.88 dB
- Red dashed line showing 3 dB minimum requirement

**Key insight:**
- Optical has 8.9× more margin than RF
- Optical exceeds requirement by 22.66 dB
- RF barely meets the requirement

**Use in presentation:**
- Lead with this chart - it's the most important comparison
- Shows the fundamental advantage of optical

---

## 2. Data Rate Scalability (`2_data_rate_scalability.png`)

**What it shows:**
- How link margin changes as data rate increases from 0.5 to 10 Gbps
- Two lines: Optical (stays high), RF (quickly goes negative)
- Red shaded region shows where links fail (margin < 0 dB)

**Key insight:**
- Optical maintains 15.66 dB margin even at 10 Gbps
- RF fails at 2 Gbps (margin goes negative)
- Shows optical is future-proof for data rate growth

**Use in presentation:**
- Demonstrates scalability advantage
- Answers "what if we need more bandwidth later?"

---

## 3. Range Sensitivity (`3_range_sensitivity.png`)

**What it shows:**
- How link margin changes with satellite separation distance (100-600 km)
- Green dashed line at 250 km (baseline mission)
- Two lines showing optical remains robust, RF fails at longer ranges

**Key insight:**
- Optical maintains 19.62 dB margin even at 500 km (2× baseline)
- RF fails at 500 km (-3.12 dB margin)
- Shows optical is robust to orbital variations

**Use in presentation:**
- Demonstrates robustness to range changes
- Important for constellation design (satellites drift)

---

## 4. Five-Parameter Radar Chart (`4_radar_chart.png`)

**What it shows:**
- Pentagon/spider chart comparing all 5 assignment parameters
- Optical (blue) vs RF (purple) overlaid
- Each axis represents one parameter (normalized 0-10 scale)

**Parameters shown:**
1. Link Margin (higher better) - Optical wins
2. Aperture Size (smaller better) - Optical wins
3. Power (lower better) - Optical wins
4. Data Rate (higher better) - Optical wins
5. Pointing (easier better) - RF wins

**Key insight:**
- Optical wins 4 of 5 categories
- RF only wins on pointing ease
- Visual shows optical dominates overall

**Use in presentation:**
- Great summary chart showing all factors at once
- Easy to see that optical has larger "coverage area"

---

## 5. SWaP Comparison (`5_swap_comparison.png`)

**What it shows:**
- Three grouped bar charts comparing:
  - Aperture: 10 cm (optical) vs 30 cm (RF)
  - Mass: 2.2 kg (optical) vs 4.2 kg (RF)
  - Power: 0.122W (optical) vs 1.2W (RF)

**Key insight:**
- Optical is 3× smaller, 2 kg lighter, 10× lower power
- Critical for small satellite missions
- Launch cost savings: 2 kg × $5k/kg = $10k per satellite

**Use in presentation:**
- Demonstrates practical engineering advantages
- Shows optical enables cubesat deployment

---

## 6. Beam Divergence Illustration (`6_beam_divergence.png`)

**What it shows:**
- Two diagrams (top: optical, bottom: RF)
- Shows beam cones from Sat A to Sat B at 250 km separation
- Spot size circles at receiver
- Optical: 18.9 μrad divergence → 4.73 m spot
- RF: 2.183° beamwidth → ~9,550 m spot

**Key insight:**
- Optical beam is 115,000× narrower than RF
- This is why pointing is much harder for optical
- But also why optical has better link performance (focused beam)

**Use in presentation:**
- Visual explanation of pointing challenge
- Helps audience understand the trade-off

**Note:** Angles are exaggerated for visibility; actual optical beam would be imperceptibly narrow at this scale.

---

## 7. Link Budget Waterfall Charts (`7_waterfall_charts.png`)

**What it shows:**
- Two side-by-side waterfall charts (optical left, RF right)
- Shows step-by-step gains and losses from transmit power to final margin
- Green bars = gains, Red bars = losses, Blue/Purple = final powers/margin

**Optical stages:**
1. Tx Power: 0.122W (-9.14 dBW)
2. Free Space Loss: -246.1 dB
3. Tx Gain: +106.1 dBi (10 cm telescope)
4. Rx Gain: +106.1 dBi
5. Pointing Loss: -3.0 dB
6. Line Losses: -6.0 dB
7. Received Power: -52.0 dBW
8. Required Power: -77.67 dBW
9. **Margin: 25.66 dB**

**RF stages:**
1. Tx Power: 1.2W (0.8 dBW)
2. Tx Gain: +37.8 dBi (30 cm antenna)
3. Free Space Loss: -170.5 dB
4. Rx Gain: +37.8 dBi
5. Pointing Loss: -1.0 dB
6. Other Losses: -3.0 dB
7. Received Power: -98.1 dBW
8. C/N0: 102.4 dB-Hz
9. Required C/N0: 99.6 dB-Hz
10. **Margin: 2.88 dB**

**Key insight:**
- Shows WHERE the performance difference comes from
- Optical has huge gains (+212 dBi total) that compensate for higher path loss
- RF has lower gains, resulting in minimal margin

**Use in presentation:**
- For technical audiences who want to see the math
- Explains the "why" behind the performance difference

---

## Suggested Usage in Documents

### For Assignment Submission:
- Include Charts 1, 4, and 5 (margin comparison, radar chart, SWaP)
- These directly answer the assignment requirements

### For Technical Presentation:
- Use all 7 charts in this order:
  1. Chart 1: Lead with margin comparison (main result)
  2. Chart 4: Show overall comparison (5 parameters)
  3. Chart 5: Demonstrate SWaP advantages
  4. Chart 6: Explain pointing trade-off
  5. Chart 2: Show data rate scalability
  6. Chart 3: Show range robustness
  7. Chart 7: Explain the link budget details

### For Executive Briefing:
- Use Charts 1, 4, and 5 only (simple, visual, non-technical)
- Skip the waterfall chart (too detailed)

---

## File Locations

All images are saved in:
```
satellite-crosslink-analysis/outputs/
```

Files:
- `1_link_margin_comparison.png` (10 × 6 inches, 300 DPI)
- `2_data_rate_scalability.png` (12 × 7 inches, 300 DPI)
- `3_range_sensitivity.png` (12 × 7 inches, 300 DPI)
- `4_radar_chart.png` (10 × 10 inches, 300 DPI)
- `5_swap_comparison.png` (15 × 6 inches, 300 DPI)
- `6_beam_divergence.png` (14 × 10 inches, 300 DPI)
- `7_waterfall_charts.png` (16 × 8 inches, 300 DPI)

## Regenerating Visualizations

To regenerate all visualizations (e.g., if you modify parameters):

```bash
cd satellite-crosslink-analysis
python create_visualizations.py
```

The script will overwrite existing images.

---

**End of Visualization Guide**
