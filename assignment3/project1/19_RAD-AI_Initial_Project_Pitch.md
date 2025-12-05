# RAD-AI CubeSat Mission: Initial Project Pitch
**Radiation-Tolerant Edge AI for Autonomous Space Operations**

**Course:** CubeSat Systems - Masters in Space Operations
**Assignment:** Project Outline (50 points)
**Date:** 2025-11-02

---

## EXECUTIVE SUMMARY

**Mission:** RAD-AI demonstrates radiation-tolerant edge artificial intelligence in a 6U CubeSat, validating autonomous vision and control capabilities critical for future deep-space missions where communication delays prevent real-time ground control.

**Problem:** Artemis, Mars Sample Return, and asteroid missions require autonomous decision-making, but current rad-hard processors lack AI capability while commercial AI chips aren't space-qualified.

**Solution:** Integrate RISC-V processor with AI acceleration in CubeSat platform; validate through onboard vision tasks and radiation characterization in LEO.

**Impact:** De-risks autonomous AI technology for NASA flagship missions; enables Mars landing hazard avoidance, asteroid proximity operations, and commercial satellite autonomy.

**Selection Rationale:** Scored 90/100 using comprehensive evaluation methodology (Document 17) balancing innovation (4/5), impact (5/5), validated need (4/5), and CSLI probability (90%) [1].

**Cost:** $100-120k (development) + CSLI free launch ($250k value)
**Timeline:** 12 months design, 12 months build/test, 12 months operations

---

# SECTION 1: INTRODUCTION

## 1.1 Mission Concept

RAD-AI is a 6U CubeSat technology demonstrator that validates radiation-tolerant edge AI processing for autonomous spacecraft operations. The mission addresses a critical gap: future deep-space missions (Mars, asteroids, lunar surface) require real-time autonomous decision-making, but communication delays (6-44 minutes for Mars) make ground control impossible [2].

**Key Innovation:** Integration of RISC-V open-architecture processor with AI accelerator hardware, running autonomous vision algorithms (star tracking, horizon detection, hazard identification) while characterizing radiation effects in the space environment.

## 1.2 Objectives

**Primary Objective:**
Demonstrate radiation-tolerant AI processing executing autonomous vision-based tasks in Low Earth Orbit for 12 months.

**Secondary Objectives:**
1. Characterize radiation effects (single-event upsets, total ionizing dose) on AI processor performance
2. Validate fault mitigation techniques through controlled error injection
3. Generate flight dataset enabling autonomous deep-space mission designs
4. Benchmark AI inference performance degradation over mission lifetime

**Success Criteria:**
Per CubeSat 101 best practices for defining measurable outcomes [3, Ch.2]:
- **Minimum Success:** AI processor operates 30 days; basic inference tasks execute
- **Baseline Success:** Autonomous vision tasks successful for 6 months; radiation characterized
- **Full Success:** 12-month operation; complete radiation database; 7-day ground-independent autonomy demonstrated

## 1.3 Why This Matters - Problem Validation

### NASA Strategic Need (TIER 2 Validated - Document 17)

**Artemis Lunar Landings:**
NASA's Artemis Plan (2024) explicitly states: "Autonomous precision landing is critical for Artemis missions to establish sustainable lunar presence" [4]. Current rad-hard processors (RAD750 operating at ~200 MHz [5]) cannot execute modern computer vision algorithms at the frame rates required for real-time hazard detection during powered descent (10-30 Hz processing requirement [6]).

**Mars Sample Return:**
The Mars Sample Return Campaign Plan identifies "autonomous hazard detection and avoidance during Mars Ascent Vehicle launch and rendezvous operations" as a critical technology gap [7]. Communication delay to Mars ranges from 6-44 minutes one-way depending on planetary positions [2], making ground-in-the-loop control impossible for time-critical maneuvers.

**Technology Roadmap Gap:**
NASA Technology Roadmap TA4.4 (Relative GN&C) and TA4.5 (Autonomy for EDL) identify radiation-tolerant edge computing for autonomous decision-making as a high-priority gap [8, p.47].

### Current Technology Gap Analysis

**Existing Radiation-Hardened Processors:**
- **RAD750** (BAE Systems): 200 MHz PowerPC, 256 MB RAM, no AI acceleration [5]
  - Heritage: Mars Curiosity, Perseverance, Juno
  - Limitation: Cannot run modern CNN/vision algorithms at required frame rates

- **RAD5545** (BAE Systems): 466 MHz PowerPC, 4 GB RAM [9]
  - Recent (2019), limited flight heritage
  - Limitation: Still lacks dedicated AI acceleration hardware

**Commercial AI Processors (Not Space-Qualified):**
- **NVIDIA Jetson Nano:** 4-core ARM + 128-core GPU, excellent AI performance (~500 GFLOPS) [10]
  - Limitation: Unknown radiation tolerance, not qualified for deep space

- **Google Coral Edge TPU:** 4 TOPS AI inference performance [11]
  - Limitation: Commercial-grade, no radiation testing data

**Gap:** No current processor combines radiation tolerance with AI acceleration at CubeSat-appropriate size, weight, power (SWaP).

### RAD-AI's Contribution

**Technology Validation:** De-risks AI processor technology through $100-120k CubeSat demonstration (Section 4.1) vs. $10M+ risk if first flown on flagship mission [3, Ch.1 - cost of failure].

**Flight Data:** Radiation effects data from real space environment informs future processor designs. LEO radiation environment provides sufficient TID and SEU exposure for validation (Section 1.4.3).

**Multi-Mission Applicability:**
- Artemis autonomous landing (hazard detection/avoidance)
- Mars Sample Return autonomous operations
- Asteroid proximity operations (DART follow-on missions)
- Commercial satellite autonomy (constellation management, debris avoidance)

## 1.4 Mission Requirements - Design Drivers

### 1.4.1 Orbit Selection

**Requirement:** Low Earth Orbit (LEO), 400-600 km altitude, any inclination

**Rationale:**
- **Launch Flexibility (CSLI Priority):** CubeSat 101 states "Flexibility is key" for CSLI selection [3, Ch.1, p.8]. Any LEO orbit maximizes launch opportunities.
- **Radiation Environment:** LEO at 400-600 km provides adequate radiation exposure:
  - South Atlantic Anomaly (SAA) passes: ~6-10 per day [12]
  - Total Ionizing Dose (TID): ~5-10 krad/year at 500 km [13]
  - Single Event Upset (SEU) rate: ~10^-6 to 10^-5 upsets/bit/day for commercial electronics [14]
- **Orbital Lifetime:** 25-year deorbit requirement per NASA STD 8719.14 [15]:
  - At 500 km: Natural decay in ~8-15 years (compliant) [16]
  - At 600 km: 15-25 years (marginal, may need drag sail)

**Selected:** 500 km circular, any inclination (baseline for budgets)

### 1.4.2 Form Factor Selection

**Requirement:** 6U CubeSat

**Trade Study:**

| Form Factor | Pros | Cons | Decision |
|-------------|------|------|----------|
| **3U** | Lower cost, simpler | Insufficient volume for AI processor + cameras + battery | ❌ Too small |
| **6U** | Standard size, adequate volume, flight-proven dispensers | Moderate complexity | ✅ **SELECTED** |
| **12U** | Maximum volume/power | Higher cost, limited launch opportunities, increased complexity [3, Ch.1] | ❌ Over-scoped |

**Rationale for 6U:**
1. **Volume Requirement:**
   - AI payload (processor board + 2 cameras + rad sensors): ~1.5U (Section 3.2.1)
   - Power system (battery + EPS): ~1.5U [17, p.23 - typical 6U battery sizing]
   - ADCS, C&DH, Comms, Structure: ~3U
   - **Total:** ~6U (at envelope, acceptable per preliminary estimate)

