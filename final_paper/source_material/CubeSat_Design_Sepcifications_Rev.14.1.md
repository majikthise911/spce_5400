CubeSat Design Specification Rev. 14.1
The CubeSat Program, Cal Poly SLO
Document
Classification
X Public Domain
CubeSat Design Specification
(1U – 12U)
REV 14.1
CP-CDS-R14.1
Cal Poly – San Luis Obispo, CA
CubeSat Design Specification Rev. 14.1
The CubeSat Program, Cal Poly SLO
Effective
Date Revision Author July
2020
14 Alicia
Johnstone
February
2022
14.1 Alicia
Johnstone
2
REV14 CHANGE SUMMARY
Description of Changes
CDS Rev 14 supersedes CDS Rev 13 and 6U CDS Rev 1.0.
For Revision 14, the CDS was updated to reflect current industry
standards as well as include standards for 6U and 12U CubeSats.
Previous versions of the CDS were presented as a set of requirements,
many of the specifications in Rev 14 have been revised to serve more as
guidelines than hard requirements in an effort to make the CDS into a
useful tool for CubeSat Developers. Sections were added with
information on available CubeSat dispensers. Appendix drawings were
also updated.
See Appendix A for the full Change History Log and detailed revision
history.
Removed DRAFT and published as official Rev 14.1. Added and
updated dispenser information in Sections 4 and 5. Added clarifying
language to Sections 2 and 3.
See Appendix A for the full Change History Log and detailed revision
history.
CubeSat Design Specification Rev. 14.1
The CubeSat Program, Cal Poly SLO
3
TABLE OF CONTENTS
1. INTRODUCTION ............................................................................................ 7
1.1 Overview ........................................................................................................................................... 7
1.2 Purpose ............................................................................................................................................. 8
1.3 Mission Requirements ..................................................................................................................... 8
1.4 Non-compliance with CDS .............................................................................................................. 9
1.5 Definitions ......................................................................................................................................... 9
1.6 Definition of Terms .......................................................................................................................... 9
2. CUBESAT SPECIFICATION ......................................................................... 9
2.1 General Specifications ..................................................................................................................... 9
2.2 CubeSat Mechanical Specifications ............................................................................................. 10
2.3 Electrical Specifications ................................................................................................................ 14
2.4 Operational Specifications ............................................................................................................ 15
3. TESTING REQUIREMENTS ....................................................................... 16
3.1 Random Vibration ......................................................................................................................... 16
3.2 Thermal Vacuum Bakeout ............................................................................................................ 16
3.3 Shock Testing ................................................................................................................................. 16
3.4 Visual Inspection ............................................................................................................................ 16
3.5 CubeSat Testing Philosophy ......................................................................................................... 16
4. CUBESAT DISPENSER ................................................................................ 18
4.1 Interface .......................................................................................................................................... 18
5. DISPENSER OPTIONS ................................................................................. 20
6. CONTACTS .................................................................................................... 23
CubeSat Design Specification Rev. 14.1
The CubeSat Program, Cal Poly SLO
4
APPENDICES
A. CHANGE HISTORY LOG ....................................................................................... 24
B. CUBESAT SPECIFICATION DRAWINGS ........................................................... 27
CubeSat Design Specification Rev. 14.1
The CubeSat Program, Cal Poly SLO
List of Acronyms and Abbreviations
5
ADC Attitude Determination and Control
AFSPCMAN Air Force Space Command Manual
C&DH Command and Data Handling
CA California
Cal Poly CIFP California Polytechnic State University, San Luis Obispo
CDS CubeSat Design Specification
CubeSat Inspection and Fit-check Procedure
cm Centimeters
CP Cal Poly
CPCL Cal Poly CubeSat Laboratory
CVCM Collected Volatile Condensable Mass
DAS Debris Assessment Software
ESA European Space Agency
FAA Federal Aviation Administration
FCC Federal Communication Commission
GEVS General Environmental Verification Standard
GSFC Goddard Space Flight Center
IARU International Amateur Radio Union
ISIS Innovative Solutions in Space
ITU International Telecommunication Union
JAXA Japan Aerospace Exploration Agency
kg Kilogram
kHz Kilohertz
lbf Pound-force
LSP Launch Services Program
LV Launch Vehicle
mA milli-Amps
MIN Minimum
mm Millimeters
N Newton
N/A Not Applicable
NASA National Aeronautics and Space Administration
CubeSat Design Specification Rev. 14.1
The CubeSat Program, Cal Poly SLO
6
NOAA National Oceanic and Atmospheric Administration
NLAS Nanosatellite Launch Adapter System
NPR NASA Procedural Requirements
P-POD Poly Picosatellite Orbital Deployer
PSC Planetary Systems Corporation
PSL-P PicoSatellite Launch-Pack
RBF Remove Before Flight
REQ Requirement
Rev. Revision
RF Radio Frequency
RTC Real Time Clock
SLO San Luis Obispo
SMCS Space and Missile Systems Center Standard
SSDL Space Systems Development Lab
SSOD Small Satellite Orbital Deployer
STD Standard
TML Total Mass Loss
U Unit
UL Underwriters Laboratories
Wh Watt-hours
µm Micrometer
Applicable Documents
The following documents form a part of this document to the extent specified herein.
Air Force Space Command Manual 91-710, Range Safety User Requirements Manual
(AFSPCMAN 91-710)
General Environmental Verification Standard for GSFC Flight Programs and Projects
(GSFC-STD-7000 A)
LSP Program Level P-POD and CubeSat Requirements Document (LSP-REQ-317.01 B)
NASA Procedural Requirements for Limiting Orbital Debris (NPR 8715.6B)
Space and Missile Systems Center Standard Test Requirements for Launch, Upper-Stage
and Space Vehicles (SMC-S-016)
Standard Materials and Processes Requirements for Spacecraft (NASA-STD-6016)
CubeSat Design Specification Rev. 14.1
The CubeSat Program, Cal Poly SLO
7
1. Introduction
1.1 Overview
Started in 1999, the CubeSat Project began as a collaborative effort between Prof. Jordi Puig-Suari
at California Polytechnic State University (Cal Poly), San Luis Obispo, and Prof. Bob Twiggs at
Stanford University’s Space Systems Development Laboratory (SSDL). The intent of the CubeSat
Project was to reduce cost and development time, increase accessibility to space, and sustain
frequent launches. A CubeSat is a class of satellites that adopt a standard size and form factor,
which unit is defined as ‘U’. A 1U CubeSat is a 10 cm cube with a mass of up to 2 kg. This standard
primary objective is to provide specifications for the design of CubeSats ranging from 1U to 12U.
The standard secondary objective is to provide information on available CubeSat dispensers and
their corresponding interfaces. To view the most updated versions of the CubeSat Design
Specification, please visit: http://www.cubesat.org/.
Figure 1: The first CubeSats developed at Cal Poly, CP1 and CP2, are pictured here with four other
1U CubeSats before being integrated into two early generation P-PODs in 2006.
CubeSat Design Specification Rev. 14.1
The CubeSat Program, Cal Poly SLO
8
1U 1.5U 2U 3U 6U 12U
Figure 2: The Current CubeSat Family (1U – 12U)
1.2 Purpose
CubeSat developers should play an active role in ensuring the safety and success of CubeSat
missions by implementing good engineering practice, testing, and verification of their systems.
Failures of CubeSats, CubeSat dispensers, or interface hardware can damage the LV or a primary
payload, putting the entire CubeSat Program in jeopardy. As such, the purpose of the specifications
described in this document is to help ensure the success and safety of the mission, as well as provide
baseline requirements for CubeSat developers to design their spacecraft, such that they will be
compatible with as many CubeSat dispensers and launch opportunities as possible.
As part of the CubeSat Community, all participants have an obligation to ensure safe operation of
their systems, obtain the required licensing from the appropriate agencies, and to meet the design
and minimum testing requirements outlined in this document.
1.3 Mission Requirements
Although mission requirements are oftentimes similar to the requirements in the CDS, the CubeSat
Developer will only be responsible for meeting the requirements provided by the Launch Provider.
The requirements in this document are meant for preliminary design purposes, and are written
conservatively to allow for the best chances of compatibility with any launch vehicle.
Launch vehicle provider requirements supersede the requirements in this document.
CubeSat Design Specification Rev. 14.1
The CubeSat Program, Cal Poly SLO
9
1.4 Non-compliance with CDS
Prior to a CubeSat being manifested on a launch, the specifications and requirements stated in the
CDS provide guidance on the CubeSat design to ensure safe operation of the system.
After a CubeSat is manifested on a launch, the Launch Provider requirements supersede the CDS
requirements. In some cases, CDS specifications and requirements may be more restrictive than
the Launch Provider requirements. Ideally, a CubeSat that complies with all CDS requirements will
comply with the requirements for most, if not all, Launch Provider requirements. For more
information, please contact the Cal Poly CubeSat Laboratory: cubesat@calpoly.edu.
Developers should understand that each requirement deviation potentially reduces the
chances of finding a suitable launch opportunity.
1.5 Definitions
1.5.1 Developer: Person or organization responsible for the creation and delivery of the CubeSat
1.5.2 Dispenser integrator: Person or organization responsible for safely stowing the CubeSat
into the dispenser and preparing the dispenser for the launch vehicle
1.5.3 Dispenser manufacturer: Person or organization responsible for the construction of the
CubeSat dispenser
1.5.4 Launch Provider: Person or organization responsible for the launch vehicle and/or the
system delivering the CubeSat to orbit
1.6 Definition of Terms
Throughout this document, one of three different operational words will be used in each
specification. Their associated definitions are shown below.
1.6.1 1.6.2 1.6.3 1.6.4 Shall is used to denote requirements that must be met and will need formal verification.
Should is used to denote a strong recommendation or a suggestion to make formal
verification of another requirement easier. In many cases, failure to adhere to “should”
statements will limit launch opportunities.
Will is used to denote a situation that is going to happen regardless of inputs from the
launch vehicle and/or spacecraft developer. “Will” statements serve to indicate events that
the spacecraft developers should be prepared for.
Note is used to denote a recommendation or advice meant to aid the CubeSat Developer.
2. CubeSat Specification
2.1 General Specifications
2.1.1 2.1.2 2.1.3 All parts shall remain attached to the CubeSats during launch, ejection and operation.
Pyrotechnics shall conform to AFSPCMAN 91-710, Volume 3.
Any propulsion systems shall be designed, integrated, and tested in accordance with
AFSPCMAN 91-710 Volume 3.
2.1.4 Propulsion systems shall have at least 3 inhibits to activation.
10
CubeSat Design Specification Rev. 14.1
The CubeSat Program, Cal Poly SLO
2.1.5 2.1.6 2.1.7 2.1.7.1 2.1.7.2 2.1.8 2.1.9 Note: It is recommended to consider Federal Aviation Administration (FAA) requirements
for Batteries Carried by Airline Passengers. For example, the maximum allowed capacity
for consumer-sized lithium ion batteries in carry-on baggage is 100 Wh per battery.
CubeSat hazardous materials shall conform to AFSPCMAN 91-710, Volume 3.
CubeSat materials shall satisfy low out-gassing criteria, as defined in 2.1.7.1 and 2.1.7.2,
to prevent contamination of other spacecraft during integration, testing, and launch. A list
of NASA approved low out-gassing materials can be found at: http://outgassing.nasa.gov.
CubeSats materials shall have a Total Mass Loss (TML) of less than or equal to 1.0 %
CubeSat materials shall have a Collected Volatile Condensable Material (CVCM) of
less than or equal to 0.1%
The magnetic field of any passive magnets shall be limited to 0.5 Gauss above Earth’s
magnetic field, outside the CubeSat static envelope.
The CubeSat shall be designed to accommodate ascent venting per ventable volume/area
of less than 50.8 meters (2000 inches).
2.2 CubeSat Mechanical Specifications
CubeSat dimensions and features are outlined in the CubeSat Specification Drawings (Appendix
B).
Note: The CubeSat Inspection and Fit-check Procedure (CIFP) can be used to aid in verifying that
the CubeSat meets the dimensional requirements specified in Appendix B. The CIFP can be found
on cubesat.org.
These requirements are applicable for all dispensers not utilizing the tab constraint method.
CubeSats designed with tabs can find those specific requirements at the PSC website
(planetarysystemscorp.com).
2.2.1 2.2.1.1 2.2.1.2 The CubeSat shall use the coordinate system as defined in Appendix B. The origin of the
CubeSat coordinate system is located at the geometric center of the CubeSat.
The CubeSat configuration and physical dimensions shall conform to the appropriate
section of Appendix B.
Note: The standoff length dimension [“(0.5-7.0) 0.1 MIN +/- Z FACES”], specified in
the drawings in Appendix B, exists to prevent interference with potential neighboring
CubeSats and dispenser interfaces.
Note: Extra volume may be available for 3U, 6U, and 12U CubeSats. This extra volume
is shown in Figure 3, sometimes referred to as the “Tuna Can” volume. The availability
and volume dimensions are dispenser dependent.
2.2.1.3 
CubeSat Design Specification Rev. 14.1
The CubeSat Program, Cal Poly SLO
11
12U+ Volume
(Tuna Can)
-Z Face
Figure 3: Optional Extra Volume shown on 3U and 12U –Z Face (also known as a "Tuna Can"). The
Extra Volume is also an optional feature for the 6U configuration.
2.2.2 2.2.3 2.2.3.1 2.2.4 2.2.5 2.2.5.1 The –Z face of the CubeSat will be inserted first into the dispenser.
No components on the yellow shaded sides (see Appendix B CDS drawings) shall protrude
farther than 6.5 mm normal to the surface from the plane of the rail.
Note: Please refer to the CIFP for recommended protrusion measurement technique.
Deployables shall be constrained by the CubeSat, not the dispenser. This requirement
originates from requirements of most Launch Providers.
Rails shall have a minimum width of 8.5mm measured from the edge of the rail to the first
protrusion on each face.
Note: An example is shown in Figure 4.
Figure 4: Distance measured from edge of rail to first protrusion
CubeSat Design Specification Rev. 14.1
The CubeSat Program, Cal Poly SLO
12
2.2.6 2.2.6.1 2.2.7 2.2.7.1 2.2.8 2.2.8.1 2.2.9 Rails should have a surface roughness less than 1.6 µm.
Note: This is typically met if the rail material is shown to be properly anodized.
Otherwise, if the surface appears rough, more testing may be required.
The edges of the rails should be rounded to a radius of at least 1 mm.
Note: This is typically met using engineering drawings and manufacturer certification.
The ends of the rails on the +/- Z face shall have a minimum surface area of 6.5 mm x 6.5
mm contact area with neighboring CubeSat rails (as per drawing in Appendix B).
Note: If the CubeSat is not sharing the dispenser with another spacecraft, the Launch
Provider may choose to waive this surface area requirement.
At least 75% of the rail should be in contact with the dispenser rails. 25% of the rails may
be recessed.
2.2.10 Note: Table 1 shows the typical maximum mass for each U configuration.
Table 1: CubeSat Mass Specifications
U Configuration Mass
[kg]
1U 2.00
1.5U 3.00
2U 4.00
3U 6.00
6U 12.00
12U 24.00
2.2.10.1 Note: Masses larger than the one presented in Table 1 may be evaluated on a mission-
to-mission basis. Verify constraints with your dispenser provider or Launch Provider.
2.2.10.2 Note: Acceptable masses may vary depending on the dispenser capabilities. Verify
capabilities with your dispenser provider.
2.2.11 The CubeSat center of gravity shall fall within the ranges specified in Table 2.
Table 2: Ranges of acceptable center of gravity locations as measured from the geometric center on
each major axis
X Axis Y Axis Z Axis
1U + 2 cm / -2 cm + 2 cm / -2 cm + 2 cm / -2 cm
1.5U + 2 cm / -2 cm + 2 cm / -2 cm + 3 cm / -3 cm
2U + 2 cm / -2 cm + 2 cm / -2 cm + 4.5 cm / -4.5 cm
3U + 2 cm / -2 cm + 2 cm / -2 cm + 7 cm / -7 cm
6U + 4.5 cm / -4.5 cm + 2 cm / -2 cm + 7 cm / -7 cm
12U + 4.5 cm / -4.5 cm + 4.5 cm / -4.5 cm + 7 cm / -7 cm
2.2.12 2.2.12.1 The CubeSat structure should be made from aluminum alloy.
Note: Typically, Aluminum 7075, 6061, 6082, 5005, and/or 5052 are used for both the
main CubeSat structure and the rails. If materials other than aluminum are used, the
CubeSat developer should contact the Launch Provider or dispenser manufacturer.
CubeSat Design Specification Rev. 14.1
The CubeSat Program, Cal Poly SLO
13
2.2.13 Any aluminum CubeSat external surfaces, such as rails and standoffs that are in contact
with the dispenser rails, shall be hard anodized to prevent any cold welding within the
dispenser.
2.2.14 If a CubeSat shares a dispenser with another CubeSat(s), each CubeSat shall employ a
mechanism to encourage separation from neighboring CubeSats within the dispenser.
2.2.14.1 Note: Any mechanism that will provide separation is acceptable. The common
assumption with separation springs is that “stronger is better”. This is not always the
case. Stronger separation springs can overpower the CubeSat dispenser deployment
spring force during ejection and yield unpredictable separation characteristics, possibly
re-contacting neighboring CubeSats. On the other hand, lower force springs may not
have sufficient energy to separate the CubeSats the required amount. The general
guideline is to select a separation spring with a max force less than 6.7 N (1.5 lbf) but
with a stroke length greater than 2.5 mm (0.1 inches)
2.2.14.2 The separation mechanism shall not extend beyond the level of the standoff in a
stowed configuration.
2.2.14.3 Note: The most common placement of the CubeSat separation mechanism is centered
on the end of the two standoffs on the CubeSat’s –Z face as per Figure 5.
2.2.14.4 Note: A separation mechanism is not required for CubeSats that do not share a
dispenser with another CubeSat(s).
Figure 5: Recommended Deployment Switches and Separation Spring Locations
CubeSat Design Specification Rev. 14.1
The CubeSat Program, Cal Poly SLO
14
2.3 Electrical Specifications
Electronic systems will be designed with the following safety features. These specifications are
applicable for all dispensers.
2.3.1 2.3.1.1 2.3.1.2 2.3.2 2.3.2.1 2.3.2.2 2.3.2.3 2.3.2.4 2.3.3 2.3.3.1 2.3.3.2 2.3.3.3 2.3.4 2.3.4.1 2.3.5 2.3.5.1 2.3.5.2 2.3.6 2.3.7 To prevent CubeSat from activating any powered functions, the CubeSat power system
shall be at a power off state from the time of delivery to the LV through on-orbit
deployment.
Note: CubeSat powered function include the variety of subsystems such as C&DH, RF
Communication, ADC, deployable mechanism actuation. CubeSat power systems
include all battery assemblies and solar cells.
Powered-on battery protection circuitry may be permitted per specification 2.3.6.
The CubeSat shall have, at a minimum, one deployment switch, which is actuated while
integrated in the dispenser.
In the actuated state, the CubeSat deployment switch shall electrically disconnect the
power system from the powered functions.
The deployment switch shall be in the actuated state at all times while integrated in the
dispenser.
In the actuated state, the CubeSat deployment switch should be at or below the level of
any external surface that interfaces with the dispenser or neighboring CubeSat. This
ensures that the switch will not damage or interfere with the contacting surface.
If the CubeSat deployment switch toggles from the actuated state and back, the
satellite shall reset to a pre-launch state, including reset of transmission and
deployable timers.
Real Time Clocks (RTC) may be permitted, if they satisfy requirements 2.3.2.1 through
2.3.2.3.
RTC circuits shall be isolated from the CubeSat’s main power system.
RTC frequencies shall be less than 320 kHz.
RTC circuits shall be current limited to less than 10 mA.
The RBF pin and all CubeSat umbilical connectors shall be within the designated access
port locations if available on the CubeSat’s dispenser. Please contact the manufacturer for
specific charging and diagnostic port locations and procedures.
Note: Some dispensers do not have access ports, therefore the RBF must be removed
before insertion into the dispenser. It is advised that the CubeSat developer takes this
possibility into account when designing the power-on and boot-up sequence.
The CubeSat shall include an RBF pin, which cuts all power to the satellite once it is
inserted into the satellite.
Access to the CubeSat is not guaranteed during or after integration. The RBF pin shall
be removed from the CubeSat before integration into the dispenser, if the dispenser does
not have access ports.
The RBF pin shall protrude no more than 6.5 mm from the CubeSat rail surface when
it is fully inserted into the satellite.
CubeSats shall incorporate battery circuit protection for charging/discharging to avoid
unbalanced cell conditions. Additional manufacturer documentation and/or testing will be
required for modified, customized, or non-UL-listed cells.
The CubeSat shall have at least three independent RF inhibits to prohibit inadvertent RF
transmission.
CubeSat Design Specification Rev. 14.1
The CubeSat Program, Cal Poly SLO
15
2.3.7.1 2.3.7.2 2.3.7.3 2.3.8 Note: An inhibit is a physical device between a power source and a hazard.
Note: A timer is not considered an independent inhibit.
Note: Some launch vehicle providers will only require one or two independent inhibits
depending on the CubeSat’s RF power output. However, the use of three independent
inhibits is highly recommended and can reduce required documentation and analyses.
The CubeSat shall have at least three independent inhibits to prohibit the inadvertent
release of any deployable structures such as antennas or solar panels.
2.4 Operational Specifications
CubeSats will meet certain requirements pertaining to integration and operation to meet legal
obligations and ensure safety of other CubeSats.
2.4.1 Operators shall obtain and provide documentation of proper licenses for use of radio
2.4.1.1 2.4.2 2.4.2.1 2.4.3 2.4.3.1 2.4.3.2 2.4.3.3 2.4.3.4 2.4.4 2.4.5 2.4.5.1 2.4.6 2.4.7 frequencies.
Note: For amateur frequency use, this requires proof of frequency coordination by the
IARU. Applications can be found at www.iaru.org.
CubeSats shall comply with their country’s radio license agreements and restrictions.
Note: CubeSat operator should refer to the International Telecommunication Union
(ITU) to determine what licenses and approvals are needed for their country.
CubeSat mission design and hardware shall be in accordance with NPR 8715.6 to limit
orbital debris.
Any CubeSat component shall re-enter with energy less than 15 Joules.
Developers should be ready to provide orbital debris mitigation data if requested by
the licensing agency or Launch Provider.
Note: Analysis can be conducted to satisfy the above with NASA DAS, available at
https://orbitaldebris.jsc.nasa.gov/mitigation/.
Note: The European Space Agency (ESA) offers debris assessment software at
https://sdup.esoc.esa.int.
All deployables such as booms, antennas, and solar panels shall wait to deploy a minimum
of 30 minutes after the CubeSat's deployment switch(es) are activated during dispenser
ejection.
CubeSats shall not generate or transmit a signal earlier than 45 minutes after on-orbit
deployment.
Note: The CubeSat can be powered on immediately following deployment from the
dispenser.
Note: Private entities (non-U.S. Government) under the jurisdiction or control of the United
States who propose to operate a remote sensing space system (satellite), such as a visual
imager, may need to have a remote sensing license as required by U.S. law. For more
information visit http://www.nesdis.noaa.gov/CRSRA/licenseHome.html.
The dispenser developer will conduct a minimum of one fit check in which the CubeSat
flight unit will be inspected and integrated into the dispenser or engineering dispenser to
verify the fit. A final fit check will be conducted just prior to integration of the CubeSat
flight unit to the dispenser.
CubeSat Design Specification Rev. 14.1
The CubeSat Program, Cal Poly SLO
16
2.4.7.1 Note: It is recommended to verify dimension limits using documentation specific to the
intended dispenser. In lieu of a document provided by the dispenser vendor, the CIFP
located at cubesat.org can be used.
3. Testing Requirements
All testing levels and requirements are mission specific and vary with every launch. The examples
provided in this document, are typically, the most stringent to encompass requirements from most
of the possible launch opportunities to date.
Testing will be performed to meet the Launch Provider requirements as well as any additional
testing requirements deemed necessary to ensure the safety of the CubeSats, dispenser, and the
primary launch vehicle payload. If the launch vehicle environment is unknown, the General
Environmental Verification Standard (GEVS, GSFC-STD-7000A) and SMC-S-016 can be used to
define testing environments and requirements. Note that the test levels defined in GSFC-STD-
7000A and SMC-S-016 are not guaranteed to encompass or satisfy all LV testing environments.
Test requirements and levels that are not generated by the Launch Provider are considered
unofficial. The Launch Provider testing requirements will supersede testing environments from any
other source. Typically, all CubeSats will undergo the following tests.
3.1 Random Vibration
3.1.1 Launch Provider.
Random vibration testing shall be performed to the levels and duration as defined by the
3.2 Thermal Vacuum Bakeout
3.2.1 3.2.2 Thermal vacuum bakeout shall be performed to ensure proper outgassing of components.
The test specification will be defined by the Launch Provider.
3.3 Shock Testing
3.3.1 3.3.1.1 Shock testing shall be performed as defined by the Launch Provider.
Note: Shock testing is typically not required for CubeSats.
3.4 Visual Inspection
3.4.1 Visual inspection of the CubeSat and measurement of critical areas will be performed per
the CIFP (cubesat.org) or as defined by the Launch Provider.
3.5 CubeSat Testing Philosophy
This section outlines a conservative test flow approach for CubeSats to meet environmental test
requirements for launch. The CubeSat shall be subjected to either qualification or protoflight
testing as defined in the CubeSat Testing Flow Diagram, shown in Figure 6. The test levels and
durations will be supplied by the Launch Provider.
3.5.1 Qualification
Qualification testing is performed on an engineering unit that is identical to the flight model
CubeSat. Qualification levels will be determined by the Launch Provider. Both SMC-S-016 and
CubeSat Design Specification Rev. 14.1
The CubeSat Program, Cal Poly SLO
17
GSFC-STD-7000A are used as guides in determining test levels and durations. The flight model
will then be tested to acceptance levels on its own. The Launch Provider may also require a final
acceptance/workmanship random vibration test on the CubeSat and flight dispenser after
integration.
Additional testing may be required if modifications or changes are made to the CubeSat after
qualification testing.
3.5.2 Protoflight
Protoflight testing is performed on the flight model CubeSat. Protoflight levels will be determined
by the Launch Provider. Both SMC-S-016 and GSFC-STD-7000A are used as guides in
determining test levels and durations. The flight model will be tested to protoflight levels on its
own. The Launch Provider may also require a final acceptance/workmanship random vibration test
on the CubeSat and flight dispenser after integration. The flight CubeSat shall not be disassembled
or modified after protoflight testing. Disassembly of hardware after protoflight testing will require
the developer to adhere to the waiver process prior to disassembly.
Additional testing will be required if modifications or changes are made to the CubeSat after
protoflight testing.
3.5.2.1 Note: Some launch providers consider any physical or mechanical changes to the
spacecraft’s configuration to invalidate any previous vibration tests. For example,
actuating deployment mechanisms for a deployment test would constitute a change to
the spacecraft’s configuration.
3.5.3 Acceptance
After delivery and integration of the CubeSat into the dispenser, additional testing may be
performed on the integrated system. This test ensures proper integration of the CubeSat into the
dispenser. Acceptance test levels will be determined by the Launch Provider. Both SMC-S-016 and
GSFC-STD-7000A are used as guides in determining testing levels. The CubeSat shall not be
deintegrated at this point. If a CubeSat failure is discovered, a decision to deintegrate the dispenser
will be made by the Launch Provider based on mission safety concerns.
The developer is responsible for any additional testing required due to corrective
modifications to deintegrated dispensers and CubeSats.
CubeSat Design Specification Rev. 14.1
The CubeSat Program, Cal Poly SLO
18
CubeSat Qualification / Acceptance Test Flow
Hardware Qualification ProtoFlight Acceptance Flight
CubeSat Qual Unit
Vibration Testing
Shock Testing
CubeSat
Qual
Unit
YES
NO
Information
CubeSat Flight Unit
Vibration Testing
TVAC Bakeout
CubeSat Flight Unit
Vibration Testing
Shock Testing
TVAC Bakeout
PPOD Flight
System
Vibration
Flight
Figure 6: CubeSat General Testing Flow Diagram
Note: CubeSat test flows will vary from mission to mission. The Launch Provider will provide the
CubeSat Developer with the approved test flow for a specific mission.
4. CubeSat Dispenser
4.1 Interface
The CubeSat dispenser is designed to carry CubeSats, and serve as the interface between the
CubeSat and LV. A payload from the dispenser viewpoint may be a single CubeSat that makes use
of the dispenser’s total volume, or a combination of multiple CubeSats that amount to the
dispenser’s full capacity.
Multiple companies are developing dispensers which all adhere to one of two standardized
constraint systems. The first system, originally developed by CPCL for the Poly Picosatellite
Orbital Deployer (P-POD), utilizes a rail design. The second system, developed by Planetary
Systems Corporation (PSC), utilizes a tab design and employ a constraint mechanism, CSD flange,
that clamps onto these tabs, which creates a stiff invariant load path when integrated.
In both cases, the deployment force is provided by a spring driving the internal pusher plate. The
pusher plate, in turn, interfaces with the CubeSat, which glides along the dispenser rails as it is
ejected into orbit. Mechanical requirements for the CubeSat rail system are outlined in Section 2.2,
and the mechanical requirements for tabbed CubeSats can be found at planetarysystemcorp.com.
Developers are encouraged to explore both options to determine which is optimal for their needs.
Due to the mechanical differences in dispenser designs, CubeSats are not expected to be compatible
with both types of dispenser. To ensure safety and success of the mission, CubeSats will be
compatible with either the rail system or the tab system dispensers by meeting the applicable
requirements outlined in this document or the PSC website.
CubeSat Design Specification Rev. 14.1
The CubeSat Program, Cal Poly SLO
19
Rail Pairs (x4)
Pusher Plate
Access Port
Figure 7: Poly Picosatellite Orbital Deployer (P-POD) and cross section utilizing the rail system
Figure 8: Planetary Systems Corporation (PSC) 3U Dispenser and detail utilizing the tab system
(image credit PSC)
Figure 9: An Example of a 3U Rail-based Dispenser designed by ISIS (ISIPOD)
CubeSat Design Specification Rev. 14.1
The CubeSat Program, Cal Poly SLO
20
Figure 10: (Left) 6U Dispenser designed by Planetary Systems Corporation (CDS, tab-based) and
(Right) 6U Dispenser designed by Tyvak (NLAS, rail-based)
Figure 11: One Example of 12U Rail-based Dispenser designed by AstroFein (PSL-P)
5. Dispenser Options
Dispenser specific options are available to support specific CubeSat mission requirements. Please
contact the dispenser provider for details about any options prior to incorporating them into your
CubeSat design. A summary of the dispenser capabilities is presented in Table 3. For further details,
consult the dispenser developer website as provided in Table 4.
Keep in mind that designing a spacecraft to a specific feature that is not available in all dispensers
will restrict the spacecraft’s ability to qualify for launch opportunities.
To request another dispenser be added to the next revision of this document, please contact the Cal
Poly CubeSat Laboratory at cubesat@calpoly.edu.
CubeSat Design Specification Rev. 14.1
The CubeSat Program, Cal Poly SLO
21
Table 3: CubeSat Dispenser Options
Max
Access Ports
Additional Mass
Extended Body Length
Extended Protrusions
Power/ Data Port
Purge
RF Insulation
Vibration
Attenuation
Constraint
Constraint
-Z Additional Volume
(Tuna Can)
Type
Volume
PSL
Astro-Fein Rail 3U X X X
PLS-P
Astro-Fein Rail 12U X X X
P-POD
Cal Poly Rail 3U X X COSPOD
COSATS Rail 12U X X X X-Y
Z
X X X X X X
X X X
EXOpod
Exolaunch Rail 12U X X X X X X
ISIPOD
ISIS Rail 3U X X X X X
6-POD
ISIS Rail 6U X X X X X
QuadPack
ISIS Rail 12U X X X X X X
E-SSOD
JAXA Rail 3U X X
J-SSOD
JAXA Rail 3U, 6U X 6U X
CSD
Planetary
Systems
Tab 3U, 6U,
12U X X X X X
RailPOD
Tyvak Rail 3U NLAS
Tyvak Rail 6U X X X X X X X X X
X X X X X X X X X X
12U Dispenser
Tyvak Rail 12U RAMI
UARX Rail 12U X X X X X X X X
X X
Note: If a dispenser provider would like to update, revise, or add information to Table 3, please
contact the Cal Poly CubeSat Laboratory, cubesat@calpoly.edu.
CubeSat Design Specification Rev. 14.1
The CubeSat Program, Cal Poly SLO
22
Table 4. Capabilities Description of the Available Dispensers
Access Ports Additional Mass Extended Body
Length
Extended
Protrusions from
Body
Power/Data Port Gaseous Purge X-Y Constraint Z Constraint -Z Additional
Volume
Access ports are used to physically access the satellite while the CubeSat is
integrated within the 6U dispenser. The access ports allow the RBF pins to be
removed post-integration into a 6U dispenser, and they can be used to visually
verify separation switch engagement after the CubeSat has been integrated.
Some dispensers have been designed to accommodate a larger payload mass than
this document specifies. Please refer to the dispenser website for specific mass
limits. The mass limits of a dispenser are dependent on the dynamic environments
of a launch.
Some dispensers have been designed to accommodate a longer overall 3U body
length in the Z direction. Please refer to the dispenser website for specific length
limits.
Some dispensers have been designed to accommodate longer protrusions on the
CubeSat X and Y surfaces than the 6.5mm that is specified in this document.
Please refer to the dispenser website for specific protrusion limits. PSC utilizes a
dynamic envelope and does not require rails. Therefore, it does not have
“protrusions”.
This option allows the CubeSat to electrically interface with the dispenser while
integrated. For specific information regarding power-on capabilities, please refer
to the dispenser website.
This option allows the dispenser to be configured for gaseous purge throughout
launch. For specific information regarding purge capabilities, please refer to the
dispenser website.
PSC utilizes long flat tabs, in lieu of rails, to which the dispenser applies a
clamping pre-load. This constrains the CubeSat while integrated in the dispenser.
CubeSats designed to a tab system specification may not be compatible with a
rail-based 6U dispenser, and visa-versa.
The ISIS 6-POD dispenser and Tyvak 12U dispenser employ constraint systems
that are compatible with the rail design.
Please see the dispenser website for a full list of mechanical requirements
associated with each constraint system.
All current dispensers fully constrain the payload in the Z axis.
This option offers a cylindrical volume extension on the –Z face of the CubeSat
(also known as the “Tuna Can”). It is usually only offered to 3U, 6U, or 12U
CubeSats that won’t be sharing dispenser space with other CubeSats, but smaller
U configurations may Contact the dispenser developer for further details.
CubeSat Design Specification Rev. 14.1
The CubeSat Program, Cal Poly SLO
23
Table 5. Dispenser Developer Websites
Company or Institution Website
Astro-Fein http://www.astrofein.com/
Cal Poly CubeSat Laboratory http://www.cubesat.org/
COSATS cosatspace.com
Exolaunch www.exolaunch.com
ISIS www.isispace.nl
JAXA https://global.jaxa.jp/projects/rockets/epsilon/
Planetary Systems www.planetarysystemscorp.com
Tyvak www.tyvak.com
UARX www.uarx.com
6. Contacts
Cal Poly CubeSat Lab Director
Prof. John Bellardo
Aerospace Engineering Dept.
(805) 756-5087
bellardo@calpoly.edu
Cal Poly CubeSat Program Manager
Ryan Nugent
(805) 756-5087
rnugent@calpoly.edu
Cal Poly CubeSat Lab
(805) 756-5087
cubesat@calpoly.edu
CubeSat Design Specification Rev. 14
The CubeSat Program, Cal Poly SLO
24
Appendix A:
Change History Log
Effective
Date Revision Author Description of Changes
N/A 8 Simon Lee N/A
5/26/05 8.1 Amy Hutputanasin Formatting updated.
5/15/06 9 Armen Toorian Information and presentation revised.
8/2/07 10 Wenschel Lan Information updated.
10/02/08 11 Riki Munakata Format, Design specification and Mk.III P-POD compatibility
update.
8/1/09 12 Riki Munakata Requirements update, waiver form requirements, and 3U CubeSat
Specification drawing.
3/30/12 12.1 Justin Carnahan Reformatted document to improve readability, updated to include
1.5U, 2U, and 3U+. Added and modified some req.
7/12/13 13-draft David Pignatelli
Added applicable documents section. Removed restrictions on
propulsion, added guidance for propulsion systems and hazardous
materials. Added magnetic field restrictions and suggestions.
Cleaned Section 3.2. Added custom spring plunger specs and
recommendation. Extended restrictions on inhibits. Added links to
outside resources. Cleaned Section 4.
2/20/14 13 Arash Mehrparvar
Fixed page numbering, error in spring plunger thread callout, other
minor edits based on external suggestions. Update 6-April-2015:
1.5U length req. was 170.25 +/-0.1 revised to 170.2 +/-0.1 (p. 25);
2U length req. tolerance was +/-0.1 revised to +/-0.2 (p. 27); 3U
length req. tolerance was +/-0.1 revised to +/-0.3 (p. 29 and p. 31);
1U CAC mass spec was 1.0 +0.5/-0.2 kg revised to < 1.33kg (p. 34);
1U CAC length spec was 113.5 +/-0.5mm revised to 113.5+/-0.1mm
(p. 34); 1.5U CAC mass spec was 1.5 +0.7/-0.3kg revised to <
2.00kg (p. 36); 1.5U CAC length spec was 170.2 +/-0.7mm revised
to 170.2 +/-0.1mm (p. 36); 2U CAC mass spec was 2.0 +0.7/-0.4kg
revised to < 2.66kg (p. 38); 2U CAC length spec was 227.0 +/-
0.1mm revised to 227.0 +/-0.2mm (p. 38); 3U and 3U+ CAC mass
spec was < 4kg revised to < 4.00kg (p. 40 and 42); 3U and 3U+
CAC length spec was 340.5 +/-1.5mm revised to 340.5 +/-0.3mm (p.
40 and 42). All drawing dates were updated to 02/20/14. Update 14-
Oct-2016: Added Update 6-April-2015 to change log
July
2020
14 Alicia Johnstone
CubeSat Design Specification Rev. 14
The CubeSat Program, Cal Poly SLO
25
Added 6U and 12U specifications. Title page: removed ITAR and Internal classification options. Update logo. Detailed
change log moved to Appendix A. Page2: document update summary added. Add appendices to ToC. List of Acronyms
updated and changed to List of Acronyms and Abbreviations. Applicable Documents updated to most recent revisions
and MIL-HDBK-5 was removed. Introduction Section text updated to include 6U and 12U, and improve language.
Figure 1 caption added detail to the description. Waiver Process section removed. Added Mission Requirements section.
Added Non-compliance with CDS section. Added Definitions and Definition of Terms sections. P-POD and Interface
sections removed.
CubeSat Specifications section was 3, is 2. Req 3.1.1 removed and all following req #’s adjusted accordingly.
General Specifications: Section renamed from Requirements to Specifications. Req(Spec) 3.1.2 (2.1.1) removed “No
additional space debris will be created.” Req(Spec) 3.1.3 (2.1.2) revised to reference AFSPCMAN 91-710 and remove
pyrotechnics prohibition. Req(Spec) 3.1.4 (2.1.5) revised to a Note and language changed to guideline referencing FAA
battery requirements. Req(Spec) 3.1.9 and 3.1.9.1 removed. Req(Spec) 3.1.10 (2.1.8) revised from Note to “shall” and
language revised. Req(Spec) 3.1.11 (2.1.9) specification was inches, is now meters and inches conversion.
Mechanical Specifications: P-POD image removed. Tab configured dispenser statement added. Req(Spec) 3.2.1(2.2.1)
removed reference to P-POD. Req(Spec) 3.2.1.2(2.2.1.2) included additional relevant U configurations. Req(Spec)
3.2.2(2.2.2) P-POD reference replaced with dispenser. Req(Spec) 3.2.3(2.2.3) reference to green shaded areas on
Appendix drawings removed. Req(Spec) 3.2.3.1(2.2.3.1) CAC reference changed to CIFP. Req(Spec) 3.2.4(2.2.4) P-
POD reference replaced with dispenser. Req(Spec) 3.2.5 (2.2.5) Measurement described in greater detail. Spec 2.2.5.1
added, image added. Req(Spec) 3.2.6(2.2.6) Will changed to should. Spec 2.2.6.1 note added. Req(Spec) 3.2.7(2.2.7)
Will changed to should. Spec 2.2.7.1 note added. Req(Spec) 3.2.8(2.2.8) Figure 6 reference replaced with Appendix B
reference. Spec 2.2.8.1 note added. Req(Spec) 3.2.9(2.2.9) Will changed to should and P-POD reference removed. Req
3.2.10 through 3.2.13.1 replaced with Spec 2.2.10, 2.2.10.1, and 2.2.10.2 and Table 1. Req 3.2.14 through 3.2.14.4
replaced with Spec 2.2.11and Table 2. Req(Spec) 3.2.15(2.2.12) and 3.2.15.1(2.2.12.1) will changed to should and Note.
Req(Spec) 3.2.16(2.2.13) updated language. Req(Spec) 3.2.17(2.2.14) replaced “separation spring” with “mechanism to
encourage separation”. Req(Spec) 3.2.17.1(2.2.14.1) Cal Poly custom separation springs replaced with general
separation mechanism and guidance for separation mechanism design added. Req(Spec) 3.2.17.2(2.2.14.2) separation
spring replaced with separation mechanism and language updated. Req(Spec) 3.2.17.3(2.2.14.3) will replaced with Note
and separation spring replaced with separation mechanism. Req(Spec) 3.2.17.4(2.2.14.4) revised to a Note, language
updated, and separation spring replaced with separation mechanism. Table1: CubeSat Separation Spring Characteristics
and Figure 5: Custom Spec Spring Plunger (Separation Spring) removed. Figure 7 (Figure 5) Separation Spring replaced
with Separation Mechanism. Figure 6 (Figure 3) updated.
Electrical Specifications: Req(Spec) 3.3.1(2.3.1) language updated. Spec 2.3.1.1 and 2.3.1.2 added. Req(Spec)
3.3.2(2.3.2) updated language and remove Figure 7 reference. Req(Spec) 3.3.3(2.3.2.1) updated language. Req(Spec)
3.3.4(2.3.2.2) P-POD changed to dispenser. Req(Spec) 3.3.4.1(2.3.2.3) will changed to should and language updated.
Req(Spec) 3.3.5(2.3.2.4) language updated. Spec 2.3.3 and 2.3.3.1-2.3.3.3 RTC specification added. Req(Spec)
3.3.6(2.3.4) language updated. Req(Spec) 3.3.6.1(2.3.4.1) language updated. Req(Spec) 3.3.7(2.3.5) language updated.
Req 3.3.7.1-3.3.7.3 replaced by Spec 2.3.5.1-2.3.5.2. Req(Spec) 3.3.8(2.3.6) language updated. Req 3.3.9, 3.3.9.1, and
3.3.9.2 replaced with Spec 2.3.7 and 2.3.7.1-2.3.7.3. Spec 2.3.8 added.
Operational Specifications: Req(Spec) 3.4.1(2.4.1) will changed to shall. Req(Spec) 3.4.1.1(2.4.1.1) revised to Note.
Req(Spec) 3.4.2(2.4.2) will changed to shall. Spec 2.4.2.1 added. Req(Spec) 3.4.3.2(2.4.3.2) will changed to should. Req
3.4.2.1 removed. Spec 2.4.3.4 added. Req(Spec) 3.4.4(2.4.4) P-POD reference removed. Req(Spec) 3.4.5(2.4.5) language
updated. Spec 2.4.5.1 added. Req(Spec) 3.4.6(2.4.6) language updated and revised to Note. Req(Spec) 3.4.7(2.4.7)
language updated, Cal Poly and P-POD specific language removed. Spec 2.4.7.1 added.
Testing Requirements: Updated language and updated standards sources. Req(Spec) 4.1(3.1.1) language updated. Req
4.2 replaced with Specs 3.2.1-3.2.2. Req 4.3 replaced by 3.3.1. Spec 3.3.1.1 added. Req(Spec) 4.4(3.4.1) replace CAC
with CIFP. Req(Spec) 4.5(3.5) language updated. Req(Spec) 4.5.1-4.5.3(3.5.1-3.5.3) language updated. Figure 8(Figure
6) Note added.
CubeSat Dispenser: section added.
Dispenser Options: section added.
Contacts: Points of contact updated.
Appendix A: Waiver form removed and Change History Log details added.
Appendix B: Added 6U and 12U drawings; replaced 3U+ drawing with U+ drawing.
Appendix C: section removed.
CubeSat Design Specification Rev. 14
The CubeSat Program, Cal Poly SLO
26
February
2022
14.1 Alicia Johnstone
Added PSL-P to List of Acronyms. Added Notes 2.2.1.2 and 3.5.2.1
to clarify the preceding specification. Updated Figure 11. Updated
Tables 3 and 5.
Drawing Revision History (Appendix B)
March
2020 14 Alicia Johnstone
1U: removed P-POD access port locations; removed coordinate
systems; added X/YZ face identifier flags; updated ADDITIONAL
NOTES section; added Detail B; updated dim D5/6 to ref. range and
MIN note; remove radius dim Detail A; removed dims 8.5 MIN
E/F2; updated DWG number for rev14; added REVISION
HISTORY note
1.5U: removed coordinate systems; added X/YZ face identifier flags;
updated ADDITIONAL NOTES section; added Detail B; updated
dim D5/6 to ref. range and MIN note; remove radius dim Detail A;
removed dims 8.5 MIN E/F2; updated DWG number for rev14;
added REVISION HISTORY note
2U: same as 1U
3U: removed P-POD access port locations; removed coordinate
systems; added X/YZ face identifier flags; updated ADDITIONAL
NOTES section; added Detail B; updated dims D5 & D8 to ref.
range and MIN note; remove radius dim Detail A; removed dims 8.5
MIN E/F2; updated DWG number for rev14; added REVISION
HISTORY note
3U+: removed
U+: added
6U: new for CDS rev 14, previously published in 6U CDS as 6U
RAIL CUBESAT rev 1.0; added Detail A and Detail B; removed
coordinate systems; added X/YZ face identifier flags; updated
ADDITIONAL NOTES section; DWG number updated for CDS rev
14; dims in E3 and E4 removed, replaced in Detail B; added ref dim
to D7/8; replaced views -Z and -X faces to +X and -Z faces
12U: new for CDS rev 14
CubeSat Design Specification Rev. 14
The CubeSat Program, Cal Poly SLO
27
Appendix B:
1U, 1.5U, 2U, 3U, U+, 6U, and 12U
CubeSat Specification Drawings
CubeSat Design Specification Rev. 14
The CubeSat Program, Cal Poly SLO
28
CubeSat Design Specification Rev. 14
The CubeSat Program, Cal Poly SLO
29
CubeSat Design Specification Rev. 14
The CubeSat Program, Cal Poly SLO
30
CubeSat Design Specification Rev. 14
The CubeSat Program, Cal Poly SLO
31
CubeSat Design Specification Rev. 14
The CubeSat Program, Cal Poly SLO
32
CubeSat Design Specification Rev. 14
The CubeSat Program, Cal Poly SLO
33
CubeSat Design Specification Rev. 14
The CubeSat Program, Cal Poly SLO
34