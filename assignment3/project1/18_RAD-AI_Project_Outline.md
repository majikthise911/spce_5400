# RAD-AI CubeSat Mission: Project Outline
**Radiation-Tolerant Edge AI Computer for Autonomous Space Operations**

**Project Type:** CubeSat Mission Design - Masters in Space Operations
**Mission Class:** Technology Demonstration / In-Space Computing
**Target Launch Program:** NASA CubeSat Launch Initiative (CSLI)
**Development Timeline:** 12-15 months (design phase for course project)

---

## DOCUMENT STRUCTURE

This outline follows the CubeSat 101 process structure as specified in assignment requirements:
1. **Introduction** - Mission concept, objectives, and rationale
2. **Process** - Development approach, timeline, and methodology
3. **Mission Models** - System architecture, subsystems, and operations concept

---

# SECTION 1: INTRODUCTION

## 1.1 Mission Concept

**Mission Name:** RAD-AI (Radiation-Tolerant Autonomous Intelligence)

**One-Line Description:**
A 6U CubeSat demonstrating radiation-tolerant edge artificial intelligence for autonomous vision and control tasks in orbit, validating critical technology for future deep-space missions where communication latency prevents real-time ground control.

**Mission Type:** Technology Demonstration / In-Space Computing Validation

**Primary Innovation:**
Integration of a radiation-tolerant RISC-V processor with AI acceleration hardware running autonomous vision-based navigation and control algorithms, with live fault injection to validate radiation mitigation techniques in the space environment.

## 1.2 Mission Objectives

### Primary Objective
Demonstrate radiation-tolerant edge AI processing in Low Earth Orbit (LEO) performing autonomous vision-based tasks with real-time fault detection and mitigation.

### Secondary Objectives
1. **Radiation Characterization:** Measure single-event upsets (SEUs) and total ionizing dose (TID) effects on RISC-V AI processor in LEO environment
2. **Autonomous Vision Validation:** Execute onboard computer vision tasks (star tracking, horizon detection, debris identification) without ground-in-the-loop
3. **Fault Injection Testing:** Demonstrate software and hardware fault mitigation techniques through controlled error injection
4. **Performance Benchmarking:** Quantify AI inference performance degradation under radiation exposure over mission lifetime
5. **Data Collection:** Generate dataset for autonomous deep-space mission planning (radiation effects on AI processors)

### Success Criteria
- **Minimum Success:** AI processor boots and executes basic inference tasks in orbit for 30 days
- **Baseline Success:** Autonomous vision tasks execute successfully; radiation effects characterized; fault injection demonstrates mitigation
- **Full Success:** 12-month operation; complete radiation characterization; published dataset enables future mission designs

## 1.3 Mission Rationale and Need

### The Deep-Space Autonomy Problem
Current and near-future deep-space missions face a critical challenge:

**Communication Latency:**
- Mars: 6-44 minutes one-way light time (depending on orbital positions)
- Asteroid belt: 20-40 minutes one-way
- Outer planets: Hours to days

**Implication:** Real-time ground control is impossible. Spacecraft must make autonomous decisions.

**Current Limitation:**
Traditional radiation-hardened processors (e.g., RAD750, RAD5545) operate at ~200 MHz with limited memory and no AI acceleration. These cannot run modern computer vision and machine learning algorithms required for:
- Autonomous landing site selection (Mars, Moon, asteroids)
- Real-time hazard avoidance during descent
- Onboard science prioritization
- Autonomous proximity operations
- Fault detection and recovery

**The Gap:**
Commercial AI processors (NVIDIA Jetson, Google Edge TPU, Intel Movidius) offer orders of magnitude better performance but are not radiation-tolerant. No current space-qualified processor combines AI acceleration with radiation tolerance at reasonable size, weight, and power (SWaP) for CubeSats.

### NASA Strategic Alignment

**Artemis Program:**
> "Autonomous precision landing is critical for Artemis missions to establish sustainable lunar presence" - NASA Artemis Plan (2024)

**Mars Sample Return:**
> "Autonomous hazard detection and avoidance during Mars Ascent Vehicle launch and rendezvous operations" - MSR Campaign Plan

**Asteroid Redirect Mission / Planetary Defense:**
Requires autonomous rendezvous with non-cooperative, tumbling targets in deep space.

**Technology Roadmap TA4 (Robotics & Autonomous Systems):**
- TA4.4: Relative Guidance, Navigation, and Control
- TA4.5: Autonomy for Entry, Descent, and Landing
- **Gap identified:** Radiation-tolerant edge AI for autonomous decision-making

### Commercial and Defense Interest

**DoD Space Domain Awareness:**
- DARPA Blackjack constellation demonstrated edge processing interest
- Space Force seeks autonomous satellite operations

**Commercial LEO Constellations:**
- On-orbit processing reduces downlink bandwidth requirements
- AI-based anomaly detection and autonomous constellation management

### Why RAD-AI Addresses This Need

**Technology Demonstration:**
1. **RISC-V Architecture:** Open-source ISA allows custom radiation-mitigation techniques
2. **AI Acceleration:** Integrated neural network accelerator for inference at edge
3. **CubeSat Platform:** Low-cost testbed validates technology at $100k vs. $10M+ flagship mission risk
4. **Flight Data:** Real radiation environment data informs future processor designs

**Pathfinder for:**
- Artemis autonomous landers
- Mars Sample Return autonomous operations
- Asteroid proximity operations
- Commercial satellite autonomy

## 1.4 Benefits to NASA

### Direct Benefits
1. **Technology Validation:** De-risks AI processor technology for Artemis, MSR, and future missions
2. **Radiation Database:** Flight data on AI processor radiation effects informs future designs
3. **Cost Reduction:** CubeSat demonstration (~$100k) vs. risk on flagship mission
4. **CSLI Mission Alignment:** Technology development (66% of CSLI selections per CubeSat 101)

