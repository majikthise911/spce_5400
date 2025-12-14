GODDARD TECHNICAL
HANDBOOK
GSFC-HDBK-8007
Goddard Space Flight Center Greenbelt, MD 20771 Approved: 12/16/2019
Revalidation Date: 12/16/2024
Mission Success Handbook for Cubesat Missions
MEASUREMENT SYSTEM IDENTIFICATION:
METRIC/SI (ENGLISH)
THIS STANDARD HAS BEEN REVIEWED FOR EXPORT CONTROL RESTRICTIONS;
APPROVED FOR PUBLIC RELEASE
DISTRIBUTION IS UNLIMITED
GSFC-HDBK-8007
NASA GODDARD SPACE FLIGHT CENTER
Greenbelt, Maryland 20771
Approved By:
Original Signed By:
Tupper Hyde
Chief Engineer
Goddard Space Flight Center
Original Signed By:
Felicia Jones
Director of Engineering and Technology
Goddard Space and Flight Center
Original Signed By:
Dave Mitchell
Director of Flight Projects
Goddard Space Flight Center
Original Signed By:
Felicia Jones
Director of Engineering and
Technology
Goddard Space and Flight Center
Original Signed By:
Eric Isaac
Director of Safety and
Mission Assurance
Goddard Space Flight Center
Check the GSFC Technical Standards Program website at http://standards.gsfc.nasa.gov or contact the Executive
Secretary for the GSFC Technical Standards Program to verify that this is the correct version prior to use.
2 of 24
GSFC-HDBK-8007
`
DOCUMENT HISTORY LOG
Status Document
Revision
Approval Date Description
Baseline TBD Initial Release
Check the GSFC Technical Standards Program website at http://standards.gsfc.nasa.gov or contact the Executive
Secretary for the GSFC Technical Standards Program to verify that this is the correct version prior to use.
3 of 24
GSFC-HDBK-8007
FOREWORD
This handbook is published by the Goddard Space Flight Center (GSFC) to provide uniform
engineering and technical requirements for processes, procedures, practices, and methods that
have been endorsed as standard for NASA programs and projects, including requirements for
selection, application, and design criteria of an item.
This handbook establishes
Requests for information, corrections, or additions to this handbook should be submitted via
“Contact Us” on the GSFC Technical Standards website at http://standards.gsfc.nasa.gov.
Original Signed by: James S. Milne for:
Josef Wonsever
Technical Standard Coordinator
Goddard Space Flight Center
Check the GSFC Technical Standards Program website at http://standards.gsfc.nasa.gov or contact the Executive
Secretary for the GSFC Technical Standards Program to verify that this is the correct version prior to use.
4 of 24
GSFC-HDBK-8007
TABLE OF CONTENTS
SECTION
PAGE
DOCUMENT HISTORY LOG........................................................................... 3
FOREWORD ..................................................................................................... 4
TABLE OF CONTENTS ................................................................................... 5
LIST OF TABLES ............................................................................................. 6
1. SCOPE ................................................................................................ 7
1.1 Purpose ................................................................................................ 7
1.2 Applicability ....................................................................................... 7
2. APPLICABLE DOCUMENTS .......................................................... 7
2.1 General ................................................................................................ 7
2.2 Government Documents ..................................................................... 8
3. PROCESS ........................................................................................... 8
3.1 Selecting Mission Success Activities ................................................. 8
3.2 Reliability ............................................................................................ 9
3.3 Other Processes ................................................................................... 9
3.4 Safety and “Do No Harm” .................................................................. 10
4. MISSION SUCCESS ACTIVITY SELECTION…………………… 10
Appendix A Environmental Test for Cubesats ............................................ 16
Check the GSFC Technical Standards Program website at http://standards.gsfc.nasa.gov or contact the Executive
Secretary for the GSFC Technical Standards Program to verify that this is the correct version prior to use.
5 of 24
GSFC-HDBK-8007
LIST OF TABLES
TABLE PAGE
1 Risk Tolerance (Risk Classification) ................................................. 11
2 Expected Lifetime .............................................................................. 12
3 Mission Success Tiers for Cubesats ................................................... 13
Check the GSFC Technical Standards Program website at http://standards.gsfc.nasa.gov or contact the Executive
Secretary for the GSFC Technical Standards Program to verify that this is the correct version prior to use.
6 of 24
GSFC-HDBK-8007
Mission Success Handbook for Cubesat Missions
1. SCOPE
1.1 Purpose
The purpose of this handbook is to provide guidance for laying out a mission success approach
for cubesat missions to cover a range of different mission lifetimes, and independently a range of
different criticalities. For example, there may be cases for a very short lifetime mission that is
critical (analogous to a launch vehicle placing in orbit a key national asset). The guidance below
accounts for the fact that no matter what the criticality or lifetime of the mission, the use of a
cubesat brings with it tremendous constraints in size/compactness as well as cost and schedule
available, relative to larger missions. This document begins with the assumption that while there
may be critical and/or long lifetime cubesats, the A and B classifications applied to larger
spacecraft carry with them burdens that currently are not implementable under cubesat
constraints even for constellations. The risk postures in this document range from the most
common, i.e., “Do No Harm” (highest risk posture) classification through a NASA mission Class
C as the lowest risk posture approach addressed in this handbook, representing the highest level
of criticality. This may change over the years as technology and cubesat development
experiences evolve. Even more importantly than for larger spacecraft development, this
document should be used as a guidance tool as part of a holistic, systems-centric engineering
approach for developing cubesat missions, and no one element should be considered sacred to
the process. This document follows the logic of GPR 8705.4, drawing in some of the verbiage
directly, but foremost is driven by the common constraints in cubesat development.
1.2 Applicability
This handbook is targeted towards an in-house effort to produce a cubesat. The principles are
applicable to support an out-of-house development or acquisition, but vendor capabilities and
proven practices should be the driver for an external procurement; thus this document is not
intended to supplant successful development practices in industry or other outside organizations.
Actual broad requirements are outside of the scope of this document, but they generally arise
from the documents referenced in the Safety and “Do No Harm” section, 4.4.
2. APPLICABLE DOCUMENTS
2.1 General
Documents listed in this section contain provisions that constitute requirements of this
handbook as cited in the text of Section 4. The latest issuances of cited documents shall be used
unless otherwise approved by the Technical Authority (TA). The applicable documents are
accessible via the NASA Technical Standards System at http://standards.nasa.gov, directly from
the Standards Developing Organizations, or from other document distributors.
Check the GSFC Technical Standards Program website at http://standards.gsfc.nasa.gov or contact the Executive
Secretary for the GSFC Technical Standards Program to verify that this is the correct version prior to use.
7 of 24
GSFC-HDBK-8007
2.2 Government Documents
NASA-STD-8719.14. Process for Limiting Orbital Debris
NASA-STD-8719.24. NASA Expendable Launch Vehicle Payload Safety Requirements
NPR 8715.6 NASA Procedural Requirements for Limiting Orbital Debris and
Evaluating the Micrometeoroid and Orbital Debris Environments
GPR 8705.4 Risk Classification Guidelines and Risk-Based SMA Practices for GSFC
Payloads and Systems
3. PROCESS
3.1 Selecting Mission Success Activities
Three tables in this document comprise the collective guidance for assembling a development
plan. Table 1 represents a risk tolerance element, analogous to NASA’s risk classification
system. Each of the classifications is described within the table, and is accordingly to be defined
by the stakeholder, or in some cases by the developer with concurrence from the stakeholder.
The table conveys what the primary emphasis should be for the given risk posture and
subsequently suggests the activities from Table 3 to consider initially in forming a development
plan.
Table 2 is a breakdown by required lifetime, independent of the risk posture, suggesting the
decisions that will enable a range of desired lifetimes. It may be considered essentially a
modifier with respect to Table 3 in that maintaining the desired risk posture for longer duration
missions may necessitate implementing additional assurance activities.
Table 3 is a three-tiered breakdown of activities in two different categories that comprise a
structured approach for aligning mission success activities with risk classification levels. The
breakdown follows the mantra that risk classification is aligned with two main logical elements,
(1) the ratio of programmatic risk (i.e., threats against cost and schedule) taken in development to
technical risk (i.e., threats against meeting level 1 requirements while on-orbit) in operation, and
(2) the ratio of programmatic resources (i.e., cost and schedule) used in development to
technical risk in implementation. (Put in simple terms, “how much risk or cost can I take on in
development to make the risk of mission success on orbit very low?”) These represent the two
columns in the table. The rows in the table are subjective “high”, “medium”, and “low” ratio
clusters of activities for each category. The highest risk posture (i.e., those with greatest
tolerance for risk) projects in general (starting with “do no harm”) would use mostly activities
from Tier 1, while activities would be added from the higher tiers as the tolerance for any
technical risk goes down.
The Appendix provides further guidance for the environmental test recommendations within the
table, as well as overall guidance for cubesat environmental test in general. Broad consideration
Check the GSFC Technical Standards Program website at http://standards.gsfc.nasa.gov or contact the Executive
Secretary for the GSFC Technical Standards Program to verify that this is the correct version prior to use.
8 of 24
GSFC-HDBK-8007
should be given to the Appendix as a whole to best outfit the environmental test campaign for the
mission.
3.2 Reliability
It is important to note that at this very early stage in cubesat development maturity, there is no
valid statistical basis for assessing cubesat reliability, and hence the most meaningful measures
of reliability upon which to build do not exist. While it would be natural to suggest that the high
failure rate of cubesats is due to a lack of understanding of how to build a reliable cubesat, more
completely it is the inability to define the resources needed up front, combined with a lack of
understanding of how to build a reliable cubesat and the lack of knowledge of how to effectively
test it under realistic conditions and constraints (resource and technical).
Hence, a large percentage of cubesat missions may have failed prematurely because they ran out
of resources (time or money) and to avoid cancellation flew whatever they had at the time. This
is in part a simplistic view as there may also have been many substantive technical factors such
as poor quality in standard components used, a lack of knowledge of the launch vibroacoustic
environment, and the fact that the mere size of cubesats has opened the door to development by
organizations that have very limited spaceflight experience and capability. Presently therefore,
the expectation that any cubesat will have a “high” likelihood of lasting a significant amount of
time (one year or greater) should be very low. It will take a period of years to accumulate
sufficient real data to start establishing higher reliability expectations for individual cubesats.
One of the most promising aspects of cubesats for reliability at the mission level is the prospect
of using multiple cubesats in a fault-tolerant constellation architecture. Given the current debris
environment, such an architecture must be considered very thoughtfully, because any suggestion
of a greater likelihood of producing debris may not be acceptable. Therefore, an appropriate
mission design with either low-enough altitude or a robust safety mechanism that would ensure a
reasonably prompt post-mission re-entry would be a key part of an “m for n” cubesat
constellation architecture.
3.3 Other Processes
There are many other activities and processes that can further mitigate risks of building and operating a
cubesat. Such efforts should always be considered using a risk-based approach where the rigor is
commensurate with programmatic resources and programmatic risk available to buy down technical
risk. For example, good practices for materials and processes from a document such as NASA-STD-
6016 should be applied with discretion. Workmanship practices from experienced and workmanship-
trained technicians, are likely to be sufficient for cubesats with the lowest risk tolerance. Cubesat
applications with higher risk tolerance may serve as a good training ground for less experienced
technicians, but in such cases inspections and workmanship verifications become more important.
Electrostatic discharge (ESD) practices should be aligned based more on ESD sensitivity of the items in
question as opposed to the risk tolerance of the project. Note also that while level 2 and level 3 parts are
in recommended guidance above, these screening levels, defined in EEE-INST-002 and the various
pertinent military specifications, do not actually correlate with part reliability in typical space system
operating environments, nor do they address radiation in general. The screening levels do, however, asCheck the GSFC Technical Standards Program website at http://standards.gsfc.nasa.gov or contact the Executive
Secretary for the GSFC Technical Standards Program to verify that this is the correct version prior to use.
9 of 24
GSFC-HDBK-8007
increased, help to reduce the presence of many risk-driving factors, such as moisture and other
contaminants, foreign particles, and workmanship flaws. When planning out a development approach, it
is important to recognize how piece-part screening and testing activities may limit available resources
for system-level testing, which may drive up risk for a highly-resource-constrained mission.
3.4 Safety and “Do No Harm”
“Do No Harm” in this document enters in two forms. First, it is the risk classification per GPR 8705.4
as defined in Table 2. Second, it describes the actual protections in place so that there is no harm to
people, to the environment (orbital environment), or to any equipment or infrastructure that is not within
the project’s own risk purview to damage. In this category, the leeway imparted to mission success risks
(as described in the prior sections of this document) for cubesats is not imparted to such safety risks.
Therefore cubesats must abide by launch services restrictions, such as LSP-Req-317.01 (for LSP hosted
cubesats), ISS safety requirements (for ISS-launched cubesats), do no harm requirements from other
pertinent ride-providers, orbital debris requirements in NASA-STD-8719.14 (as called from NPR
8715.6), and range safety requirements in NASA-STD-8719.24 (as called from NPR 8715.3) as apply.
The particular ride opportunity will indicate which of the above documents pose driving requirements
for do no harm.
4. MISSION SUCCESS ACTIVITY SELECTION
This document provides guidance in terms of risk mitigation activities as a function of the “risk
ratios” and “cost-to-risk ratios” defined in Table 3 across the range of the common mission
success activities most applicable to cubesats. Table 3 can be considered a “how much bang for
the buck” table, where Column A represents “the buck” in terms of programmatic risk and
Column B represents “the buck” in terms of project cost and schedule. As one progresses from
Tier 1 in the table down through Tier 3, one would move into activities that generally have less
bang for the buck (less efficient use of resources), while the lowest bang for the buck (Tier 3)
would be reserved for the missions that have the least tolerance for risk and the most resources
available (i.e., cost and schedule or risk against cost and schedule) available to buy down
technical risk. Note that some elements in the table may be specified by another entity and hence
not selectable by the developer using this handbook.
One of the first steps prior to selection of activities should be a risk and reliability analysis
(referred to in Table 3 as an “early holistic risk assessment”), that will be key to understanding
the critical and susceptible points in the mission as well as any natural fault tolerance in the
mission architecture (e.g., 5 satellites, 3 of which needed for mission success). Part of this
assessment should be a recognition that designing to achieve the absolute maximum performance
within the given technical and resource constraints typically has a negative effect on reliability
(e.g., a race car tends to be less reliable than a sedan). This analysis should also consider
heritage and inherited elements being brought to bear for development, such as a standard
reaction wheel that has prior flight history. This analysis should be used to make specific
selection decisions for the activities based on the risks and priorities involved for the project.
This document is not intended for use to make a blind declaration that a project is not meeting
requirements for a given class. There are multiple viable paths to achieving a desired risk
Check the GSFC Technical Standards Program website at http://standards.gsfc.nasa.gov or contact the Executive
Secretary for the GSFC Technical Standards Program to verify that this is the correct version prior to use.
10 of 24
GSFC-HDBK-8007
Do No Harm 7120.8 Stakeholder
perspective
posture (e.g., more detailed independent design review vs more test time) and the nature of a
given project may influence which path is more appropriate. The project should have a clear
rationale for their selection of project requirements from the guidelines provided herein or for
using alternate methods that have similar intent. This document does not exclude alternate
approaches outside of these guidelines. The environmental test elements are underlined in the
table and provided for a general reference to indicate a starting point. These should prompt a
review of the associated section in Appendix A, which includes detailed guidelines for each
respective environmental test approach, to select the appropriate environmental test activity for
the project. Furthermore, Appendix A should be used as a set of recommended testing
approaches to construct an appropriate environmental test campaign. The recommendations in
the Appendix are geared toward NPR 7120.5 Class missions, so those in the 7120.8 or “Do No
Harm” Class should take considerable leeway based on resources and tolerance for
programmatic risk associated with conservative overtest.
Table 1: Risk Tolerance (Risk Classification)
Drivers: mission criticality determined by stakeholder
Implications: significant relevant, positive heritage
7120.5 Class D Cost and schedule
are of equal or
greater
consideration
compared to
mission success
risks. Allowable
technical risk is
medium by design
(may be
dominated by
yellow risks).
Many credible
mission failure
mechanisms may
exist. New
technologies may
be employed that
may not be fully
compatible with
some traditional
requirements.
7120.5 Class C
Acceptable
technical risk is
very high.
There are no
requirements to
last any amount
of time, only
not to harm the
host platform
(ISS, host
spacecraft, etc.).
No mishap
would be
declared if the
mission doesn’t
perform as
planned. Such
missions may
be considered to
be an “on-orbit
environmental
test”.
Acceptable
technical risk is
high. Some level
of failure at the
project level is
expected but at a
higher level
(program level),
there would
normally be an
acceptable failure
rate of individual
missions (such as
85% mission
success rate over
some time period).
Premature failure
of an individual
mission is
considered as an
accepted risk, and
not a mishap.
An instrument
or spacecraft
whose loss
would result in
a loss or delay
of some key
national science
objectives. New
technologies
may be
employed that
may not be
fully
compatible
with some
traditional
requirements,
requiring
alternative
approaches for
ensuring
mission
success.
Key emphasis Protecting the
host, learning
from anomalies
and failures
“Program level”
fault tolerance
(some failures
expected)
Thorough testing
and some
consideration of
fault tolerance
Check the GSFC Technical Standards Program website at http://standards.gsfc.nasa.gov or contact the Executive
Secretary for the GSFC Technical Standards Program to verify that this is the correct version prior to use.
11 of 24
GSFC-HDBK-8007
Tier selection
from Table 3
Select 1A and
1B elements
1A and 1B 1A, 1B, and select
2A and 2B
elements
Robust testing
and
consideration
of fault
tolerance in the
mission
architecture and
hardware
designs
Table 2: Expected Lifetime
Drivers: Time for complete science collection
Implications: limited life items, expendables, qualification/life test period
< 3 months 3-months-1 year 1-5 years > 5 years
Main attributes Min. 100-hrs
system-level
testing time. No
additional EEE
part or
component
screening or
qualification
(acceptance
only) – does it
function at
launch
Min. 200-hrs
system-level
testing time.
Selective
part/component
screening and
qualification
(beyond COTS)
– thorough
environmental
test
Min. 500-hrs
system-level
testing time.
Thorough part
and component
screening and
qualification,
thorough
environmental
test
Min. 1000-hrs
system-level
testing time.
Complete part
and component
screening and
qualification,
testing
consistent with
large spacecraft
Limited life (LL)
items,
expendables
Sizing
expendables is
the primary
consideration
Increased
analysis or
margins for
expendables plus
analysis or test
for selected LL
items
Increased
analysis and
margins for
expendables plus
analysis and test
for most LL
items
Increased
analysis and
margins for
expendables plus
analysis and test
for all LL items
Table 3: Mission Success Tiers for Cubesats
1A: Low Ratio of Programmatic Risk to
Technical Risk
- First two TVAC cycles, minimum 50
1B: Low Ratio of Programmatic Resources
to Technical Risk
- First four thermal cycles
hours
- Random vibe
- Last 150 hours of failure free
- First 500 hours of operation
operation
- Vibe at 1.05 flight levels
- EMI self-compatibility
- Close-out inspection
- Early holistic risk assessment
- “iphone” photography
Check the GSFC Technical Standards Program website at http://standards.gsfc.nasa.gov or contact the Executive
Secretary for the GSFC Technical Standards Program to verify that this is the correct version prior to use.
12 of 24
GSFC-HDBK-8007
Radiation-tolerant design - informal independent SME review
(graybeard mentoring)
- spare printed circuit board” for
coupon for future DPA
2A: Medium Ratio of Programmatic Risk to
Technical Risk
- Protoflight vibe
2B: Medium Ratio of Programmatic
Resources to Technical Risk
- 3-6 TVAC cycles (after 2 earlier)
- RS testing
- Level 3 EEE parts
- 1000 or more hours of operation
- Select mandatory inspection points
- Use of formal WOA system
- Select engineering units for high
risk/new items
- Focused engineering peer review
- Fault-tolerant design using FMECA,
FTA, and/or critical items analysis as a
basis
- Design for manufacturability
- FPGA peer review
- Observatory level qualification
- Self-performed software assurance
- GIDEP self-review
- GOLD rules as guidance
- Radiation qualification by similarity
3A: High Ratio of Programmatic Risk to
Technical Risk
- Prototype vibe
- Upscreened level 2 EEE parts (longer
duration missions)
- CS01 and CS06 testing
- Shock testing
- Radiation lot qualification
3B: High Ratio of Programmatic Resources
to Technical Risk
- 7+ TVAC cycles
- High fidelity engineering units and/or
spares
- MIL-SPEC level 2 EEE parts (longer
duration missions)
- Continuous on-site QA
- Class 3 or greater PCB requirements
with coupon testing
- Many mandatory inspection points
- Independent software assurance
- Formal milestone reviews
- FPGA formal design review
- Full component level qualification
- Full, closed-loop GIDEP
- Full GOLD rule implementation
- Radiation-hardened parts
-
Check the GSFC Technical Standards Program website at http://standards.gsfc.nasa.gov or contact the Executive
Secretary for the GSFC Technical Standards Program to verify that this is the correct version prior to use.
13 of 24
GSFC-HDBK-8007
Example: 3 cubesat mission, one-year lifetime, under NPR 7120.8. This example is intended to convey
the general logic employed to develop a mission success plan.
Consider a 3-satellite mission where the satellites form a “string-of-pearls” in circular equatorial orbit at
350 km altitude, with a 5-minute phasing between satellites. The mission involves collection of time-
phased radiometric data from Earth by each satellite over common points. Minimum mission success
requires 2 out of the 3 satellites to function at any one time over the duration of a year. Each satellite is
a standard 6U cubesat. The cubesat structure, reaction wheel assembly, deployment system (retaining
wire and burn wire), power system, and S-band comm system have all flown in an environment that
envelopes the current mission environment for a minimum of 1.5-year operating time. The new item on
each cubesat is a radiometer that includes 9 commercial detectors, 6 of which are required in a single
instrument to collect minimum science. The detectors have been used in many long duration (> 3 year)
ground applications and briefly in space demonstrations in different orbital environments. Using solar
flux and geomagnetic index estimates, propulsion will be required to maintain satellites within science
tolerances in orbit. Uncontrolled re-entry is predicted to satisfy orbital debris requirements.
Furthermore, analysis tools indicate that the debris casualty area will be well within requirements, even
for the cumulative set of three satellites. Propulsion expendables will be sized for 1.5-year mission
duration. The only limited-life item identified is the burn-wire system for deployments. The limited life
will necessitate a minimal level of testing prior to flight, one actuation in ambient pressure and another
in vacuum. In the 7120.8 category, the primary tiers from Table 1 would be 1A and 1B from Table 2.
Using Table 3, we will set 200 hours as the minimum testing time, but with a goal of 500 hours, so 500
will be used for planning purposes in a success-oriented schedule. A reliability and risk analysis
identifies the deployment system and power system as the most critical items, with no fault-tolerance on
the deployment system and the power system being a new design without no pre-defined fault-tolerance.
The burn-wire-based deployment system has some history, but with different sizing and manufacturer
components. Therefore, 10 qualification sets of retaining wire and burn wire will be tested in vacuum in
at the range of potential environmental conditions to ensure that the system is qualified for the current
environment. For the power system, radiation effects will be considered, but with no resources available
for radiation hardened parts, most parts will be derated to well below EEE-INST-002 levels. Parts used
in new applications will be commercial parts with previous qualification history and high confidence in
the lot-to-lot variability. At the core of the power system is a DC/DC converter, which will be selected
as one of the commercial versions from one of the top power converter manufacturers. Launch provider
is not known at initiation, so the qualification levels for vibration will be determined from consideration
of the launch loads from one of two providers. Strength will be determined by static loads analysis,
while random vibe will serve as a protoflight vibe and workmanship verification. EMI self-
compatibility will be performed after 3 thermal vac cycles, selected to balance out vacuum operating
time and sufficient time at thermal extremes. The core engineering team will consist of 4 junior
engineers at full time, two experienced engineers at 25% level and a senior engineer who participates 3-
5 hours per week. NASA trained technicians will be performing the electrical assembly work, using
workmanship standards as guidelines. Worst Case Circuit analysis and part stress analysis will be
performed on the power system. Workmanship issues and past reliability problems are associated with
the reaction wheel package. Elevated risk will be carried in the risk database to monitor this package
and closeout inspections are planned for both the reaction wheel electronics and the power boards. The
power system and instrument boards will be built to a minimum of IPC 6012D Class 2, with Class 3 as a
target. Power board coupons will be microsectioned and analyzed by the developers. Flight softwareCheck the GSFC Technical Standards Program website at http://standards.gsfc.nasa.gov or contact the Executive
Secretary for the GSFC Technical Standards Program to verify that this is the correct version prior to use.
14 of 24
GSFC-HDBK-8007
assurance and validation will be performed by the software engineer with support at key milestones
from an independent branch member. Engineering models will be developed and maintained for the
detector electronics and the power system. Risks will be tracked in a spreadsheet and reviewed with the
senior engineer biweekly. Engineering peer reviews will be performed for the detector subsystem and
the power system, each involving at least 3 independent engineers. At the time of launch, the expected
risks will be:
1. Uncertainties in the launch environment and unresolved discrepancies between the launch
provider and the environmental test performed.
2. Potential repeat or repercussion from unresolved anomalies
3. Uncertainties due to testing that did not cover the complete relevant environment
Note that an NPR 7120.8 project is an R&D project by definition, so the mission in space may be
maturing technologies from lower technology readiness levels.
Check the GSFC Technical Standards Program website at http://standards.gsfc.nasa.gov or contact the Executive
Secretary for the GSFC Technical Standards Program to verify that this is the correct version prior to use.
15 of 24
GSFC-HDBK-8007
APPENDIX A
Environmental Test for CubeSats
Section 1 This Appendix provides recommendations for and describes the risks retired with the
verifications described in the General Environmental Verification Standard (GEVS) for GSFC
Flight Programs and Projects (GSFC-STD-7000), with the focus on cubesats or other
applications where limited resources and limited programmatic risk tolerance (i.e., risk of
failures in I&T that may not have occurred on-orbit) and relatively high on-orbit risk tolerance
will lead projects to reduce the scope or stress levels of testing. This section provides the
expanded recommendations for the underlined elements in Table 1. The emphasis in this section
is on NPR 7120.5 Class C and D missions, while Section 4 in this document provides guidance
for those missions with greater technical risk tolerance and less resources and tolerance for
programmatic risk.
The following directly references specific paragraph numbers in GEVS rev A, dated 4/22/2013.
Section 2.2 of GEVS provides general guidance on environmental verification.
Section 2.2.2 Verification Program Tailoring
This section is particularly applicable to cubesats, since a full, GEVS-defined approach would be
overkill for a cubesat. GEVS is written assuming a project with very low tolerance for on-orbit
risk.
Section 2.3 Electrical Function Test Requirements
Section 2.3.1 Electrical Interface Tests
This section describes the importance of verifying interfaces prior to connecting electronics.
These tests are commonly referred to as safe-to-mate tests. Thorough safe-to-mate tests take
some time to plan out and execute, but they prevent damage caused by errors in electrical
interfaces. A knowledgeable engineer must determine the resistances and signal levels expected
on each pin of an electrical interface, determine the proper test equipment (the wrong meter can
cause damage in some cases), and capture that information in a procedure. These measurements
are then made with a break-out box prior to integration. For interfaces with many signals, these
tests frequently catch mistakes in pin assignments or errors in harness wiring. These tests also
catch errors in signal waveforms caused by mistakes or misunderstandings in the design or
assembly errors.
This section of GEVS does not mention interface tests prior to flight integration, but, in general,
all projects should plan to conduct interface tests as soon as breadboard designs exist, per GSFC-
STD-1000, rule 1.44. These tests will identify mistakes and misunderstandings at a time when
the problems can be fixed with little or no schedule and cost impact.
Section 2.3.2 Comprehensive Performance Test (CPT)
All projects should follow the principles described here, although what is considered
“comprehensive” will certainly be much less for a cubesat than a larger mission. CPTs areCheck the GSFC Technical Standards Program website at http://standards.gsfc.nasa.gov or contact the Executive
Secretary for the GSFC Technical Standards Program to verify that this is the correct version prior to use.
16 of 24
GSFC-HDBK-8007
generally run once before environmental testing as a baseline, once spread out over the hot
environmental testing, once spread out over the cold environmental testing, and once at the end
of environmental testing. It may not be possible to cover all items in the CPT during the hot and
cold testing. For cubesats, the project may need to further descope some aspects of the standard
CPT testing, based on the costs of the test relative to the risks retired by the testing.
Section 2.3.3 Limited Performance Tests (LPT)
Limited Performance Tests are frequently called “functional” tests. For a cubesat, the CPT may
be short enough that no LPT is necessary. The primary purpose of the LPT is to ensure nothing
has broken during environmental testing. With large spacecraft, the CPT is too long to execute
multiple times during environmental testing.
Section 2.3.4 Performance Operating Time and Failure-Free Performance Testing
GOLD rule 2.01 in GSFC-STD-1000 duplicates the requirements associated with this section of
GEVS, but it allows fewer than 1000 operating hours for missions that are class D and below.
Operating hours as a system provides a higher likelihood that rare timing problems will manifest
themselves. Total component operating hours on the ground help screen out early failures
related to manufacturing defects and design errors. Hours in vacuum are generally more
stressful on components, especially at hot temperature, because there is no convection to cool the
parts. In general, the more operating hours the better, to identify problems.
Cubesat projects should investigate alternative testing options, such as a 500-hour burn-in at
elevated temperature, which can provide screening for a variety of parts, design, and
workmanship issues. The duration of a cubesat mission should be factored in to the
considerations related to operating time and failure-free performance testing, e.g., using Table 3
in Section 4 of this document.
Section 2.4 Structural and Mechanical Verification Requirements
It is of utmost importance to ensure that the cubesat hardware poses no risks to any primary
payload with which it is manifested. The second consideration should be to reduce the risk of
structural and mechanical failure of the cubesat as much as possible given the programmatic
constraints of the cubesat in development.
Given the constrained resources of most cubesat projects, a structural qualification unit is not
likely. Most cubesat projects that are launching a single cubesat will want to follow a protoflight
model for structural verification. Missions with multiple identical cubesats will want to consider
protoflight testing for the first unit with acceptance testing for the follow-on units.
The baseline structural and mechanical verification program defined in GEVS assumes that a
payload is sufficiently modularized to allow for testing lower levels of assembly. For cubesats
this is typically not the case, so mechanical verification testing will almost always be performed
at the payload level on the cubesat mounted in its dispenser system. Verification tests defined in
GEVS for lower levels of assembly should be addressed as required during cubesat testing.
Section 2.4.1 Structural Loads Qualification
Qualification of the cubesat for its structural loads environment will be accomplished by a
combination of test and analysis. Structural loads qualification is typically performed by test andCheck the GSFC Technical Standards Program website at http://standards.gsfc.nasa.gov or contact the Executive
Secretary for the GSFC Technical Standards Program to verify that this is the correct version prior to use.
17 of 24
GSFC-HDBK-8007
accompanied by analysis showing positive margins of safety against limits loads using the
factors defined in Table 2.2-3 in GEVS. For metallic structure, it may be possible to
demonstrate strength qualification by analysis only using higher no-test factors of safety.
Determining the structural loading environment for cubesats will depend on a number of factors
including the first frequency of the cubesat-dispenser system and whether or not a vibration
isolation system is used. For larger payloads, a coupled-loads analysis (CLA) is used to derive
the quasi-static limit loads for structural loads verification. Since most cubesats do not respond
dynamically to the low-frequency launch environment, a dedicated CLA will not be run to derive
launch loads. The cubesats will be analyzed and tested for a set of conservative quasi-static limit
loads that have been developed to envelope the expected loads for a given launch configuration.
If the first frequency of the combined cubesat-dispenser (and possible load isolation system) falls
below 100 Hz, a model of the cubesat system might need to be provided to the launch vehicle
provider for inclusion in the coupled loads analysis to derive limit loads for structural
qualification. Cubesat systems with modes below 100 Hz may also need to provide a test-
verified model that has been correlated through a modal survey or vibration testing.
Whenever possible, structural testing of the cubesat should be performed inside its dispenser or
an identical substitute. This ensures that the interfaces and loads on the cubesat are as flight like
as possible. In addition, the rail-style dispenser can result in rattling of the cubesat, which results
in non-linear response, which can only be simulated by test. Tests should be performed in each
of three orthogonal axes.
Section 2.4.1.1 Coupled Loads Analysis
Given the late manifesting, high frequency and low mass nature of cubesats, a formal coupled-
loads analysis is unlikely to be possible for most cubesat projects. When developing the
structural loads for a cubesat, the mechanical experts should try to envelop the structural loads
from all possible launch services.
Section 2.4.1.2 Modal Survey – Frequency Verification
Because of their low mass, high frequency and simple mode shapes, a dedicated modal survey
test of the cubesat-dispenser system is generally not necessary. Usually a test verified model
would only be required if the cubesat or cubesat-deployer system has modes below 100 Hz. If a
test-verified model of the cubesat-dispenser system is required, the correlation can usually be
performed based on measured responses from vibration testing that can be used to tune the finite-
element model so that it accurately represent the frequency and response amplitudes from the
test. In most cases, if a test verified model is not required, a low-level signature test (sine or
random) in each axis is sufficient to verify the first frequency of the cubesat system. A low-level
signature test is generally performed before and after vibration testing to ensure that the
structural characteristics of the system have not changed after exposure to the vibration
environment.
Section 2.4.1.3 Design Strength Qualification
Strength qualification of cubesats can be accomplished in a number of ways. First, if the random
vibration (or sine vibration, if required) environment is the enveloping source of structural loads,
the vibration test can serve as the strength qualification test. Care should be taken when using
Check the GSFC Technical Standards Program website at http://standards.gsfc.nasa.gov or contact the Executive
Secretary for the GSFC Technical Standards Program to verify that this is the correct version prior to use.
18 of 24
GSFC-HDBK-8007
this approach to ensure that realistic analytical assumptions for damping and load paths are used
to determine loading under dynamic vibration.
If vibration cannot be shown to be the driving environment for structural loads and the cubesat
has simple, easy-to-analyze load paths, strength verification can be accomplished through
analysis only using no-test factors of safety as outlined in this section of GEVS. It should be
noted that a no-test approach is only applicable to metallic structures and cannot be used for
beryllium, welded, ceramic, composite, or bonded structures.
If vibration testing or a no-test analytical approach cannot be shown to be adequate to
demonstrate structural qualification, the project should perform a dedicated strength test.
Section 2.4.1.4 Structural Reliability (Residual Strength Verification)
Cubesat projects should assess the structural risks associated with using materials not in table 1
of MSFC-SPEC-3029. The risks will be primarily related to mission success, since the launch
container provides protection to the primary payload.
Section 2.4.1.5 Acceptance Requirements for Strength Qualification
This section applies to all cubesats. Strength testing is generally not required for a follow-on
cubesat whose design has been previously demonstrated to be strength qualified except for
structures using materials that have been identified as requiring proof testing.
Section 2.4.2 Vibroacoustic Qualification
Random vibration, without acoustics testing, is generally sufficient for cubesats. Cubesats do not
have large surface areas that can absorb acoustic energy, and the stiffness of most dispensers
provides additional protection. Random vibration is likely to be the most important mechanical
environments test for most cubesats. It is the primary structural loading environment for
cubesats with a first frequency greater than 100 Hz. It is also an excellent workmanship test.
This test alone may be sufficient for a cubesat.
Force limiting will generally NOT be useful for cubesats because of their low mass, but special
circumstances may make the extra complexity of force limiting worth the effort (for instance, an
interface with high random environment but not much mass available to deliver energy to the
cubesat or a cubesat deployer on an isolation system with high mass participation modes that
would result in unrealistic loading during vibration testing).
Section 2.4.2.3 Payload Random Vibration Qualification Tests
Whenever possible, vibration testing of the cubesat should be performed inside its dispenser or
an identical substitute. This ensures that the interfaces and loads on the cubesat are as flight like
as possible. Cubesats typically do not have levels of assembly below the payload level.
Therefore, all vibration testing is performed at the payload level of assembly. However, the
requirement to expose electrical, electronic, and electro-mechanical hardware to minimum
workmanship levels should be maintained for cubesats as a screen for workmanship flaws in
electronics boards. The cubesat protoflight vibration environment should therefore be derived as
the envelope of limit level + 3dB and minimum workmanship.
Check the GSFC Technical Standards Program website at http://standards.gsfc.nasa.gov or contact the Executive
Secretary for the GSFC Technical Standards Program to verify that this is the correct version prior to use.
19 of 24
GSFC-HDBK-8007
Section 2.4.2.5 Component/Unit Vibroacoustic Qualification
This section is not typically applicable to cubesats as all verification testing will be performed at
the payload level of assembly.
Section 2.4.2.8 Retest of Reworked Hardware
This section provides guidance on testing after rework.
Section 2.4.3 Sinusoidal Sweep Vibration Qualification
Because of the higher resonant frequencies in a small cubesat, a sinusoidal sweep is generally not
necessary. A sine test would only be necessary if the resonant frequency of the cubesat is less
than 1.5 times the upper frequency defined for the launch vehicle sine environment. A
mechanical engineer should verify this assumption for all cubesats.
A sine vibration test should also be considered if cubesat uses a rail-style dispenser or a load
isolation system. The rail-style dispenser system can cause non-linear responses due to rattling
under the low-frequency dynamic launch environment simulated by sinusoidal vibration. The
load isolation system may drop the frequency of the system to where it could respond to a sine
input.
Whenever possible, sine vibration testing of the cubesat should be performed inside its dispenser
or an identical substitute. This ensures that the interfaces and loads on the cubesat are as flight
like as possible.
Section 2.4.4 Mechanical Shock Environment
Self-induced and externally induced shock should be considered when assessing the cubesat for
sensitivity to the shock environment. Release from the launch container will provide an external
shock to a cubesat. Launch vehicle separation events are also sources of external shock for
cubesat payloads. However, the interfaces between launch vehicle shock sources and the launch
container plus the interface between the container and the cubesat will help reduce the severity of
the launch vehicle shock environment. All external shock sources for the cubesat should be
captured in interface requirements from the container manufacturer or the launch provider.
Cubesat designers also need to consider internal sources of shock from deployments (both the
release and the hard stop of any undamped release) of on-board mechanisms and from any other
sudden release of stored energy that will occur during operation of the payload.
Section 2.4.4.1 Subsystem Mechanical Shock Tests
This section provides guidance on testing for shock and for assessing the risk associated with not
performing a shock test. The shock verification approach defined in this section is applicable to
cubesats.
Section 2.4.4.2 Payload (Spacecraft) Mechanical Shock Tests
As stated above, the cubesat designer should consider the environment and determine whether or
not a system-level test is appropriate.
Section 2.4.5 Mechanical Function Verification
This section provides guidance on verification of mechanisms, including life tests and torque
margin. Some or all of it may be applicable, depending on the type of mechanisms in theCheck the GSFC Technical Standards Program website at http://standards.gsfc.nasa.gov or contact the Executive
Secretary for the GSFC Technical Standards Program to verify that this is the correct version prior to use.
20 of 24
GSFC-HDBK-8007
system. The primary difference between a cubesat and a large, class B mission may just be in
the level of detail in the analyses. Cubesat designers should make conservative, simplifying
assumptions and move forward, assuming the margin requirements are met. Be aware of forces
that become significant for small mechanisms, such as friction, electrostatic force, surface
tension, etc., and ensure sufficient force is available to drive the mechanism under all conditions.
During design, consider how the deployments will be tested. Under most cases, the designer
should be able to provide enough force and strength to perform deployment tests on the ground
without g-negation devices.
Section 2.4.6 Pressure Profile Qualification
Cubesat designers should ensure adequate venting for the worst-case pressure profile. A good
rule of thumb that envelopes all launch vehicles is to provide a vent area of 0.05 square inches
(0.25” diameter hole) per cubic foot of enclosed volume. This will ensure that the peak pressure
level with the volume is less than 0.5 psi during launch. The small volume of a cubesat limits
the concerns associated with pressure profile.
Section 2.4.7 Mass Properties Verification
As this section states, mass properties verification is dependent on mission requirements.
Section 2.5 Electromagnetic Compatibility Requirements
Given that cubesats typically launch unpowered, the interference to the launch vehicle or from
the launch environment is not applicable in most cases. In general, the most significant concerns
for cubesats consist of self-compatibility, compatibility with ground-based tracking radars, and
compatibility with on-board antenna(s) on-orbit.
GEVS is based primarily on MIL-STD-461, which specifies tests at the component level prior to
integration into a larger platform, e.g. instrument, payload, spacecraft, etc. Because cubesats are
generally small, self-contained enclosures, the equivalent of a “component level” test program
would apply at the card level, for which the tests specified in GEVS are generally not applicable.
This places an emphasis on the need to identify and correct potential issues at the card level to
the extent feasible. This may be accomplished with a combination of test and analysis, the
specifics of which must be determined by the needs of each platform. A minimum set of
recommendations is provided in section 2.5.1 below.
The integrated cubesat platform must demonstrate compatibility with its communications
subsystem. A minimum set of recommendations is provided in section 2.5.2 below.
Card Level Tests
For cards that provide sources of power to other cards, an assessment of power quality should be
performed at card level. This may consist of a simple measurement of differential voltage ripple
in the time domain (i.e. on an oscilloscope). The voltage ripple limit must be determined by the
specific needs of the platform, but a recommended limit is 200 mV peak-to-peak on top of a 12
Vdc bus, measured in the time domain with a bandwidth of 1 MHz.
Check the GSFC Technical Standards Program website at http://standards.gsfc.nasa.gov or contact the Executive
Secretary for the GSFC Technical Standards Program to verify that this is the correct version prior to use.
21 of 24
GSFC-HDBK-8007
Most cubesat platforms consist of a single instrument. On such platforms, there are no hard and
fast requirements for conducted emissions (CE), conducted susceptibility (CS), or power quality
to be applied. Such requirements are intended to establish compatibility between multiple
instruments or payloads operating from a common power bus. Thus the main issue regarding
power on single instrument cubesats reduces to compatibility between the single instrument and
the power subsystem.
On cubesat platforms that include more than one instrument or experiment, measures must be
taken to control the ripple generated by any instrument that may be seen by the other
instrument(s). This is best done with a measurement of current ripple at card level. The limit
must be tailored to each specific platform. A recommended starting point is to characterize the
impedance between the power source and the common distribution point. The current limit may
be derived from the allowable voltage ripple at the distribution point and the common source
impedance, while also allowing for the number of different loads. Because the source impedance
varies with frequency, the current limit will also vary with frequency. Thus it is recommended
that this measurement be performed in the frequency domain with a spectrum analyzer, similar to
the CE101 test method of MIL-STD-461G.
Once all of the cards are integrated but prior to closing up the box, a measurement of aggregate
time domain differential voltage ripple should be performed at the common distribution point in
the power subsystem in order to verify that the voltage ripple requirement above is still met with
all of the loads operating. Designers of the system should consider a layout that enables this test.
On cubesat platforms with one or more instruments that are particularly sensitive to magnetic
fields (e.g. magnetometers), it may be necessary to apply some limit of magnetic field emissions
to other equipment in the system. This may be done at the card level with a tailored version of
the RE101 test method of MIL-STD-461G. The ultimate verification will be an assessment of
card-to-card compatibility in the integrated configuration.
Integrated Cubesat Level Tests
At the integrated cubesat level, it must be demonstrated that its radiated emissions do not
interfere with the uplink signal(s) to its receiving antenna(s). The recommended method, per
MIL-STD-464, is first to connect the output of the receive antenna directly to an external EMI
receiver or spectrum analyzer, then measure the received RF power levels at the uplink
frequencies while the platform is put through its normal operations. If it is possible to define a
limited set of “most emissive modes,” it may be sufficient to test only in those modes, and it will
make most efficient use of test time.
A radio frequency (RF) link margin analysis should be performed in order to determine the
minimum signal that may be read by the on-board receiver(s). This level is used as the
benchmark for the measurement outlined above. Thus the combination of measurement and
analysis provides a direct assessment of radio frequency (RF) self-compatibility while also
providing an assessment of margin.
Also, the integrated cubesat must demonstrate that it is compatible with the RF energy generated
by its transmitter(s) and antenna(s). This may be demonstrated by transmitting the full power
Check the GSFC Technical Standards Program website at http://standards.gsfc.nasa.gov or contact the Executive
Secretary for the GSFC Technical Standards Program to verify that this is the correct version prior to use.
22 of 24
GSFC-HDBK-8007
levels out of each transmit antenna while the platform is put through its normal operations. If it is
possible to define a limited set of “most susceptible modes,” it may be sufficient to test only in
those modes, and it will make most efficient use of test time.
Section 2.6.1 Summary of Requirements
Due to the small size and integrated nature of cubesats, the project should determine how much
testing is appropriate prior to integration vs. conducting all testing at the system level.
Component-level testing reduces the risk that a problem will be found later, after integration.
Specifics on thermal vacuum testing:
 Bakeout: payload.
From a “do no harm” perspective, a system-level bakeout is generally required
to ensure the cubesat does not have any outgassing products that might damage the prime
 Balance: Thermal balance testing at the system level will demonstrate proper thermal
analysis and temperature control.
 Temperature: Testing the system over temperature ensures that all components work
together as timing and other parameters change over temperature.
 Cycling: Thermal cycling stresses components and assemblies to weed out weak designs
and workmanship issues. Because of the small size of components and even the entire
system, the temperature can generally be cycled fairly quickly, so the cost of performing
a cycle is not that great. Other testing, such as a high-temperature burn in, might be
considered as an alternate approach to extra cycling.
Section 2.6.2 Thermal-Vacuum Qualification
This section, with the margins and cycles, is appropriate for cubesats, with the considerations
listed above.
The use of a TQCM is not required if the cubesat can meet the time-at-temperature requirements
of bakeout.
It is not necessary for a cubesat to dwell for 24 hours at each extreme. Dwell times should be
based on how quickly the spacecraft internal temperatures will stabilize and how long it takes to
run performance testing.
Failure-free performance duration of 100 hours hot and 100 hours cold reduces the risk that some
vacuum or temperature related problem is missed during the testing. The project should
carefully look at the risks vs. benefits of reducing these times.
Section 2.6.3 Thermal Balance Qualification
This section is generally applicable to cubesats.
The survival case for cubesats might be unpowered during launch.
Because of the small size, the cubesat may be more susceptible to heat leaks through cabling and
mounting.Check the GSFC Technical Standards Program website at http://standards.gsfc.nasa.gov or contact the Executive
Secretary for the GSFC Technical Standards Program to verify that this is the correct version prior to use.
23 of 24
GSFC-HDBK-8007
Section 2.6.4 Temperature-Humidity Verification
This section is only applicable for components in pressurized volumes.
Section 2.6.5 Leakage (Integrity Verification)
Any components that rely on a pressurized volume should be tested to ensure they do not leak
more than is acceptable.
Section 2.7 Contamination and Coatings Engineering, and Planetary Protection
Section 2.7.1 Contamination
The first step is determination of contamination sensitivity. Sensitivity to contamination should
be based upon the optical, thermal, and mechanical system performance requirements.
Assessments should address all environments including materials outgassing, on-orbit and
thermal vacuum molecular transport, particle generation, materials degradation, thruster plume
impingement, solar radiation, atomic oxygen, charged particle effects, and any synergistic effects
among these environments. The primary payload may drive the contamination control
requirements for the cubesat system. For many cubesats, proper material selection and relatively
straightforward handling techniques may be sufficient to achieve the necessary contamination
control.
Section 2.7.2 Coatings Engineering
Since many cubesats have a short mission duration, the degradation of coatings from beginning
of life to end of life will likely be relatively small. GSFC Coatings Committee and thermal
engineering experts maintain the latest coatings performance information. Unproven coatings
should be reviewed by the GSFC Coatings Committee.
Section 2.7.3 Planetary Protection
Cubesats will be required to comply with planetary protection requirements if they are leaving
Earth orbit or going to the moon.
Section 2.8 End-to-End Testing
End-to-end testing per this section of GEVS is applicable to cubesats. It is easy to miss subtle
design issues that will cause problems in flight. Compatibility testing and mission simulations
provide an inexpensive way to retire these types of risks
Check the GSFC Technical Standards Program website at http://standards.gsfc.nasa.gov or contact the Executive
Secretary for the GSFC Technical Standards Program to verify that this is the correct version prior to use.
24 of 24