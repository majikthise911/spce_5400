# CubeSat Mission Evaluation Rubric
**Based on NASA CSLI CubeSat 101 Chapters 1-3**

---

## Overview

This rubric evaluates CubeSat mission concepts against the key requirements and best practices outlined in NASA's CubeSat 101 document for the CSLI program. Each mission will be scored on a 1-5 scale across multiple criteria.

---

## Scoring Scale

- **5 = Excellent**: Exceeds requirements, ideal alignment
- **4 = Good**: Meets requirements well, minor concerns
- **3 = Adequate**: Meets minimum requirements, moderate concerns
- **2 = Poor**: Below requirements, significant concerns
- **1 = Unacceptable**: Fails to meet requirements, critical issues

---

## Evaluation Criteria (10 Categories)

### 1. NASA Strategic Plan Alignment (Weight: x2)
**CSLI Requirement**: Mission must clearly benefit NASA and support at least one goal/objective in NASA Strategic Plan

**Scoring Guidelines**:
- **5**: Directly addresses multiple NASA Strategic Plan goals; clear, compelling benefit to NASA
- **4**: Addresses at least one NASA goal with clear benefit
- **3**: Addresses NASA goal but benefit is indirect or limited
- **2**: Weak connection to NASA goals
- **1**: No clear NASA benefit or strategic alignment

**Key NASA Mission Areas to Consider**:
- Science (Space Weather, Earth Science, Planetary Science, Heliophysics)
- Technology Development (Communications, Propulsion, Navigation/Control)
- Enabling future missions (Mars, asteroid exploration)

---

### 2. Mission Simplicity (Weight: x1.5)
**CSLI Guidance**: "KEEP IT SIMPLE" - Complex features may limit launch opportunities

**Scoring Guidelines**:
- **5**: Very simple mission, minimal complex systems, no prohibited features
- **4**: Simple mission with 1-2 moderately complex systems
- **3**: Moderate complexity with several complex systems but manageable
- **2**: High complexity with multiple challenging systems (propulsion, complex mechanisms)
- **1**: Extremely complex with prohibited systems (pyrotechnics) or unrealistic scope

**Complexity Factors**:
- Propulsion systems (discouraged)
- Deployable mechanisms
- Multiple payloads
- Novel/untested technologies
- Inter-satellite operations

---

### 3. CubeSat Form Factor Compliance (Weight: x1)
**CSLI Requirement**: Must conform to standard CubeSat sizes and mass limits

**Scoring Guidelines**:
- **5**: Fits well within standard form factor (1U-3U), significant margin
- **4**: Fits within standard form factor (3U-6U) with adequate margin
- **3**: Fits within larger form factor (6U-12U) with minimal margin
- **2**: Questionable fit, may require custom dispenser or special accommodation
- **1**: Exceeds standard CubeSat limits, not feasible

**Standard Sizes**:
- 1U: 10×10×11 cm, 1-1.33 kg
- 2U: 10×10×22 cm, 2-2.66 kg
- 3U: 10×10×34 cm, 3-4 kg
- 6U: 20×10×34 cm, 6-14 kg
- 12U: 20×20×34 cm, 12-24 kg

---

### 4. Design & Development Feasibility (Weight: x2)
**Context**: This is a DESIGN project - feasibility = "can I model/design this effectively"

**Scoring Guidelines**:
- **5**: Straightforward modeling with existing tools; well-understood physics
- **4**: Moderate complexity; specialized tools available; good precedent
- **3**: High complexity but designable; may require learning new tools
- **2**: Very complex; limited tools/precedent; extensive simulation required
- **1**: Extremely challenging to model; many unknowns; beyond typical academic scope

**Design Feasibility Factors**:
- Availability of modeling/simulation tools
- Understanding of underlying physics
- Precedent/heritage from similar missions
- Scope appropriate for class project timeline
- Availability of design resources and expertise

---

### 5. Funding Realism (Weight: x1.5)
**CSLI Reality**: NASA provides launch ($300k), but YOU pay for everything else

**Scoring Guidelines**:
- **5**: Very reasonable cost; likely <$50k with COTS components
- **4**: Moderate cost $50-100k; achievable with university/grant funding
- **3**: Higher cost $100-200k; requires substantial funding effort
- **2**: Very high cost $200-500k; funding highly uncertain
- **1**: Extremely high cost >$500k; unrealistic for educational/small organization

**Major Cost Components**:
- Payload components (sensors, instruments)
- COTS subsystems vs. custom development
- Environmental testing (vibration, thermal vacuum)
- Ground station
- Labor (often in-kind for universities)
- Travel for reviews and integration

---

### 6. Launch Flexibility (Weight: x1)
**CSLI Selection Key**: "Flexibility is key" - flexible requirements = faster manifesting

**Scoring Guidelines**:
- **5**: Highly flexible - any LEO orbit, no specific altitude/inclination requirements
- **4**: Flexible with minor preferences (e.g., altitude range but not critical)
- **3**: Some constraints on orbit parameters (sun-synchronous, specific altitude)
- **2**: Tight orbital requirements limiting launch opportunities
- **1**: Very specific orbit (GTO, Mars, specific body) severely limiting opportunities

**Flexibility Factors**:
- Orbital altitude requirements
- Inclination requirements
- Sun-synchronous requirements
- Deep space vs. LEO
- Launch date constraints

---

### 7. Component Heritage & Availability (Weight: x1.5)
**CSLI Best Practice**: Use familiar components with flight heritage; use COTS when available

**Scoring Guidelines**:
- **5**: All major components are COTS with extensive flight heritage
- **4**: Mostly COTS/heritage; minor custom development
- **3**: Mix of COTS and custom; some heritage components
- **2**: Mostly custom components; limited heritage
- **1**: All custom/novel components; no flight heritage; high risk