2. **Power Generation:**
   - AI payload power requirement: 15-30W (Section 1.4.3)
   - 6U body-mounted solar panels: ~40-50W BOL in LEO [17, p.18]
   - 3U inadequate (~20-25W BOL)

3. **Heritage:** 6U is second most common CubeSat size (after 3U) with extensive dispenser availability [18].

### 1.4.3 Power Budget Derivation

**Requirement:** <40W average power

**Rationale - Component-by-Component:**

| Component | Power (W) | Source/Justification |
|-----------|-----------|---------------------|
| **AI Processor** | 15-30W | NVIDIA Jetson Nano: 5-10W typical [10]; scaled to RISC-V + NPU: 15-25W (custom estimate); +5W margin = 30W peak |
| **Vision Cameras (2x)** | 2W total | Star tracker cameras: ~1W each [19, Blue Canyon NST datasheet]; horizon camera: CMOS <1W |
| **Radiation Sensors** | 0.5W | Dosimeters: passive; SEU detector: <0.5W (SRAM readback) |
| **C&DH** | 2W | ARM Cortex-M4 flight computer: 1-2W typical [20, Pumpkin Supernova spec] |
| **ADCS** | 3W | Magnetorquers: ~2W; magnetometer + sun sensors: ~1W [21, AAC Clyde ADCS spec] |
| **Comms (average)** | 1W | UHF transceiver: 8W TX at 5% duty cycle, 1W RX at 10% duty cycle [22, GomSpace NanoCom] = ~1W avg |
| **Thermal Heaters** | 0-5W | Battery survival heater: ~5W worst-case (cold eclipse) [17, p.29]; 0W nominal |
| **Margin (20%)** | 6W | Per CubeSat 101: "Don't design to envelope limits" [3, Ch.2, p.15]; 20% power margin standard |
| **TOTAL AVERAGE** | **~36W** | Sum of average power across all modes |

**Solar Power Generation:**
- **6U Body-Mounted Panels:** 4 faces (±X, ±Y) with triple-junction GaAs cells (30% efficiency) [17, p.18]
- **Total Panel Area:** ~0.15 m² (4 faces × 10 cm × 34 cm × 0.5 sun factor accounting for sun angle)
- **LEO Average Insolation:** 1367 W/m² × 0.5 (eclipse + sun angle factor) = 683 W/m² [23]
- **Power Generation (BOL):** 0.15 m² × 683 W/m² × 0.30 efficiency = **~45W Beginning of Life**
- **Power Generation (EOL, 12 mo):** 45W × 0.9 (10% degradation) = **~40W End of Life** [17, p.19]
- **Margin:** 40W EOL - 36W avg load = **4W (11% margin)**

**Battery Sizing:**
- **Eclipse Duration:** ~35 minutes per 90-minute orbit at 500 km [24]
- **Peak Load During Eclipse:** 30W (AI processor inference) + 2W C&DH + 3W ADCS + 5W heaters = 40W
- **Energy Required:** 40W × (35 min / 60) = **23 Wh per eclipse**
- **Battery Capacity:** 23 Wh × 1.5 (depth-of-discharge margin) × 1.3 (aging) = **45 Wh minimum**
- **Selected Battery:** 60 Wh Li-ion (provides 33% margin) [25, Clyde Space 60Wh battery datasheet]

### 1.4.4 Mission Duration

**Requirement:** 12 months primary mission (6 months minimum acceptable)

**Rationale:**
1. **Radiation Characterization:** Long-term TID effects require >6 months exposure [14]
2. **Statistical Significance:** SEU event rate ~10^-5 per bit-day requires months of operation for statistically significant dataset
3. **CSLI Alignment:** Typical CSLI mission duration is 6-24 months [3, Ch.1, mission examples]
4. **Orbital Lifetime:** 500 km orbit provides 8+ years natural decay, adequate for 12-month mission + deorbit margin [16]

---

# SECTION 2: PROCESS

## 2.1 Development Approach

### Heritage-First Strategy (Per CubeSat 101 Best Practices)

CubeSat 101 emphasizes: "Use familiar components with flight heritage; use COTS when available" [3, Ch.2, p.13].

**RAD-AI Implementation:**
- ✅ **COTS CubeSat bus** (Blue Canyon Technologies BCT XACT 6U [26] or AAC Clyde Space 6U [27]) for proven subsystems
- ✅ **Custom payload only:** AI processor board with RISC-V + AI accelerator (mission-unique, no COTS exists)
- ✅ **Flight-proven cameras:** Star tracker-grade vision sensors with CubeSat heritage [19]
- ✅ **Minimize risk:** Develop only what doesn't exist commercially

**Rationale:** Custom development limited to core innovation (AI processor); all other subsystems use proven COTS reduces risk and cost [3, Ch.2].

### Multiple-Unit Build Philosophy

CubeSat 101 recommends: "Plan to build multiple units (ETU, FlatSat, 2 flight units)" [3, Ch.2, p.16].

**RAD-AI Plan:**
- **Engineering Test Unit (ETU):** For environmental testing (destructive vibration, thermal vac)
- **Flight Model 1 (FM1):** Primary flight article
- **Flight Model 2 (FM2):** Spare (or second flight for extended mission if funding available)

**Cost Implication:** Build costs scaled for 2-3 units in Section 4.1.

## 2.2 Development Timeline

### Phased Development (24 months post-design)

**Phase 1: Design & Trade Studies (Months 1-4)**

**Activities:**
- Processor selection trade study (RISC-V core: SiFive U74 [28] vs. custom implementation)
- Radiation mitigation architecture design (software TMR, checkpointing, selective shielding)
- Subsystem specifications and Interface Control Documents (ICDs)
- Power, mass, thermal, link budget refinement

**Deliverables:**
- Mission Requirements Document (MRD)
- System Requirements Review (SRR) package
- Preliminary Design Review (PDR) package

**Key Decisions:**
- RISC-V core selection (recommend SiFive U74: 1.5 GHz quad-core, proven IP [28])
- AI accelerator architecture (custom FPGA-based NPU vs. integrated solution)
- CubeSat bus vendor selection (Blue Canyon vs. AAC Clyde vs. in-house)

**Phase 2: Build & Component Test (Months 5-10)**

**Activities:**
- AI payload board fabrication (4-layer PCB with RISC-V SoC, AI accelerator, power regulation)
- Component bring-up and functional testing
- Radiation ground testing (Section 2.4)
- Flight software development (RTOS, AI algorithms, fault detection/recovery)
- Vision camera integration and calibration

**Deliverables:**
- Functioning AI payload board (TRL 5→6)
- Radiation test report (SEU cross-section, TID tolerance curves)
- Software validation test results
- Critical Design Review (CDR) package

**Phase 3: Integration & Environmental Test (Months 11-14)**

**Activities:**
- Full CubeSat assembly (payload integrated with bus)
- System-level functional testing
- Environmental testing per GEVS (General Environmental Verification Standard) [29]:
  - Vibration testing: Random vibration (14.1 Grms) and sine sweep
  - Thermal vacuum testing: -20°C to +50°C operational range
  - EMI/EMC testing if required by launch provider
- 72-hour "Day In The Life" (DITL) mission simulation [3, Ch.3, p.22]
- Post-environmental functional verification

**Deliverables:**
- Flight-ready CubeSat (TRL 7→8)
- Test reports (vibration, thermal vac, DITL)
- Flight Readiness Review (FRR) package
- Acceptance by launch provider

**Phase 4: Launch & Operations (Months 15-26)**

**Activities:**
- Integration into P-POD or other CubeSat dispenser
- Delivery to launch site and final integration
- Launch via NASA CSLI
- Early operations: Deployment, antenna release, subsystem commissioning (2 months)
- Science operations: Autonomous AI experiments, fault injection, radiation monitoring (12 months)
- Data analysis and publication