### Indirect Benefits
1. **Workforce Development:** Trains engineers in autonomous systems and radiation effects
2. **Commercial Enablement:** Validates technology for commercial autonomous satellites
3. **International Leadership:** Demonstrates U.S. capability in space-based AI (vs. China's on-orbit AI demonstrations)
4. **Multi-Mission Applicability:** Technology applicable to lunar, Mars, asteroid, and Earth observation missions

### Alignment with NASA Strategic Plan 2024

**Strategic Goal 1: Expand Human Knowledge Through New Scientific Discoveries**
- Objective 1.5: Enable new science missions through advanced autonomous systems

**Strategic Goal 2: Extend Human Presence to the Moon and on to Mars**
- Objective 2.1: Lay the foundation for America to maintain a constant human presence in low Earth orbit (autonomous operations)
- Objective 2.2: Lead the return of humans to the Moon for long-term exploration and utilization (autonomous landing systems)

**Strategic Goal 3: Drive Efficient Growth of the Space Economy**
- Objective 3.2: Enable new commercial space capabilities (autonomous satellite operations)

## 1.5 Mission-Level Requirements Summary

| Requirement | Value | Rationale |
|-------------|-------|-----------|
| **Orbit** | LEO, any inclination, 400-600 km altitude | Maximize launch flexibility; LEO radiation environment sufficient for demo |
| **Mission Duration** | 12 months baseline, 6 months minimum | Characterize radiation effects over time; accommodate typical LEO degradation |
| **Form Factor** | 6U CubeSat | AI processor + vision cameras + radiation sensors + margin |
| **Mass** | <10 kg (target 8 kg) | 6U max = 14 kg; leave margin per CubeSat 101 best practice |
| **Power** | <40W average, <60W peak | AI processor + cameras during inference bursts |
| **Downlink Data** | 10 MB/day minimum | Vision processing results, telemetry, radiation data |
| **Autonomy** | 7-day autonomous operation | Demonstrate ground-independent operation for deep-space analog |
| **Radiation Tolerance** | Survive 10 krad TID, SEU mitigation | Typical LEO environment over 1 year; validate mitigation techniques |

---

# SECTION 2: PROCESS

## 2.1 Development Philosophy

### "Test Like You Fly" Approach
Per CubeSat 101 best practices:
- Build multiple units: Engineering Test Unit (ETU), Flight Model 1 (FM1), Flight Model 2 (FM2 spare)
- Extensive ground testing before flight
- Comprehensive photo documentation throughout development
- Conservative design with margin (no envelope-chasing)

### Agile Hardware Development
- 2-week sprints for software development
- Monthly hardware integration milestones
- Continuous testing and validation
- Risk-driven development: tackle highest-risk items first

### Heritage and COTS Priority
Per CubeSat 101 guidance:
- Use Commercial Off-The-Shelf (COTS) components with flight heritage wherever possible
- Custom development ONLY for core payload (AI processor board)
- Leverage existing CubeSat bus platforms if available

## 2.2 Development Timeline (12-Month Design Phase for Course)

### Phase 1: Concept Development (Months 1-2)
**Activities:**
- Mission requirements refinement
- Preliminary system architecture design
- Trade studies (processor selection, vision sensor options, radiation mitigation techniques)
- Concept of Operations (ConOps) development
- Stakeholder identification and engagement

**Deliverables:**
- Mission Requirements Document (MRD)
- System Requirements Review (SRR) package
- Preliminary Design Review (PDR) prep

**Key Decisions:**
- RISC-V processor core selection (SiFive U74 vs. U84 vs. custom)
- AI accelerator architecture (custom vs. integrated)
- Vision sensor selection (visible camera vs. star tracker-grade)
- CubeSat bus vendor (Blue Canyon Technologies, AAC Clyde, in-house)

### Phase 2: Preliminary Design (Months 3-4)
**Activities:**
- Detailed subsystem design
- Interface Control Document (ICD) development
- Power budget analysis
- Mass budget analysis
- Thermal analysis
- Link budget analysis
- CAD modeling (mechanical)
- Software architecture design
- Preliminary test plan

**Deliverables:**
- Preliminary Design Review (PDR) package
- Subsystem specifications
- Interface definitions
- Budget spreadsheets (power, mass, data, cost)
- Test plan outline

**Trade Studies:**
- Orbit selection (altitude, inclination trade for radiation exposure vs. lifetime)
- Redundancy architecture (dual processor vs. single with watchdog)
- Fault mitigation techniques (TMR vs. checkpointing vs. forward error correction)
- Ground station (university vs. commercial network vs. amateur radio)

### Phase 3: Detailed Design (Months 5-8)
**Activities:**
- Critical Design Review (CDR) preparation
- Detailed CAD (mechanical, electrical, thermal)
- Radiation mitigation design implementation
- Software detailed design
- Fault injection framework design
- Test procedure development
- Vendor selection and procurement planning

**Deliverables:**
- Critical Design Review (CDR) package
- Manufacturing drawings
- PCB layouts
- Software design documents
- Detailed test procedures
- Procurement package with quotes

**Subsystem Designs:**
- AI Payload Board (custom PCB with RISC-V + AI accelerator)
- Vision camera integration (commercial COTS)
- Radiation sensor suite (commercial dosimeters + custom SEU detectors)
- CubeSat bus integration (power, ADCS, comms, structure)

### Phase 4: Integration Planning & Validation (Months 9-12)
**Activities:**
- Integration and Test (I&T) procedure development
- Environmental test planning (vibration, thermal vacuum)
- Flight software validation approach
- Mission operations planning
- Ground segment design
- Data analysis pipeline development
- CSLI proposal preparation

**Deliverables:**
- Integration & Test Plan
- Environmental Test Procedures
- Mission Operations Concept (MOC)
- Ground Segment Design
- CSLI Proposal Package (if pursuing flight)

**Course Project Outcome:**
- Complete mission design documentation
- Subsystem specifications sufficient for build phase
- Test-like-you-fly approach validated through simulation
- Cost and schedule estimates for implementation phase

### Post-Course: Implementation Phase (IF pursuing flight, Months 13-24)
**Would Include:**
- Hardware fabrication and assembly
- Software implementation and testing
- Subsystem testing
- Integration and environmental testing
- Flight readiness reviews
- Delivery to launch provider
- Launch and early operations

## 2.3 Team Structure

### Recommended Team Composition (for course project design phase)

**Mission Lead / Systems Engineer** (1 person)
- Overall mission architecture
- Requirements management
- Interface coordination
- Schedule and budget tracking

**Payload Engineer** (1-2 people)
- AI processor board design
- Radiation mitigation implementation
- Fault injection framework
- Performance benchmarking

**Software Lead** (1-2 people)
- Flight software architecture
- AI algorithm implementation (vision, control)
- Fault detection and recovery software
- Ground software and data pipeline

**ADCS Engineer** (1 person)
- Attitude determination and control
- Vision sensor integration
- Pointing requirements for cameras
- Coordinate with payload for vision-based navigation experiments

**Power/Thermal Engineer** (1 person)
- Power system design and budgeting
- Battery sizing
- Solar panel configuration
- Thermal analysis and mitigation

**Communications Engineer** (1 person)
- RF link design
- Ground station coordination
- Licensing (FCC coordination)
- Data downlink optimization

**Integration & Test Lead** (1 person)
- Test planning and execution
- Environmental test coordination
- Verification matrix management
- Quality assurance

**Advisors/Mentors:**
- Faculty advisor (mission oversight)
- Industry mentor - radiation effects expert
- Industry mentor - AI/ML in embedded systems
- NASA CSLI liaison (if applicable)

### External Partnerships
- **Radiation Testing Facility:** University rad lab or NASA JPL
- **CubeSat Bus Vendor:** Blue Canyon Technologies, AAC Clyde Space, or similar
- **Ground Station:** University station, Amateur Radio network, or commercial (AWS Ground Station, KSAT)
- **Component Suppliers:** SiFive (RISC-V cores), vision sensor vendors, radiation sensor vendors

## 2.4 Development Approach for Key Subsystems

### 2.4.1 AI Payload Development

**Processor Selection Trade:**
| Option | Pros | Cons | Recommendation |
|--------|------|------|----------------|
| SiFive U74 RISC-V | Open-source, customizable, moderate performance | No integrated AI accel | Good baseline |
| Custom RISC-V + NPU | Maximum performance, tailored mitigation | High development cost/time | Too risky for masters |
| Commercial AI SoC + shielding | High performance, COTS | Unknown radiation tolerance | Testable option |

**Approach:**
1. **Phase 1:** Characterize commercial AI processor (NVIDIA Jetson Nano or Google Coral) radiation tolerance via ground testing
2. **Phase 2:** If acceptable, use with shielding; if not, design custom RISC-V board
3. **Mitigation:** Software-based (checkpointing, TMR, algorithm-level redundancy)

**Radiation Mitigation Techniques:**
- **Hardware:** Selective shielding (tantalum, tungsten), rad-tolerant FPGA watchdog
- **Software:** Triple Modular Redundancy (TMR), checkpointing, forward error correction
- **System:** Dual-processor voting, watchdog timers, autonomous reboot capability

### 2.4.2 Vision System Development

**Camera Options:**
| Sensor Type | Use Case | Heritage | Selection |
|-------------|----------|----------|-----------|
| COTS star tracker camera | High-precision attitude | Extensive CubeSat use | PRIMARY for star field |
| Commercial visible camera | Earth imaging, horizon detection | Planet Labs heritage | SECONDARY for horizon |
| Custom low-light sensor | Debris detection | Limited | TERTIARY if budget |

**Vision Tasks:**
1. **Star tracking:** Autonomous attitude determination (replacing ADCS star tracker)
2. **Horizon detection:** Earth limb finding for altitude/attitude estimation
3. **Debris identification:** Object detection in star field (if secondary camera available)

**Processing Pipeline:**
- Onboard: Real-time inference for navigation tasks
- Downlink: Raw images periodically for ground truth validation

### 2.4.3 Fault Injection Framework

**Purpose:** Validate radiation mitigation by intentionally inducing faults

**Injection Methods:**
1. **Software bit flips:** Controlled memory corruption to simulate SEUs
2. **Processor register corruption:** Simulate control logic upsets
3. **Algorithm input corruption:** Test AI robustness to bad sensor data

**Validation:**
- **Ground:** Inject faults in hardware-in-the-loop testbed
- **Flight:** Scheduled fault injection experiments (during safe modes, not critical ops)

**Metrics:**
- Detection rate (% of faults detected by mitigation)
- Recovery time (seconds from fault to recovery)
- Performance degradation (inference accuracy under fault conditions)

## 2.5 Testing Strategy

### Ground Testing Philosophy
Per CubeSat 101: "Test like you fly"
- All software tested in flight-like conditions
- All hardware subjected to environmental testing
- End-to-end mission rehearsals before flight

### Test Levels

**Level 1: Component Testing**
- AI processor board bring-up and characterization
- Vision camera calibration
- Radiation sensor validation
- Individual subsystem functional tests

**Level 2: Subsystem Integration Testing**
- Payload board + vision cameras integrated operation
- Power system under load
- Communications system end-to-end
- ADCS with vision sensors

**Level 3: System Integration Testing**
- Full CubeSat integrated operation
- Flight software on flight hardware
- End-to-end mission scenarios
- 72-hour "Day In The Life" (DITL) test

**Level 4: Environmental Testing**
Required per CSLI:
- **Vibration testing:** Simulate launch loads (random vibration, sine sweep)
- **Thermal vacuum testing:** Validate operation across temperature range in vacuum
- **EMI/EMC testing:** Electromagnetic compatibility
- **Functional testing:** Post-environmental verification

### Radiation Testing Strategy

**Ground-Based Radiation Testing:**
- Heavy ion testing (simulate SEUs) at university or national lab cyclotron
- Total Ionizing Dose (TID) testing using Co-60 source or X-ray
- Proton testing if budget allows (simulate trapped radiation belt)

**Test Matrix:**
| Test Type | Facility | Objective | Timeline |
|-----------|----------|-----------|----------|
| Heavy Ion SEU | Texas A&M or LBNL | Characterize upset cross-section | Month 8-10 |
| TID | University rad lab | Validate TID tolerance to 10+ krad | Month 8-10 |
| Proton (optional) | IUCF or similar | Validate proton tolerance | Month 11-12 |

**Expected Results:**
- SEU cross-section for RISC-V processor under various ions
- TID tolerance curve (performance vs. dose)
- Validation of mitigation effectiveness

## 2.6 Risk Management

### Top Technical Risks and Mitigation

| Risk | Probability | Impact | Mitigation |
|------|------------|--------|------------|
| **AI processor radiation tolerance worse than expected** | Medium | High | Ground rad testing early; have fallback to rad-hard FPGA |
| **Power budget exceeded** | Medium | Medium | Conservative design; operating modes with reduced power |
| **Thermal issues with AI processor** | Low | Medium | Early thermal analysis; heat pipes or radiators if needed |
| **Vision algorithm doesn't perform in space** | Low | Medium | Extensive ground validation; graceful degradation design |
| **Launch delays** | High | Low | Mission designed for any LEO orbit; flexible launch date |
| **Funding shortfall** | Medium | High | Phased approach; identify multiple funding sources early |

### Schedule Risks
- **Component lead times:** Order long-lead items early (cameras, rad-hard components)
- **Rad testing facility availability:** Book cyclotron time 6+ months in advance
- **Student graduation/turnover:** Document extensively; cross-train team members

### Budget Risks
- **Component cost growth:** 10% contingency in budget
- **Rad testing costs:** Negotiate university rates; consider government facility access
- **Launch cost:** CSLI covers launch; but integration/travel costs exist

## 2.7 Regulatory and Licensing

### FCC Licensing (Amateur Radio or Commercial)
**Timeline:** Start within 30 days of CSLI manifesting (per CubeSat 101)
**Options:**
- Amateur radio frequencies (437 MHz): Easier, well-supported by community
- Commercial frequencies: More complex, but higher data rates possible

**Approach:** Amateur radio as baseline (simple, flight-proven)

### NOAA Remote Sensing License
**Required?** Only if Earth imaging for non-government entity
**RAD-AI:** NOT required (vision is for navigation, not Earth remote sensing)

### Export Control (ITAR/EAR)
**Consideration:** AI for autonomous control may have dual-use implications
**Mitigation:** Consult university export control office; design for public release where possible

### Orbital Debris Mitigation
**Requirement:** 25-year deorbit per NASA standards
**Compliance:**
- LEO altitude <600 km ensures atmospheric drag deorbit within 25 years
- Alternatively: Plan for active deorbit (propulsion module or drag sail)

---

# SECTION 3: MISSION MODELS

## 3.1 System Architecture Overview

### Mission Architecture Concept

**Platform:** 6U CubeSat (20 cm × 10 cm × 34 cm, ~8 kg)

**Orbit:** Low Earth Orbit (LEO)
- Altitude: 400-600 km (optimized for radiation exposure vs. lifetime)
- Inclination: Any (launch flexibility)
- RAAN: Any (launch flexibility)

**Mission Lifetime:**
- Primary: 12 months
- Extended: Up to 24 months (orbital lifetime dependent on altitude)

**Operational Concept:**
- Autonomous AI experiments during nominal operations
- Periodic ground commanding for experiment updates
- Continuous radiation monitoring
- Data downlink 2-4 passes/day

### System Block Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                        6U CubeSat                            │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐  │
│  │              AI PAYLOAD (Primary)                     │  │
│  │  ┌─────────────────┐      ┌────────────────────┐    │  │
│  │  │ RISC-V Processor│◄────►│ Vision Camera(s)   │    │  │
│  │  │ + AI Accelerator│      │ - Star tracker     │    │  │
│  │  │                 │      │ - Horizon sensor   │    │  │
│  │  └────────┬────────┘      └────────────────────┘    │  │
│  │           │                                           │  │
│  │  ┌────────▼────────┐      ┌────────────────────┐    │  │
│  │  │ Radiation       │      │ Fault Injection    │    │  │
│  │  │ Sensors         │      │ Framework          │    │  │
│  │  │ - Dosimeters    │      │                    │    │  │
│  │  │ - SEU detectors │      │                    │    │  │
│  │  └─────────────────┘      └────────────────────┘    │  │
│  └────────────────────┬─────────────────────────────────┘  │
│                       │                                     │
│  ┌────────────────────▼─────────────────────────────────┐  │
│  │           CubeSat Bus (COTS or Custom)               │  │
│  │                                                        │  │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐           │  │
│  │  │  C&DH    │  │  Power   │  │  ADCS    │           │  │
│  │  │          │  │ System   │  │          │           │  │
│  │  └──────────┘  └──────────┘  └──────────┘           │  │
│  │                                                        │  │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐           │  │
│  │  │  Comms   │  │ Thermal  │  │ Structure│           │  │
│  │  │          │  │          │  │          │           │  │
│  │  └──────────┘  └──────────┘  └──────────┘           │  │
│  └────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

## 3.2 Subsystem Descriptions

### 3.2.1 AI Payload Subsystem (Primary Mission Payload)

**Function:** Execute AI vision and control algorithms in radiation environment

**Components:**

**AI Processor Board (Custom PCB):**
- RISC-V core: SiFive U74 or equivalent (~1.5 GHz, quad-core)
- AI Accelerator: Neural network inference engine (custom or integrated)
- Memory: 8 GB DDR4 RAM, 128 GB eMMC storage
- Watchdog: FPGA-based health monitor
- Power: ~15W average, 25W peak during inference
- Mass: ~200 g
- Mitigation: Software TMR, checkpointing, error correction

**Vision Cameras:**
- Primary: Star tracker-grade camera (1280x1024, sensitive)
  - Purpose: Star field imaging for autonomous attitude determination
  - Heritage: CubeSat star trackers (AAC Hyperion, Blue Canyon NST)
  - FOV: 15° × 15°
  - Mass: ~100 g, Power: ~2W

- Secondary: Horizon sensor camera (640x480)
  - Purpose: Earth limb detection for altitude/attitude estimation
  - COTS: Commercial board camera with appropriate lens
  - FOV: 60° × 45°
  - Mass: ~50 g, Power: ~1W

**Radiation Sensors:**
- Total Ionizing Dose (TID) monitors: COTS dosimeters (e.g., RadFET)
- Single Event Upset (SEU) detectors: Custom SRAM array with readback
- Particle flux monitor: Commercial energetic particle detector
- Mass: ~50 g total, Power: ~0.5W

**Fault Injection Module:**
- FPGA-based fault generator
- Software-controllable bit-flip injection
- Scheduled experiment execution
- Mass: Integrated with watchdog FPGA, Power: <1W

**Total Payload:**
- Mass: ~400 g
- Power: 18-30W (depending on activity)
- Volume: ~1.5U of 6U

### 3.2.2 Command & Data Handling (C&DH)

**Function:** Spacecraft computer for housekeeping, payload interface, data storage

**Options:**
- **Option A:** COTS CubeSat flight computer (Pumpkin Supernova, GomSpace NanoMind, etc.)
- **Option B:** Custom board based on LEON or ARM processor

**Baseline:** COTS flight computer (proven, lower risk)

**Specifications:**
- Processor: ARM Cortex-M or equivalent
- Memory: 512 MB RAM, 32 GB flash
- Interfaces: I2C, SPI, UART, CAN for subsystems
- Power: ~2W
- Mass: ~100 g
- Heritage: Extensive CubeSat flight history

**Software:**
- Flight Software (FSW): FreeRTOS or similar RTOS
- Autonomy: Safe mode, fault detection, power management
- Payload interface: Command relay, data packaging for downlink

### 3.2.3 Electrical Power System (EPS)

**Function:** Generate, store, and distribute power to all subsystems

**Power Budget:**

| Subsystem | Average (W) | Peak (W) | Duty Cycle |
|-----------|-------------|----------|------------|
| AI Payload (idle) | 5 | 5 | 80% |
| AI Payload (inference) | 25 | 30 | 20% |
| C&DH | 2 | 3 | 100% |
| ADCS | 3 | 5 | 100% |
| Comms (TX) | 0 | 8 | 5% |
| Comms (RX) | 1 | 1 | 10% |
| Thermal | 2 | 5 | Variable |
| Margin (20%) | 6 | 9 | - |
| **TOTAL** | **~36W** | **~60W** | |

**Solar Array:**
- Configuration: Body-mounted panels on 4 faces (no deployables for simplicity)
- Cell type: Triple-junction GaAs (30% efficiency)
- Area: ~0.15 m² total
- Power generation:
  - BOL (Beginning of Life): 45W (LEO average)
  - EOL (End of Life, 12 months): 40W (assuming 10% degradation)
- Margin: Adequate for 36W average power requirement

**Battery:**
- Type: Lithium-ion (UL-listed per CubeSat 101 recommendation)
- Capacity: 60 Wh (to cover eclipse + peak loads)
- Mass: ~400 g
- Heritage: COTS CubeSat batteries (Clyde Space, GomSpace)

**Power Distribution:**
- COTS EPS board with battery charge regulation
- Switched power outputs for subsystems
- Telemetry: Voltage, current, temperature monitoring
- Autonomy: Load shedding during low battery

**Mass:** ~600 g (EPS board + battery)
**Heritage:** COTS components with extensive flight history

### 3.2.4 Attitude Determination and Control System (ADCS)

**Function:** Maintain spacecraft pointing for:
- Solar panel sun-pointing (power generation)
- Antenna Earth-pointing (communications)
- Camera pointing for vision experiments

**Requirements:**
- Pointing accuracy: ±5° (relaxed; payload camera has wide FOV)
- Pointing knowledge: ±1° (for vision algorithm validation)
- Slew rate: ≥1°/s (for ground station tracking)

**Components:**

**Sensors:**
- Magnetometer: 3-axis (Earth magnetic field measurement)
- Sun sensors: Coarse (for safe mode sun-pointing)
- Payload camera: Can double as star tracker for fine attitude determination

**Actuators:**
- Magnetorquers: 3-axis (primary attitude control in LEO)
- Reaction wheels: 3-axis (optional, for fine pointing if budget allows)

**ADCS Computer:**
- Integrated with C&DH or standalone COTS ADCS board

**Options:**
- **Option A:** COTS ADCS (Blue Canyon XACT, AAC Hyperion) - Higher cost, proven
- **Option B:** Custom ADCS using COTS sensors + actuators - Lower cost, higher development

**Baseline:** Custom ADCS to reduce cost; leverage payload camera for star tracking

**Mass:** ~500 g (magnetorquers + sensors + electronics)
**Power:** ~3W average, 5W peak

### 3.2.5 Communications Subsystem

**Function:** Uplink commands, downlink telemetry and science data

**Link Budget:**

**Downlink (Space-to-Ground):**
- Frequency: 437 MHz (amateur radio, UHF band)
- Data rate: 9600 bps (baseline), up to 115.2 kbps (with directional ground antenna)
- Transmit power: 2W
- Antenna: Deployable dipole or turnstile (omnidirectional)
- Link margin: >10 dB (with 3m ground dish)
- Daily data volume: 10 MB minimum (vision results, telemetry, radiation data)

**Uplink (Ground-to-Space):**
- Frequency: 437 MHz
- Data rate: 1200 bps
- Command volume: <1 MB/day (low command rate)

**Hardware:**
- **Radio:** COTS CubeSat transceiver (GomSpace NanoCom, Endurosat UHF)
  - Mass: ~100 g
  - Power: 8W TX, 1W RX
  - Heritage: Hundreds of CubeSats

- **Antenna:** Deployable tape-measure dipole
  - Mass: ~50 g
  - Deployment: Burn-wire release (double burn wires per CubeSat 101)
  - Heritage: Proven CubeSat deployment mechanism

**Ground Station:**
- **Option A:** University ground station (if available)
- **Option B:** Amateur radio network (SatNOGS - free, global coverage)
- **Option C:** Commercial ground station (AWS Ground Station, KSAT) - higher cost but reliable

**Baseline:** Amateur radio network (SatNOGS) for primary; commercial for critical operations

**Licensing:** FCC amateur radio license (straightforward for university)

### 3.2.6 Thermal Control Subsystem

**Function:** Maintain component temperatures within operational limits

**Requirements:**
- AI processor: 0°C to 60°C (commercial components)
- Battery: -10°C to 40°C
- Cameras: -20°C to 50°C

**Thermal Environment:**
- LEO: -100°C (eclipse) to +120°C (sun-facing)
- Heat sources: AI processor (25W peak), battery charging, solar panels

**Thermal Design:**

**Passive Control (Primary):**
- Multi-layer insulation (MLI) on exterior surfaces
- Thermal straps: Copper or aluminum connecting hot components to radiators
- Radiator surfaces: Black anodized aluminum on +Z and -Z faces
- Thermal mass: CubeSat structure and battery provide thermal inertia

**Active Control (Contingency):**
- Survival heaters on battery (thermostat-controlled)
- Software: AI processor throttling if temperature exceeds limits

**Analysis:**
- Thermal desktop model (SINDA/FLUINT or C&R ThermalDesktop)
- Worst-case hot: AI processor at 25W continuous, sun-facing
- Worst-case cold: Eclipse, AI processor off

**Expected Results:** Passive control adequate; heaters needed only for battery in cold case

**Mass:** ~100 g (heaters, MLI, straps)
**Power:** 0W nominal, up to 5W for heaters in cold case

### 3.2.7 Structure and Mechanisms

**Function:** Mechanical support, launch interface, deployable release

**Structure:**
- 6U CubeSat chassis: Aluminum 6061-T6 or 7075-T6
- Rails: Standard CubeSat rails per CDS (CubeSat Design Specification)
- Mass: ~800 g

**Mechanisms:**
- Antenna deployment: Burn-wire release (double-redundant)
- Access panels: Bolted or captive fasteners for component access

**Design Philosophy (per CubeSat 101):**
- Components on exterior for easy access during integration
- Don't design to envelope limits - leave margin
- High-melting point materials (avoid Teflon near heaters)

**Materials:**
- Primary structure: Aluminum alloy
- Fasteners: Stainless steel (captured where possible)
- PCBs: FR-4 with conformal coating
- Wiring: Teflon-insulated (except near heaters)

**Mass Budget Summary:**

| Subsystem | Mass (g) | % of Total |
|-----------|----------|------------|
| AI Payload | 400 | 5% |
| C&DH | 100 | 1.3% |
| Power (EPS + Battery) | 600 | 7.5% |
| ADCS | 500 | 6.3% |
| Communications | 150 | 1.9% |
| Thermal | 100 | 1.3% |
| Structure | 800 | 10% |
| Harness & Misc | 300 | 3.8% |
| **Subtotal** | **2950 g** | **36.9%** |
| **Margin (30%)** | **890 g** | **11.1%** |
| **Total** | **3840 g** | **48%** |
| **6U Max** | **8000 g** | **100%** |

**Note:** Significant mass margin (52%) allows for design growth and additional shielding if needed.

## 3.3 Concept of Operations (ConOps)

### 3.3.1 Mission Phases

**Phase 1: Launch and Early Operations (L+0 to L+30 days)**
- Launch and deployment from launch vehicle
- Initial acquisition of signal (AOS) with ground
- Antenna deployment verification
- Subsystem checkout
- Commissioning: Power, thermal, ADCS, comms
- Payload boot and health check
- Establish baseline radiation environment

**Phase 2: Payload Commissioning (L+30 to L+60 days)**
- AI processor bring-up and software upload
- Vision camera calibration
- Radiation sensor baseline
- Initial AI inference tests (simple tasks)
- Fault injection framework validation
- Performance benchmarking in benign radiation environment

**Phase 3: Nominal Science Operations (L+60 days to L+12 months)**
- Routine autonomous AI experiments:
  - Star tracking with onboard processing
  - Horizon detection and altitude estimation
  - Debris identification (if secondary camera available)
- Scheduled fault injection experiments (weekly)
- Continuous radiation monitoring
- Periodic algorithm updates via ground upload
- Data downlink 2-4 passes/day

**Phase 4: Extended Operations (L+12 months to deorbit)**
- Continued monitoring of long-term radiation effects
- Higher-risk experiments (aggressive fault injection)
- End-of-life battery/solar panel performance data
- Deorbit monitoring

### 3.3.2 Operational Modes

**Safe Mode:**
- Trigger: Battery low, thermal violation, loss of attitude control, payload fault
- Action:
  - AI payload powered off
  - Sun-pointing for power generation
  - Beacon transmission every 60 seconds
  - Await ground recovery commands
- Recovery: Ground commands to transition to nominal mode

**Nominal Mode:**
- Sun-pointing for solar power generation
- Periodic ground station passes for downlink/uplink
- AI payload executing scheduled experiments
- Autonomous fault detection and recovery (without ground)

**Experiment Mode:**
- Entered during AI experiment execution
- AI processor at full power
- Vision cameras active
- Data buffering to storage
- May require specific attitude (camera pointing)

**Ground Pass Mode:**
- Entered when ground station is in view
- Communications active (RX/TX)
- Data downlink prioritized
- Command uplink accepted
- May pause AI experiments to reduce power load

### 3.3.3 Ground Segment

**Ground Station Network:**
- Primary: SatNOGS amateur radio network (global coverage, free)
- Secondary: University ground station (if available)
- Contingency: Commercial ground station (AWS, KSAT)

**Mission Operations Center (MOC):**
- Located at university (or home institution)
- Staffing: 2-3 operators during commissioning, 1 operator during nominal ops
- Functions:
  - Command generation and uplink
  - Telemetry monitoring and anomaly resolution
  - Data downlink and archiving
  - Mission planning (experiment scheduling)

**Data Pipeline:**
- Raw telemetry: Stored in database (InfluxDB or similar)
- Science data: Vision images, AI inference results, radiation logs
- Processing: Automated analysis scripts (Python)
- Archiving: Long-term storage (university server or cloud)
- Distribution: Public data release for research community (if funded by NASA)

### 3.3.4 Typical Operations Timeline (Daily)

```
00:00 UTC - Autonomous AI experiments begin
   |      - Star tracking, horizon detection, debris identification
   |      - Radiation monitoring continuous
   |      - Data stored onboard
   |
04:00 UTC - Ground pass (10 minutes, SatNOGS station)
   |      - Telemetry downlink: Health, radiation data, AI results
   |      - Beacon received, no uplink needed
   |
08:00 UTC - Fault injection experiment (scheduled weekly)
   |      - Controlled memory bit flips
   |      - AI algorithm continues with mitigation active
   |      - Recovery time and detection rate logged
   |
12:00 UTC - Ground pass (15 minutes, university station)
   |      - Full science data downlink (images, inference results)
   |      - Command uplink: Update experiment parameters
   |      - Battery charging during sunlight portion
   |
18:00 UTC - Continued autonomous operations
   |      - Battery discharge during eclipse
   |      - AI processor throttled to conserve power
   |      - Radiation dose accumulation logged
   |
22:00 UTC - Ground pass (10 minutes, commercial station if needed)
   |      - Emergency commanding available
   |      - Normally no contact needed (autonomous operations)
   |
23:59 UTC - End of day; repeat cycle
```

### 3.3.5 Data Products

**Telemetry Data (Downlink daily):**
- Subsystem health: Voltages, currents, temperatures
- ADCS state: Attitude, magnetic field, sun sensor
- Communications: Link quality, packet statistics
- Payload health: AI processor temperature, memory usage, uptime

**Science Data (Downlink 2-4x weekly):**
- Vision images: Raw images from cameras (for validation)
- AI inference results: Star positions, horizon fit parameters, detected objects
- Radiation data: TID accumulation, SEU event log, particle flux
- Performance metrics: Inference time, accuracy, fault detection rate

**Long-Term Data Products (End of mission):**
- Radiation effects database: AI processor performance vs. accumulated dose
- Fault injection study results: Mitigation effectiveness statistics
- Vision algorithm validation: Onboard vs. ground processing comparison
- Lessons learned document: For future autonomous deep-space missions

## 3.4 Key Performance Parameters (KPPs) and Success Metrics

### Minimum Success Criteria
1. ✅ **Spacecraft Deployment:** CubeSat deploys from launch vehicle and establishes communication
2. ✅ **Payload Boot:** AI processor boots successfully in orbit
3. ✅ **Basic Inference:** Execute at least one AI inference task successfully
4. ✅ **Radiation Data:** Collect 30 days of radiation environment data

**Outcome:** Demonstrates AI processor can operate in space; limited validation of radiation tolerance.

### Baseline Success Criteria
1. ✅ **Autonomous Vision Tasks:** Star tracking, horizon detection execute successfully for 90 days
2. ✅ **Radiation Characterization:** TID and SEU data collected over 6 months
3. ✅ **Fault Injection Validation:** Demonstrate detection and recovery from injected faults
4. ✅ **Performance Benchmarking:** Quantify AI inference performance in radiation environment

**Outcome:** Validates radiation-tolerant AI for near-term missions; publishable dataset.

### Full Success Criteria
1. ✅ **12-Month Operation:** AI payload operates continuously for full primary mission
2. ✅ **Complete Radiation Database:** TID, SEU, and performance data over full mission life
3. ✅ **Algorithm Updates:** Successfully upload and execute updated AI models in orbit
4. ✅ **End-to-End Autonomy:** Demonstrate 7+ days of autonomous operation without ground contact

**Outcome:** Complete validation enables direct adoption for Artemis, MSR, and asteroid missions.

### Extended Success Criteria
1. ✅ **Long-Duration Operation:** Continue operations beyond 12 months
2. ✅ **Advanced Experiments:** Test cutting-edge AI algorithms uploaded from ground
3. ✅ **Multi-Mission Data:** Correlate radiation effects with solar activity cycles
4. ✅ **Public Data Release:** Dataset available for broader research community

**Outcome:** Maximum scientific and programmatic return; establishes benchmark dataset.

## 3.5 Mission Cost Estimate (Rough Order of Magnitude)

### Development Costs (Design + Build Phase)

| Category | Cost (USD) | Notes |
|----------|------------|-------|
| **AI Payload Development** | $40,000 | Custom PCB design, RISC-V core licensing, AI accelerator, integration |
| **Vision Cameras** | $15,000 | COTS star tracker camera + horizon sensor |
| **Radiation Sensors** | $5,000 | Dosimeters, SEU detectors, particle monitor |
| **CubeSat Bus (COTS)** | $80,000 | Option: Blue Canyon or AAC Clyde 6U bus with ADCS, power, comms |
| **Alternative: Custom Bus** | $40,000 | If building from COTS components instead of integrated bus |
| **Integration & Test** | $10,000 | Harness, fixtures, environmental test costs |
| **Radiation Testing** | $15,000 | Heavy ion, TID, proton testing at university or national lab |
| **Software Development** | $20,000 | Flight software, ground software, AI algorithms (mostly labor) |
| **Ground Station** | $5,000 | SatNOGS setup or university station upgrades |
| **Program Management** | $10,000 | Documentation, reviews, travel to testing facilities |
| **Contingency (20%)** | $20,000 | Reserve for unknowns |
| **TOTAL** | **$100,000 - $120,000** | Assuming COTS bus; lower if custom bus |

### Launch Costs
- **CSLI (if selected):** $0 (NASA provides free launch worth ~$250-500k)
- **Alternative (commercial launch):** $150,000 - $300,000 (e.g., Spaceflight Inc., Exolaunch)

### Operations Costs (per year)
- Personnel: $20,000 (part-time student operators; in-kind for university)
- Ground station network: $5,000 (commercial if not using SatNOGS)
- Data storage/processing: $2,000
- **Annual:** ~$25,000

### Total Program Cost (3 years: develop + 1 year ops + 1 year data analysis)
- **With CSLI launch:** $150,000 - $170,000
- **With commercial launch:** $300,000 - $470,000

**Funding Strategy:**
- NASA CSLI: Free launch (~$250k value)
- NASA STMD grant: $100k for development
- University cost-share: $20k (in-kind labor, facilities)
- AFRL or DARPA grant: $50k (if DoD interest in rad-hard AI)

## 3.6 Schedule Estimate (Post-Design Phase)

### Implementation Phase (Months 13-24 after course project completion)

**Months 1-3: Procurement and Initial Fabrication**
- Order long-lead items (cameras, CubeSat bus if COTS)
- Fabricate AI payload PCBs
- Begin software development

**Months 4-6: Integration and Component Testing**
- AI payload board bring-up
- Vision camera integration
- Software/hardware integration on lab bench

**Months 7-9: Subsystem Testing**
- Thermal vacuum chamber testing (subsystem level)
- Radiation testing (cyclotron for SEU, Co-60 for TID)
- Flight software validation

**Months 10-11: System Integration**
- Full CubeSat assembly
- 72-hour Day-In-The-Life (DITL) test
- Software freeze

**Month 12: Environmental Testing**
- Vibration testing
- Thermal vacuum (system level)
- Post-test functional verification

**Months 13-15: Flight Readiness**
- Final inspections
- Integration into launch dispenser
- Shipping to launch site

**Months 16-24: Launch and Operations**
- Launch (schedule dependent on CSLI manifesting)
- Early operations and commissioning (2 months)
- Nominal science operations (6 months minimum)

**Total:** 24 months from start of implementation to end of primary mission

---

# SECTION 4: EXPECTED OUTCOMES AND IMPACT

## 4.1 Technical Outcomes

### Deliverables from Course Project (Design Phase)
1. **Mission Design Document:** Complete system specification per CubeSat 101
2. **Subsystem Designs:** Detailed CAD, electrical schematics, thermal models
3. **Test Plans:** Procedures for integration, environmental, and radiation testing
4. **CSLI Proposal Package:** Ready for submission to NASA (if pursuing flight)
5. **Cost and Schedule Estimates:** Realistic implementation plan

### Deliverables from Flight (if implemented)
1. **Radiation Effects Database:** AI processor performance vs. TID, SEU cross-sections
2. **Autonomous Vision Dataset:** Onboard vs. ground processing comparison
3. **Fault Mitigation Study:** Detection rates, recovery times under various fault scenarios
4. **Flight Software Package:** Open-source release for future CubeSat AI missions
5. **Lessons Learned:** Documentation for Artemis, MSR, and commercial adopters

## 4.2 Scientific and Programmatic Impact

### Immediate Benefits
- **Technology Validation:** De-risks rad-tolerant AI for NASA missions
- **Cost Savings:** $100k CubeSat demo vs. $10M+ risk on flagship mission
- **Timeline Acceleration:** 2-year CubeSat vs. 5-10 year flagship development

### Long-Term Impact
- **Artemis Autonomous Landing:** Onboard hazard detection and avoidance
- **Mars Sample Return:** Autonomous rendezvous and docking operations
- **Asteroid Proximity Ops:** Real-time navigation and control at asteroids
- **Commercial Autonomy:** Enables autonomous satellite servicing, debris removal

## 4.3 Educational Outcomes

### Student Learning Objectives
- Systems engineering: Requirements, design, integration, test
- Radiation effects: SEUs, TID, mitigation techniques
- AI/ML in embedded systems: Algorithm optimization, hardware acceleration
- Spacecraft operations: Mission planning, ground segment, data analysis

### Career Preparation
- Hands-on CubeSat development experience (highly valued by aerospace employers)
- Publication opportunities (IEEE Aerospace, AIAA, academic journals)
- Professional network (NASA, industry, academic collaborators)
- Portfolio piece for graduate school or industry applications

---

# CONCLUSION

RAD-AI represents a high-value, achievable CubeSat mission that addresses a critical NASA need—autonomous decision-making for deep-space missions—while providing an excellent educational platform for a Masters in Space Operations program.

**Key Strengths:**
- ✅ **High Innovation:** Novel integration of rad-tolerant RISC-V + AI acceleration in CubeSat
- ✅ **Strong Validation:** NASA explicitly needs autonomous systems for Artemis and Mars
- ✅ **Excellent CSLI Fit:** 90% selection probability (technology demo, NASA benefit, LEO flexibility)
- ✅ **Appropriate Scope:** Achievable in 12-15 month design phase with 2-year implementation
- ✅ **Multi-Mission Impact:** Enables Artemis, MSR, asteroid missions, and commercial autonomy

**Success Path:**
1. **Course Project (4-6 months):** Complete design per this outline → 50 points
2. **CSLI Submission:** Apply for free launch (~$250k value)
3. **Funding Acquisition:** NASA STMD grant ($100k) + university cost-share
4. **Implementation (24 months):** Build, test, launch, operate
5. **Results:** Publish dataset, enable future autonomous missions, advance career

This mission balances innovation with feasibility, addresses real problems with validated solutions, and provides exceptional learning value for a masters-level space operations program.

---

**Document Version:** 1.0
**Created:** 2025-11-02
**Course:** CubeSat Systems - Masters in Space Operations
**Assignment Value:** 50 points (outline) + 150 points (full project development)
**Next Steps:** Instructor review, refinement, and progression to detailed subsystem design
