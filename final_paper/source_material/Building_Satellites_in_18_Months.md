SSC20-II-07
Building Satellites in 18 Months:
Lessons Learned from the Rogue Alpha/Beta CubeSats
Matthew Navarro
Department of the Air Force
482 N Aviation Blvd, El Segundo, CA 90245; (310) 653-4831
Matthew.Navarro.2@us.af.mil
Joel Gussy, Dee Pack, Darren Rowen, Deborah Salvaggio
The Aerospace Corporation
470 Aviation Blvd, El Segundo, CA 90245; (310) 336-3535
Joel.Gussy@aero.org
ABSTRACT
The Department of the Air Force initiated the Rogue Alpha/Beta Cube Satellite program to challenge The Aerospace
Corporation to investigate rapid reconstitution capabilities. The primary objective was to demonstrate swift
development of a low cost, small size, weight, and power infrared sensing satellite in Low Earth Orbit via schedule
adherence to launch in 18 months. Aerospace achieved this goal by building two identical 3U satellites made with
commercial and non-exotic components. The team was dedicated to building, testing, and making sure the
spacecraft met all milestones successfully, providing pertinent lessons. First, complications faced during assembly
helped lay standards for future use of commercial parts in proliferated networks. Second, the team learned the
importance of conducting rigorous inspections to reduce troubleshooting later. Third was the value of developing a
commoditized bus to allow for deeper payload focus, especially for satellite constellations. Finally, the team
identified the impending need for small, affordable, and swiftly obtainable CNSSP-12 encryption solutions for
future Department of Defense missions utilizing small satellites. With the vehicles in space, the team expects to gain
valuable information on the infrared sensors used, create a baseline for LEO infrared imaging algorithm
development, and evaluate LEO concept of operations for multiple satellites.
INTRODUCTION
concept was applied to a larger constellation of
satellites.
In mid-2018, the Department of the Air Force’s Space
and Missile Systems Center (SMC) began an
unprecedented investigation with the help of The
Aerospace Corporation (shortly referred to as
“Aerospace”) to rapidly develop and field a pair of
small satellites with low-cost infrared sensors in just 18
months. The goal was to push the limits of SMC’s and
Aerospace’s designing and testing culture for small
satellites in order to simulate the ultimate need to
replace an inoperable asset, as well as investigate the
employment of new and existing techniques needed to
meet a compressed development timeline.
To achieve this, Aerospace engineers decided to build
off their existing work with Cube Satellites (CubeSats)
and concluded that two satellites would be an
appropriate measure to demonstrate capability and
redundancy. This would not only lend well to a swift
manufacturing and assembly schedule, but also provide
insight to production needs if the rapid reconstitution
The program’s narrow schedule also meant that
Aerospace would need to construct the majority of
these satellites using commercially available and non-
exotic components. They utilized a number of rapid
prototyping techniques, such as using as many
commercial off the shelf (COTS) parts as feasible
including a thermo-electrically cooled short-wave
infrared (SWIR) sensor.
The team had to rethink its approach to satellite design
and risk management; balancing performance with the
need to meet the target deadline. Prior to launch,
Aerospace completed all environmental testing and
system checks; all anomalies were resolved or deemed
acceptable with minimal residual risks.
The completed Rogue Alpha/Beta CubeSats consisted
of a pair of identical 3U-sized CubeSats, each weighing
in under 5 kg. In total, the program was built and
launched at a program cost of $4.1 million, including
Navarro 1 34th Annual
Approved for public release. OTR 2020-00721. Small Satellite Conference
labor. The program is still currently active and
conducting early on orbit tests.
EARLY MANUFACTUING & TESTING
Parts Selection, Manufacturing, & Assembly
In order to mitigate lead times, The Aerospace
Corporation engaged multiple commercial providers to
supply the parts needed to begin assembling the Rogue
Alpha/Beta CubeSats. This was especially important to
the program’s commitment to launch an unclassified
program in 18 months. Aerospace was able to take
advantage of the program’s nature and explored the use
of many commonly sourced COTS parts. This is a
technique used by various universities and smaller
government investigations, including some of those
done by Aerospace, to keep costs low. However, this
carries a certain amount of risk as most commercial
parts are not qualified for space, which can cause
hardware to degrade fairly rapidly in Low Earth Orbit
(LEO). This was one of the first tradeoffs the team
made to remain within budget and ensure schedule
adherence. Nonetheless, there was little concern about
the longevity of the parts given the targeted mission life
of one year in orbit.
Despite the CubeSats’ short life, all parts were carefully
considered, chosen, and sourced. The Rogue
Alpha/Beta spacecraft used a plethora of COTS
hardware including solar cells, context/visible camera
focal plane arrays, reaction motors, batteries, and
miscellaneous fasteners to name a few. It is worth
noting that while Rogue Alpha and Beta utilized a high
percentage of COTS components, few final assemblies
of the spacecraft remained untouched or unaltered. For
example, the solar cells were sourced from industry, but
the panels’ printed circuit boards, hinges, and harnesses
were custom designed. The same is true for the short-
wave infrared sensor that was chosen for both satellites.
The payloads required significant effort by Aerospace
engineers to adapt the design to provide the desired
capability.
The team of engineers initially chose to go with an
InGaAs short-wave infrared sensor for a few reasons:
relative short lead time and mass availability, sensor
balance between size and performance, ability of sensor
to operate uncooled, and proven usability of a similar
sensor on a previous weather experiments. Similar to
the solar panel assembly, the SWIR payload used a
COTS camera assembly that was comprised of many
custom elements. The lenses, lens housings, baffles,
and camera cards were custom designed to make
engineering a lens with sufficient optical and thermal
properties easier. They these parts were custom, many
of them were procured from commercial partners to
ensure the components in the payloads could be
acquired in large quantities with relatively short lead
times at a reasonable cost. At the time and even still,
there is not a significant precedence for flying SWIR
camera demonstrations on 3U-sized vehicles. One of
the first infrared CubeSat missions was performed by
The Aerospace Corporation when they flew a similar
FLIR Tau SWIR camera and a Tau 640 LWIR micro
bolometer on the ISARA/CUMULOS mission.
Furthermore, other SWIR sensors at the program's
kickoff were only available in small quantities with
significant cost and multi-year lead times. The
Aerospace team has dedicated vast resources towards
developing these types of low cost/size/weight,
uncooled, and mass-producible sensors in hopes of
making them more readily available for future and
larger small satellite programs.
Another measure to keep the satellites as lightweight as
possible was not including a propulsion system on the
satellites, which is very common for satellites of this
size. This also equated to a much simpler system and
allowed the team to bypass mandated certifications for
handling, testing, shipping, and launching of satellites
that do have propulsion systems. No propulsion
inherently means that neither of the satellites are
capable of altitude adjustments or orbit maintenance,
but this was acceptable for the targeted lifetime of the
satellites. Despite no propulsion system, the CubeSats
are capable of precise pointing via the use of torque
rods and reaction wheels.
Each CubeSat weighed in under the threshold target of
5 kg and the final configuration can be seen in figure 1.
In total, the design, manufacturing, and assembly
process took 14 months. At the end of this process, the
team had two identical 3U flight spacecraft that were
delivered to the testing team to be subject to various
environmental and operational testing.
Figure 1: Final Assembly of the Rogue Alpha/Beta
CubeSats
Navarro 2 34th Annual
Approved for public release. OTR 2020-00721. Small Satellite Conference
Vibration Testing
Both satellites underwent initial random vibration
(vibe) tests, conducted using a 2,000 lb.-force shaker.
This vibration table was used to perform tests that met
National Aeronautics and Space Administration
(NASA) General Environmental Verification Standard
(GEVS) prototype flight (protoflight) and workmanship
levels. All vibe test were performed on each satellite’s
x, y, and z axes. The testing procedure began with a
comprehensive functional performance test (CPT) in
order to make sure the satellites’ hardware and software
were performing as expected before each evaluation.
Table 1 shows the specific systems that were tested
during the CPT, which was repeated at the end of all
vibe tests for comparison.
Table 1: Systems Tested During CPT
Table 2: Random Vibration Test Protocol
Step Task
1 Perform Comprehensive functional Performance Test
(CPT) before vibe test
2 Secure spacecraft on one of three axes (x, y, or z)
3 Perform sine sweep (pre-random vibe)
4 Perform random vibe (Input: 14.1 Grms, 1 min)
5 Sine burst (Input: 20 g, 25 Hz)
6 Perform Sine sweep (post-random vibe)
7 Repeat steps 2-5 for other axes
8 Perform CPT after vibe test
Step System Tested
9 Inspection
1 Solar panels produce rated power
2 Batteries charged to expected levels
3 Bus ‘safe mode’ power at expected level
4 Run day-in-the-life case
5 All bus subsystems operating nominally
6 Payloads respond nominally
7 All mechanisms function properly
8 GPS fixes obtained
The CubeSats were then subjected to different levels
and types of vibrations laid out in table 2. First, low
level sine sweep tests were done before major testing to
create a baseline (via pre-random vibe). This test was
performed afterwards to detect any post-test defects.
Dynamic testing consisted of a set of random and sine
vibe tests, with inputs of 14.1 Grms per axis and sine
burst inputs of 20g at 25 Hz. Vibration level testing at
14.1 Grms was derived from the GEVS requirements
for random vibration qualification level testing of flight
hardware and components weighing 50 lbs. or less.
Thermal Vacuum Testing
Once both satellites completed and passed all
subsequent vibration testing, they moved onto thermal
vacuum tests local to The Aerospace Corporation
campus in El Segundo, California. The first test
performed was to place the CubeSats in a vacuum and
test verify that all solar wings released properly in this
environment. Thermal vacuum tests then followed,
performing both hot and cold operational temperatures
(two thermal cycles).
Many operational tests of the hardware and software
were also conducted, beginning with running the
Attitude Control System (ACS) in hybrid mode, which
utilizes the spacecraft star trackers. Additionally, the
team tested all payloads (one context, visible light
camera and one infrared sensor on each space vehicle)
to collect data at frame rates similar to those planned
for when in orbit. Command files were successfully
uploaded to both satellites while in the chamber. This
was done via radio frequency and all commands
uploaded were executed on-board successfully. The
satellites were also able to share their state of healthy
telemetry (including information on voltages, currents,
and temperature) that was tracked throughout testing.
Meanwhile, the sine burst was developed and is used as
a simpler way to perform quasi-static load testing,
qualifying the strength of the satellites’ structure.
The GEVS random vibration requirements also have a
lower level workmanship test of 6.8 Grms. These levels
were used in place of protoflight to check the
survivability of minor repairs and mitigate harm to
other components.
ANOMALIES FACED & RESOLUTION
Cracked Solar Cells
After one of the early random vibe tests, significant
cracks were discovered on the solar cells of the Alpha
space vehicle. While it is common to see minor hairline
cracks, these were prominent enough to warrant
concern that the cracks could propagate further and
stretch across an entire cell (or multiple), creating an
Navarro 3 34th Annual
Approved for public release. OTR 2020-00721. Small Satellite Conference
open loop and rendering the cells useless. The other
cells on both spacecraft were inspected, and no major
issues were found.
The team deduced that the cracks were most likely
created during the soldering process of the solar cells
and that vibe tests merely propagated the cracks. In
order to reduce this issue in future builds, new soldering
fixtures were implemented into the labs to mitigate
handling and the amount of stress put onto the solar
cells during the soldering process.
While the damage found on the Alpha vehicle’s solar
cells was not severe, the team ultimately decided to
replace the entire wing with a flight-ready spare to give
the satellite the best chance at starting its mission with
all its anticipated power.
Due to this replacement, the Alpha CubeSat needed to
go through another vibe test. This test was performed at
workmanship vibe specifications since the team felt that
a full protoflight vibe test was not needed for this
change, and to reduce the amount of wear on other
spacecraft components. Alpha passed this workmanship
vibe and inspections revealed that any existing cracks
and propagations remained minute.
Solar Power Harness Wear
A separate, full protoflight random vibe test resulted in
significant wear on the Alpha CubeSat’s solar power
wire harness. Both CubeSats have two solar power
harness each that transfer the power created by the solar
panels to the batteries for recharging. All harnesses
were manually routed and secured using Polyimide
tape. This is based on previous designs and builds,
which have never showed issues. Too much slack in the
wire harness had allowed it to shift on top of an
adjacent plastic feature during vibe, which eventually
led to the observed damage.
The loss of a wire harness would create a significant
impact to the power budget as it renders the whole wing
useless. The team elected to replace the harness and
reroute it with more clearance from any protruding
features, using more tape to secure the harness in place.
To prevent this occurrence from repeating, all other
harnesses were inspected to ensure proper routing
clearance and manual installation procedures were
updated for future CubeSats. This change alone did not
constitute a re-vibe on its own, but it would be tested in
subsequent vibe tests later.
Wing Deployment Failure
While the Beta vehicle underwent its initial protoflight
level vibe test, it experienced issues properly deploying
its solar wings. This was attributed to multiple root
causes that became apparent and resolved after various
workmanship vibe tests.
The first failure to deploy was traced down to a nut
assembly used in a slide release mechanism to deploy
the solar wings. The slide release was tested and shown
to be operating nominally. After the nut assembly was
manipulated manually, the issue was determined to be
caused by improper out-of-plane movement and a bias
of in-plane movement of the nut assembly.
While designing the release mechanism and nut
assembly, the team noticed in past builds that fixing the
nut assembly in place led to more issues and far more
failures to deploy. Therefore, they designed the nut
assembly to allow in-plane side-to-side movement that
proved to work successfully on seven other spacecraft.
However, it was discovered during inspection that this
specific nut assembly had a significant amount of out-
of-plane movement. Reinforcement was added to the
back of the nut assembly to prevent further out-of-plane
movement; however, static testing before a
workmanship re-vibe still resulted in inconsistent wing
deployment. Further manual manipulation of the nut
assembly to either side of its allowed movement
showed that there was a bias to one side over the other.
Forcing the nut assembly to one bias resulted in four
sequential failures, and four deployment tests in the
other bias resulted in four successful deployments.
Therefore, while the assembly was designed to shift, a
shim was installed to force the nut to its favorable bias.
The team performed another vibe at workmanship
levels to test the survivability of all fixes.
Unfortunately, when testing the wing deployment, the
opposite wing (which was not experiencing deployment
issues) did not deploy fully. Inspection of the wing
found that there was significant resistance due to a
protruding screw along the wing hinge (which partially
backed itself out during vibe) and was rubbing against
the body of the spacecraft. It was eventually concluded
that this specific screw was never staked in place with
epoxy during assembly.
To limit the chances of any future issues during
deployment, all excess epoxy was removed along the
wing hinges for both CubeSats, the screw was properly
staked down, and all external screws were examined for
proper staking. No other screws were found to be
without the proper amount of epoxy. The Beta vehicle
went through its final workmanship vibe and passed all
functional testing.
FROM PRODUCT ASSURANCE TO LAUNCH
ESD, Protection, & Cleanliness
Per standard operating procedure, the completely
assembled, tested, and flight-ready satellites were
stored in a picosat clean room. When the satellites were
not actively being tested, they were stored in a laminar
Navarro 4 34th Annual
Approved for public release. OTR 2020-00721. Small Satellite Conference
flow bench/hood station. Whenever the CubeSats
needed to be handled, all personnel wore electrostatic
discharge (ESD) safe coats and gloves. Any and all
handling of flight hardware, on or off the satellites, also
included a required use of ESD wrist straps.
The Rogue Alpha/Beta CubeSats are equipped with
lasers, which are used for communication and data
transfer. Whenever personnel supporting any laser tests
were in the lab, they were required to have completed
the laser safety training and wear protective eyewear at
all times. In order to prevent any accidents, there were
three redundant hardware protections put in place to
prevent any unintended laser activations.
Finally, before the satellites were prepared for delivery,
all materials on the satellite were approved for
outgassing and all hardware underwent a final clean,
inspection, and bake out.
Transportation and Delivery
After a Pre-ship Review was completed, the team
worked to wrap up the transportation process to prepare
the CubeSats’ journey from El Segundo, California to
delivery to NanoRacks in Houston, Texas. The first step
was to protect the context and SWIR cameras by
installing temporary plastic covers, shown in figure 2.
Then the spacecraft were individually wrapped in anti-
static bags and packed into a hard case lined with foam
and suited with shock sensors.
Figure 2: Rogue Alpha/Beta CubeSats Preparing for
Transport
The team then transported the CubeSats to a
NanoRacks facility, where they were transferred to a
10k clean room for incorporation into the NanoRacks
deployment pods. Aerospace personnel aided
NanoRacks in unpacking the space vehicles,
performing final functional tests, and integration. All
personnel were required to follow all previously
established ESD procedures as well and wear lint free
gloves to limit contamination, see figure 3. After the
CubeSats were placed in their launch pods, they would
remain there until their deployment.
Figure 3: CubeSat being Integrated into NanoRacks
Deployment Pods
NanoRacks then delivered the deploy complement to
NASA’s Wallops Flight Facility for integration into the
Northrop Grumman Cygnus capsule. Throughout this
time, the vehicles were constantly kept in a secure and
clean environment.
Launch & Deployment
On November 2, 2019, the Space and Missile Systems
Center, The Aerospace Corporation, NASA, Northrop
Grumman, and others celebrated a successful launch
out of the Mid-Atlantic Regional Spaceport’s Pad-0A at
NASA’s Wallops Flight Facility in Virginia.
The Rogue Alpha/Beta CubeSat program launched
aboard a Northrop Grumman Antares 230+
configuration launch vehicle. The 230+ configuration
allows the Northrop Grumman Cygnus capsule to
deliver up to 1,760 lb. (800 kg), which carried the
Rogue Alpha and Beta, among other cargo, to the
International Space Station (ISS). This launch signified
the conclusion of all ground efforts and the start of
Alpha and Beta’s voyage in orbit, as well as the success
of the 12th commercial resupply mission awarded by
NASA. The Cygnus NG-12 capsule quickly made its
way and docked to the ISS.
While the Rogue Alpha/Beta CubeSats successfully
made it to space on November 2, they remained stored
on the ISS until the capsule’s release on January 31,
2020, shown in figure 4. The team received
confirmation of the successful deployment of Alpha at
1:00 pm PT and Beta at 4:10 pm PT. Though released
at a considerable time apart from each other, their
scheduled releases allowed the CubeSats to orbit a few
hundred kilometers apart. From there, the team waited
for the first opportunity to make contact with both
vehicles. Once initial contact was made, the operations
team immediately began a state of health check. Both
assets confirmed nominal battery health and their
telemetry data provided more accurate information
about their orbits. The team used this to update a locally
Navarro 5 34th Annual
Approved for public release. OTR 2020-00721. Small Satellite Conference
sourced orbit-tracking tool to help get a better
understanding on the CubeSats’ locations.
Figure 4: Cygnus NG-12 being Released to Deploy
both CubeSats before Reentry
LESSONS LEARNED
Raising COTS Standards
During the manufacturing, assembly, and early testing
of the Rogue Alpha/Beta CubeSats’ parts, the crew
faced two major non-conformances related to the
commercial off the self parts being used. Aerospace
engineers worked extensively to determine the root
causes, fix the anomalies, and do other safety checks on
similar components. Collectively, these efforts cost the
group nine weeks in delays, but with no overall delay
on delivery to the launch provider.
1. Focal Plane Array Connectors: The first issue was
observed in the form of elevated data values when
testing the payload. The cause of the issue was
eventually traced to the focal plane array (FPA)
connectors. Upon inspection, there was a notable
fracture in one of the solder joints at the interface
between the FPA pins and the electronics board.
The team concluded this was caused by poor solder
wetting on the gold-plated pins. This ultimately led
to a break between the pins and solder when
manually mating and disconnecting the connectors.
To save the work done to the payload and to
mitigate further delays, Aerospace disassembled
the COTS FPA connectors and reflowed solder on
the connections.
In order to mitigate potential reoccurrences, this
same inspection and repair was done to the other
payload and to a flight ready spare. (Other boards
ordered in this lot were also inspected, but no
issues were found.) In addition, the team executed
extensive post repair testing prior to environmental
tests.
Overall, the team spent six weeks and many hours
to find the root cause and resolve this issue.
Aerospace also notified the vendor to prevent
future issues with new parts.
2. Camera Board Communication Failure: Another
issue identified early on was a failure to transfer
data from the camera on the Alpha vehicle.
This issue was eventually traced to cracks in the
39-pin harness of the camera board. The team has
confidence that this was caused by a defect related
specifically to the gold plating used on the copper
connectors which cracked when handled. At this
point, the use of these 39-pin harnesses was known
to create issues due to their delicate nature. The
space vehicles’ design was based on a heritage
system which has suffered from similar issues. In
an attempt to fix this issue, the harnesses were
replaced on the Alpha spacecraft with ones that
were in acceptable condition. After looking at the
hardware that had been replaced, numerous hairline
cracks were discovered that had not yet led to
failures.
The Beta vehicle continued to suffer from this
issue despite since it was unable to receive a
component in better condition due to the poor
shape of the other components and replacements.
During thermal vacuum tests, the context camera
failed to transfer data to the board. Aerospace
engineers affixed a shim to resolve the connection
cracks, which proved to maintain integrity
throughout ground testing. There is still a
possibility that the fix may fail during launch or its
operational life, however, this has not proved to be
an issue so far.
In total, it cost 3 weeks of schedule to determine
the cause and perform repairs on these harnesses.
As a result, the Aerospace team has more
awareness on the flaws of using such a delicate
component and have worked to create a new
baseline design that phases out the use of these
harnesses.
Note that these issues are not to the fault of the vendors,
but rather inherent risks of using COTS parts. It is a
byproduct of buying mass produced, readily available,
and affordable parts. These commercial parts do not
typically need to be held to the high standards of
assembling a satellite. As a result, the Rogue
Alpha/Beta CubeSat team recommends that programs
implement a higher level of screening and acceptance at
the vendor or local level. One such way could be
through an inspection by the vendor or the customer,
and/or by having the vendor provide workmanship
certification for each part or the entire lot of parts. The
team recognizes that this may increase the cost of the
parts, but it may be worthwhile compared to the labor-
hours and schedule costs that may come later.
Navarro 6 34th Annual
Approved for public release. OTR 2020-00721. Small Satellite Conference
Commoditized Bus
It was also recognized that even in this small project of
two CubeSats, to produce a constellation of satellites
quickly and affordably, it benefits to invest in
commoditizing or acquiring a reproducible bus.
For smaller projects such as the Rogue Alpha/Beta
CubeSat program, having identical satellites proved to
be extremely useful. Many of the parts were
interchangeable meaning that spares purchased were
readily available for both. This also means less overall
program costs as the sharing of parts means less spares
are ordered. Another benefit of having a reproducible
bus is that subsequent builds get done faster and make
lessons more relevant compared to ones learned from
one-off designs. Specifically, the team was frequently
able to use lessons learned from prior generations to
anticipate what to expect on these CubeSats. For larger
satellites, the improvement period is spread further
apart and may reach a point where it loses value or
never gets used. Additionally, having a standard bus
allows for more attention to be lent to payload
development and refinement.
The benefits of using a commoditized bus carries many
benefits. It is expected that eventually more industry
leaders will become interested in making mass
produced satellite buses, instead of one-off designs, to
meet needs.
Utilizing Rigorous Inspections & Prototypes
No matter if commercial parts or a replicated design are
used, the CubeSat assembly team for this program
identified the value of employing the use of multi-stage
inspections and prototype research.
In regard to this program, an issue was faced by way of
a screw not being staked down with epoxy, leading to a
significant issue resulting in improper solar wing
deployment. If a more rigorous inspection process was
exercised, it may have been able to catch this problem
sooner. A possible fix could be implementing a two-
person inspections process to have a redundancy plan.
Even so, it helps tremendously when knowing what to
look for. The failure in the camera board pin harness
and cracks in the solar cells were easily resolved
because of insight from previous iterations. However,
there are instances when the issue may not be apparent
until it is noticed in performance testing where it may
be too late. This is what makes prototypes so
invaluable. They act as a means of risk reduction by
flushing out early, unforeseen issues and optimizing
procedures for future or larger programs.
If a proliferated system is to be designed, the CubeSat
team recommends employing both of these measures as
a means of reducing the amount of issues faced long
term. This can also lead to more time and effort to be
dedicated to the development of the payload.
Swift & Affordable Encryption Solutions
The Rogue Alpha/Beta CubeSat program is not a
National Security Space mission and therefore did not
require National Security Agency (NSA) approved
encryption. As a result, the team decided to use an in-
house encryption solution proven on other unclassified
CubeSat programs. However, the program looked into
encryption options as part of the trade space. A crucial
take away is the identified need for lightweight, small,
speedy, and economic NSA compliant encryption
solutions.
At the time Rogue Alpha/Beta were designed, there was
only one compliant encryption solution available that
was a potential fit, however, the lead time to acquire it
would have pushed the schedule much longer than
allowed. There are often lengthy year-plus lead times
before an encryption solution is approved or acquired.
Additionally, the cost to integrate that solution would
have exceeded the entire budget of the program. The
spacecraft design team eventually decided that the best
option for this unclassified, one-year research
investigation would be an in-house encryption solution.
Previous Aerospace CubeSat programs served as
precedence for proving this solution’s effectiveness,
which was able to suit this program better than the
alternative.
Currently, the list of NSA compliant encryption options
has improved with more compact solutions available in
shorter lead times. This could not come at a more
pertinent time as the Department of Defense seeks to
expand its partnerships with more commercial and
university partners. In order to help these programs
remain successful, the Department of Defense must
continue to investigate even more ways to offer
encryption solutions that can be obtained in short
timelines and under small budgets, all while
maintaining an attractive form factor for small and
medium-sized satellites.
LOOKING FORWARD
At this time, the Rogue Alpha/Beta CubeSats have been
operating in space for a few months. The main goals are
to gain valuable information on the infrared sensors
used, create a baseline for LEO infrared imaging
algorithm development, and evaluate LEO concept of
operations (CONOPS) for multiple satellites. The
infrared sensors will fly dominantly in a horizon-
pointed configuration to collect frame stacks that can be
used for testing cloud scene processing algorithms and
clutter models. The team will command both satellites
simultaneously in forward, aft, and cross-track pointing
Navarro 7 34th Annual
Approved for public release. OTR 2020-00721. Small Satellite Conference
configurations, collecting scenes in benign,
intermediate, and stressing solar conditions. At present,
the program has focused on calibrating the CubeSats’
sensors and observation tasking has been minimal.
Since the Rogue Alpha/Beta CubeSats have achieved
on-orbit operation prior to other upcoming LEO
concepts, the anticipated information gathered on cloud
backgrounds, multi-frame processing, and LEO
CONOPS will prove to be especially useful.
The program is approximately halfway through, yet
there have been substantial improvements that can be
shared with the intent of helping further CubeSat
technology at large. The Rogue Alpha/Beta team hopes
that these lessons can serve some relevance to programs
big and small as there have been multiple instances in
this project alone where time and effort have been
saved because of the insight provided by others.
Acknowledgements
This work was vastly supported by a wide range of
talented and dedicated individuals. These include: Dr.
Russ Benson, Jon Bray, Igor Brin, William Chavez,
Colonel Dennis Bythewood, Dr. Jeff Emdee, Brian
Hardt, Brian Hardy, Colonel Frederick Hunt, Sara
Lampen, Colonel Woodrow Meeks, Lauren Sotez, Paul
Su, Katherine Whiteside and the Public Affairs team,
and others. A special thanks goes out to them for their
efforts to keep this program running and successful.
References
1. J. Bray, W. Chavez, B. Hardy D. Hinkley, S.
Lampen, D. Pack, D. Rowen, D. Salvaggio,
“AeroCube-15 Pre-Ship Review,” Proceedings of
the Internal Pre-Ship Review, El Segundo, CA,
September 2019.
2. R. Benson, S. Lampen, D. Pack, D. Rowen, D.
Salvaggio, P. Su, “Rogue- Alpha, Beta,”
Proceedings of an Internal Program Review, El
Segundo, CA, November 2019.
3. I. Brin, D. Bythewood, M. Navarro, D.
Salvaggio, K. Toner, “Space and Missile Systems
Center Communication and Messaging Plan
Aerospace Rogue Alpha/Beta CubeSats,” Space
and Missile Systems Center Public Affairs, El
Segundo, October 2019.
4. Pack, D.W., Ardila, D.R., Herman, E., Rowen,
D.W., Welle, R.P., Wiktorowicz, S.J., and
Hattersley, B.W., "Two Aerospace Corporation
CubeSat Remote Sensing Imagers: CUMULOS
and R3", Proceedings of the AIAA/USU
Conference on Small Satellites, SSC17-III-05,
2017.
https://digitalcommons.usu.edu/smallsat/2017/all
2017/82/
5. Pack, D.W., C.M. Coffman, J.R. Santiago “A
Year in Space for the CubeSat Multispectral
Observing System: CUMULOS”, Proceedings of
the AIAA/USU Conference on Small Satellites,
SSC19-XI-01, 2019.
https://digitalcommons.usu.edu/smallsat/2019/all
2019/148/
6. Wijker, J.J., “Spacecraft Structures,” Springer-
Verlag Berlin Heidelberg, The Netherlands,
2008.
7. F. LaRocca, S. Macmurphy, M. Ott, R. Switzer,
W. Thomes, “Vibration performance comparison
study on current fiber optic connector
technologies,” Proceedings of SPIE - The
International Society for Optical Engineering,
August 2008.
8. Clark, S, “Space station resupply mission
successfully launches from Virginia,” Spaceflight
Now, November 2019.
Navarro 8 34th Annual
Approved for public release. OTR 2020-00721. Small Satellite Conference