**Key Components to Consider**:
- Attitude Determination and Control System (ADCS)
- Power system (batteries, solar panels)
- Communication system (radio, antenna)
- Payload sensors/instruments
- On-board computer

**Special Notes**:
- Use UL-listed batteries (avoids extensive testing)
- Flight heritage increases launch provider confidence

---

### 8. Testing Requirements (Weight: x1)
**CSLI Requirements**: Must complete vibration, thermal vacuum, and potentially shock/EMI testing

**Scoring Guidelines**:
- **5**: Standard testing easily accommodated; no special requirements
- **4**: Standard testing with minor special considerations
- **3**: Standard testing plus some additional testing (EMI/EMC)
- **2**: Difficult testing requirements; may need special facilities
- **1**: Cannot be adequately tested or testing requirements are unrealistic

**Required Verification Tests**:
- Vibration testing
- Thermal vacuum testing
- Day In The Life (DITL) testing
- Potentially: Shock, EMI/EMC, static load

---

### 9. Licensing Feasibility (Weight: x1)
**CSLI Critical Requirement**: Must obtain RF license (FCC/NTIA) and potentially NOAA remote sensing license

**Scoring Guidelines**:
- **5**: Standard amateur radio frequencies; no remote sensing; straightforward licensing
- **4**: Standard frequencies with remote sensing license required
- **3**: Non-standard frequencies but precedent exists
- **2**: Challenging frequency allocation or novel remote sensing application
- **1**: Unlicensable frequencies or prohibited sensing capabilities

**Licensing Requirements**:
- RF License: FCC (commercial) or NTIA (government)
- Remote Sensing: NOAA (if non-government with imager/camera)
- Timeline: 4-6 months, must start within 30 days of manifesting
- Consequence: No license = DEMANIFEST from mission

---

### 10. Ground Station Feasibility (Weight: x1.5)
**CSLI Reality**: "Inadequate ground station = mission killer"

**Scoring Guidelines**:
- **5**: Standard amateur radio bands (437 MHz, 140 MHz); simple antenna
- **4**: Standard bands with directional antenna or higher complexity
- **3**: Non-standard but achievable; may need specialized equipment
- **2**: Very challenging (deep space, high bandwidth, specialized frequencies)
- **1**: Unrealistic ground station requirements for educational institution

**Ground Station Considerations**:
- Frequency band and licensing
- Antenna requirements (omnidirectional vs. directional)
- Data rate requirements
- Tracking requirements (LEO vs. deep space)
- Amateur radio community support available
- Can be tested before launch

---

## Weighted Scoring Summary

| Criterion | Weight | Raw Score (1-5) | Weighted Score |
|-----------|--------|----------------|----------------|
| 1. NASA Strategic Alignment | 2.0x | | |
| 2. Mission Simplicity | 1.5x | | |
| 3. Form Factor Compliance | 1.0x | | |
| 4. Design Feasibility | 2.0x | | |
| 5. Funding Realism | 1.5x | | |
| 6. Launch Flexibility | 1.0x | | |
| 7. Component Heritage | 1.5x | | |
| 8. Testing Requirements | 1.0x | | |
| 9. Licensing Feasibility | 1.0x | | |
| 10. Ground Station Feasibility | 1.5x | | |
| **TOTAL WEIGHT** | **14.0x** | | **out of 70** |

**Final Score Calculation**: Sum of weighted scores / 70 × 100 = **percentage score**

---

## Score Interpretation

- **90-100%**: Excellent CSLI candidate - strong alignment with all requirements
- **80-89%**: Very Good - meets requirements well, minor adjustments may help
- **70-79%**: Good - solid concept, some areas need attention
- **60-69%**: Acceptable - meets minimum requirements, several areas of concern
- **Below 60%**: Poor fit for CSLI - significant issues need resolution

---

## Additional CSLI Success Factors (Qualitative Assessment)

Beyond the scored criteria, consider these factors mentioned in CubeSat 101:

### Keys to CSLI Selection
- [ ] Adequate funding secured
- [ ] Great merit and feasibility reviews
- [ ] Clear demonstration of benefit to NASA
- [ ] Maximum flexibility in orbital requirements and launch dates

### Mission Area Fit
- [ ] Science mission (50% of CSLI missions)
- [ ] Technology development (66% of CSLI missions)
- [ ] Education mission

### Best Practices Checklist
- [ ] Components on exterior for easy access
- [ ] Don't design to envelope limits (leave margin)
- [ ] Double up on burn wires for deployables
- [ ] Use high-melting point materials
- [ ] Plan to build multiple units (ETU, FlatSat, 2 flight units)
- [ ] Extensive photo documentation planned
- [ ] "Test like you fly" approach

### Timeline Feasibility
- [ ] Concept to delivery: 9-24 months realistic
- [ ] Ground station: 2-12 months development time
- [ ] Hardware fabrication: 2-12 months
- [ ] All testing complete 1 month before readiness review

### Risk Factors
- [ ] Team has relevant expertise or access to mentors
- [ ] Student-led projects: plan for graduation/turnover
- [ ] Regulatory licensing started early (within 30 days of manifesting)
- [ ] Budget includes 10%+ reserve for unexpected events

---

## How to Use This Rubric

1. **Score each mission** on the 10 criteria using the 1-5 scale
2. **Multiply by weights** to get weighted scores
3. **Sum weighted scores** and calculate percentage
4. **Review qualitative factors** for additional insights
5. **Compare missions** to identify strongest candidates
6. **Identify weaknesses** for potential mitigation strategies

---

*Rubric created from NASA CubeSat 101: Basic Concepts and Processes for First-Time CubeSat Developers (Chapters 1-3)*