**Deliverables:**
- Mission operations reports
- Science data products (Section 3.5)
- Final mission summary and lessons learned

## 2.3 Team & Resources

### Team Composition (7-8 people for course project design phase)

Per CubeSat 101 guidance on team structure for university missions [3, Ch.2, p.11]:

**Core Team:**
1. **Mission Lead / Systems Engineer:** Overall mission architecture, requirements management, interface coordination
2. **AI Payload Engineer:** Custom processor board design, RISC-V integration, radiation mitigation implementation
3. **Software Lead:** Flight software architecture, AI algorithms (vision, control), fault detection/recovery
4. **ADCS/Navigation Engineer:** Attitude control, vision sensor integration, pointing requirements
5. **Power/Thermal Engineer:** EPS design, battery sizing, thermal analysis
6. **Communications Engineer:** RF link budget, ground station coordination, FCC licensing
7. **Integration & Test Lead:** Test planning, environmental test execution, verification matrix

**Advisors/Mentors:**
- Faculty advisor (mission oversight, academic guidance)
- Industry mentor - Radiation effects expert (university rad lab or NASA JPL)
- Industry mentor - AI/ML embedded systems (NVIDIA, SiFive, or similar)
- NASA CSLI liaison (if selected for launch)

**External Resources:**
- **Radiation Testing Facility:** University cyclotron (e.g., Texas A&M) or NASA JPL [30]
- **CubeSat Bus Vendor:** Blue Canyon Technologies [26], AAC Clyde Space [27], or NanoAvionics [31]
- **Ground Station:** University station, SatNOGS amateur network [32], or commercial (AWS Ground Station [33], KSAT [34])

## 2.4 Radiation Testing Strategy (Critical for Mission Success)

### Ground-Based Radiation Testing Requirements

**Objective:** Characterize AI processor radiation tolerance before flight

**Test Types:**

**1. Heavy Ion Single Event Upset (SEU) Testing**
- **Facility:** Texas A&M Cyclotron [30] or Lawrence Berkeley National Lab (LBNL) [35]
- **Objective:** Measure SEU cross-section (upsets per bit per fluence)
- **Methodology:** Expose AI processor to various heavy ions (Ne, Ar, Kr, Xe) at different energies
- **Expected Result:** SEU cross-section curve; inform fault mitigation design
- **Cost:** ~$5,000 (2 days beam time at academic rates [30])

**2. Total Ionizing Dose (TID) Testing**
- **Facility:** University Co-60 gamma source or X-ray TID facility
- **Objective:** Measure performance degradation vs. accumulated dose
- **Methodology:** Expose processor to incremental dose (1, 5, 10, 20 krad); test functionality at each step
- **Expected Result:** TID tolerance curve; determine mission lifetime limit
- **Cost:** ~$3,000 (university facility access)

**3. Proton Testing (Optional, if budget allows)**
- **Facility:** Indiana University Cyclotron Facility (IUCF) [36]
- **Objective:** Validate proton-induced SEU rate (relevant for trapped protons in Van Allen belts)
- **Cost:** ~$7,000 (competitive with heavy ion, but schedule-dependent)

**Total Radiation Testing Budget:** $5,000-15,000 (depending on proton test inclusion)

**Justification:** CubeSat 101 emphasizes testing critical components: "Test like you fly" [3, Ch.3, p.21]. Radiation tolerance is mission-critical; ground testing is mandatory before flight commitment.

## 2.5 Key Risks & Mitigation

Per CubeSat 101: "Budget includes 10%+ reserve for unexpected events" [3, Ch.2, p.17].

| Risk | Probability | Impact | Mitigation | Reference |
|------|------------|--------|------------|-----------|
| **AI processor radiation tolerance worse than expected** | Medium | High | Early ground rad testing (Phase 2); fallback to rad-hard FPGA + simplified algorithms | [3, Ch.2 - risk mgmt] |
| **Power budget exceeded** | Medium | Medium | Conservative design with 20% margin; operating modes with reduced AI duty cycle | Section 1.4.3 |
| **Launch delays (typical for CSLI)** | High | Low | Mission designed for any LEO orbit; flexible launch date; no consumables/time-sensitive payloads | [3, Ch.1, p.9 - flexibility] |
| **Funding shortfall** | Medium | High | Phased approach; identify multiple funding sources early (NASA, DoD, university); 20% contingency in budget | Section 4 |
| **Component lead times** | Medium | Medium | Order long-lead items early (cameras, rad-hard components); maintain vendor relationships | [3, Ch.3, p.19 - procurement] |
| **Student graduation/turnover** | High (university projects) | Medium | Extensive documentation; cross-training; faculty continuity | [3, Ch.2, p.12 - student projects] |

**Risk Mitigation Budget:** 20% contingency ($20k in Section 4.1) addresses unknowns.

---

# SECTION 3: MISSION MODELS

## 3.1 System Architecture

**Platform:** 6U CubeSat (20 cm × 10 cm × 34 cm per CubeSat Design Specification [37], <14 kg max mass [37])

**Orbit:** Low Earth Orbit, 500 km altitude (baseline), circular, any inclination

**Lifetime:** 12 months primary mission (orbital lifetime ~8-15 years at 500 km [16])

### System Block Diagram

```
┌────────────────────────────────────────────────┐
│              RAD-AI 6U CubeSat                 │
│                                                 │
│  ┌──────────────────────────────────────────┐ │
│  │      AI PAYLOAD (Custom - Mission Core) │ │
│  │                                           │ │
│  │  ┌─────────────────────────────────┐    │ │
│  │  │ RISC-V Processor + AI Accel     │    │ │
│  │  │ - SiFive U74 quad-core [28]     │    │ │
│  │  │ - Custom NPU (FPGA or ASIC)     │    │ │
│  │  │ - 8 GB RAM, 128 GB storage      │    │ │
│  │  └──────────────┬──────────────────┘    │ │
│  │                 │                         │ │
│  │  ┌──────────────▼──────┐ ┌─────────────┐│ │
│  │  │ Vision Cameras (2x) │ │ Rad Sensors ││ │
│  │  │ - Star tracker [19] │ │ - Dosimeters││ │
│  │  │ - Horizon sensor    │ │ - SEU detect││ │
│  │  └─────────────────────┘ └─────────────┘│ │
│  │  Power: 15-30W | Mass: 400g | Vol: 1.5U│ │
│  └─────────────────┬────────────────────────┘ │
│                    │ I2C/SPI/UART              │
│  ┌─────────────────▼────────────────────────┐ │
│  │      CubeSat Bus (COTS - BCT or AAC)     │ │
│  │  ┌──────────┐  ┌──────────┐  ┌────────┐ │ │
│  │  │C&DH [20] │  │Power [17]│  │ADCS[21]│ │ │
│  │  │ARM-based │  │60Wh batt │  │Mag+RW  │ │ │
│  │  │2W        │  │45W solar │  │3W      │ │ │
│  │  └──────────┘  └──────────┘  └────────┘ │ │
│  │  ┌──────────┐  ┌──────────┐  ┌────────┐ │ │
│  │  │Comms[22] │  │Thermal   │  │Struct  │ │ │
│  │  │UHF 437MHz│  │Passive+H │  │Al-6061 │ │ │
│  │  │8W TX     │  │0-5W      │  │800g    │ │ │
│  │  └──────────┘  └──────────┘  └────────┘ │ │
│  └──────────────────────────────────────────┘ │
└────────────────────────────────────────────────┘
```

## 3.2 Subsystem Descriptions with Justification

### 3.2.1 AI Payload (Custom - Mission-Unique)

**Components:**

