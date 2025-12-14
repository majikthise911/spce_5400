UCCS DemoSat
AMERGINT Technologies
Alondra Hauser, Edward Lundberg, Ian Heinrich, Isaac Remington, Lauren Uebel, Maxwell Albrecht
UCCS Senior Design Final Report
MAE 4511, ECE 4898,
April 25, 2023
Executive Summary ...................................................................................................................... 3
Introduction ................................................................................................................................... 4
Objective .................................................................................................................................... 4
Problem Statement .................................................................................................................... 4
Project Planning and Management ......................................................................................... 5
Problem Specifications ................................................................................................................. 6
Project Requirements ............................................................................................................... 6
Communications Requirements List: ................................................................................. 6
Power Requirements List: .................................................................................................... 6
Telemetry and Control Requirements List: ........................................................................ 7
Mechanical Requirements List: ........................................................................................... 7
Thermal Requirements List: ................................................................................................ 7
Conceptual Design ........................................................................................................................ 8
Missions ...................................................................................................................................... 8
Electrical .................................................................................................................................. 10
Structure .................................................................................................................................. 13
Electrical Testing Methods and Results ................................................................................ 16
Structural Testing Methods and Results ............................................................................... 21
Final Design ................................................................................................................................. 25
1
Mission ..................................................................................................................................... 25
Electrical .................................................................................................................................. 25
Structure .................................................................................................................................. 29
Concept of Operations ............................................................................................................ 34
System Block Definitions Diagram ........................................................................................ 35
Flight Results ............................................................................................................................... 38
Conclusion ................................................................................................................................... 42
Sponsor Interactions ................................................................................................................... 43
Team Interactions ....................................................................................................................... 43
Appendices ................................................................................................................................... 44
Appendix A – SOLIDWORKS Drawings ............................................................................. 44
Appendix B – Complete System Circuit ............................................................................... 55
Appendix C – Requirements and Verification ...................................................................... 56
Appendix D– Management..................................................................................................... 60
2
Executive Summary
_____________________________________________________________________________
The goal for project CubeSat was to evaluate a low power data link from an edge of space payload
with the help of AMERGINT Technologies. The project was based off the DemoSat program
through Colorado Space Grant Consortium criteria which lays out the basic requirements for the
size and weight of the structure, what type of sensors and data it will need to collect, as well as a
personal mission. The mission selected for the UCCS payload was to demonstrate communications
throughout the entire flight.
There were three design processes for the project that are covered in the report: the mission for the
payload, a mechanical portion that was responsible for the structure and the mounting components,
and an electrical portion that was responsible for all the hardware and software. It started out with
9 different missions that were filtered down to a low power communications demonstration. The
structure had gone through three distinctive design changes starting out with a 3d printed CubeSat
design but after testing eventually got a change for a foam core structure. The electrical
components had a similar design process, with several possible communications and computer
systems examined before a final decision was made.
The structure was designed to be a 150mm cube made all out of foam core that had 45-degree
corners to have proper adhesion with itself. The process of deciding the structure with other
CubeSat but during every test the structure would break under its own weight, eventually a solid
foam core structure was the best design because there wasn’t a worry to add any insulation as the
foam already is a good insulator and is nonconductive so there would be no interference with the
electrical components.
The design for the electrical portion was contingent on which type of mission was decided. The
chosen mission, a communications demonstration, was accomplished using two systems: an
automatic Very High Frequency (VHF) transmit-only beacon, and a half-duplex data link utilizing
an off the shelf (OTS) transceiver chip at Ultra High Frequency (UHF). A mixture of open-source
and custom written software was included to control these systems.
Flight operations conducted on 1 APR concluded with complete mission success. During a flight
that reached over 105,000 feet in altitude, the payload continuously received and sent data to a
mobile ground station. Data consisted of in-flight telemetry from onboard sensors, outbound
message traffic to an external station, and photos from an onboard camera. Primary datalink was
accomplished using the UHF link. VHF signals from the beacon were successfully received shortly
after takeoff and after landing. The payload was recovered after the 2 hour and 18-minute flight
fully intact, powered on, and capable of transmitting.
3
Introduction
Objective
The Primary objective of this project was to design, test, and manufacture a DemoSat which will
be launched attached to a high-altitude weather balloon as part of the COSGC DemoSat Design
Challenge program on April 1st, 2023. This DemoSat is intended to demonstrate communication
throughout the entire flight so that the aspirations of communication that AMERGINT has are
encompassed. By having a successful flight, the feasibility of low-cost, low-weight
communications payload in satellites can be further developed.
The secondary objective of this project is to create interest in utilizing the CubeSat designed for
the DemoSat Design Challenge program as demonstration units for future students within the
newly founded Aerospace Engineering program at UCCS. The purpose for this is to generate
interest for CubeSat programs among students who are just beginning their academic career at
UCCS.
Problem Statement
CubeSat are small satellites that can allow automatic collection of data for a bigger objective.
Colorado is one of the best locations where the aerospace industry conducts business. That is why
CU boulder is the number one launcher of CubeSats in the country. The University of Colorado in
Colorado Springs is seeking to be part of that exciting field and have a CubeSat on orbit. This
project is an investigation of the communications system and the automation of telemetry relay
from edge of space payload. The low power data links in this investigation should provide us with
a basis for a more complex system for the future of a CubeSat program at this institution.
4
Project Planning and Management
The project was planned during the senior seminar portion and executed in the senior design
semester. The senior seminar timeline of August 22, 2022- December 17, 2022, allowed for five
students to research and select experimentation for the payload. By gathering all the requirements
from sponsors (AMERGINT) and launch provider (CSGC) the team was able to evaluate any
obstacles that might arise in implementation. The team also evaluated an agile technique to pass
down specific tasks for team members using Jira as a host. In this preliminary phase of the project,
the main concern was dealing with FCC rules for communicating at certain frequencies. The team
quickly learned that the operations from the launch provider were more complex and needed to
collaborate with the recovery team at Edge of Space Sciences (EOSS) to coordinate radio
communications. By the end of the semester the team had two additional members. A master
student that is an experienced HAM radio operator to mitigate with FCC rules.
The project was divided into three phases from January 17, 2023-May 13, 2023, to ensure the
deadlines were met for Colorado Space Grant Consortium where met. A preliminary design review
(PDR), a conceptual design review (CDR), and a final readiness review (FRR) presentations of the
project process had to be presented to be able to launch. The team divided these deadlines that
worked in phases.
Phase 1: Design/Execute – To design structure, calibrate and learn electrical components selected
for system. Mitigate and anticipate problems with materials, power budget, link budget
estimations.
Phase 2: Testing/Validation- To learn about structural deficiencies and strong points by rapid
prototyping. Integrating sensors and validating links to main board and increase complexity in
automation of system. To evaluate communication links (both downlink and uplink) to mitigate
protocol problems with EOSS.
Phase 3: Integration/Verification: To do a complete system integration and verify that all
specifications placed by sponsors and space grant were followed.
Project planning was easy to implement to meet clear deadlines placed by Space Grant. It was an
effective way to guide teams to success. Gantt charts made for this project are in the appendix.
The management part of this project was mentored by the sponsors (AMERGINT). The budget
provided by the sponsor was $2500, which the team was able to stay under. Meetings with sponsors
were done every week and every two weeks close to launch day (April 1st, 2023).
This team was an interdisciplinary effort which gave some difficulties with scheduling and many
assignments and due dates coming from different departments. The mechanical engineering
department is excellent in showcasing documentation compared to the electrical engineering and
DASE curriculum. It would benefit everyone to combine the senior seminar and senior design
classes to create a pipeline of information and responsibility sharing.
5
Problem Specifications
Project Requirements
The communications requirements were derived from a combination of COSGC DemoSat
requirements, FCC regulations, and sponsor developed constraints. Some major driving
requirements that contributed to the final design of the DemoSat were COM-1,2,7 and 8. These
requirements helped to shape how the payload would function as it relayed information and data
between itself and the ground station. Other major requirements such as COM-6 played key roles
in the logistics of the launch day, ensuring all regulations and safety measures were met.
Communications Requirements List:
COM-1: Communication systems shall have uplink capability.
COM-2: The telecom system shall be capable of supporting a data volume of 1200bps.
COM-3: Antennas shall not interfere with sensors.
COM-4: System transmission power shall remain within limits of power budget allocation.
COM-5: The communications subsystem shall be compliant with restrictions set by the FCC.
COM-6: The payload shall implement its own unique satellite ID in the telemetry downstream.
COM-7: The EIRP (Effective Isotropic Radiated Power) limits.
COM-8: The communications subsystem shall be capable of interfacing with ground station
operations and support 1200bps.
COM-9: Communications Subsystem shall be able to function in simulated environment.
The power sub-system requirements were all derived from the needs of the hardware for the
payload to function. POW-1 is responsible for determining how much power is needed for the
overall system. Pow-2 and Pow-3 are then implemented to reduce risk in power drops and surges.
Power Requirements List:
POW-1: Power sub-system shall supply sufficient current to all other systems at a minimum of 5
V DC.
POW-2: Power sub-system shall provide sufficient voltage regulation from variable power
source (Batteries).
POW-3: Power sub-system shall include overcurrent and overvoltage protection.
6
The telemetry and control sub-system requirements help to dictate how the process of data
collection and transmission within the payload is executed. In Tel-1 and Tel-4, it talks about where
the data is being collected from and how/when it should be downlinked. In Con-1, it talks about
how to facilitation of the data is managed throughout the payload.
Telemetry and Control Requirements List:
TEL-1: Data collected from sensors package shall be downlinked every 5 minutes.
TEL-2: Telemetry data collected shall be exported to the memory in a readable configuration.
TEL-3: Telemetry data shall be stored locally as back-up in case of failure.
TEL-4: Telemetry data shall consist of 9-axis position data, current reading, internal temperature,
external temperature.
CON-1: The control System shall manage telemetry and comms integration by implementing a
data down-link algorithm.
The mechanical sub-system requirements focus on ensuring that the payload structure does not
compromise any other system and in turn, no other system impedes the structure. In addition to
protecting the payload, requirements such as ME-1 were required by balloon launch personnel to
ensure a safe launch and flight. These launch constraints determined what the mechanical structure
looked like and behaved like under the flight environment.
Mechanical Requirements List:
ME-1: Total system shall weigh 800 g or less.
ME-2: Frame shall maintain functional integrity at –40 C.
ME-3: Frame shall protect and ensure functional integrity after impact tests.
ME-4: Frame shall ensure functional integrity after jerk test.
The thermal sub-system requirements were based off the flight environment that the payload was
exposed to during the mission. The main environmental factor that derived these requirements was
temperature change. The batteries on board the payload began to lose power when they reached –
40 degrees Celsius so TH-1,2, and 3 were created to help retain heat.
Thermal Requirements List:
TH-1: Batteries maintained between operational temperatures.
TH-2: Batteries maintained between non-operational temperatures.
TH-3: Electrical components maintained between operational temperatures.
A more detailed description and verification method for all requirements can be found in
appendix C.
7
Conceptual Design
Missions
A variety of mission concepts were evaluated for this payload. The mission is crucial in
determining how the payload will function, what components will be needed, and how large the
payload needs to be.
Mission Concept 1: Cybersecurity Communication Test
This mission concept involves utilizing homo-morphic encryption of images as a cybersecurity
communication demonstration. This encryption requires the people with clearances (allowed) to
have access in a way of a key with no decryption needed. This would allow for this experiment to
use little computing power. This concept would demonstrate secure data transmission and would
be cost effective. The concept was well investigated but would require more expertise from the
team.
Mission Concept 2: Telemetry and Communications Demonstration
Sends live telemetry data of the payload regarding altitude, acceleration, temperature, pressure,
spin rate, moisture, and images.To demonstrates communication throughout entire flight, easy
to produce, cost effective, compact, and lightweight. The downside to this concept was that it does
not generate any majorly useful data for future experimentation.
Mission Concept 4: Lunar Dust experiment using Carbon Nanotubes
To design an experiment that would evaluate lunar dust using carbon nanotubes to repel the
electrostatic properties of carbon nanotubes. The experiment would also allow for analyzing the
behavior of lunar dust at 120,000 feet. One of the most complex concepts for an investigation is
that would last only one semester. It was voted to be one of the most complex concepts due to the
time and effort designing a control system that would allow the team to operate during harsh
environmental conditions.
Mission Concept 5: Autonomous Robotic Communication and Performance
Allows for control of a robot on the ground from a signal sent from the Payload. Signals will be
sending a robot on the ground to activate a command. The robot on the ground would then relay a
signal to confirm the operation performed. This concept would highlight a communication system
protocol for autonomous vehicles on other planets. Timeline would not permit a complex
communication system. However, this was one of the lightest options for the payload and it
generates useful data for future experimentation. Some of other difficulties with this concept was
that it may be exceedingly difficult to maintain communication throughout the flight, requires an
additional robot in addition to the payload, and difficult to accurately give GPS guided
instructions, along with doppler effected of communication downlink and uplink.
8
Mission Concept 6: Flash Lidar
Using flash lidar to map the trajectory of the flight and analyze ground statistics. Effective flash
lidar requires a high-power budget and is mostly heavy. The topological trajectory path of the high-
altitude balloon does not highlight enough ground points that the team can focus on or study. The
payload would require an attitude control system which would be complex to implement on a high-
altitude balloon. Overall, this concept would break one of the most important requirements, which
is weight.
Mission Concept 6: Stardust Collector
To take advantage of high altitude in Colorado, the team was proposing to investigate stardust
collection deposits in the area. Using aerogel and an opening closing mechanism, the team would
plan the automatic release of a valve to suck in the particles in the air. The aerogel would trap
particles collected to later examine them using an electron microscope. This concept offered the
most intense after flight investigation and requires students to learn how to operate, rent time with
electron microscope and know what they were looking for. Time wise this concept would take
dedication along the time of finals and reports due. The materials were not easily accessible and
costly.
Mission Concept 7: Deployable Radio Astronomy
In addition to the radio communication demonstration, the concept of a deployable radio
astronomy was proposed. The team quicky realized it would require an obnoxious antenna sticking
out of the payload and that the time of flight would be mostly in the day. It would also require an
attitude control system for accuracy of pointing. The components alone would break the weight
budget of 1kg. Being able to identify a celestial object by bouncing frequencies and pointing at
something in the sky sounds fascinating but the components and added complexity to the system
would not be a task to take within the amount of time given.
Mission Concept 8: Radiation protection
The mission of this concept was to evaluate varied materials or substances to measure the amount
of radiation penetrated or repelled by the material. This investigation was an often sought out one
by anyone interested in radiation. The problem with the specifications is that the payload would
only go to a max of 120,000 feet and the duration at that altitude would only be counted in minutes.
By cross-examining the investigations done in the past. The team concluded that the experiment
would not have enough exposure to have conclusive or relevant data.
Mission Concept 9: Solar Sails
Finally, solar sails to navigate a space craft have been proposed in the past. The payload would not
go to space and the payload would not be able to navigate using solar wind because it would not
be in outer space. Any solar sail device would have to be deployable which would disrupt the
balloon transition and possible other experiments on the string.
9
Electrical
A variety of electrical systems were investigated for this payload. Regardless of mission profile or
structural design, the internal electrical and computer systems must be capable of communicating
with the ground station (uplink and downlink), logging any sensor or other measured data during
the flight, and supplying power to all necessary components.
Main Computer
For the main computer, an Arduino-based development board, and two raspberry pi development
boards were considered. These options were initially chosen based on the wide range of compatible
software, ease of development, and availability.
The Arduino based system would be the cheapest and simplest option, as well as the most limited
of the suggested computers. The AtMEGA328p processor is not capable of running a full operating
system and would require a significant amount of software being written to handle both
communications and sensor control. This would be difficult to accomplish considering the limited
computational resources of the computer. The Arduino would, however, draw the least amount of
power and occupy the least amount of space in the structure.
The raspberry pi options were to use a full-size pi 4 b+, or a pi zero W. Both options can run a full
operating system, have large aftermarket support, and are readily available. The full-size pi 4 has
the greatest computational resources of the three options by a significant margin. The pi 4 has a
large amount of I/O, making development and writing software even easier than the other options.
This is also the most expensive choice, as well as taking up the most space in the structure and
requiring the largest amount of power. The pi zero W represents a middle ground, having decent
computational power while still requiring less power and space than the pi 4. The pi zero W is
priced in between the 4 and the Arduino.
Sensor Package
Additional sensors beyond the primary payload should be included to provide additional context
to the data from the primary payload. Numerous OTS sensors, both analog and digital, are cheap,
readily available, and simple to integrate with the above computer systems. Data sources initially
suggested are listed below:
• Temperature probes (internal, external, per-component)
• Gyroscopes (attitude, multi-axis acceleration, positional magnetometer)
• Pressure Altimeters
• Humidity sensors
• Visible-Light and infrared cameras
• Gas transducers (O2, CO2, CO)
10
Communications
Current FCC regulations regarding the use of certain RF bands at the power levels required for bi-
directional communications at the expected distances limits the legal options for communications
systems; consequently, all suggested solutions were within the hobbyist ham radio domain.
Specifically, three packet ham radio systems were investigated.
APRS (Automatic Packet Reporting System), a community-driven network of receivers and
transmitters, was initially investigated. This system would allow for a network of ground stations
to be able to send, receive, and forward data packets to and from the payload on the 144 MHz
band. Operating using the AX.25 specification at the data-link layer, integrated with the
community stations to provide a higher network layer and integration with the wider internet. This
solution would be simple and cost-effective to implement, owing to the large amount of hardware
and software available to implement APRS capability. A key limitation with APRS is the limited
frequency of transmissions. 144.39MHz is a busy channel, and especially at high altitude and
transmit power could become congested with other traffic. A transmission interval of not less than
5 minutes was recommended by the launch provider, significantly limiting the effective throughput
of the system.
A SDR (software defined radio) implementation was also initially suggested. This solution would
entail a custom point-to-point SDR system developed using an open-source SDR package such as
GNU radio. This would allow for precise fine-tuning of transmission parameters to provide the
maximum possible throughput and minimum power draw. This solution would be the most work
intensive, requiring an extensive test and development cycle potentially beyond what was available
during the project. This would require virtually all software to be custom-built and integrated with
a variety of external hardware. Integration with a higher-level network protocol (such as TCP/IP)
would further increase the development overhead. The SDR would require a substantial number
of computational resources to implement.
The final communications system investigated was to integrate an OTS transceiver chip out of a
hobbyist VHF/UHF radio with an existing software modem, such as DIREWOLF. This solution
would be significantly cheaper than, but potentially more difficult to implement than the APRS
solution. It would, however, provide some significant advantages. DIREWOLF implements AX.25
v2.2, which includes forward error correction. The carrier frequency could be set to a less-
congested band, allowing for more frequent transmissions. While this would be a point-to-point
system, a network layer could be easily integrated with DIREWOLF, allowing for more complex
downlinked data.
Onboard hardware was contingent on which of the above systems were implemented. Each system
would at minimum require an antenna. Due to internal space constraints, two types of external
antenna were considered: J-pole and a ¼ wave dipole. The dipole antenna would take up much
less space than the J-pole (especially when tuned for UHF frequencies) but has an undesirable
horizontal radiation pattern and horizontal polarization, making transmission reception more
difficult. The J-pole has a better radiation pattern and (when dangling from the payload) has a
vertical polarization. For the ground station, a high-gain antenna such as a Yagi was found to be
desirable, with manual and self-tracking solutions investigated. Packet radio traffic could then be
received using another ham VHF/UHF receiver, with packets being decoded by an additional
computer running DIREWOLF.
11
Power System
The primary power source for a payload such as the one described here is stored battery power. A
variety of energy storage technologies were researched, including Lithium-ion, lithium-polymer,
and disposable alkaline batteries. For the case of rechargeable batteries, the usage of a PV
(Photovoltaic) system was investigated. This would reduce both the mass and dimensional
footprint of the required energy storage but entail a more complex onboard balance charging
system, as well as external PV panels.
Power regulation could be done either via DC-DC switching converters, or linear regulators. DC-
DC converters are much more efficient and generate less heat but occupy more space and are less
physically robust compared to linear regulators. Protective elements such as relays, fuses, and a
physical on/off switch were also investigated as suggested by the launch provider.
12
Structure
A variety of different structure designs were investigated for this payload. Regardless of the
mission chosen, it is crucial that the structure can hold and protect the internal components,
surviving landing and other flight scenarios, preventing water from reaching the interior, being
lightweight, and being easily replicable.
Design Concept 1: 3D Printed Design
When deciding what structure to use for this project, many unique designs were considered. The
first design was a 3D printer structure which can be seen in Figure 5 below. When evaluating this
structure, PETG were used. In the design there are four pillars that stick out on both the top and
the bottom. These pillars were intended to function as crumple zones and absorb some of the
impact from landing before it was transferred to the remainder of the structure. This design would
also allow for extremely easy modifications to be made and allow for extremely easy replication
as it would just need to be reprinted for extra structures. However, there were two significant issues
with this structure. The first was that each wall of the structure was held together with screws
which caused large stress concentrations. The second was that this structure was not waterproof or
insulated and would require extra material to be layered around the structure to achieve the desired
insulation and waterproofing.
Figure 1: 3D Printed Structure Design
13
Design Concept 2: Foam Core and Plexiglass
Another design evaluated utilized a combination of foam core and plexiglass which can be seen in
Figure 6 below. In this design, the main enclosed area is made up of foam core walls with pillars
on each corner and a top and bottom made from laser cut plexiglass. These were held together
using hot glue that was rated for cold temperatures. This design allowed for a rigid interior area
which allowed for easy mounting of all internal components as well as the interior to be
waterproof. The foam core pillars were intended to function as crumple zones and absorb some of
the impact from landing before it was transferred to the plexiglass and interior components. This
design had two issues with it. The first was that it was time consuming to recreate as the plexiglass
needed to be laser cut. The second is that the plexiglass provided little insulation for the internal
components and would require another material to be layered on top to achieve the desired amount
of insulation.
Figure 2: Foam Core and Plexiglass Design
14
Design Concept 3: Foam Core Cube
The final design evaluated utilized ½ inch foam core with 45o cuts on every wall which can be
seen in Figure 7 below. In this design, the entire structure is made of foam core and utilizes hot
glue, rated for cold temperatures, to hold the walls together. This design allowed for a rigid interior
which allowed for components to be mounted relatively easily. This design also allowed for the
interior to be well insulated and waterproofed very easily. The large ½ inch thickness of the foam
core allowed for some impact to be absorbed before transferring the rest to the interior components.
This design was easily replicable with a 45o cutting tool being the only special tool needed for
manufacturing.
Figure 3: Foam Core Cube
15
Testing and Analysis Summary
A variety of tests were performed on electrical components that were planned to be used within
the payload. These tests are crucial to ensure that the electrical components used are working
properly and are capable of withstanding flight scenarios.
Electrical Testing Methods and Results
Sensor Integration & Calibration
An initial test of sensors to assess rudimentary functionality and calibration in a controlled
environment was conducted. The preliminary sensors identified as being mission critical were
connected to a preliminary computer system running simplified software. The complete test system
included a BME280 temperature/humidity/pressure alt. combination sensor, an INA219 current &
voltage sensor, and a raspberry pi zero W connected to bench power. The preliminary software
was run for approximately 5 seconds, generating 5 data points for each of the sensors (software
polling each sensor at 1 Hz and recording). The collected data was compiled in table 1.
Table 1. Results of Sensor Integration & Calibration
Instrument Measured Value
(Average of 5)
Actual Ambient
Conditions
BME280, Temperature 21.5855 C 20 C
BME280, Humidity 11.135 % ~ 10 %
BME280, Pressure
Altitude
1882.494 m 1889.76 m
INA219, RPI logic
voltage
3.291 V 3.3 V
DS18B20,
Temperature
20.9748 C 20 C
This test successfully verified that data could be reliably recorded and saved in a human-readable
format to the computer system. This test also verified that the sensor payload was calibrated to a
reasonable degree at low altitude (~6200 ft) and at room temperature.
16
Cold Testing, Electrical
A test of the preliminary sensors, computer system, and power system in significantly worse than
expected environmental conditions was conducted. This test was conducted simultaneously with
the initial structural cold test. The purpose of this test was to assess battery and electronic
component performance in adverse conditions.
The preliminary system consisted of the same BME280 and INA219 sensors, with the addition of
a ds18b20 temperature probe acting as an external temperature sensor. An early design of the
power system consisting of two 18650 li-ion cells and two DC-DC buck converters supplied power
to the sensors and a full-size raspberry pi running the same preliminary software as above. The
entire system was placed in an early design for the casing, powered on, and left in a -80° C freezer
for 2 hours.
Figure 4: Top: Early payload in freezer. Bottom left: Freezer test voltage. Bottom right: Freezer test internal and
external temperature.
At approximately 1 hour into the test, the temperature of the batteries dropped low enough to halt
their internal chemical reaction, causing the entire system to shut down. It was determined that,
while the payload did suffer a failure during the tests, this failure was under extreme conditions
significantly worse than expected during the flight. The system was able to log data for a full hour
before this failure, indicating that it will likely function for the entire flight duration. The only
major change to the design to come from this test was to improve the insulation capability of the
structure, with no significant alterations to the power system.
17
Spurious Transmission Evaluation
The OTS transceiver chip selected as a possible communications component, the DRA818,
generates significant harmonics and spurious transmissions. A test of the unfiltered transceiver,
and with two integrated lowpass filters was conducted.
Figure 5: Left: Transmission harmonics without filter. Right: With filter.
The test compared each filter individually, as well as cascaded, with the unfiltered transceiver.
Figure X shows the frequency response of the best suited filter configuration, a single LCFN-400+
low pass filter.
Initial 2C Verification
A test verifying the functionality of remote command & control was conducted. The test apparatus
consisted of a preliminary communications configuration consisting of an OTS transceiver and an
automated APRS beacon connected to a full-size raspberry pi. The pi was running preliminary
software consisting of a web server attached to a DIREWOLF modem allowing for on-demand
downlinks of example data and HTML content, as well as start/stop commands for the APRS
beacon and the raspberry pi itself. The transceiver was configured in the UHF band and duplexed
with the APRS unit into a single antenna. A simplified ground station was set up in the same room
as the preliminary payload.
Figure 6: Left: Antenna hanging up during initial comms test. Right: APRS traffic decoded by mobile ground
station, showing GPS altitude and example voltage, internal, and external temperature data.
18
Start/stop of the beacon, downlink of example text data, and loading of a sample webpage from
the payload was demonstrated. Proper startup and operation of the APRS beacon was also verified.
This test confirmed the capability of half-duplex communications between the payload and a
ground station.
Complete System Bench Test
A test covering all major functionalities of the near-finalized payload was conducted. The payload
consisted of a preliminary power system, completed computer system with 99% software
implemented, full sensor payload, and a communications system consisting of the DRA818 OTS
transceiver and APRS beacon.
Figure 7: Near-complete bench assembled system.
The payload was assembled on a bench and initialized under its own power. A full-dress rehearsal
of the preflight procedure was conducted, consisting of starting up the web server, initializing
DIREWOLF with the correct audio port information, startup of sensor data collection, and an
initial ‘echo’ command to verify communications on the UHF link. The ground station was also
initialized as described above. The beacon system was powered on and initially could not acquire
GPS lock. After remotely power cycling, the beacon successfully powered up and achieved GPS
lock.
In-flight functions were then verified, including downlinking text data, downscaled images, and
relaying text messages to a separate station. Startup and shutdown of the APRS beacon was again
verified, and finally a shutdown command was issued. This test confirmed that the complete
system was capable of all required mission functions.
Real Power Draw Test
The above test was repeated, except for the battery power being replaced by a bench supply
connected to a multimeter. Power draw was measured throughout the startup and operation of the
payload, allowing for a more accurate estimate of the payload’s energy usage during flight
operations.
19
The results of this test showed significant energy demand and voltage sag when transmitting. This
test also revealed that the current power system does not include a significant safety margin. The
amount of stored energy (batteries) brought on the flight should be increased, weight and internal
volume allowing.
Long-Range Communications Verification
A final test consisting of the finalized payload assembled in its housing was conducted under long-
range conditions. The payload was assembled and placed on top of the Osborne Center for Science
& Engineering at the University of Colorado, Colorado Springs. The preflight procedure was
conducted, and a mobile ground station was set up out of a team member’s truck.
The mobile ground station was then driven 16 miles to the south, with echo and data downlink
commands issued throughout the drive sent through arial antennas on the truck roof. The station
was then parked on a hill such that minimal blockage existed between the station and the payload.
A tripod-mounted Yagi antenna was set up and pointed roughly in the direction of the university.
Figure 8: Left: Mobile ground station configured with Yagi antenna. Right: Distance measurement of long-range
comms test.
During the drive, communication was intermittent. This was likely due to the significant number
of obstructions between the station and the payload (hills, buildings, etc.). Once the station was
configured with the high gain antenna, communications were consistent even with direct
obstructions consisting of a natural ridge and light foliage. This test determined that, during flight
conditions, line of sight will be guaranteed, and that the payload will be able to communicate with
the ground station for most of, if not the entire duration of flight.
20
Structural Testing Methods and Results
There were multiple tests that were performed on each design structure to verify the integrity of
the structure and the adhesives holding it together. These tests were dropped testing, whip testing,
cold testing, and pitch testing. These tests were intended to simulate the scenarios that the payload
would encounter during the flight. Before these tests were conducted, simulation components were
installed around the structure in the locations where flight ready components would be installed.
Drop Testing:
During the drop testing, the payload was dropped from approximately 20ft in elevation onto
concrete. To conduct this test, the balcony attached to the Osborne building at the University of
Colorado, Colorado Springs was used. This test simulated the impact that the payload would
encounter during landing and verified that the structure and connection methods used could
withstand this impact. For this test all the conceptual designs were used.
The first structure evaluated was the PETG 3D printed design. This structure failed this test as the
location where the structure was screwed together snapped upon impact which can be seen in
Figure 8 below. Due to this, this design was no longer being considered as it was determined that
this design was not capable of withstanding the flight even with heavy modification.
Figure 9: PETG 3D Printed Structure Following Drop Test
The second structure to be drop tested was the foam core and plexiglass design. This design did
survive drop testing, however, the plexiglass on the bottom of the structure did crack upon impact
which can be seen in Figure 10 below.
21
Figure 10: Foam Core and Plexiglass Design Following Drop Test
The final structure to be drop tested was the foam core cube connected with 45o angles. This
structure was superior to the other two designs drop evaluated with the only damage being that the
corner of the structure where impact occurred was crumpled. Seen in Figure 11 below.
Figure 11: Foam Core Cube Connected with 45o Angles.
Following this test, the PETG 3D printed structure was ruled out as it was not able to survive the
drop test. The foam core and plexiglass design were allowed to move onto following testing with
the cracked plexiglass as it was still intact.
22
Cold Testing, Structural:
During the cold test, the payload designs were placed in a –80oC freezer with a thermometer placed
inside and was allowed to sit for 2 hours. The freezer used was found inside the biology lab found
inside of the Centennial building at the University of Colorado, Colorado Springs. This test
simulated extremely cold temperatures, which would exceed the temperature that the payload
would encounter at the extremely high elevations it would reach. This test primarily ensured that
the interior of the structure was able to maintain enough internal temperature to allow for the
electronics and batteries to maintain function. This test also made sure that the structure materials
and adhesive used could withstand these temperatures and would keep everything secure during
the flight. For this test only the foam core and plexiglass design and foam core cube were
evaluated.
The first design that was cold tested was the foam core and plexiglass design. This design had no
issues with the materials used as the plexiglass, foam core, and hot glue were all intact with no
noticeable issues following the test. However, this design did not provide good insulation as the
internal temperature reached -68oC after being in the freezer for 2 hours. This would be too cold
or the electronics and batteries inside to properly work. This is most likely due to the plexiglass
lid and bottom not providing much insulation to the interior.
The second design that was cold tested was the foam core cube. This design also had no issues
with the materials used as the foam core and hot glue were all intact with no noticeable issues
following the test. This design, however, was superior to the foam core and plexiglass design as it
provided significantly better insulation as the internal temperature on reached -42oC after being in
the freezer for 2 hours. This, while still being extremely cold, would still allow for the electronics
and batteries inside to be able to work. This was most likely due to the entire structure being made
from thick foam core all around which allowed for significantly more internal temperature kept.
After this test, the foam core and plexiglass design were ruled out as it did not provide enough
insulation to the interior electronics and batteries. This left only the foam core cube design to move
onto following testing.
23
Whip and Pitch Testing:
The whip and pitch tests were conducted together as the main purpose of these tests were to
validate that the internal components would remain secure. To secure components to the structure,
PLA printed mounts were made for all components and secured to the structure using cold
temperature rated hot glue. During the whip test, a string like the flight string used to connect the
payload to the high-altitude weather balloon was connected to the structure with 4ft of excess
string. Using the excess string, the structure was swung as fast as possible, then the direction of
the spin was abruptly switched. This was repeated two times. This test simulated abrupt rotation
caused by the popping of the high-altitude weather balloon once it reached its peak elevation and
verified that the structure and adhesive used could withstand this intense rotation. During the pitch
test, the payload was rolled down two flights of concrete stairs. The concrete stairs used for this
test were the stairs between the third and fourth floor of the Osborne building at the University of
Colorado, Colorado Springs. This simulated the situation where after landing the wind dragged the
payloads along the ground and verified that the structure and adhesive used were capable of
withstanding this dragging motion. The only design used for this test was the foam core cube
design.
Upon completion of these tests, the structure was opened to verify that the internal components
were still intact and secure which can be seen in Figure 12 below. All components were still
securely connected to the structure demonstrating no issues with the securing methods. All wires
attached between test components were also still intact verifying that the connections between
components survived with no issues.
Figure 12: Foam Core Cube Design Following Whip and Pitch Tests
24
Final Design
Mission
The Finalized mission was, Mission 2: Telemetry and Communications Demonstration. This
mission was decided before any testing of the electrical system was done due to not knowing what
hardware was needed to successfully complete the mission. This mission had to be chosen because
this was the only requirement given to the team from AMERGINT. No other mission was chosen
due to either it being too much extra weight or the execution of the mission being too complicated
to demonstrate in a 2–3-hour flight.
Electrical
A complete circuit diagram can be found in Appendix B.
Main Computer
The primary computer system chosen for the payload was a raspberry pi 4 model B 2Gb. This
device was chosen due to the massive amount of computing power, ease of integration, and large
catalog of open-source software. This device served as the only major piece of control hardware
onboard the payload.
A full-operating system, Raspbian, was installed on the device. The operating system is
manufacturer recommended for the raspberry pi and is a feature-complete port of the Debian
distribution of Linux. Running an operating system significantly simplified the development of
software and flight operations for the payload. The next major software component was
DIREWOLF, an open-source packet modem and virtual ‘soundcard’ implementing AX.25 v2.2.
This package manages the encoding and decoding of digital information to and from an audio
signal, like a dial-up modem. DIREWOLF was configured to communicate at 2400 baud using
phase-shift keying (PSK) and with forward error correction enabled.
An open-source program, TNCAttach, was used to connect DIREWOLF to the operating system
as a standard network interface. This allows for data communications as if the payload was a
TCP/IP device operating on a local area network. A LightTPD web server was installed on the
device to facilitate data transfer, with a simple PHP file allowing for image and sensor data to be
loaded on a web page.
In addition to the web page, a method of direct command was developed to interact with the
payload. This program allowed for an ‘echo’ test (like a ping test), on-demand sensor data
downlink, text message relaying, and a shutdown command. FastCGI was used to allow this
program to interface with the web server during flight operations.
Simple Python scripts were written to facilitate sensor and image data acquisition, storage, and
retrieval. Sensors were polled at 1 Hz, while images were taken at 10 second intervals. While full-
resolution images were taken and saved locally, transmitted image data was downscaled before
being downlinked.
25
A final set of programs were written in python to initially configure the communications
equipment. This software also runs automated processes for certain equipment during the flight.
Sensor Package
Based on the chosen mission profile, sensors that describe the status of the payload and especially
the power system were prioritized. A summary of sensors used can be found in table 2.
Table 2: Summary of included sensors.
Name Measurement Interface Notes
INA219 Voltage I2C Measures voltage at
battery pack
BME280 Altitude, Humidity,
Internal Temperature
I2C Onboard altimeter
and primary internal
temperature sensor
DS18B20 External Temperature 1W External temperature
probe
BCM2711 CPU Temperature Proprietary Built-in temperature
probe on Pi CPU
Pi-Cam Visual Proprietary External Camera
Sensors were connected directly to the raspberry pi using their respective interfaces, with I2C data
and clock routed through the power/data bus board. The Pi-Cam and DS18B20 were attached
externally, while the remainder of the sensors were attached along the internal surface of the
structure.
Communications
Two communications platforms were implemented: an OTS transceiver chip DRA818, and an OTS
automatic APRS beacon BigRedBee.
The BigRedBee is a community sourced APRS transmitter designed specifically for applications
like high altitude balloon missions. The system was powered by the main power system and
interfaced to the computer using USB. The beacon was configured to automatically transmit GPS
coordinates, internal temperature, external temperature, and battery voltage every 5 minutes. The
beacon was only capable of sending APRS packets and could only be controlled through the main
computer. The beacon operated on the 144.39 MHz band using standard APRS protocols at 1 W
transmit power.
26
Figure 13: BigRedBee APRS Beacon
The DRA818 was integrated with a specific circuit board that included LED indicators for power,
Push-To-Talk enable, and receive enable. The device had a dedicated buck converter for power,
fed directly off the main batteries. A single LCFN-400+ low pass filter was connected to the output
of the chip. Initial configuration of the DRA818 was done over a UART interface from the
raspberry pi GPIO. Squelch, power enable, and push to talk were also controlled via the raspberry
pi GPIO. The audio in and out lines were connected to an OTS USB digital to analog converter
connected to the raspberry pi. The transceiver operated on 441.00 MHz band using DIREWOLF
and the software described above at 1 W transmit power.
Figure 14: Left: Assembled & powered up transceiver board. Right: Circuit diagram of transceiver board
To simplify the antenna design, a J-pole antenna was selected. The antenna was custom-cut in the
‘Slim Jim’ configuration to ensure that the ½ - ¼ relationship in the antenna wire length matched
the UHF and VHF frequencies selected. Both the UHF and VHF systems were diplexed into the
single antenna, which then would hang below the payload during flight.
27
The mobile ground station was mounted in a team member’s truck. The system was built around
a Kenwood TM-D710G dual-band transceiver tied to a laptop running DIREWOLF and the
ground-station component of the above software. Two antenna systems were used: whip antennas
mounted to the roof of the truck, and a manually aimed Yagi. The Yagi required for the truck to be
stationary, while the whip antennas could be utilized while the truck was moving.
Power System
Based on both initial power budget calculations and the electrical freezer test, a main battery
component consisting of four 18650 lithium-ion cells in a 2-parallel, 2-series (2P-2S) configuration
was selected. At sea level and room temperature, the batteries provided 10.4 amp-hours of current
at a nominal 7.2 V. The batteries were connected directly to the transceiver board described above
and separate integrated power/data bus board. The only protective device included was an external
single-pole, single-throw toggle switch breaking connection with the batteries at the positive
terminal.
Solar power was determined to be not worth implementing, owing to the large internal volume of
the final structure and simplicity of a battery-only solution.
The power/data bus board consisted of three DC-DC buck converters, an indicator LED,
smoothing capacitors, and four breakaway buses: +5 V, GND, I2C-DATA, and I2C-CLK. The
power rails on the breakaways were connected to the first buck converter and provided power to
all sensors and the computer. An additional buck converter was configured specifically to power
the BigRedBee at 5.5 V.
Figure 15: Left: Assembled power/data bus board. Right: Circuit diagram of power section of power/data bus board
with batteries.
In addition to a dedicated buck converter, the startup process of the beacon required complete
power isolation. A 3.3 V relay was added for this purpose, controlled via the raspberry pi GPIO
and coil current supplied from a third buck converter at 2.2 V. The input sides of all three converters
were connected to the battery pack.
DC-DC converters were utilized extensively, as they provide excellent voltage regulation and
efficiency. Switching converters, however, typically generate high-frequency noise undesirable for
sensitive RF equipment. To rectify this, smoothing capacitors were utilized where necessary. In
addition, each sensor, communications device, and the main computer have built-in linear
regulators, further improving the quality of power delivered.
28
Structure
The final design chosen for the structure was the foam core cube design. This design was chosen
due to it being superior to the PETG 3D printed and foam core and plexiglass design in both drop
and cold testing. This design also passed the whip and pitch testing without any issues.
This design utilized a 48inX24in sheet of ½ inch black foam core board which was cut into 6
150mmX150mm section. The reason black foam core was chosen was so that it would absorb
significantly more heat from radiation from the sun than lighter color foam core. Once the foam
core was cut to size, a 45o angle cutting tool was used to cut 45o angles onto all sides of each
section which can be seen in Figure 16 below. Once this was complete, two of the sections would
have a 12.5mm diameter hole drilled into the center of the section. These two sections would be
the top and the bottom of the structure.
Figure 16: Foam Core Section with 45o angle cut into it.
To mount all electrical components to the foam core sections, mounts for each component were
designed in SOLIDWORKS after taking measurements of each component. The mounts were then
printed using a 1kg spool of PLA filament. The mounts designed for the Raspberry Pi 4 and
batteries can be seen in Figures 17 and 18 below (Mounts for all other components and drawings
of each mount can be found inside of Appendix A).
Figure 17: Raspberry Pi4 Mount Model Figure 18: Battery Mount Model
29
Once mounts for all of the electrical components were made, the mounts that held circuit boards
were screwed together using 10mm length M2 screws and 5mm M2 nuts and the batteries were
clipped into their mounts. The foam core sections were then laid out in a grid pattern and electrical
components began being connected which can be seen in Figure 19 below.
Figure 19: Components Being Attached to Foam Core Sections
30
Once all the electrical components were connected, the mounts were then adhered to their
designated locations within the structure which can be seen in the model in Figures 20 and 21
below.
Figures 20: Component Mounting Locations in Model
Figures 21: Component Mounting Locations in Model Continued
31
Once each component was adhered to their designated location within the structure, the structure
was assembled in the shape of a cube and held together temporarily using a roll of painter’s tape
which can be seen in Figure 22 below.
Figure 22: Structure Held Together with Painter’s Tape
32
Carefully with one section off at a time, four sticks of hot glue were used to adhere each section
of the foam core to the other section. ½ inch washers were then adhered around the hole drilled
into the top and bottom sections of foam core. Carefully, a 1ft long section of ½ inch opaque plastic
tubing was inserted into the holes drilled into the top and bottom sections of the foam core. The
tubing was held in place using a paperclip at both the top and bottom. Finally, aluminum tape was
wrapped around every corner of the structure. The final assembly and its weight can be seen in
Figures 23.
Figure 23: Final Assembly and Weight of Payload
33
Concept of Operations
The CONOPS diagram seen in Figure 1 below walks through how the payload should function
throughout the duration of a successful mission. In step 1, the balloon is launched with the power
on. This is activated by an external switch. This then activates all the sub-systems inside the
payload as seen in step 2. In step 3, the sensor package starts to gather data such as temperature,
voltage, and pictures. This data is pulled in repetitive intervals so that memory and power can be
conserved. In step 4, the data retrieved is then sent to storage and then step 5 pulls the data to begin
a downlink. In step 6, data moves from the control package to the comms package and the data is
injected. In step 7, that data is then broadcast down to the ground station. A loop starting at step 3
and going to step 7 is maintained until the payload is powered off. This provides a steady flow of
data collecting and downlink. To maintain a viable connection for downlink capabilities during
flight, the ground station must follow the balloon. After the mission is complete, the payload is
powered off.
CONOPS Diagram
Figure 24: Concept of Operations (CONOPS) Diagram
34
System Block Definitions Diagram
The external system diagram seen in Figure 2 below illustrates the hierarchy of subsystems that
make up the mission environment. Everything that is responsible for the mission to be conducted
is attached to the high-altitude balloon. Attached to the balloon then is the DemoSat system and
the system is made up of payload. The payload is then made up of 4 main branches: structural,
power, control, and comms. Structure is then further connected to thermal. Power is connected to
both control and comms along with their remaining subsections also. Control consists of the sensor
package and the storage for the data. Comms consists of telemetry hardware and the down
broadcast information. Control and comms are both connected as well.
External System Diagram
Figure 25: External System Diagram
35
The internal system diagram seen in Figure 3 below provides a view of how the different
subsystems within the payload are connected. Starting with the power button, which is connected
to the battery pack and that power is sent to a buck converter. The buck converter then goes to the
sensors, Raspberry Pi, and the transmitter. This allows all 5 sensors and the Pi camera to gather
data. That data is then directed into the storage system managed by the control system. That data
is then pulled by the control system and sent to the comms system for data injection. Is it then sent
to the transmitter and relayed to the ground station. The comms system also has a digital on/off
switch onboard.
Internal System Diagram
Figure 26: Internal System Diagram
36
The functional system diagram seen in Figure 4 below serves as a visual to depict how the transfer
of information is conducted across the different subsystems to complete the mission objectives.
Like the other views, the power source is applied to the entire system. The power applied to the
control system is then used to communicate with the sensors and camera. Each one of those data
mediums is then incrementally written to a respective file via the Raspberry Pi for data storage.
While the data is being collected and stored, the transmitter and comms system pings the Raspberry
Pi with a command to request data. The Raspberry Pi then sends back a command for approval
and the data injection is conducted. The data pull is then carried through the transmitter and on to
the antenna where the down broadcast takes place. The destination for this data is then the ground
station.
The ground station works as a relay as seen in the diagram being able to downlink and uplink
information. Uplinked information was completed by having the antenna and transmitter
connected to the DIREWOLF software modem via the Raspberry Pi control system.
Functional System Diagram
Figure 27: Functional System Diagram
37
Flight Results
The location for flight lift-off was Deer Trail Colorado at 7 am the day of April 1st, 2023. The
3,000-gallon (hydrogen) balloon carried multiple student payloads from different institutions. The
high-altitude balloon reached 107,835 feet and landed in the Stratton Colorado area. Travel time
was 2 hours, 18 minutes.
Figure 28: yellow line from Deer Trail CO. line shows the trajectory of the balloon to its final location in Stratton
CO. (Image/data provided by Edge of Space Science and Google Earth)
Environmental factors guided the team to successfully implement a design to survive the
conditions. The sensor package captures these environmental factors to support the survival of the
payload. The data collected from the SD card onboard the Raspberry Pi 4 was analyzed. The
temperature specification that the team was given was -40℃, and the trajectory took the payload
to only to a low external temperature of -31.6℃. The image bellow also shows the lowest internal
temperature of -13℃. The electrical components produced a small amount of heat during flight
that allowed the system to stay functional. The insulation properties of foam core were enough to
keep internal temperature from lowering any further than most electronics were rated for. Internal
temperature was the most crucial to electrical system and the lowest temperature occurred before
1 hour had passed.
38
Figure 29: External and internal temperature noted minimum.
The voltage sensor gave a visual of the non-linearity of discharge from the lithium-ion batteries
most likely due to temperature and dragging movement of payload. Batteries show stability during
the 5000 second mark that is also the time of highest altitude, which is also the most serene in
terms of movement. It can be determined that the batteries became stable in terms of chemical
reaction and most likely the system was the most stable. The final voltage drop of batteries was
0.51 Volts. This power budget would have allowed the payload to run for significantly longer than
the flown mission.
Figure 30: Voltage drop during flight.
39
The testing of low power data links was achieved with the final low effective isotropic radiated
power (EIRP) of 80mW from antenna. System echoes were received, and system data downlinked
on-demand throughout the flight. Seven photographs were also transmitted (again, on-demand)
during the flight, the last one broadcasted at near maximum altitude shortly before balloon burst.
Primary datalink was accomplished using the UHF system, which performed as expected. The
VHF system proved less reliable. Data was initially received once during preflight and once after
takeoff. After the 2nd transmission, the balloon had climbed above a few thousand feet AGL and
transmissions were no longer received by either the mobile ground station or the greater APRS
network (APRS.fi). This would continue until after the payload had landed, when traffic was
received by the larger network.
This represents the only major anomaly encountered in-flight. While the primary objective was
accomplished via the UHF link, the failure to receive APRS traffic from the beacon meant that the
payload itself was not transmitting GPS coordinates. To track the balloon, the team operating the
ground station had to rely on separate beacons attached to the balloon operated by the launch
provider. These updated less frequently than the 5-minute interval configured at the payload and
made manual tracking more difficult.
Because traffic was received without incident before and after the flight, but not during the flight,
the beacon likely experienced a failure in maintaining GPS lock. The device requires a good GPS
signal before sending a packet; if the balloon were moving too fast, the device might have had
trouble measuring its position. This is consistent with early testing, where the BigRedBee would
occasionally not acquire GPS and need a reset before properly functioning.
All transmissions followed federal communications commission (FCC) protocols, with a licensed
ham radio operator brought on to supervise and operate the communications equipment.
Figure 31: Altitude vs time
40
Figure 32: Seven images transmitted in real time from payload.
An experiment was performed, and two radio operators were able to relay messages using the
payload. The image below shows that about one hour into flight the radio operator was able to
send a message to the payload. The message was relayed to another radio operator at a different
location, as if both were connected via a LAN. The command line printout at the ground station is
shown below, where the message “this is a test message from Caleb…through the high-altitude
balloon” was sent to another ham radio operator. The other operator replies, “Hello World!”.
41
The payload was recovered structurally intact and with a functional electrical system that can be
reused.
Figure 33: Team members at recovery site. Left to right (Caleb, Edward, Lauren, Maxwell, Ian, Alondra, Isaac)
Conclusion
The CubeSat team designed, evaluated, and flew a payload that was able to show reliable and
consistent communication from and to a ground station that had a Yagi antenna through a DRA818
transceiver that was mounted in the payload. The only requirement for the project was to be able
to communicate with a payload at 120,000 feet in elevation. There were multiple designs for the
structure of the but the structures that eventually won out was a 150m cube made all out of foam
core due to its impact resistance and its low thermal conductivity. All the mounts for the electrical
sensors, power boards and batteries were all 3d printed from PLA. The electrical parts were bolted
to the mounts and the mounts were hot glued to the structure, the entire structure was all hot glued
together due to it being the strongest and the fastest drying adhesive.
As the flight went very smoothly there are a few considerations if the project was done again.
Firstly, is to plan out the wiring for the electrical components as even though there were no
problems with the wiring it can get very messy and hard to trouble shoot if there is anything wrong
with it such as a short or a wire gets disconnected. Another would be to design a structure after the
electrical components are already chosen due to the case needing to be increased in size multiple
times to make sure the electrical components can fit. As well with the communication even though
the performed as intended it would be much easier if a SDR system was used it would’ve allowed
for precise tuning of transmission parameters to provide the maximum possible throughput and
minimum power draw.
42
Sponsor Interactions
For the duration of the project the meeting with the sponsor was online or in person every two
weeks. While communication with the sponsor occurred at least once a week. The main contact
Jon Gomez often came to the machine shop to deliver parts for the project and conduct meetings.
Email communications happened often mainly pertaining to ordering and receiving parts. The
frequency of communication and meetings worked well for the project. AMERGINT supplied all
needed resources and supported the team when needed. No issues noted and no changes needed.
Team Interactions
Finally, communication between team members were done using a Discord server and Microsoft
teams. Communication was constant throughout the week for questions, problem solving, and
assignment adjustments. The team including Caleb Hill, who worked on the project as an
independent study, met every Friday to do work in person. Occasionally in person meetings were
conducted online, typically in cases of harsh weather. During spring break, the week before launch,
the team met every day to assemble and fix any problems that arise.
The weekly team meetings were beneficial, it was a day most team members set aside solely for
the project. Having a day when everyone could meet made it easy for a lot of work to get done in
one day. The frequency of the meetings is something that would not need to be changed if the
project were to be restarted but the organization of them would. Meetings would occur but would
lack structure. To improve structure a single team member could be appointed to delegate tasks
with a more specific schedule. When it comes to communication using two platforms could be
confusing at times when information was conveyed on one and not the other.
43
Appendices
Appendix A – SOLIDWORKS Drawings
Assembly Drawings:
3D Printed Design
44
Foam Core and Plexiglass Design
45
Foam Core Cube Design
46
Part Drawings:
Raspberry Pi 4 Mount
47
Battery Mount
48
Pi Cam Mount
49
Transceiver Board Mount
50
Power Board Mount
51
Relay Board Mount
52
BME Sensor Mount
53
BNO and INA Sensor Mounts
54
Appendix B – Complete System Circuit
55
Appendix C – Requirements and Verification
Requirements:
Communications Requirements
ID Requirement Rationale Expected
Value CO
M-1
Communication systems
shall have uplink capability.
To support backup control of
communications subsystem and
for any changes in mission
parameters. Each transmitter
shall be capable of being shut
down in flight in the event of
interference with
essential EOSS channels or other
users.
CO
M-2
The telecom system shall be
capable of supporting a data
volume of 1200bps.
A 1200bps data volume must be
met so that the data from sensor
package can be obtained.
Requirement assumes mission
duration of up to 3 hours.
1200bps CO
M-3
antennas shall not interfere
with sensors.
position of components to
decrease interference CO
M-4
System transmission power
shall remain within limits of
power budget allocation.
To support power of system but
shall not exceed Effective
Isotropic Radiated Power (EIRP)
(300mW)
CO
M-5
The communications
subsystem shall be
compliant with restrictions
set by the FCC.
Specified by the FCC. The
following frequencies are off-
limits during all launch and
recovery day activities: 144.340
MHz, 147.555 MHz and 445.975
MHz.Allowed:145.600 MHz and
446.050 MHz
Communications Requirements Continued
ID Requirement Rationale Expected
Value COM
-6
The payload shall
implement its own unique
satellite ID in the telemetry
downstream.
Each transmitter shall be
operated by a licensed
HAM and ID'd per Part 97 of the
FCC Rules.
Verification
Shut off
demonstrati
on
Demonstrati
on
Inspection
Test E2
Demonstrati
on
Verification
Demonstrati
on
56
COM
-7
COM
-8
COM
-9
ID POW
-1
POW
-2
POW
-3
ID TEL-1
The EIRP (Effective Isotropic
Radiated Power) limits.
Shall be max 300m or no more
than 1W (30dBm) FCC while
remaining within the limits of
the link budget
The communications
subsystem shall be capable
of interfacing with ground
station operations and
support 1200bps.
transmissions must be capable of
interfacing with ground station
to provide telemetry for up to
three hours. (Estimated duration
of flight)
Communications Subsystem
shall be able to function in
simulated environment.
Shall function in environmental
specifications provided by
DemoSat
Sub-System Requirements - Power
Requirement Rationale Power sub-system shall
supply sufficient current to
all other systems at a
minimum of 5 V DC.
The primary purpose of the
power system is to supply
sufficient energy to all other
onboard systems
Power sub-system shall
provide sufficient voltage
regulation from variable
power source (Batteries).
Due to the sensitivity of onboard
RF equipment to dirty power,
the sub-system must provide
clean power from a variable
source
Power sub-system shall
include overcurrent and
overvoltage protection.
The power subsystem must be
resilient to potential electrical
hazards such as fire and battery
RUD
Sub-System Requirements – Telemetry/Control
Requirement Rationale Data collected from sensors
package shall be downlinked
every 5 minutes.
Due to the main mission of this
payload being centered around
communications, having data to
communicate is a paramount
goal.
300mW>1
W
1200bps Parent
Requirement Power Power Power Parent
Requirement Telemetry demonstrati
on
demonstrati
on
Demonstrati
on
Verification
Demonstrati
on
Demonstrati
on
Demonstrati
on
Verification
Demonstrati
on
57
TEL-2
TEL-3
TEL-4
CON-
1
ID ME-
1
ME-
2
ME-
3
ME-
4
Telemetry data collected
shall be exported to the
memory in a readable
configuration.
When the data is transferred,
the format should maintain a
human-readable output so that
the information is useful.
Telemetry data shall be
stored locally as back-up in
case of failure.
Due to the risks associated
during flight, the data stored
should be saved so that the
mission is not a total loss.
Telemetry data shall consist
of 9-axis position data,
current reading, internal
temperature, external
temperature.
Since this is the data that will be
transmitted, it is important to
get a picture of what the
CubeSat is experiencing during
flight both internally and
externally.
The control System shall
manage telemetry and
comms integration by
implementing a data down-
link algorithm.
Once the sensors gather and
store the data, the control
system must facilitate the data
push to the comms system
Sub-System Requirements - Mechanical
Requirement Rationale
Total system shall weigh 800
g or less
As listed as a design requirement
from the COSGC, each CubeSat
must be within this weight range
for a nominal flight.
Frame shall maintain
functional integrity at –40 C
Due to the max altitude that the
payload will be exposed to, it
must be able to function at this
low temperature.
Frame shall protect and
ensure functional integrity
after impact tests
As listed as a flight readiness
requirement, the CubeSat must
survive the respective impact
tests. In case of a failure during
flight, this requirement will
further protect the payload.
Frame shall ensure
functional integrity after jerk
test
As listed as a flight readiness
requirement, the CubeSat must
survive the respective jerk tests.
In case of a failure during flight,
this requirement will further
protect the payload.
Comms Sensors Sensors Control Parent
Requiremen
t
Structure Structure Structure Structure Demonstrati
on
Inspection
Demonstrati
on
Demonstrati
on
Verification
Inspection
Test M4
Test M1, M3
Test M2
58
Sub-System Requirements - Thermal
ID Requirement Rationale Required
Values
Expected
Values Verification
TH
-1
Batteries maintained
between operational
temperatures.
Maintain System Operation -20°C to
60°C
-15°C
to 50°C Test
TH
-2
Electrical components
maintained between
operational
temperatures.
Maintain System Operation -30°C to
65°C
-15°C
to 50°C Test
59
Appendix D– Management
60
61
Weight Budget
Monetary Budget
62
63