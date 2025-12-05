# NASA CubeSat 101: Chapters 1-3 Summary & Cheatsheet
**Comprehensive Reference Guide for First-Time CubeSat Developers**

---

## Table of Contents
- [Chapter 1: Introduction](#chapter-1-introduction)
- [Chapter 2: Development Process Overview](#chapter-2-development-process-overview)
- [Chapter 3: Mission Models](#chapter-3-mission-models)
- [Key Terms Glossary](#key-terms-glossary)
- [Quick Reference Tables](#quick-reference-tables)

---

# CHAPTER 1: INTRODUCTION

## 1.1 What is a CubeSat?

### Definition & Standards
A **CubeSat** is a standardized small satellite that must conform to specific criteria for shape, size, and weight:

- **1U (Unit)**: 10 cm × 10 cm × 10 cm cube, mass ~1-1.33 kg
- **Common sizes**: 1.5U, 2U, 3U, 6U, 12U

### Why Standardization Matters
- Enables mass-produced, off-the-shelf components
- Reduces engineering and development costs
- Simplifies transportation and deployment
- Makes space more accessible to universities, schools, and small organizations

### Key Document: CubeSat Design Specification (CDS)
- Available at: http://www.cubesat.org
- Contains general requirements for all CubeSats
- **NOT** the official requirements for your specific launch
- Essential for preliminary design planning

---

## 1.2 CubeSat Dispenser Systems

### What is a Dispenser?
The **dispenser** is the interface between the CubeSat and the launch vehicle (LV). It provides:
- Attachment to the launch vehicle
- Protection during launch
- Controlled release into space at the appropriate time

### 1.2.1 3U Dispensers

**Poly-Picosatellite Orbital Deployer (P-POD)**
- First CubeSat dispenser (developed by Cal Poly)
- Holds up to 3U of payload (any combination: three 1Us, two 1.5Us, one 3U, etc.)
- Bolts directly onto launch vehicle
- Door opens via electrical signal from LV

**Key Features**:
- Safe container with door mechanism
- Launch vehicle sends deployment signal
- Multiple vendors now available

### 1.2.2 6U Dispensers

**Introduced**: 2014
**Form Factor**: Two 3Us side-by-side (twice as wide)
**Flexibility**: Can accommodate any configuration (one 6U, six 1Us, two 3Us, etc.)

### Important Note
⚠️ You typically won't choose your dispenser—whoever pays for the launch does. However, understanding dispenser types is critical for design planning.

---

## 1.3 Launch Vehicles (LVs) - aka: Rockets

### How CubeSats Get to Space

**Primary Method**: Dispenser bolted to rocket where space is available

**Alternative Methods**:
1. **ISS Deployment**: Sent with cargo resupply missions, deployed from Space Station
2. **Manual Release**: Extremely uncommon (e.g., Peruvian Chasqui 1 hand-tossed by cosmonaut)

### U.S. Launch Vehicles Used for CubeSats
- Super Strypi
- Minotaur I & IV
- Taurus XL
- Delta II
- Antares
- Falcon 9 & Falcon 9 Heavy*
- Atlas V
- Electron*
- LauncherOne*
- Space Launch System (SLS)*

*As of 2017, these had not yet flown CubeSats but had them manifested

---

## 1.4 NASA CubeSat Launch Initiative (CSLI)

### What is CSLI?
NASA initiative providing **free launch opportunities** for qualified CubeSats as:
- Auxiliary payloads on launches with excess capacity
- Deployments from the International Space Station (ISS)

### What NASA Provides
- Launch services (up to $300,000 value, typically enough for 3U to LEO)
- Integration services
- Dispenser

### What YOU Must Provide
⚠️ **CRITICAL**: CubeSat developers are responsible for ALL development and operational costs:
- Materials and labor to build the CubeSat
- Testing expenses
- Ground station development and operations
- Travel costs for required meetings and delivery

### Eligibility Requirements
Your CubeSat **investigation** must:
- Clearly benefit NASA
- Support at least one goal/objective in NASA Strategic Plan
- Available at: http://www.nasa.gov

### Application Process
- **When**: Annual solicitation, typically early August
- **Where**: Announcement of Partnership Opportunity (AoPO) on https://sam.gov
- **Deadline**: Typically November of the same year

### CSLI Mission Areas
**Science** (~50% of missions):
- Space Weather
- Earth Science
- Biological science
- Near Earth objects
- Climate change
- Orbital debris
- Planetary science
- Space-based astronomy
- Heliophysics

**Technology Development** (~66% of missions):
- Communications
- Propulsion
- Navigation and control
- Radiation testing
- Solar sails
- Additive manufacturing
- Femtosatellites

---

# CHAPTER 2: DEVELOPMENT PROCESS OVERVIEW

## Complete Timeline: Concept to Operations

### Project Duration
- **Minimum**: 9 months (design, build, test, deliver)
- **Typical**: 18-24 months
- **After delivery**: 4 weeks to 6 months until launch
- **Post-launch**: Mission operations variable, up to 20 years

---

## 2.1 Concept Development (1-6 months)

### Key Questions
1. What do you want your CubeSat to do?
2. Does it align with NASA's interests?
3. Is funding available?
4. Are there potential partners?

### Keys to CSLI Selection ⭐
- ✓ Adequate funding
- ✓ Great merit and feasibility reviews
- ✓ Clear demonstration of benefit to NASA
- ✓ **FLEXIBILITY IS KEY**: Keep orbital requirements and launch dates as flexible as possible

### Strategic Partnering
Consider collaborating with other organizations to:
- Combine resources
- Share expertise
- Increase funding opportunities
- Formalized through agreements

---

## 2.2 Securing Funding (1-12 months)

### Critical Warning ⚠️
- NASA only covers **launch costs** (up to $300,000)
- If you run out of funds and can't complete your CubeSat:
  - Launch opportunity lost
  - May demanifest other co-manifested CubeSats
  - Could be required to reimburse NASA for integration/launch costs

### Funding Sources

**Government Agencies**:
- National Science Foundation
- NASA Earth Science Technology Office (ESTO)
- NASA Space Grant Consortium (every state has one)

**Educational Institutions**:
- Faculty and administrators
- University funding for prestige projects

**Other Options**:
- Technology demonstration sponsors
- Crowdfunding (supplementary funding)
- Request for Proposals (RFPs) from various organizations

### Cost Components
**Major Expenses**:
- Materials
- Labor
- Environmental testing (vibration, thermal vacuum, shock, EMI/EMC)
- Ground station development
- Travel (for reviews, integration, delivery)
- **Budget tip**: Include at least 10% reserve for unexpected events

### Technology Demonstration Missions
- Government/commercial organizations fund CubeSats to test new tech
- Lowers risk for expensive primary missions
- Excellent option for newer organizations/universities

---

## 2.3 Merit and Feasibility Reviews (1-2 months)

### Purpose
Assure mission stakeholders that your team can:
- Fulfill obligations
- Complete a successful mission
- Deliver on time and on budget

### Merit Review
**Assesses**:
- Quality of investigation (science/education/technology)
- Alignment with NASA Strategic Plan goals
- Why flight opportunity is required

**Reviewers**: Experts with knowledge/experience in your focus area

### Feasibility Review
**Assesses**:
- Technical implementation feasibility
- Resiliency and risk
- Probability of success
- Team's ability to deliver on time/budget

**Reviewers**: Ideally space flight/spacecraft experts, or hardware/project development specialists

### Important Notes
- ⚠️ Reviewers must NOT be on project team
- Not just "checking a box"—seek honest, valuable feedback
- CSLI interested in how you addressed reviewer findings

---

## 2.4 CubeSat Design (1-6 months)

### Research Phase
- Learn from others' mistakes and successes
- Attend CubeSat conferences
- Review published materials online
- Network with experienced developers

### Component Selection
**Commercial Off-The-Shelf (COTS)**:
- Increasingly available
- List of vendors at http://www.cubesat.org (Developer Resources page)

**In-House Development**:
- Keeps costs low
- Enhances educational experience
- Requires more time and expertise

### Design Best Practices ⭐

**1. KEEP IT SIMPLE**
- CDS requirements are conservative
- Prohibits pyrotechnics
- Discourage complex systems (e.g., propulsion)
- Complex features may limit launch opportunities

**2. IMPORTANT COMPONENTS ON EXTERIOR**
- Easier access for repairs
- May avoid re-testing after fixes
- Components inside structure = disassembly = likely re-test

**3. DO NOT DESIGN TO LIMITS**
- Stay within CDS envelope (length/height/width)
- If it doesn't fit, it doesn't fly
- Target optimal dimensions, not maximum
- Watch protrusions (CDS allows up to 6.5mm)

**4. DOUBLE UP ON BURN WIRE**
- Used to constrain deployable components (solar panels, antennas)
- Fishing line around resistor, melts when current applied
- Risk: line can come loose during vibration/ascent
- Solution: Use TWO separate burn wires

**5. USE FAMILIAR COMPONENTS**
- Choose components with flight heritage
- Major components: batteries, antennas, ADCS
- Reduces risk and increases launch provider confidence

**6. USE UL LISTED BATTERIES**
- UL, LLC certification = industry-recognized reliability
- Non-UL batteries require extensive additional testing
- Tampering with UL batteries voids certification

**7. USE HIGH-MELTING POINT MATERIALS**
- Critical for safety and debris mitigation

---

## 2.5 Development & Submittal of Proposal (3-4 months)

### Timing
- **AoPO Posted**: Early August
- **Proposals Due**: November
- **Instructions**: Detailed in AoPO at https://sam.gov or http://go.nasa.gov/CubeSat_initiative

### Critical Requirements ⚠️
- Follow AoPO instructions exactly
- Include ALL requested information
- **Non-compliance = removal from consideration**
- Must resubmit to future AoPO if rejected

### Focus Areas
Select one or more:
- Science
- Technology investigation
- Education

**Important**: If multiple focus areas selected, proposal must address goals/objectives for EACH equally

### CRADA (Cooperative Research And Development Agreement)
- Contract between NASA and developer after selection
- Contains legal terms (liability, risk, data-sharing)
- **Strongly advised**: Have legal expert review
- Universities: Use university legal department

---

## 2.6 Selection and Manifesting (1-36 months)

### Selection Process
1. CSLI Selection Recommendation Committee reviews proposals
2. Creates prioritized list of qualifying projects
3. Prioritized list released ~12-16 weeks after proposal deadline

### How to Rank High
- Excellent merit and feasibility reviews
- Hit all "Keys to CSLI Selection" points
- Clear contribution to NASA Strategic Plan goals
- Interesting and/or groundbreaking proposal

### Manifesting
**Priority ≠ Next Launch**
- Must be matched with compatible launch
- Higher priority = first dibs on matching launches
- NASA LSP pairs CubeSats with best-suited launches
- Considers: orbit, completion dates, special constraints
- ELaNa mission number assigned when manifested

---

## 2.7 Mission Coordination (9-18 months)

### What is Mission Coordination?
Overall mission planning and documentation tracking between:
- CubeSat developers
- Launch vehicle provider
- Mission integrator (manages coordination)

### Mission Integrator Responsibilities
- Managing integration schedules
- Tracking deliverable documentation
- Requirement verification management
- Creating mission-specific ICD (Interface Control Document)
- Providing document templates
- Organizing regular teleconferences

### Your Responsibilities
- Attend kickoff meeting (teleconference)
- Follow hardware/document deliverable schedule
- Show CubeSat meets all ICD requirements
- Regular status updates via telecons
- Work with integrator on requirement verification

### Interface Control Document (ICD)
**The Official Rulebook**:
- Derived from CDS and LV-specific needs
- Specifies environmental testing levels and durations
- Must meet EVERY requirement in ICD

---

## 2.8 Regulatory Licensing (4-6 months)

### Critical Timeline ⚠️
- **Start application**: Within 30 days of manifesting (or earlier)
- **Must have licenses**: Before final delivery date
- **No license = Demanifest from mission**

### Radio Frequency (RF) License

**Who Regulates**:
- **NTIA** (National Telecommunications and Information Administration): U.S. Government-operated satellites
- **FCC** (Federal Communications Commission): All other non-Federal Government satellites

**Why Needed**: Federal law requires license for RF transmission

### Remote Sensing License

**Who Regulates**: NOAA (National Oceanic and Atmospheric Administration)

**When Needed**: Non-Government owned U.S. CubeSat with imager/camera

**Important**: FCC needs NOAA license before finishing RF license processing

### Licensing Horror Story ⚠️
**Real incident**:
- CubeSat integrated into dispenser and onto LV
- No approved FCC RF license
- Days before launch, still not approved
- Integrator planned to disable release mechanism
- License came through just in time
- **Otherwise: Mission scrubbed AND CubeSat lost**

---

## 2.9 Flight-Specific Documentation (10-12 months)

### Purpose
Verify CubeSat meets all safety and launch requirements in ICD

### Process
- Mission integrator provides deliverables list
- Each document has specified due date
- First documents due shortly after kickoff meeting
- Templates provided by mission integrator

### Documentation Details
See Chapter 6 of full document for complete requirements

---

## 2.10 Ground Station Design, Development, & Testing (2-12 months)

### Basic Requirements
**Minimum Components**:
- Radio
- Antenna

### Build Early
- Consumes significant time and energy
- Critical for mission success

### Resources
**Amateur Radio Community**:
- Off-the-shelf amateur radio components
- Local amateur radio clubs willing to help
- American Radio Relay League: http://www.arrl.org/
- Design information: http://www.cubesat.org

### Testing is Critical ⭐
**Ground station functions**:
- Locate satellite
- Send commands
- Downlink data

**Inadequate ground station = Mission killer**

### Development Testing Strategies

**1. Monitor Existing Satellites**:
- Gain operational experience
- Practice with equipment
- Learn software and command structure

**Recommended Targets**:
- **437 MHz (70 cm) band**: CubeSat beacons (look for recently launched)
- **140 MHz (2 m) band**: NOAA weather satellites (produce images)

**2. Contact Satellite Operators**:
- Some allow commanding with coordination
- Invaluable operations experience

**3. Join CubeSat Community**:
- IRC channel: irc.freenode.net #cubesat
- Active during/after launches
- Many "first contacts" happen here
- Volunteer trackers worldwide

### Troubleshooting Basics
**Systematic Approach**:
- Check antenna pointing (use calibration: mountains, Sun, Moon)
- Use vector network analyzer for impedance checks (antenna, cables, adapters)
- Confirm radio tuning, mode, and line levels
- Software defined radios (RTL2832, FunCube) for RF capture/replay practice

---

## 2.11 CubeSat Hardware Fabrication & Testing (2-12 months)

### Build Strategy

**Multiple Units Recommended**:
1. **Engineering Test Unit (ETU)**: Practice assembly, fit checks, testing
2. **FlatSat**: Components on flat board (no structure) for troubleshooting
3. **Two Flight Units**: Choose best hardware for flight

**Why Multiple Units**:
- Launch opportunities are fluid
- Launch failures possible
- Cheaper to build multiple at once
- No two satellites are exactly the same

### Documentation is Critical ⭐
**Take Photos Throughout**:
- Regular intervals during assembly
- All integration phases
- All testing phases

**Why It Matters**:
- Photo documentation has saved missions
- Prevents knowledge loss when team members leave
- Critical for student organizations (graduations)
- Avoid "reinventing the wheel"

### Two Types of Testing

**1. Development Testing**:
- Internal testing for your purposes
- No documentation due to CSLI
- Test as much as you want

**2. Verification Testing**:
- Proves to CSLI/LV provider safety and sturdiness
- Specific testing required by ICD
- Test plans and reports submitted to mission integrator
- **After verification: NO MORE WORK or must re-test**

### Required Verification Tests
- Vibration testing
- Thermal vacuum testing
- Shock testing (sometimes)
- EMI/EMC testing (sometimes)
- Static load tests (sometimes)
- Day In The Life (DITL) testing

### Testing Best Practices

**"Test Like You Fly"**:
- Use evaluation/development kits before fabricating boards
- Test PCBs standalone before interfacing with other systems
- Keep scope small, add components systematically
- Never assume standalone success = integrated success
- Thermal/vibration test subsystems before full integration
- Catches design issues early, reduces over-testing

**Testing Containers**:
- Simplified version of flight dispenser
- Flight-like interface for testing apparatus
- Ask mission integrator about availability

### Timing
All testing and documentation must be submitted **at least 1 month before readiness reviews**

---

## 2.12 Mission Readiness Reviews (Half-Day)

### What is MRR?
Presentation summarizing evidence that CubeSat satisfies all ICD requirements

### Prerequisites
- All deliverable documentation submitted AND accepted
- All testing completed
- CubeSat completely finished

### Format
- **In-person presentation required** (at least one representative)
- Cannot be completed by telephone
- Budget for travel!
- Location determined by LSP and mission integrator

### Timeline
- **1 month before review**: Receive MRR outline/template
- **2+ weeks before review**: Submit draft presentation
- **Purpose of pre-check**: Catch errors, ensure all information covered

### Attendees
- All CubeSat teams manifested on mission
- Mission integrator
- CSLI representatives

---

## 2.13 CubeSat-to-Dispenser Integration & Testing (2 days)

### Day 1: Integration

**Delivery Day Checklist**:
- Arrive at integration site (location determined by integrator)
- Unpack CubeSat in clean room
- Pre-integration physical measurements
- May assist with integration (positioning, insertion into dispenser)
- Photo opportunities (great publicity!)
- Dispenser door closed and sealed

**Important**: Last time you'll see your CubeSat!

### Day 2: Final Testing
- Dispenser + CubeSat vibration test as single unit
- Verifies successful integration
- Integrator takes over from here

### Special Accommodations
**Request at mission start**:
- Clean room requirements
- Temperature/humidity needs
- Security requirements
- Storage needs
- Ground Support Equipment (GSE) you'll bring
- Potential hazards (e.g., laser emitters—you provide safety gear)

### Pre-Delivery Activities (if approved)
- System diagnostics
- Battery charging
- **After dispenser closed**: No access (except extreme circumstances with long delays)

### Post-Integration
- Dispenser inspected one more time
- Packaged and shipped to LV integration site

---

## 2.14 Dispenser-to-Launch Vehicle Integration (1 day)

### What Happens
Loaded dispenser attached to rocket

### Who's Invited
**Essential Personnel Only**:
- LSP representatives
- Mission integrator
- Launch provider technicians

**You are NOT invited** (LV providers protective of rockets)

### Integration Process
1. Mission integrator arrives with loaded dispenser
2. LV technicians lead to attachment location
3. Final cleaning and inspection
4. Integrator hands off dispenser to LV technicians
5. Prescribed procedure to attach dispenser
6. Photos taken as evidence

### Timing
Typically **2 weeks to 4 months before launch** (varies by LV)

---

## 2.15 Launch (1 day)

### Important Facts
- **Launch location**: Depends on primary mission (known before manifesting)
- **Launch date**: May change (only primary mission or LV can change)
- **CubeSats have NO influence** on launch date or window
- **If delayed**: Launch will NOT wait for you
- **If not delivered on time**: LV leaves without your CubeSat

### Your Role
- No active role in launch operations
- Usually invited to watch launch
- Travel at your own expense
- May participate in public affairs/outreach (NASA EDGE interviews, photos)

### Important Warnings ⚠️
- Launch date subject to change anytime
- Day-of-launch scrubs are common (weather, other factors)
- Plan extra days for potential delays

---

## 2.16 Mission Operations (Variable, up to 20 years)

### Initial Operations Challenges
- Most exciting part for first-time flyers
- Also most challenging
- Mission integrator will help with communications

### Pre-Launch Preparation
**Practice is Essential**:
- Use ground station on engineering/flight versions
- Track existing CubeSats
- Request permission to uplink to other CubeSats
- Experience helps determine best commands for orbit

### Tracking Satellites

**Two-Line Element (TLE) Sets**:
- Data format encoding orbital elements
- Entered into satellite tracking software
- Predicts satellite position

**Primary TLE Source**:
- **Joint Space Operations Center (JSpOC)** at Vandenberg AFB
- Website: http://www.space-track.org
- Records back to 1957
- Most widely available and accurate

### Post-Launch Satellite Identification

**Challenge**: Determining which new object is YOUR satellite

**Tools Available**:
1. **Preliminary State Vectors**: From launch provider before launch
2. **Actual State Vectors**: Provided after ejection, convert to TLEs
3. **JSpOC TLEs**: Rough TLEs in few days to a week, refined over following weeks

**Identification Process**:
- Mission integrator works with JSpOC and teams
- GPS-equipped CubeSats help (process of elimination)
- Can take several weeks to identify all satellites

### Amateur Radio Community Assistance

**For amateur band frequencies**:
- Post announcements online for volunteer satellite trackers
- Very helpful for identifying CubeSats
- Active community support

### CubeSat IRC Channel
- Most active amateur satellite-tracking enthusiasts meet here
- During/after launch
- Share observations and work on identification
- Many "first contacts" from worldwide community
- **Join**: irc.freenode.net #cubesat

---

# CHAPTER 3: MISSION MODELS

## Overview

CSLI has worked with different organizations that sponsor launches, each with their own "mission model"—the way they run missions. Your CubeSat team will work with requirements and organizational structures specific to your assigned mission type.

### Five Mission Models:
1. NASA-Procured Launch Vehicle
2. Operationally Responsive Space (ORS) Rideshare
3. National Reconnaissance Office (NRO) Rideshare
4. Commercial Launch Service Through Third-Party Broker
5. International Space Station (ISS) Deployment

---

## 3.1 NASA-Procured Launch Vehicle Mission Model

### Overview
CubeSats ride on NASA missions procured by NASA Launch Services Program (LSP)

### Requirements Basis
- LSP-REQ-317.01
- CubeSat Design Specification (CDS)

### Organizational Structure
```
NASA Primary Mission
      ↓
NASA LSP (Mission Management)
      ↓
CSLI Mission Integrator (Mission Coordination, Dispenser Integration, Testing)
      ↓
CSLI CubeSats
```

### Mission Integrator Duties
- Coordinating safety documentation with range safety
- Interfacing with CubeSat developers
- Verifying ICD requirements
- Point of contact for FCC and NOAA
- CubeSat-to-dispenser integration and testing
- Coordinating with JSpOC for orbit identification

### Your Responsibilities
- Regular mission tag-ups via telephone
- Provide development status updates
- Alert integrator to any issues
- Submit all deliverables to mission integrator (reviewed and approved by NASA LSP)
- Present in-person readiness review to integrator with NASA LSP as advisor

### NASA's Role
- Ensure orbital debris mitigation compliance
- Generate Orbital Debris Assessment Report for all CSLI CubeSats

---

## 3.2 Operationally Responsive Space (ORS) Rideshare Mission Model

### Overview
ORS Office (U.S. Department of Defense joint effort) provides launch opportunities for CSLI and other CubeSats

### Organizational Structure
```
ORS Office
      ↓
ORS Mission Integrator (Mission Management)
      ↙        ↘
CSLI Mission    ORS CubeSats
Integrator
      ↓
CSLI CubeSats
```

### Two-Tier Integration
**ORS Mission Integrator**:
- Overall mission management
- Safety documentation with range safety
- ICD verification
- FCC and NOAA point of contact
- JSpOC coordination
- Physical CubeSat-to-dispenser integration

**CSLI Mission Integrator** (Scaled-back responsibilities):
- Track CubeSat development
- Perform ICD verification tasks
- Provide updates to ORS mission integrator
- Participate in ORS mission tag-ups
- Speak on behalf of CubeSat teams
- Hold separate tag-ups for CSLI CubeSats

### Your Responsibilities
- Submit deliverables to CSLI mission integrator
- Regular tag-up meetings with CSLI mission integrator
- Present in-person readiness review to CSLI integrator, ORS integrator, and NASA LSP (advisor)

### NASA's Role
- Ensure orbital debris mitigation compliance
- Generate Orbital Debris Assessment Report

### From Developer Perspective
Very similar to NASA mission model: regular tag-ups, submit documentation, present readiness review

---

## 3.3 National Reconnaissance Office (NRO) Rideshare Mission Model

### About NRO
- U.S. intelligence community agency
- Designs, builds, operates reconnaissance satellites
- Established 1961 (declassified 1992)
- Website: http://www.nro.gov
- Excellent supporter of CubeSat technologies

### Organizational Structure
```
OSL (Office of Space Launch, under NRO)
      ↙        ↘
LV Provider   APIC (Auxiliary Payload Integration Contractor)
              Mission Integration
                    ↓
              NASA LSP (Mission Management)
                    ↓
          CSLI CubeSats    NRO CubeSats
```

### APIC (Auxiliary Payload Integration Contractor)
- Can be multiple organizations
- Mission integrator duties
- Reports to LV provider and OSL

### Your Responsibilities
- **No participation** in APIC reports or reviews to OSL
- Separate biweekly tag-ups with APIC via teleconference
- Provide status updates
- Alert APIC to schedule/requirement issues
- Submit deliverables to APIC (reviewed by APIC)
- Present in-person readiness review to APIC team, NASA LSP, and OSL

### NASA's Role
- Ensure orbital debris mitigation compliance
- Generate Orbital Debris Assessment Report

### From Developer Perspective
Similar to other models: regular tag-ups, submit documentation, present readiness review

---

## 3.4 Commercial Launch Service Through Third-Party Broker

### Overview
Launch purchases through brokers on non-Government (commercial or foreign) missions

### Organizational Structure
```
Third-Party Broker (Mission Manager)
      ↙        ↘
LV Provider   CSLI CubeSats
```

### Key Differences
- Requirements come from LV provider via broker
- **NASA LSP does NOT verify requirements**
- Broker serves as mission integrator or assigns one
- Mission integrator creates CubeSat-to-dispenser ICD
- Determines schedule for deliverables
- **May not require readiness reviews** (tracks deliverables instead)

### NASA's Role
- Ensure orbital debris mitigation compliance
- Generate Orbital Debris Assessment Report

### Flexibility
Most flexible model—requirements and processes vary by broker and LV provider

---

## 3.5 International Space Station (ISS) Deployment Model

### How It Works
1. CubeSats integrated into dispensers on ground
2. Transported to ISS in pressurized cargo vessel (SpaceX Dragon, Orbital ATK Cygnus, etc.)
3. Hand carried onto ISS from cargo vessel
4. Astronauts deploy CubeSats from ISS (typically 1-3 months after arrival)

### Organizational Structure
```
NASA ISS LV Provider
      ↓
Mission Integrator (Mission Coordination, ISS Integration, Acceptance Testing)
      ↓
NASA LSP (Mission Management)
      ↓
CSLI CubeSats    Other CubeSats
```

### Requirements
- Similar to CDS (mechanical and electrical)
- **NanoRacks**: Currently only commercial organization for ISS deployment
- Website: http://nanoracks.com
- Must comply with current NanoRacks ICD

### Process
- Submit flight safety review documents to mission integrator
- Mission integrator handles ISS team reviews

### NASA's Role
- Ensure orbital debris mitigation compliance
- Generate Orbital Debris Assessment Report

---

# KEY TERMS GLOSSARY

## General Terms

**CubeSat Developer**
Any person or organization designing, building, and preparing a CubeSat for flight.

**Investigation**
The mission, scientific or otherwise, that your CubeSat will perform. Used interchangeably with "mission."

**Mission**
All-encompassing term for the entire enterprise from development, testing, integration, launch, to operations. Sometimes used interchangeably with "project" or "investigation."

**Form Factor**
The size, shape, and/or component arrangement of a device. For CubeSats, refers to the standard size and mass specifications.

**Interface**
Any point where two or more components are joined together (mechanical, electrical, etc.).

**Payload**
In aerospace, the cargo being delivered to space. For CubeSat dispensers, the payload is the CubeSat.

**Manifesting**
The process of assigning CubeSats to available slots on a launch opportunity.

**Strategic Partnering**
Combining strengths and resources of multiple organizations to achieve greater goals, typically formalized by agreement.

## Testing & Development Terms

**ADCS (Attitude Determination and Control System)**
System designed to stabilize and orient the CubeSat toward a given direction. Critical for mission success (solar panel pointing, Earth imaging, etc.).

**ETU (Engineering Test Unit)**
CubeSat built like flight unit but not intended for launch. Used for practice assembly, fit checks, and testing.

**FlatSat**
Engineering unit with all components except structure, typically mounted on flat board. Used for testing and troubleshooting without full integration.

**Breadboard**
Board used to make experimental model of components for testing.

**Margin**
Extra resources (time, budget, performance) that provide safety buffer against unexpected events.

**Electrical Inhibit**
Physical device that interrupts the power path needed to turn on CubeSat and/or potentially hazardous devices.

## Mission & Operations Terms

**Mission Integrator**
Organization/person responsible for mission coordination activities. Sometimes called mission coordinator (terms used interchangeably).

**Integration Services**
Typically includes: deliverables review, dispenser provision, CubeSat integration into dispenser, dispenser/CubeSat system testing, and dispenser/CubeSat integration onto LV.

**Deliverables**
Anything your team agreed to submit to mission integrator as part of legal obligations under CRADA.

**Range Safety**
Person designated to protect people and assets on launch range and downrange when LV might expose them to danger.

**Two-Line Element (TLE)**
Data format encoding orbital elements of Earth-orbiting CubeSat for given point in time (epoch). Used with prediction formula to estimate position and velocity.

**Terminal Node Controller (TNC)**
Device used by amateur radio operators for AX.25 packet radio networks. Assembles data into packets, keys transmitter, and reassembles received packets.

---

# QUICK REFERENCE TABLES

## Timeline Summary

| Phase | Duration | Key Activities |
|-------|----------|----------------|
| 1. Concept Development | 1-6 months | Define mission, align with NASA goals, find partners |
| 2. Securing Funding | 1-12 months | Identify funding sources, create budget |
| 3. Merit & Feasibility Reviews | 1-2 months | Conduct independent reviews of mission quality and feasibility |
| 4. CubeSat Design | 1-6 months | Research, select components, design CubeSat |
| 5. Proposal Development | 3-4 months | Develop and submit proposal to CSLI AoPO |
| 6. Selection & Manifesting | 1-36 months | CSLI selection process, matching with launch |
| 7. Mission Coordination | 9-18 months | Regular tag-ups, coordination with integrator |
| 8. Licensing | 4-6 months | RF license (FCC/NTIA), Remote Sensing (NOAA if needed) |
| 9. Documentation | 10-12 months | Develop and submit flight certification documents |
| 10. Ground Station | 2-12 months | Design, build, and extensively test ground station |
| 11. Hardware Fabrication | 2-12 months | Build and test CubeSat units |
| 12. Mission Readiness Review | Half-day | In-person presentation to integrator and stakeholders |
| 13. Dispenser Integration | 2 days | Deliver, integrate, final vibration test |
| 14. LV Integration | 1 day | Dispenser attached to rocket |
| 15. Launch | 1 day | Launch day (possibly delayed) |
| 16. Mission Operations | Variable | Up to 20 years |

## CubeSat Standard Sizes

| Size | Dimensions | Typical Mass | Notes |
|------|-----------|-------------|-------|
| 1U | 10 cm × 10 cm × 11 cm | 1-1.33 kg | Basic unit |
| 1.5U | 10 cm × 10 cm × 16.5 cm | ~1.5-2 kg | Less common |
| 2U | 10 cm × 10 cm × 22 cm | ~2-2.66 kg | Moderate size |
| 3U | 10 cm × 10 cm × 34 cm | ~3-4 kg | Very popular |
| 6U | 20 cm × 10 cm × 34 cm | ~6-14 kg | Introduced 2014 |
| 12U | 20 cm × 20 cm × 34 cm | ~12-24 kg | Large format |

## Design Best Practices Checklist

| Best Practice | Why It Matters | Reference |
|--------------|----------------|-----------|
| ✓ Keep it simple | Fewer complex systems = more launch opportunities | 2.4 |
| ✓ Important components on exterior | Easier repairs, may avoid re-testing | 2.4 |
| ✓ Don't design to envelope limits | If it doesn't fit, it doesn't fly | 2.4 |
| ✓ Double up on burn wire | Prevents premature deployable release | 2.4 |
| ✓ Use familiar components | Flight heritage reduces risk | 2.4 |
| ✓ Use UL listed batteries | Avoids extensive additional testing | 2.4 |
| ✓ Use high-melting point materials | Safety and debris mitigation | 2.4 |
| ✓ Keep mission flexible | Faster manifesting to launch | 2.1 |
| ✓ Build multiple units | ETU, FlatSat, 2 flight units | 2.11 |
| ✓ Take extensive photos | Saves missions, preserves knowledge | 2.11 |
| ✓ Test like you fly | Catch issues early, reduce risk | 2.11 |

## Mission Model Comparison

| Model | Primary Contact | Tag-Up Style | Readiness Review Attendees | Key Difference |
|-------|----------------|--------------|---------------------------|----------------|
| NASA-Procured LV | CSLI Mission Integrator | Direct with integrator | Integrator + NASA LSP (advisor) | Direct NASA oversight |
| ORS Rideshare | CSLI Mission Integrator | Via CSLI integrator to ORS | Both integrators + NASA LSP | Two-tier integration |
| NRO Rideshare | APIC | Separate from APIC-OSL meetings | APIC + NASA LSP + OSL | Developer separate from primary meetings |
| Third-Party Broker | Broker/Mission Manager | Varies | May not require MRR | Most flexible, varies by broker |
| ISS Deployment | Mission Integrator | Direct with integrator | Integrator + relevant ISS team | Deployment from Space Station |

## Critical Deadlines & Warnings

| Item | Deadline/Timing | Consequence of Missing |
|------|----------------|------------------------|
| RF License Application | Within 30 days of manifesting | Potential demanifest from mission |
| RF License Approval | Before final delivery date | **DEMANIFEST** - Mission scrubbed, possibly lose CubeSat |
| NOAA License (if needed) | Before FCC processes RF license | FCC cannot complete processing |
| All Testing Complete | 1 month before MRR | Cannot proceed to readiness review |
| Deliverables Submitted | Per integrator schedule | Cannot proceed to readiness review |
| CubeSat Delivery | Per integrator schedule (4 wks - 6 mo before launch) | Launch leaves without you, no delays |
| Funding Secured | Throughout development | Possible liability for NASA costs already spent |

## Essential Resources & Websites

| Resource | URL | Purpose |
|----------|-----|---------|
| CubeSat.org | http://www.cubesat.org | CDS, component vendors, design resources |
| CSLI Website | http://go.nasa.gov/CubeSat_initiative | CSLI information, prior awards |
| Federal Opportunities | https://sam.gov | AoPO announcements |
| NASA Strategic Plan | http://www.nasa.gov | Alignment for proposal |
| Space Grant Consortium | (State-specific) | Student STEM funding |
| JSpOC Tracking | http://www.space-track.org | TLE data, satellite tracking |
| Amateur Radio League | http://www.arrl.org/ | Ground station help |
| NanoRacks | http://nanoracks.com | ISS deployment requirements |
| CubeSat IRC | irc.freenode.net #cubesat | Community, tracking, first contacts |
| NRO Information | http://www.nro.gov | NRO background |

## Funding Sources Quick Reference

| Source Type | Examples | Best For |
|-------------|----------|----------|
| Government Agencies | NSF, NASA ESTO, NASA Space Grant Consortium | Research, technology, education missions |
| Educational Institutions | Faculty, administrators, university programs | Student-led projects |
| Technology Demonstration | Government/commercial sponsors | Testing new components |
| Crowdfunding | Kickstarter, etc. | Supplementary funding, public engagement |
| Partnerships | Strategic partners with similar goals | Complex missions, resource sharing |

## Common Cost Categories

| Category | Examples | Notes |
|----------|----------|-------|
| Materials | Components, structure, batteries | Research suppliers early |
| Labor | Team members, consultants | Often in-kind for universities |
| Environmental Testing | Vibration, thermal vacuum, shock, EMI/EMC | Varies by facility |
| Ground Station | Radio, antenna, software | Amateur components popular |
| Travel | Reviews, integration, delivery | Often overlooked |
| Reserves | 10%+ of total budget | For unexpected events |

---

## Study Tips

### For Exam Preparation
1. **Memorize timeline**: Know the 16 phases and typical durations
2. **Understand mission models**: Be able to compare and contrast the 5 models
3. **Know critical deadlines**: Especially licensing requirements
4. **Review best practices**: Understand the "why" behind each recommendation
5. **Study glossary**: Many terms are used interchangeably in practice

### For Project Planning
1. **Start with timeline**: Use as framework for Gantt chart
2. **Budget early**: Include ALL cost categories, especially reserves
3. **Design conservatively**: Simple designs get more launch opportunities
4. **Document everything**: Photos and notes save missions
5. **Test extensively**: Ground station and CubeSat both critical

### Key Takeaways
- **Flexibility is your friend**: Flexible requirements = faster manifesting
- **Licensing is critical**: Start early, no exceptions
- **Testing is insurance**: Development testing prevents verification failures
- **Community helps**: CubeSat community is open and supportive
- **Plan for the long term**: Typical timeline is 18-24 months minimum

---

*Document prepared from NASA CubeSat 101: Basic Concepts and Processes for First-Time CubeSat Developers, Chapters 1-3*

*For complete information, refer to full NASA CubeSat 101 document and current CSLI requirements*