**AI Processor Board:**
- **RISC-V Core:** SiFive U74 quad-core, 1.5 GHz [28]
  - **Rationale:** Open-source ISA allows custom radiation mitigation; proven IP core; licensable for ~$10k [28]
- **AI Accelerator:** Custom neural processing unit (NPU) implemented in radiation-tolerant FPGA or ASIC
  - **Options:** Lattice CrossLink-NX FPGA [38] or custom ASIC if budget allows
  - **Performance Target:** 10-50 GOPS for vision inference (10 Hz frame processing)
- **Memory:** 8 GB DDR4 RAM (with ECC), 128 GB eMMC storage
- **Watchdog:** FPGA-based health monitor for autonomous fault detection
- **Power:** 15-30W (derived in Section 1.4.3)
- **Mass:** ~200g (PCB + components + heatsink)
- **Radiation Mitigation:**
  - Software: Triple Modular Redundancy (TMR), checkpointing [39]
  - Hardware: Selective shielding (2mm tantalum over processor, ~50g) [40]

**Vision Cameras:**
- **Primary Camera:** Blue Canyon NST star tracker camera [19]
  - Resolution: 1280×1024 pixels
  - FOV: 15° × 15°
  - Mass: ~100g, Power: ~1W
  - **Rationale:** Flight-proven on multiple CubeSats; serves dual role (attitude determination + AI vision input)

- **Secondary Camera:** COTS board camera (e.g., Raspberry Pi Camera v2 or similar)
  - Resolution: 640×480 pixels (adequate for horizon detection)
  - FOV: 60° × 45°
  - Mass: ~50g, Power: ~1W
  - **Rationale:** Low-cost COTS; horizon detection doesn't require star-tracker precision

**Radiation Sensors:**
- TID monitors: RADFETs (radiation-sensitive FETs) [41] - ~10g, <0.1W
- SEU detectors: SRAM array with periodic readback (custom board) - ~20g, ~0.3W
- Particle flux: Commercial energetic particle detector (e.g., Teledyne CEASE [42]) - ~20g, ~0.2W
- **Total:** ~50g, ~0.5W

**Fault Injection Module:**
- Integrated with FPGA watchdog
- Software-controllable memory bit-flip injection for validation of fault tolerance
- **Mass/Power:** Included in processor board estimates

**Total AI Payload Mass:** 200g (processor) + 100g (star tracker) + 50g (horizon cam) + 50g (rad sensors) = **400g**

**Total AI Payload Power:** 15-30W (processor, Section 1.4.3) + 2W (cameras) + 0.5W (rad sensors) = **17.5-32.5W**

### 3.2.2 CubeSat Bus (COTS - Baseline: Blue Canyon Technologies XACT 6U)

**Rationale for COTS Bus:**
Per CubeSat 101: "Use COTS when available" [3, Ch.2, p.13]. Integrated 6U bus reduces integration risk and development time.

**Options:**
1. **Blue Canyon Technologies (BCT) XACT 6U** [26]
   - Includes: C&DH, EPS, ADCS (reaction wheels + star tracker), structure
   - Mass: ~3.5 kg (bus only, without payload)
   - Power: Supports up to 60W payloads
   - Cost: ~$80k (published CubeSat bus pricing [43])
   - Heritage: 100+ spacecraft, high reliability

2. **AAC Clyde Space 6U Platform** [27]
   - Similar capabilities to BCT
   - Mass: ~3.2 kg
   - Cost: ~$70k
   - Heritage: Extensive European missions

**Selected Baseline:** BCT XACT 6U (slight mass increase acceptable; proven U.S. vendor; strong ADCS)

**Subsystem Specifications (from BCT XACT datasheet [26]):**

| Subsystem | Specification | Source |
|-----------|---------------|--------|
| **C&DH** | ARM Cortex processor, 2W power | [26] |
| **EPS** | 60 Wh battery, 45W solar generation (BOL) | [26] |
| **ADCS** | Reaction wheels + magnetorquers, ±0.02° pointing | [26] |
| **Comms** | UHF transceiver, 437 MHz, 9600 bps | Separate procurement [22] |
| **Structure** | 6U Al-6061 chassis, CubeSat Design Spec compliant [37] | [26] |

**Alternative (Custom Bus):**
If budget constraints prohibit COTS bus (~$80k), custom bus from COTS components estimated at ~$40k (Section 4.1).

## 3.3 Mass & Power Budgets - Detailed Derivation

### 3.3.1 Mass Budget (with COTS Bus Baseline)

| Subsystem | Mass (g) | Source / Justification | % of 8kg |
|-----------|----------|------------------------|----------|
| **AI Payload** | 400 | Section 3.2.1 breakdown | 5.0% |
| **BCT XACT Bus** | 3500 | BCT XACT datasheet [26] | 43.8% |
| **UHF Radio** | 100 | GomSpace NanoCom AX100 [22] | 1.3% |
| **UHF Antenna** | 50 | Deployable dipole (ISIS deployable [44]) | 0.6% |
| **Harness** | 200 | Rule of thumb: 5-10% of electronics mass [45] | 2.5% |
| **Thermal MLI** | 100 | Multi-layer insulation, ~100g for 6U [17, p.28] | 1.3% |
| **Margin (30%)** | 1335 | Per CubeSat 101: leave margin [3, Ch.2] | 16.7% |
| **Subtotal (with margin)** | **5685 g** | Sum | **71.1%** |
| **Available Growth** | **2315 g** | 8000g max [37] - 5685g | **28.9%** |

**Mass Margin Analysis:**
- Current best estimate (CBE): 4350g (no margin)
- With 30% margin: 5685g
- **Margin relative to 8 kg limit: 29%** (conservative, acceptable for preliminary design)

**Sensitivity:**
If COTS bus unavailable, custom bus estimate ~2000g (vs. 3500g COTS). Total mass ~3850g, **margin increases to 52%**.

### 3.3.2 Power Budget - Detailed by Operational Mode

Per CubeSat 101: Power budget should account for different operational modes [3, Ch.3, p.14].

**Mode 1: AI Inference (20% duty cycle)**

| Subsystem | Power (W) | Source |
|-----------|-----------|--------|
| AI Processor (full power) | 30 | Section 1.4.3 |
| Vision Cameras (active) | 2 | Section 3.2.1 |
| Rad Sensors | 0.5 | Section 3.2.1 |
| C&DH | 2 | BCT XACT spec [26] |
| ADCS | 5 | BCT XACT with RWs active [26] |
| Comms (RX) | 1 | GomSpace NanoCom [22] |
| Thermal | 0 | Nominal (no heaters in sunlight) |
| **Subtotal** | **40.5W** | |
| **With 20% margin** | **48.6W** | |

**Mode 2: AI Idle (70% duty cycle)**

| Subsystem | Power (W) | Source |
|-----------|-----------|--------|
| AI Processor (idle/sleep) | 5 | Estimated 1/6 of full power |
| Vision Cameras (off) | 0 | |
| Rad Sensors | 0.5 | Continuous monitoring |
| C&DH | 2 | Always on |
| ADCS | 3 | Magnetorquers only [26] |
| Comms (RX) | 1 | Listening for commands |
| Thermal | 0 | Nominal |
| **Subtotal** | **11.5W** | |

**Mode 3: Ground Pass (5% duty cycle)**

| Subsystem | Power (W) | Source |
|-----------|-----------|--------|
| AI Processor | 5 | Idle during downlink |
| C&DH | 2 | Processing telemetry |
| ADCS | 5 | Pointing antenna to ground [26] |
| Comms (TX) | 8 | GomSpace NanoCom transmit [22] |
| Thermal | 0 | |
| **Subtotal** | **20W** | |

**Mode 4: Safe Mode (5% duty cycle - eclipses with low battery)**

| Subsystem | Power (W) | Source |
|-----------|-----------|--------|
| AI Processor | 0 | Off to conserve power |
| C&DH | 2 | Minimum |
| ADCS | 3 | Sun-pointing (magnetorquers) |
| Comms (beacon) | 1 | Low-duty beacon |
| Thermal (heaters) | 5 | Battery survival heaters [17, p.29] |
| **Subtotal** | **11W** | |

**Weighted Average Power:**
(40.5W × 0.20) + (11.5W × 0.70) + (20W × 0.05) + (11W × 0.05) = **8.1 + 8.05 + 1.0 + 0.55 = 17.7W average**

**With 20% margin:** 17.7W × 1.2 = **21.2W average** (conservative case)

**Solar Generation:** 45W BOL → 40W EOL (Section 1.4.3)

**Margin:** 40W - 21.2W = **18.8W (47% margin)** ← Very healthy

**Note:** Earlier estimate of 36W average (Section 1.4.3) was conservative worst-case assuming higher AI duty cycle. Realistic duty cycle (20% inference, 70% idle) yields 21W average.

## 3.4 Concept of Operations

### 3.4.1 Mission Phases (Per CubeSat 101 Mission Planning [3, Ch.3])

**Phase 1: Launch & Early Operations (L+0 to L+30 days)**
- CubeSat deployed from P-POD dispenser on launch vehicle
- Initial acquisition of signal (AOS) with ground station
- Antenna deployment (burn-wire release, double-redundant per CubeSat 101 [3, Ch.2, p.15])
- Subsystem commissioning: Power, thermal, ADCS, comms checkout
- Payload remains powered off during this phase (risk mitigation)

**Phase 2: Payload Commissioning (L+30 to L+60 days)**
- AI processor first boot in orbit
- Vision camera calibration and initial image acquisition
- Radiation sensor baseline establishment (pre-exposure measurements)
- Initial AI inference tests (simple tasks: star identification, horizon fitting)
- Fault injection framework validation (controlled tests)
- Performance benchmarking in benign radiation environment (pre-SAA exposure)

**Phase 3: Nominal Science Operations (L+60 days to L+365 days)**
- Routine autonomous AI experiments:
  - Star tracking with onboard AI processing (10 Hz)
  - Horizon detection and altitude estimation
  - Debris/object identification in star field (if secondary camera available)
- Scheduled fault injection experiments (weekly)
- Continuous radiation monitoring (dosimetry, SEU logging)
- Periodic algorithm updates via ground upload (monthly)
- Data downlink 2-4 passes/day (10 MB/day target, Section 1.4)

**Phase 4: Extended Operations (L+365+ days, if spacecraft healthy)**
- Continued monitoring of long-term radiation effects (TID > 10 krad)
- Higher-risk experiments (aggressive fault injection, experimental algorithms)
- End-of-life battery/solar panel performance characterization
- Deorbit monitoring (passive decay from 500 km)

### 3.4.2 Daily Operations Timeline (Nominal Phase)

**Typical 24-Hour Period:**

```
00:00 UTC - Autonomous AI experiments begin
   |      - Inference Mode: Star tracking, horizon detection (20% duty cycle)
   |      - Idle Mode: Processor sleep between tasks (70% duty cycle)
   |      - Radiation monitoring: Continuous
   |      - Data stored onboard (128 GB storage, Section 3.2.1)
   |
04:00 UTC - Ground pass #1 (SatNOGS station, North America)
   |      - Duration: 10 minutes (typical LEO pass [32])
   |      - Activity: Telemetry downlink, beacon verification
   |      - No uplink needed (autonomous operations)
   |
08:00 UTC - Fault injection experiment (weekly schedule)
   |      - Controlled memory bit flips during non-critical operations
   |      - AI algorithm continues with mitigation active (TMR, checkpointing)
   |      - Recovery time and detection rate logged for analysis
   |
12:00 UTC - Ground pass #2 (University station, if available)
   |      - Duration: 15 minutes
   |      - Activity: Full science data downlink (images, inference results, rad data)
   |      - Command uplink: Update experiment parameters, upload new algorithms
   |
16:00 UTC - Eclipse period begins
   |      - AI processor throttled to conserve battery (reduce to 10% duty cycle)
   |      - Battery discharge monitored (60 Wh capacity, Section 1.4.3)
   |      - Thermal heaters activate if battery temperature < 0°C [17]
   |
18:00 UTC - Ground pass #3 (SatNOGS station, Europe or Asia)
   |      - Duration: 10 minutes
   |      - Activity: Health telemetry downlink, beacon
   |
22:00 UTC - Continued autonomous operations
   |      - Solar panels illuminated, battery recharging
   |      - AI experiments resume normal 20% duty cycle
   |
23:59 UTC - End of day; cycle repeats
```

**Annual Operations Summary:**
- **Ground passes:** ~1,500 passes/year (4+ per day average at 500 km [32])
- **Commanding:** Weekly updates (low command rate reduces operational burden)
- **Data volume:** 10 MB/day × 365 days = **3.65 GB/year total science data**
- **Operator burden:** Low (2-3 hours/week for routine ops; university-feasible)

### 3.4.3 Ground Segment

**Ground Station Options:**

| Option | Coverage | Cost/Year | Datasheet/Reference | Decision |
|--------|----------|-----------|---------------------|----------|
| **SatNOGS Network** | Global, 100+ stations [32] | Free (amateur radio community) | [32] | ✅ **PRIMARY** |
| **University Ground Station** | Local (if available) | $5k setup, in-kind ops | Varies by university | Secondary |
| **AWS Ground Station** | Global, on-demand [33] | ~$10k/year (pay-per-pass) | [33] | Contingency |
| **KSAT Lite** | Global commercial [34] | ~$15k/year | [34] | Contingency |

**Selected:** SatNOGS as primary (free, adequate for 9600 bps UHF); commercial backup for critical operations.

**Mission Operations Center (MOC):**
- **Location:** University campus (or home institution)
- **Staffing:** 2-3 student operators (part-time); 1 faculty supervisor
- **Software:** Open-source satellite operations tools (e.g., FreeFlyer [46], GMAT [47], custom Python scripts)
- **Data Pipeline:**
  - Raw telemetry → Database (InfluxDB or similar)
  - Science data → Processing scripts (Python: OpenCV for vision validation, radiation analysis)
  - Archiving → University server or AWS S3 (long-term storage)

## 3.5 Expected Outcomes & Data Products

### 3.5.1 Technical Deliverables

**1. Radiation Effects Database**
- **Content:** AI processor performance vs. total ionizing dose (TID); single-event upset (SEU) rates vs. orbit position (SAA correlation); inference accuracy degradation curves
- **Format:** CSV data files, plots, technical report
- **Audience:** NASA, ESA, commercial satellite developers (public release if NASA-funded)
- **Value:** Informs future rad-tolerant AI processor designs for Artemis, MSR, commercial missions

**2. Autonomous Vision Performance Dataset**
- **Content:** Onboard AI inference results (star positions, horizon fits) vs. ground truth (post-processed with commercial software)
- **Format:** Image files (raw + annotated), inference metrics (accuracy, latency), comparison plots
- **Audience:** Autonomous GN&C researchers, computer vision community
- **Value:** Validates vision algorithms for autonomous landing/proximity ops

**3. Fault Mitigation Effectiveness Study**
- **Content:** Fault injection experiment results (detection rates, recovery times, performance degradation under faults)
- **Format:** Statistical analysis, fault injection logs, mitigation algorithm descriptions
- **Audience:** Fault-tolerant computing researchers, spacecraft autonomy developers
- **Value:** Quantifies effectiveness of software-based radiation mitigation (TMR, checkpointing)

**4. Open-Source Flight Software Package**
- **Content:** RISC-V flight software (RTOS, drivers, AI inference code, fault detection/recovery)
- **Format:** GitHub repository with documentation
- **License:** Open-source (Apache 2.0 or MIT, if no ITAR restrictions)
- **Value:** Accelerates future CubeSat AI missions; reduces development costs for community

### 3.5.2 Strategic Impact (Mission Success Scenarios)

**Minimum Success (30-day operation):**
- ✅ Demonstrates AI processor can boot and operate in space
- ✅ Initial radiation environment characterization
- → **Value:** Proof-of-concept; identifies failure modes for follow-on missions

**Baseline Success (6-month operation with full autonomy demo):**
- ✅ Autonomous vision tasks validated (star tracking, horizon detection)
- ✅ Radiation effects characterized (TID, SEU) over meaningful duration
- ✅ Fault mitigation techniques validated via injection experiments
- → **Value:** Technology validated for near-term missions (Artemis lander pathfinder); publishable dataset

**Full Success (12-month operation with complete dataset):**
- ✅ Long-term radiation degradation quantified
- ✅ Algorithm updates demonstrated (upload new models, execute successfully)
- ✅ 7-day autonomous operation without ground contact (deep-space analog)
- → **Value:** Direct adoption for Artemis, MSR; commercial product development; benchmark dataset for field

**Extended Success (>12 months with advanced experiments):**
- ✅ Multi-year radiation data (correlate with solar cycle)
- ✅ Cutting-edge AI algorithms tested (advanced vision, reinforcement learning for control)
- ✅ Public dataset enables broader research community
- → **Value:** Maximum scientific return; establishes U.S. leadership in space-based AI

### 3.5.3 Educational Outcomes

**Student Learning:**
- Systems engineering: Requirements → Design → Integration → Test → Operations
- Radiation effects: SEU, TID, mitigation techniques (TMR, shielding, checkpointing)
- Embedded AI: Algorithm optimization, hardware acceleration, real-time constraints
- Spacecraft operations: Mission planning, ground segment, data analysis

**Career Preparation:**
- Hands-on CubeSat experience (highly valued by NASA, SpaceX, Blue Origin, etc.)
- Publication opportunities: IEEE Aerospace Conference [48], AIAA SmallSat [49], academic journals
- Professional network: NASA mentors, industry collaborators, academic partnerships
- Portfolio: Demonstrated spacecraft development (design → flight → operations)

---

# SECTION 4: FUNDING & BUDGET

## 4.1 Cost Estimate - Detailed Breakdown

Per CubeSat 101: "YOU pay for everything else" beyond CSLI launch [3, Ch.1, p.7]. Realistic budgeting is critical for mission success.

### Development & Hardware Costs

| Category | Item | Cost (USD) | Source / Justification |
|----------|------|------------|------------------------|
| **AI Payload Development** | | | |
| | RISC-V IP license (SiFive U74) | $10,000 | SiFive licensing model [28] |
| | Custom PCB design & fabrication (3 units) | $15,000 | 4-layer PCB, complex routing; 3 units (ETU, FM1, FM2) |
| | FPGA for AI accelerator (3x) | $5,000 | Lattice CrossLink-NX [38] ~$1500/unit × 3 |
| | Memory (RAM, eMMC) + components | $5,000 | Bulk electronics, 3 units |
| | Radiation shielding (tantalum) | $2,000 | 2mm tantalum sheet, ~50g [40] |
| | Engineering labor (payload design) | $8,000 | 200 hours × $40/hr (student rate); in-kind for university |
| **Vision Cameras** | | | |
| | Blue Canyon NST star tracker | $12,000 | Published CubeSat star tracker pricing [19] |
| | COTS horizon camera | $500 | Raspberry Pi Camera v2 or similar |
| **Radiation Sensors** | | | |
| | Dosimeters (RADFETs) | $2,000 | Commercial dosimeter set [41] |
| | SEU detector (custom board) | $1,000 | Simple SRAM board, 3 units |
| | Particle flux monitor | $3,000 | Teledyne CEASE or similar [42] |
| **CubeSat Bus** | | | |
| | **Option A: BCT XACT 6U (COTS)** | **$80,000** | Published CubeSat bus pricing [26, 43] |
| | **Option B: Custom bus from COTS subsystems** | **$40,000** | Alternative if budget-constrained (see breakdown below) |
| **Integration & Test** | | | |
| | Test harness & fixtures | $3,000 | Custom cables, interface boards |
| | Vibration testing | $5,000 | University facility or commercial (2 days) [29] |
| | Thermal vacuum testing | $5,000 | University facility or commercial (3 days) [29] |
| | DITL testing (72-hour mission sim) | $2,000 | University lab time, consumables |
| **Radiation Testing** | | | |
| | Heavy ion SEU testing | $5,000 | Texas A&M Cyclotron, 2 days [30] |
| | TID testing (Co-60 or X-ray) | $3,000 | University facility |
| | Proton testing (optional) | $7,000 | IUCF [36] - include if budget allows |
| **Software Development** | | | |
| | Flight software (RTOS, drivers, FSW) | $10,000 | 250 hours × $40/hr; in-kind for university |
| | AI algorithms (vision, control) | $5,000 | 125 hours × $40/hr; graduate student work |
| | Ground software (ops, data pipeline) | $5,000 | 125 hours × $40/hr |
| **Ground Station** | | | |
| | SatNOGS setup (if new station needed) | $2,000 | Antenna, SDR, Raspberry Pi [32] |
| | AWS Ground Station backup | $3,000 | 1 year subscription for critical passes [33] |
| **Program Management** | | | |
| | Documentation, reviews, travel | $5,000 | PDR/CDR preparation, travel to testing facilities |
| | **Subtotal (with COTS bus)** | **$105,500** | |
| | **Contingency (20%)** | **$21,100** | Per CubeSat 101: 10%+ reserve [3, Ch.2, p.17] |
| | **TOTAL DEVELOPMENT (COTS bus)** | **$126,600** | Rounded to **$120k-130k** |
| | **TOTAL DEVELOPMENT (Custom bus)** | **$86,600** | If using custom bus option (~$40k savings) |

**Custom Bus Breakdown (Option B):**
If COTS bus ($80k) is unaffordable, custom integration from COTS subsystems:

| Subsystem | Component Example | Cost (USD) | Source |
|-----------|-------------------|------------|--------|
| C&DH | Pumpkin Supernova [20] | $8,000 | Published pricing |
| EPS | Clyde Space 60Wh battery + EPS [25] | $15,000 | Vendor quote |
| ADCS | AAC Hyperion star tracker + magnetorquers [21] | $18,000 | Vendor pricing |
| Comms | GomSpace NanoCom AX100 [22] | $5,000 | Published pricing |
| Structure | 6U chassis (ISIS, Pumpkin) [44] | $3,000 | Commercial CubeSat structure |
| **Custom Bus Total** | | **~$40,000** | |

**Launch Costs:**
- **NASA CSLI (if selected):** $0 (free launch worth ~$250-500k [3, Ch.1])
- **Alternative (commercial launch):** $150,000-$300,000 (Spaceflight Inc., Exolaunch, Rocket Lab)

### Operations Costs (Annual)

| Category | Cost (USD) | Source |
|----------|------------|--------|
| Personnel (2-3 student operators, part-time) | $20,000 | In-kind for university (RA stipends) |
| Ground station network (commercial backup) | $3,000 | AWS Ground Station on-demand [33] |
| Data storage/processing (cloud) | $1,000 | AWS S3, EC2 [50] |
| Consumables & misc | $1,000 | Spare parts, travel |
| **Annual Ops Total** | **$25,000** | |

### Total Program Cost Summary

| Phase | Cost (USD) | Duration |
|-------|------------|----------|
| Development (COTS bus) | $120,000-$130,000 | 24 months |
| Development (Custom bus) | $85,000-$90,000 | 24 months |
| Launch (CSLI) | $0 | Included |
| Operations (1 year) | $25,000 | 12 months |
| **Total (COTS bus + CSLI)** | **$145,000-$155,000** | 36 months |
| **Total (Custom bus + CSLI)** | **$110,000-$115,000** | 36 months |

**If commercial launch required (CSLI not selected):**
Add $150k-$300k → Total: $260k-$455k

## 4.2 Funding Strategy & Sources

### Primary Funding: NASA CubeSat Launch Initiative (CSLI)

**What CSLI Provides:**
- Free launch (valued at $250-500k) [3, Ch.1, p.7]
- Launch integration support
- Access to NASA technical expertise

**CSLI Selection Criteria (from CubeSat 101 [3, Ch.1, p.8]):**
1. ✅ **Benefit to NASA:** RAD-AI enables Artemis, MSR autonomy (Section 1.3)
2. ✅ **Feasibility:** Realistic design, proven subsystems, achievable timeline (Sections 2-3)
3. ✅ **Merit:** Addresses NASA Technology Roadmap gap [8]
4. ✅ **Flexibility:** Any LEO orbit, any launch date (Section 1.4.1)

**RAD-AI CSLI Probability:** 90% (Document 17 evaluation [1]) based on:
- NASA Strategic Alignment: 9/10 (technology development for Artemis/MSR)
- Mission Simplicity: 6/7.5 (moderate complexity, single primary objective)
- Form Factor: 5/5 (standard 6U)
- Launch Flexibility: 5/5 (any LEO orbit)

**Application Timeline:**
- CSLI solicitation: Annual (typically March-April) [51]
- Selection notification: ~6 months after application
- Manifesting: 1-3 years after selection (highly variable [3, Ch.1])

### Development Funding Sources

**1. NASA Space Technology Mission Directorate (STMD) Grants**
- **Programs:** Space Technology Research Grants (STRG) [52], Flight Opportunities Program
- **Typical Award:** $50,000-$150,000
- **Fit:** Technology demonstration missions like RAD-AI are priority
- **Timeline:** Annual solicitation, 6-month review cycle

**2. DoD / Air Force Research Laboratory (AFRL)**
- **Programs:** University Nanosat Program [53], AFRL Small Business Innovation Research (SBIR) Phase I/II
- **Typical Award:** $50,000-$100,000 (university grants)
- **Fit:** Rad-hard AI for Space Force applications (autonomous satellite operations, space domain awareness)
- **Approach:** Emphasize dual-use (NASA science + DoD operational applications)

**3. University Cost-Share / Internal Grants**
- **Amount:** $10,000-$30,000
- **Sources:** University research office, department discretionary funds, alumni donations
- **Fit:** Educational value (student training, curriculum development)
- **In-Kind:** Lab space, faculty time, student labor (RA/TA stipends)

**4. Industry Partnerships**
- **SiFive (RISC-V vendor):** In-kind RISC-V IP license or discounted licensing (~$10k value) [28]
- **Blue Canyon / AAC Clyde:** Educational pricing or partnership (10-20% discount on bus)
- **NVIDIA / Google:** AI processor sponsorship (donate Jetson or Coral dev kits for ground testing)

### Funding Timeline & Approach

**Year 0 (Course Project - Design Phase):**
- **Funding Needed:** Minimal ($5k for preliminary studies, student stipends)
- **Sources:** University department funds, faculty startup funds
- **Activity:** Complete design (this document → detailed design)

**Year 1 (Implementation Phase - Months 1-12):**
- **Funding Needed:** $80k-100k (procurement, fabrication, testing)
- **Sources:**
  - NASA STMD grant application (submit Month 1): $75k target
  - AFRL University Nanosat application (submit Month 2): $50k target
  - University cost-share: $20k committed
  - **Total Available:** $145k (exceeds $100k need; provides margin)
- **Activity:** Build payload, procure bus, integration, environmental testing

**Year 2 (Launch & Operations - Months 13-24):**
- **Funding Needed:** $25k (operations)
- **Sources:**
  - Remainder of NASA/AFRL grants (carryover from Year 1)
  - University operations budget (in-kind student labor)
- **Activity:** Launch, commissioning, science operations

**Contingency Plan (if primary funding not secured):**
- **Phased Approach:** Build payload only (~$60k); defer bus procurement until funding confirmed
- **Custom Bus Option:** Reduces cost from $120k → $85k (Section 4.1)
- **Commercial Launch Alternative:** If CSLI not selected, pursue NASA Venture Class Launch Services [54] (lower-cost commercial launches)

---

# CONCLUSION & NEXT STEPS

## Summary

RAD-AI represents a high-value, achievable CubeSat mission that directly addresses NASA's critical need for autonomous decision-making in deep-space missions. The mission balances innovation (radiation-tolerant RISC-V + AI integration at CubeSat scale) with practicality (COTS bus, flight-proven subsystems, realistic budget) to deliver technology validation that enables Artemis autonomous landing, Mars Sample Return operations, and commercial satellite autonomy applications.

## Why RAD-AI Succeeds

**✅ Strong Validation (Tier 2):** NASA explicitly states need for autonomous spacecraft in Artemis Plan [4] and MSR Campaign [7]; Technology Roadmap gap identified [8]

**✅ High Innovation (4/5):** Novel integration of RISC-V open-architecture processor with AI acceleration hardware in radiation-tolerant CubeSat platform; no current space-qualified solution exists

**✅ Excellent CSLI Fit (90% probability):** Technology demonstration (66% of CSLI missions [3]); strong NASA benefit; maximum launch flexibility (any LEO orbit)

**✅ Appropriate Scope:** 12-month design + 12-month implementation achievable for masters program; realistic budget ($100-130k + CSLI free launch)

**✅ Multi-Mission Impact:** Pathfinder technology for Artemis landers, MSR autonomy, asteroid proximity ops, and commercial autonomous satellites

**✅ Documented Design Basis:** All requirements, budgets, and design decisions justified with references (this document includes 54 citations to technical sources)

## Next Steps (Course Project Progression)

**Immediate (Weeks 1-2):**
1. ✅ Instructor review of initial pitch (this document)
2. Feedback incorporation and design refinement
3. Decision: Proceed with RAD-AI or iterate concept

**Phase 1 (Weeks 3-6): Detailed Trade Studies**
- RISC-V processor core selection (SiFive U74 vs. alternatives; detailed comparison)
- AI accelerator architecture (FPGA vs. ASIC; performance/cost/risk trades)
- CubeSat bus vendor selection (BCT vs. AAC Clyde vs. custom; final decision with quotes)
- Radiation mitigation technique selection (software TMR vs. hardware redundancy)
- **Deliverable:** Trade study report, preliminary design package

**Phase 2 (Weeks 7-10): Subsystem Specifications**
- AI payload board detailed design (schematic, PCB layout, BOM)
- Vision camera integration design (mechanical, electrical, optical interfaces)
- Power system detailed analysis (battery sizing validation, solar panel layout)
- Thermal analysis (SINDA model or thermal desktop)
- **Deliverable:** Subsystem specification documents, CAD models

**Phase 3 (Weeks 11-14): Integration Planning & Verification**
- Integration & Test (I&T) plan development
- Environmental test procedures (vibration, thermal vac per GEVS [29])
- Mission operations plan (ConOps refinement, ground segment design)
- Verification matrix (requirements → test mapping)
- **Deliverable:** I&T plan, operations plan, verification matrix

**Phase 4 (Weeks 15-16): CSLI Proposal Preparation**
- CSLI application package (if pursuing flight)
- Budget finalization with vendor quotes
- Partnership letters (university, industry mentors)
- Risk assessment and mitigation plan
- **Deliverable:** Complete CSLI proposal (ready for submission)

**Post-Course (if pursuing flight):**
- Submit CSLI application (March-April annual cycle [51])
- Secure development funding (NASA STMD, AFRL applications)
- Transition to implementation phase (24-month build/test/fly)

---

# REFERENCES

[1] Document 17: Mission Table Comprehensive Evaluation. Internal project document, 2025-11-02.

[2] NASA Mars Facts - Earth-Mars Distance: https://mars.nasa.gov/all-about-mars/facts/ (Communication delay: 6-44 minutes one-way)

[3] NASA CubeSat 101: Basic Concepts and Processes for First-Time CubeSat Developers. NASA CubeSat Launch Initiative, 2017. (Course-provided document)

[4] NASA Artemis Plan. NASA, 2024. https://www.nasa.gov/artemis/

[5] BAE Systems RAD750 Datasheet. BAE Systems, 2020.

[6] Autonomous Landing Hazard Avoidance Technology (ALHAT). NASA Langley Research Center. (10-30 Hz processing requirement for terrain relative navigation)

[7] Mars Sample Return Campaign Plan. NASA/ESA, 2023.

[8] NASA Technology Roadmaps TA4: Robotics and Autonomous Systems. NASA Office of Chief Technologist, 2020, p.47.

[9] BAE Systems RAD5545 Datasheet. BAE Systems, 2019.

[10] NVIDIA Jetson Nano Datasheet. NVIDIA Corporation, 2023. (5-10W power consumption, 500 GFLOPS)

[11] Google Coral Edge TPU Datasheet. Google LLC, 2023. (4 TOPS inference performance)

[12] South Atlantic Anomaly (SAA) passage frequency at LEO altitudes. Heynderickx, D., et al., "ESA's Space Environment Information System (SPENVIS)," 2004.

[13] Total Ionizing Dose (TID) rates in LEO. Barth, J.L., "Modeling Space Radiation Environments," NASA/JPL Short Course, 1997.

[14] Single Event Upset (SEU) rates for commercial electronics. Petersen, E.L., "Single Event Effects in Aerospace," IEEE Press, 2011.

[15] NASA-STD-8719.14: Process for Limiting Orbital Debris. NASA, 2019. (25-year deorbit requirement)

[16] Orbital Lifetime Calculator. NASA Orbital Debris Program Office. (500 km: 8-15 year decay; 600 km: 15-25 years)

[17] Wertz, J.R., et al., "Space Mission Engineering: The New SMAD," Microcosm Press, 2011. (CubeSat power/thermal design guidelines)

[18] Swartwout, M., "CubeSat Database," Saint Louis University, 2024. (Statistics on CubeSat form factors and launch rates)

[19] Blue Canyon Technologies NST (Nano Star Tracker) Datasheet, 2023. (~1W power, 1280x1024 resolution)

[20] Pumpkin Supernova Flight Computer Datasheet. Pumpkin Inc., 2022. (ARM Cortex-M4, 1-2W power)

[21] AAC Clyde Space ADCS Datasheet, 2023. (Magnetorquers + reaction wheels)

[22] GomSpace NanoCom AX100 Transceiver Datasheet, 2023. (UHF 437 MHz, 8W TX, 1W RX)

[23] Solar Constant and LEO Insolation. ASTM E490 Standard for Solar Irradiance. (1367 W/m² at 1 AU)

[24] Eclipse Duration in LEO. Curtis, H., "Orbital Mechanics for Engineering Students," 4th ed., 2020. (~35 min eclipse per 90 min orbit at 500 km)

[25] AAC Clyde Space 60Wh Battery Datasheet, 2023.

[26] Blue Canyon Technologies XACT-6U Datasheet, 2023. (~3.5 kg, 60W payload support, ~$80k published pricing)

[27] AAC Clyde Space 6U CubeSat Platform Datasheet, 2023. (~3.2 kg, ~$70k)

[28] SiFive U74 RISC-V Core Product Brief, 2023. (1.5 GHz quad-core, licensing ~$10k)

[29] GEVS (General Environmental Verification Standard). NASA-GSFC-STD-7000B, 2021. (Vibration: 14.1 Grms random)

[30] Texas A&M University Cyclotron Institute. Heavy ion testing services. (Academic rates ~$2500/day)

[31] NanoAvionics CubeSat Platforms, 2023.

[32] SatNOGS (Satellite Networked Open Ground Station). https://satnogs.org/ (Global amateur radio ground station network, free)

[33] AWS Ground Station Pricing, 2024. https://aws.amazon.com/ground-station/pricing/ (~$10k/year for LEO CubeSat)

[34] KSAT Lite Ground Station Services, 2024. (~$15k/year for LEO)

[35] Lawrence Berkeley National Lab (LBNL) 88-Inch Cyclotron. Heavy ion radiation testing facility.

[36] Indiana University Cyclotron Facility (IUCF). Proton radiation testing services.

[37] CubeSat Design Specification (CDS) Rev 14. California Polytechnic State University, 2022. (6U: 20×10×34 cm, <14 kg)

[38] Lattice CrossLink-NX FPGA Datasheet, 2023. (Radiation-tolerant option available)

[39] Lyons, R.E., Vanderkulk, W., "The Use of Triple-Modular Redundancy to Improve Computer Reliability," IBM Journal, 1962. (TMR mitigation technique)

[40] Selective Shielding for Electronics. Holmes-Siedle, A., Adams, L., "Handbook of Radiation Effects," 2nd ed., 2002. (2mm tantalum provides ~10× TID protection)

[41] RADFETs (Radiation-Sensitive FETs). REM Oxford Ltd. Dosimeter products.

[42] Teledyne CEASE (Compact Environmental Anomaly Sensor). Teledyne Brown Engineering, 2022.

[43] CubeSat Bus Pricing Survey. Nanosats.eu database, 2023. (COTS 6U bus: $70k-$120k range)

[44] ISIS Deployable Antenna System Datasheet. Innovative Solutions In Space, 2023. (~50g dipole antenna)

[45] Spacecraft Harness Mass Estimation. Wertz, J.R., "Spacecraft Harness Mass Rules of Thumb," SMAD, 2011. (5-10% of electronics mass)

[46] FreeFlyer Astrodynamics Software. Analytical Graphics Inc. (Mission planning tool)

[47] GMAT (General Mission Analysis Tool). NASA Goddard Space Flight Center. (Open-source mission design software)

[48] IEEE Aerospace Conference. Annual conference (March), Snowmass, CO. (Primary CubeSat publication venue)

[49] AIAA/USU SmallSat Conference. Annual conference (August), Logan, UT. (CubeSat research dissemination)

[50] AWS Pricing Calculator. https://calculator.aws/ (Cloud storage/compute cost estimation)

[51] NASA CSLI Solicitation Schedule. https://www.nasa.gov/cubesat-launch-initiative (Annual cycle, typically March-April)

[52] NASA Space Technology Research Grants (STRG). https://www.nasa.gov/strg/ (University research grants, $50k-$150k)

[53] AFRL University Nanosat Program. https://www.airuniversity.af.edu/AFROTC/Display/Article/2166855/university-nanosat-program/ (DoD small satellite university grants)

[54] NASA Venture Class Launch Services (VCLS). https://www.nasa.gov/vcls/ (Low-cost commercial launch procurement)

---

**Document Type:** Initial Project Pitch with Complete Technical Justification
**Created:** 2025-11-02 (Revised with citations and design rationale)
**Word Count:** ~8,500 words
**References:** 54 technical sources cited
**Compliance:** CubeSat 101 Chapters 1-3, Assignment requirements
**Status:** Ready for instructor review
**Next Version:** Incorporate instructor feedback → Detailed design phase
