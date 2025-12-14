{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;\f1\froman\fcharset0 Garamond;\f2\ftech\fcharset0 Wingdings-Regular;
}
{\colortbl;\red255\green255\blue255;\red255\green255\blue254;\red216\green225\blue94;\red24\green39\blue67;
\red22\green64\blue129;\red20\green20\blue19;\red34\green121\blue130;\red50\green50\blue49;\red15\green147\blue73;
\red89\green25\blue82;\red236\green239\blue163;\red42\green55\blue83;\red80\green81\blue80;\red198\green12\blue32;
}
{\*\expandedcolortbl;;\cscmyk\c0\c0\c0\c0;\cscmyk\c13000\c0\c70000\c0;\cscmyk\c100000\c82000\c34000\c20000;
\cscmyk\c94500\c67700\c1500\c0;\cscmyk\c0\c0\c0\c100000;\cscmyk\c80000\c25000\c33000\c0;\cscmyk\c0\c0\c0\c85000;\cscmyk\c81400\c3600\c85400\c100;
\cscmyk\c60000\c100000\c20000\c5000;\cscmyk\c6500\c0\c35000\c0;\cscmyk\c85000\c69700\c28900\c17000;\cscmyk\c0\c0\c0\c70000;\cscmyk\c3000\c100000\c100000\c0;
}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\pardirnatural\partightenfactor0

\f0\fs18 \cf2 National Aeronautics and\
Space Administration\

\fs110 CubeSat 
\fs224 \cf3 101\

\fs60 \cf4 Basic Concepts and Processes for\
First-Time CubeSat Developers\

\fs30 \cf2 NASA CubeSat Launch Initiative\

\fs18 For Public Release \'96 Revision Dated October 2017
\fs110 \cf5 CubeSat 
\fs224 \cf3 101\

\fs60 \cf4 Basic Concepts and Processes for\
First-Time CubeSat Developers\

\fs30 \cf6 NASA CubeSat Launch Initiative\

\fs18 For Public Release \'96 Revision Dated October 2017
\fs19 \cf2 \uc0\u65279 \

\fs20 \cf7 Produced under contract by the\
\cf8 California Polytechnic State University, San Luis Obispo (Cal Poly) CubeSat Systems Engineer Lab\

\fs66 \cf2 Acknowledgements\

\fs20 \cf6 This guide was produced by the following to support NASA\'92s CubeSat Launch Initiative:\

\fs24 \cf2 Writers and Contributors\

\fs17 \cf9 California Polytechnic\'92s PolySat Program,\
California Polytechnic State University\'97\
San Luis Obispo\

\fs22 \cf6 Jamie Chin\
Roland Coelho\
Justin Foley\
Alicia Johnstone\
Ryan Nugent\
Dave Pignatelli\
Savannah Pignatelli\
Nikolaus Powell\
Jordi Puig-Suari\

\fs17 \cf9 NASA Launch Services Program\

\fs22 \cf6 William Atkinson, Kennedy Space Center\
Jennifer Dorsey, Kennedy Space Center\
Scott Higginbotham, Kennedy Space Center\
Maile Krienke, Kennedy Space Center\
Kristina Nelson, Kennedy Space Center/ai Solutions\
Bradley Poffenberger, Kennedy Space Center\
Creg Raffington, Kennedy Space Center\
Garrett Skrobot, Kennedy Space Center\
Justin Treptow, Kennedy Space Center\
Anne Sweet, NASA Headquarters\

\fs17 \cf9 NASA Advanced Exploration Systems Division\

\fs22 \cf6 Jason Crusan, NASA Headquarters\
Carol Galica, NASA Headquarters/Stellar Solutions\

\fs17 \cf9 NASA Space Communications and Navigation Division\

\fs22 \cf6 William Horne, NASA Headquarters Space\
Communications and Navigation Spectrum\
Management\

\fs17 \cf9 NASA Jet Propulsion Laboratory\

\fs22 \cf6 Charles Norton, Jet Propulsion Laboratory\
Formulation Lead for Small Satellites\

\fs17 \cf9 NOAA\

\fs22 \cf6 Alan Robinson, NOAA Commercial Remote Sensing\
Regulatory Affairs Office\

\fs24 \cf2 Editors and Graphic Designer\

\fs17 \cf9 Communications Support Services Center\

\fs22 \cf6 Maxine Aldred, NASA Headquarters/Media Fusion\
Andrew Cooke, NASA Headquarters/Media Fusion\
Tun Hla, NASA Headquarters/Media Fusion\
Michele Ostovar, NASA Headquarters/Media Fusion\
Jennifer Way, NASA Headquarters/Media Fusion\
For more information visit: \cf10 http://go.nasa.gov/CubeSat_initiative\

\fs26 \cf2 ii\

\fs18 \cf11 CubeSat 101\cf2 : Basic Concepts and Processes for First-Time CubeSat Developers \cf12 NASA CubeSat Launch Initiative
\fs22\fsmilli11050 \cf2 CubeSat\
101\

\fs78 Table of Contents\

\fs18 \cf6 Acknowledgments.  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . ii\
\cf13 Pictured above:\

\fs17 \cf8 NASA mentors and the student launch\
team for \cf9 StangSat\cf8  and \cf9 PolySat\cf8  go\
through final checks in the CubeSat lab\
facility at Cal Poly. [VAFB/Kathi Peoples]\

\fs26 \cf9 1 
\fs22 \cf6 Introduction 1\

\fs20 \cf5 1.1 \cf6 CubeSats . . . . . . . . . . . . . . . . . . . . . . . . 4\
\cf5 1.2 \cf6 CubeSat Dispenser Systems . . . . . . . . . . . . . . 4\

\fs18 \cf10 1.2.1 \cf6 3U Dispensers 5\
\cf10 1.2.2 \cf6 6U Dispensers 6\

\fs20 \cf5 1.3 \cf6 Launch Vehicles (LVs)\'97aka: Rockets . . . . . . . . . . 6\

\fs26 \cf9 2 
\fs22 \cf6 Development Process Overview 9\

\fs20 . . . . 11\
. . . . 11\
. . . . 14\
. . . . 15\
Response\
. . . . 17\
. . . . 18\
. . . . 19\
. . . . 20\
Submittal (10\'9612 months) . . . . . . . . . . . . . . . 21\
\cf5 2.1 \cf6 Concept Development (1\'966 months). . . . . . \cf5 2.2 \cf6 Securing Funding (1\'9612 months). . . . . . . . \cf5 2.3 \cf6 Merit and Feasibility Reviews (1\'962 months) . . \cf5 2.4 \cf6 CubeSat Design (1\'966 months). . . . . . . . . \cf5 2.5 \cf6 Development and Submittal of Proposal in to CSLI Call (3\'964 months) . . . . . . . . . . . \cf5 2.6 \cf6 Selection and Manifesting (1\'9636 months) . . . \cf5 2.7 \cf6 Mission Coordination (9\'9618 months). . . . . . \cf5 2.8 \cf6 Regulatory Licensing (4\'966 months) . . . . . . \cf5 2.9 \cf6 Flight-Specific Documentation Development and\

\fs18 \cf11 CubeSat 101\cf2 : Basic Concepts and Processes for First-Time CubeSat Developers \cf12 NASA CubeSat Launch Initiative\

\fs26 \cf2 iii
\fs22\fsmilli11050 CubeSat\
101\

\fs19 Table of Contents\

\fs20 \cf5 2.10 \cf6 Ground Station Design, Development, and Testing\
(2\'9612 months) . . . . . . . . . . . . . . . . . . . . . 22\
\cf5 2.11 \cf6 CubeSat Hardware Fabrication and Testing\
(2\'9612 months) . . . . . . . . . . . . . . . . . . . . . 23\
\cf5 2.12 \cf6 Mission Readiness Reviews (Half-Day). . . . . . . . . 25\
\cf5 2.13 \cf6 CubeSat-to-Dispenser Integration and Testing (2 days). 26\
\cf5 2.14 \cf6 Dispenser-to-Launch Vehicle Integration (1 day) . . . . 27\
\cf5 2.15 \cf6 Launch (1 day) . . . . . . . . . . . . . . . . . . . . 28\
\cf5 2.16 \cf6 Mission Operations (variable, up to 20 years) . . . . . 29\

\fs26 \cf9 3 
\fs22 \cf6 Mission Models 31\

\fs20 \cf5 3.1 \cf6 NASA-Procured Launch Vehicle Mission Model . . . . 32\
\cf5 3.2 3.3 \cf6 Operationally Responsive Space (ORS) Rideshare\
Mission Model. . . . . . . . . . . . . . . . . . . . . 34\
National Reconnaissance Office (NRO) Rideshare\
Mission Model. . . . . . . . . . . . . . . . . . . . . 35\
\cf5 3.4 \cf6 Commercial Launch Service Through a\
Third-Party Broker Mission Model. . . . . . . . . . . 37\
\cf5 3.5 \cf6 International Space Station (ISS)\
Deployment Mission Model . . . . . . . . . . . . . . 38\

\fs26 \cf9 4 
\fs22 \cf6 Requirement Sources for Launch 39\

\fs20 \cf5 4.1 \cf6 Mission-Specific Interface Control Documents (ICDs) . 40\
\cf5 4.2 \cf6 Launch Services Program (LSP)\'97\
Program-Level Requirements . . . . . . . . . . . . . 40\
\cf5 4.3 \cf6 CubeSat Design Specifications (CDS) . . . . . . . . . 40\
\cf5 4.4 \cf6 Dispenser Standards/Specifications. . . . . . . . . . 41\
\cf5 4.5 \cf6 Federal Statutes. . . . . . . . . . . . . . . . . . . . 41\
\cf5 4.6 \cf6 Range Safety Requirements. . . . . . . . . . . . . . 42\

\fs17 \cf9 ChargerSat-1\cf8 \'92s mission was\
developed by students from the\
University of Alabama, Huntsville\
to conduct three technology\
demonstrations: a gravity gradient\
stabilization system will passively\
stabilize the spacecraft; deployable\
solar panels will nearly double the\
power input to the spacecraft; and\
the same deployable solar panels will\
shape the gain pattern of a nadir-facing\
monopole antenna, allowing improved\
horizon-to-horizon communications.\
[University of Alabama, Huntsville]\

\fs26 \cf9 5 
\fs22 \cf6 Licensing Procedures 43\

\fs20 \cf5 5.1 \cf6 Radio Frequency (RF) Licensing. . . . . . . . . . . . 43\
\cf5 5.2 \cf6 Remote Sensing. . . . . . . . . . . . . . . . . . . . 51\

\fs26 \cf2 iv\

\fs18 \cf11 CubeSat 101\cf2 : Basic Concepts and Processes for First-Time CubeSat Developers \cf12 NASA CubeSat Launch Initiative
\fs22\fsmilli11050 \cf2 CubeSat\
101\

\fs19 Table of Contents\

\fs26 \cf9 6 
\fs22 \cf6 Flight Certification Documentation 53\

\fs20 \cf5 6.1 \cf6 Orbital Debris Mitigation Compliance . . . . . . . . . 54\
\cf5 6.2 \cf6 Transmitter Surveys . . . . . . . . . . . . . . . . . . 55\
\cf5 6.3 \cf6 Materials List . . . . . . . . . . . . . . . . . . . . . 55\
\cf5 6.4 \cf6 Mass Properties Report. . . . . . . . . . . . . . . . 56\
\cf5 6.5 \cf6 Battery Report . . . . . . . . . . . . . . . . . . . . 57\
\cf5 6.6 \cf6 Dimensional Verifications . . . . . . . . . . . . . . . 57\
\cf5 6.7 \cf6 Electrical Report . . . . . . . . . . . . . . . . . . . 58\
\cf5 6.8 \cf6 Venting Analysis. . . . . . . . . . . . . . . . . . . . 58\
\cf5 6.9 \cf6 Testing Procedures/Reports. . . . . . . . . . . . . . 59\

\fs18 \cf10 6.9.1 \cf6 Day In The Life (DITL) Testing 59\
\cf10 6.9.2 \cf6 Dynamic Environment Testing (Vibration/Shock) 60\
\cf10 6.9.3 \cf6 Thermal Vacuum Bakeout Testing 62\

\fs20 \cf5 6.10 \cf6 Compliance Letter. . . . . . . . . . . . . . . . . . . 64\
\cf5 6.11 \cf6 Safety Package Inputs (e.g., Missile System Prelaunch\
Safety Package, Flight Safety Panel). . . . . . . . . . 64\

\fs22 Appendices 65\

\fs20 \cf5 A \cf6 List of Abbreviations. . . . . . . . . . . . . . . . . . 65\
\cf5 B \cf6 Glossary . . . . . . . . . . . . . . . . . . . . . . . 66\
\cf5 C \cf6 Templates. . . . . . . . . . . . . . . . . . . . . . . 69\

\fs18 \cf10 1. \cf6 ODAR Inputs 69\
\cf10 2. \cf6 CubeSat Components ODAR Template 71\
\cf10 3. \cf6 Transmitter Survey 72\
\cf10 4. \cf6 Materials List 74\
\cf10 5. \cf6 Compliance Letter 77\
\cf10 6. \cf6 CubeSat Acceptance Checklists 79\

\fs20 \cf5 D \cf6 Technical Reference Documents for CubeSat\
Requirements. . . . . . . . . . . . . . . . . . . . . 84\
\cf5 E \cf6 Notional Timeline of Events/Deliverables. . . . . . . . 85\

\fs18 \cf11 CubeSat 101\cf2 : Basic Concepts and Processes for First-Time CubeSat Developers \cf11 CubeSat 101\cf2 : Basic Concepts and Processes for First-Time CubeSat Developers \cf12 NASA CubeSat Launch Initiative\
NASA CubeSat Launch Initiative\

\fs26 \cf2 v
\fs22\fsmilli11050 CubeSat\
101\

\fs224 \cf3 1
\fs78 \cf2 Introduction\

\fs22 IN THIS CHAPTER\

\fs20 \cf5 1.1 
\fs16 \cf6 CubeSats\

\fs20 \cf5 1.2 
\fs16 \cf6 CubeSat Dispenser Systems\

\fs18 \cf10 1.2.1 
\fs16 \cf6 3U Dispensers\

\fs18 \cf10 1.2.2 
\fs16 \cf6 6U Dispensers\

\fs20 \cf5 1.3 
\fs16 \cf6 Launch Vehicles (LV),\
aka: Rockets\

\fs67\fsmilli33624 H
\fs22 ow do you start a CubeSat project? As popular as CubeSats have become,\
it\'92s surprising how little information is out there to help someone just enter-\
ing the field. That\'92s why this document was created\'97to lay out everything you\
need to take a great CubeSat idea and make it into an actual spacecraft that is\
launched into orbit. If you\'92ve been involved in the CubeSat world for a while, this\
guide will be a good reference for anything on which you might need a refresher.\
However, this guide is written for first-time CubeSat developers, and especially\
for CubeSats being developed at educational institutions. So, if this is your first\
foray into CubeSats, you\'92ll want to read through carefully to get an idea of the\
scope and the amount of work this project will require.\
Before we get to the nitty-gritty, let\'92s start with a little\
background. CubeSats began as a collaborative effort in\
1999 between Jordi Puig-Suari, a professor at California\
Polytechnic State University (Cal Poly), and Bob Twiggs, a\
professor at Stanford University\'92s Space Systems Development\
Laboratory (SSDL). The original intent of the project was\
to provide affordable access to space for the university sci-\
ence community, and it has successfully done so. Thanks\
to CubeSats, many major universities now have a space\
program. But it\'92s not just big universities; smaller universi-\
ties, high schools, middle schools, and elementary schools\
have also been able to start CubeSat programs of their own.\

\fs18 \cf14 FIGURE 1
\fs22 \cf6  shows university students in their clean room taking\
measurements of a CubeSat they helped to develop. In addi-\
tion to educational institutions, Government agencies and\

\fs18 \cf13 Pictured above:\

\fs17 \cf8 Launch of NASA\'92s National Polar-\
orbiting Operational Environmental\
Satellite System (NPOESS) Preparatory\
Project (NPP) mission on Oct. 28,\
2011, which deployed five CubeSats\
as part of the Educational Launch of\
Nanosatellites (ELaNa)-III Mission. [U.S.\
Air Force/Staff Sgt. Andrew Satran]\

\fs20 \cf14 FIGURE 1:
\fs17 \cf8  University student taking measurements of\
a 2U CubeSat (CP9). [Cal Poly]\

\fs18 \cf11 CubeSat 101\cf2 : Basic Concepts and Processes for First-Time CubeSat Developers \cf12 NASA CubeSat Launch Initiative\

\fs26 \cf2 1
\fs22\fsmilli11050 CubeSat\
101\

\fs19 \cf11 CHAPTER 1\cf14  \cf2 Introduction\

\fs22 \cf6 commercial groups around the world have developed CubeSats. They recognized\
that the small, standardized platform of the CubeSat can help reduce the costs\
of technical developments and scientific investigations. This lowered barrier to\
entry has greatly increased access to space, leading to an exponential growth in\
the popularity of CubeSats since their inception. In addition, this world of small,\
affordable spacecraft has gotten more diverse and complicated each year, as more\
and more researchers find utility in these small packages.\
This document was created mainly for 
\fs18 \cf7 CubeSat developers
\fs22 \cf6  who are working\
with NASA\'92s CubeSat Launch Initiative (CSLI), but most chapters also will be\
useful to CubeSat developers launching through other organizations.\
What\'92s CSLI, you ask? CSLI is a NASA initiative that provides opportunities\
for qualified CubeSats to fly as auxiliary payloads on future launches that have\
excess capacity or as deployments from the International Space Station (ISS). In\
very simple terms that means that NASA will cover the cost of providing your\
CubeSat a ride to space in exchange for a report on the results of your CubeSat\
investigation.\
CSLI enables NASA to develop public-private partnerships that provide a low-\
cost platform for NASA science missions, including planetary exploration, Earth\

\fs20 \cf11 CubeSat developer:
\fs17  
\fs18 \cf2 You\'92ll\
hear this term a lot in the CubeSat\
world. This is the standard term for\
any person or organization that is\
designing, building, and preparing\
a CubeSat for flight.\

\fs17 \cf8 Illustration of ELaNa 23 \cf9 RadSat-G\
\cf8 CubeSat from Montana State\
University in orbit around Earth.\
[Montana State University]\

\fs26 \cf2 2\

\fs18 \cf11 CubeSat 101\cf2 : Basic Concepts and Processes for First-Time CubeSat Developers \cf12 NASA CubeSat Launch Initiative
\fs22\fsmilli11050 \cf2 CubeSat\
101\

\fs19 \cf11 CHAPTER 1\cf14  \cf2 Introduction\

\fs22 \cf6 observation, and fundamental Earth and space science.\
These efforts are a cornerstone in the development of cut-\
ting-edge NASA enabling technologies including laser\
communications, next generation avionics approaches,\
power generation, distributive sensor systems, sat-\
ellite-to-satellite communications, and autonomous\
movement. Leveraging these missions for collaboration\
optimizes NASA\'92s technology investments, fosters open\
innovation, and facilitates technology infusion. CubeSat\
missions are enabling the acceleration of flight-qualified\
technology assistance in raising Technology Readiness\
Levels, which aligns to NASA\'92s objective of advancing\
the Nation\'92s capabilities by maturing cross-cutting inno-\
vative space technologies. About half of all CSLI missions are conducting scientific investigations, most\
frequently Space Weather and Earth Science. Specific science investigation areas\
include: biological science, study of near Earth objects, climate change, snow/ice\
coverage, orbital debris, planetary science, space-based astronomy, and heliophys-\
ics. Sixty-six percent of all CSLI missions are conducting technology develop-\
ment or demonstrations. Communications, propulsion, navigation and control,\
and radiation testing lead the topics in this area. Other notable technologies are\
solar sails, additive manufacturing, femtosatellites, and smart phone satellites.\
The low cost of development for a CubeSat allows for conducting higher risk\
activities that would not be possible on large-scale NASA missions.\
To be eligible for CSLI, your CubeSat 
\fs18 \cf7 investigation
\fs22 \cf6  must be of clear bene-\
fit to NASA by supporting at least one goal or objective stated in the NASA\
Strategic Plan. This plan can be found on NASA\'92s Web site 
\f1 (
\f0\fs18 \cf10 http://www.nasa.\
gov
\fs22 \cf6 ). Each year\'97typically in early August\'97the CSLI solicits proposals through\
an Announcement of Partnership Opportunity (AoPO) on the Federal Business\
Opportunities Web site 
\f1 (
\f0\fs20 \cf10 https://sam.gov)
\fs22 \cf6 ; proposals are typically due in\
November of that same year.\
If you\'92d like to read more about CSLI, their Web page can be found at 
\fs18 \cf10 http://\
go.nasa.gov/CubeSat_initiative
\fs22 \cf6 .\

\fs17 \cf9 ARMADILLO\cf8  (Attitude Related\
Maneuvers And Debris Instrument in\
Low (L) Orbit) is a 3U CubeSat under\
development at the University of\
Texas at Austin. [University of Texas\
at Austin]\

\fs20 \cf11 investigation: 
\fs18 \cf2 This term gets\
used often when talking about\
a CubeSat\'92s mission. It refers\
to the investigation, scientific or\
otherwise, that your CubeSat will\
be performing. In this context,\
\'93investigation\'94 is commonly used\
interchangeably with a CubeSat\
\'93mission.\'94\
\cf11 CubeSat 101\cf2 : Basic Concepts and Processes for First-Time CubeSat Developers \cf12 NASA CubeSat Launch Initiative\

\fs26 \cf2 3
\fs19 \cf11 CHAPTER 1\cf14  \cf2 Introduction\

\fs32 \cf14 1.1 \cf4 CubeSats\

\fs22 \cf6 Let\'92s explain what the \'93CubeSat\'94 designation means,\
compared to other small satellites. A small satellite is\
generally considered to be any satellite that weighs less\
than 300 kg (1,100 lb). A CubeSat, however, must con-\
form to specific criteria that control factors such as its\
shape, size, and weight.\
The very specific standards for CubeSats help reduce\
costs. The standardized aspects of CubeSats make it\
possible for companies to mass-produce components\
and offer off-the-shelf parts. As a result, the engineer-\
ing and development of CubeSats becomes less costly\
than highly customized small satellites. The standard-\
ized shape and size also reduces costs associated with\
transporting them to, and deploying them into, space.\
CubeSats come in several sizes, which are based on the\
standard CubeSat \'93unit\'94\'97referred to as a 1U. A 1U\
CubeSat is a 10 cm cube with a mass of approximately\
1 to 1.33 kg. In the years since the CubeSat\'92s inception,\
larger sizes have become popular, such as the
\f1  1.5U,
\f0  2U, 3U, 6U, and 12U.\
Examples of a 1U and 3U are shown in 
\fs18 \cf14 FIGURE 2
\fs22 \cf6 .\
To get a better idea of the design requirements, take a look at the
\fs18 \cf7  CubeSat Design\
Specification (CDS)
\fs22 \cf6  at 
\fs18 \cf10 http://www.cubesat.org
\fs22 \cf6 . We\'92ll explain more about the\
CDS and the documents you will need in the Requirements Sources chapter. For\
now, checking out the CDS at the CubeSat Web site is a great place to start your\
preliminary design planning.\

\fs17 1U Standard\
Dimensions:\
10 cm \'d7 10 cm \'d7 11 cm\
3U Standard\
Dimensions:\
10 cm \'d7 10 cm \'d7 34 cm\

\fs20 \cf14 FIGURE 2:
\fs17 \cf8  1U CubeSat CP1 (left)\
3U CubeSat CP10 (right) [Cal Poly]\

\fs20 \cf11 CDS: 
\fs18 \cf2 The CDS is a set of general\
requirements for all CubeSats,\
but is not the official set of\
requirements that you will need to\
follow for your launch.\

\fs32 \cf14 1.2 \cf4 CubeSat Dispenser Systems\

\fs22 \cf6 We\'92ve described the CubeSat itself, but there\'92s another important piece of the\
puzzle: the dispenser, which is the interface between the CubeSat and the\
launch vehicle (LV). The dispenser provides attachment to a launch vehicle (or\
rocket), protects the CubeSat during launch, and releases it into space at the\
appropriate time.\

\fs26 \cf2 4\

\fs18 \cf11 CubeSat 101\cf2 : Basic Concepts and Processes for First-Time CubeSat Developers \cf12 NASA CubeSat Launch Initiative
\fs19 \cf11 CHAPTER 1\cf14  \cf2 Introduction\

\fs22 \cf6 There are a number of different types of dispensers on the market. Each has\
different features, but they are all designed to hold satellites that conform to the\
standard CubeSat 
\fs18 \cf7 form factor
\fs22 \cf6 .\
Chances are you won\'92t be choosing the dispenser for your CubeSat; that honor\
will go to whoever is footing the bill for the launch costs. It\'92s still important to\
understand the 
\fs18 \cf7 interface
\fs22 \cf6  between your CubeSat and the launch vehicle. To that\
end, this chapter will outline the types of dispensers with which you are likely\
to work.\

\fs20 \cf11 form factor:
\fs18  \cf2 This is a term used\
to describe the size, shape, and/\
or component arrangement of a\
particular device. When we use\
it in reference to the standard\
CubeSat, we\'92re referring to the\
specific size and mass that defines\
a CubeSat.\

\fs24 \cf11 1.2.1 \cf2 3U Dispensers\

\fs20 \cf11 interface:
\fs18 \cf2  \'93Interface\'94 is a general\
term that refers to any point\
where two or more components\
are joined together. For instance,\
someone may ask, \'93How does\
the CubeSat interface with the\
dispenser?\'94 or, \'93Is there an\
electrical interface between the\
CubeSat and the Dispenser?\'94\
(These questions mean, \'93Can I\
electrically connect the CubeSat\
to the dispenser somehow?\'94)\

\fs20 \cf14 FIGURE 3:
\fs17 \cf8  Poly-Picosatellite Orbital\
Deployer (P-POD) Developed by Cal\
Poly, San Luis Obispo. [Cal Poly]\

\fs22 \cf6 The first dispenser for CubeSats was\
the Poly-Picosatellite Orbital Deployer\
(P-POD). It was developed by Cal Poly,\
San Luis Obispo. The current revision\
of the P-POD is pictured in 
\fs18 \cf14 FIGURE 3
\fs22 \cf6 .\
It can hold up to three Us of CubeSat\

\fs18 \cf7 payload
\fs22 \cf6 (s) (meaning any combination\
that adds up to three Us, such as three\
1Us, two 1.5Us, one 3U, etc.) and bolts\
directly onto the launch vehicle. When\
it\'92s time to release the payload, the\
launch vehicle sends an electrical signal\
to the P-POD, which causes the door\
to open and release the CubeSat(s) into\
orbit. Although most dispensers on the market have different designs, they all\
tend to follow the same basic idea of a safe container with a door that opens at the\
launch vehicle\'92s command, which then ejects the CubeSat into space.\
In the beginning, the P-POD may have been the only option for CubeSats, but\
now there are several dispenser choices. The manufacturers and vendors are easy\
to find; just type keywords like \'93CubeSat dispenser\'94 into your favorite search\
engine and start clicking! Even though you might not have the final say in which\
dispenser you use, you should take some time to understand the different dis-\
pensers on the market and the kinds of features that are available before you start\
designing your CubeSat.\

\fs20 \cf11 payload:
\fs18 \cf2  In the aerospace\
industry, \'93payload\'94 is a general\
term used to describe the cargo\
(e.g., a satellite or spacecraft)\
being delivered to space. When\
we\'92re talking about CubeSat\
dispensers, the payload always\
refers to the CubeSat.\
\cf11 CubeSat 101\cf2 : Basic Concepts and Processes for First-Time CubeSat Developers \cf12 NASA CubeSat Launch Initiative\

\fs26 \cf2 5
\fs19 \cf11 CHAPTER 1\cf14  \cf2 Introduction\

\fs24 \cf11 1.2.2 \cf2 6U Dispensers\

\fs22 \cf6 After a number of successful launches using the 3U dispenser,\
developers quickly started planning for the next stage of\
CubeSat design: let\'92s make them bigger! And thus in 2014, the\
6U was born. The form factor of the 6U is essentially the same\
as two 3Us side-by-side, making it twice as wide. You can see\
an example of a 6U CubeSat in 
\fs18 \cf14 FIGURE 4
\fs22 \cf6 . Multiple companies\
within the industry have developed dispensers to accommodate\
the larger size. And\'97you guessed it\'97those companies can be\
found with a simple Internet search. The 6U dispensers\'92 fea-\
tures vary, but most allow for any CubeSat configuration (e.g.,\
one 6U, six 1Us, two 3Us, etc.), and function similarly to the\
3U dispensers.\

\fs20 \cf14 FIGURE 4:
\fs17 \cf8  Example of a 6U CubeSat\
(Dellingr CubeSat) [NASA]\

\fs32 \cf14 1.3 \cf4 Launch Vehicles (LVs)\'97aka: Rockets\

\fs22 \cf6 Finally, let\'92s talk about how the dispenser which contains your CubeSat will get\
into orbit. CSLI contracts with multiple launch services that allow CubeSats to\
hitch a ride. When the CubeSat/dispenser package was first dreamed up, the\
idea was to bolt the dispenser onto the rocket where space was available. That is\
still how most CubeSats make the journey, although there are now other options\

\fs17 \cf8 Students Jacob Hambur and\
Trisha Joseph from the University\
of Central Florida constructing the\
\cf9 Q-PACE\cf8  CubeSat. [University of\
Central Florida]\

\fs26 \cf2 6\

\fs18 \cf11 CubeSat 101\cf2 : Basic Concepts and Processes for First-Time CubeSat Developers \cf12 NASA CubeSat Launch Initiative
\fs22\fsmilli11050 \cf2 CubeSat\
101\

\fs19 \cf11 CHAPTER 1\cf14  \cf2 Introduction\

\fs20 \cf14 FIGURE 5: 
\fs17 \cf8 This United Launch Alliance (ULA) image shows where on the launch vehicle\
the CubeSats might be located for a typical ULA CubeSat mission. The inset pictures\
show a Naval Postgraduate School Cubesat Launcher Lite (NPSCul-Lite) housing eight\
3U P-PODs and attached to the LV via an Aft Bulkhead Carrier (ABC) plate. [United\
Launch Alliance]\

\fs22 \cf6 available (see 
\fs18 \cf14 FIGURE 5
\fs22 \cf6 ). For example, a CubeSat can be sent with\
the cargo on a resupply mission to the Space Station. The CubeSat\
would be taken aboard the Space Station and released into space in\
a specially designed deployer.\
You also may forgo the dispenser altogether, like the Peruvian\
Chasqui 1 did in 2014. During a spacewalk, a cosmonaut released\
Chasqui 1 from the Space Station by tossing it by hand into orbit.\
There\'92s even a video of this online! 
\fs18 \cf14 FIGURE 6
\fs22 \cf6  is a still from that video.\
Keep in mind that although it has been done, this type of release is\
extremely uncommon.\

\fs20 \cf14 FIGURE 6:
\fs17 \cf8  Russian cosmonaut preparing to launch\
a 1U CubeSat that he is holding in his hand. [NASA]\

\fs18 \cf11 CubeSat 101\cf2 : Basic Concepts and Processes for First-Time CubeSat Developers \cf12 NASA CubeSat Launch Initiative\

\fs26 \cf2 7
\fs22\fsmilli11050 CubeSat\
101\

\fs19 \cf11 CHAPTER 1\cf14  \cf2 Introduction\

\fs20 U.S. Launch Vehicles Used for\
CubeSat Launch\
\cf6 Super Strypi\
Minotaur I\
Minotaur IV\
Taurus XL\
Delta II\
Antares\
Falcon 9\
Atlas V\
Electron*\
Falcon 9 Heavy*\
LauncherOne*\
Space Launch System (SLS)*\

\fs17 \cf8 58.3 m\
17 m\

\fs16 \cf6 *\
 These launch vehicles have not flown CubeSats as of\
the writing of this document in 2017, but have included\
CubeSats in the manifests of upcoming flights.\

\fs17 Super Strypi\
Minotaur I\
Taurus XL\
Delta II\
Antares\
Falcon 9\
Atlas V\

\fs20 \cf14 FIGURE 7: 
\fs17 \cf8 U.S. Launch Vehicles Used for CubeSat Launches.\

\fs18 \cf14 FIGURE 7
\fs22 \cf6  shows all of the launch vehicles that have taken CSLI CubeSats to orbit\
as of the writing of this document in 2017, as well as launch vehicles that are\
planning to carry their first set of CubeSats on a future launch. Your CubeSat is\
by no means limited to the launch vehicles included on this list; any rocket could\
be a potential CubeSat launch vehicle given the right circumstances. The launch\
vehicle has to have additional performance margin, be going to your desired\
orbit, and can adapt to having dispensers installed.\

\fs26 \cf2 8\

\fs18 \cf11 CubeSat 101\cf2 : Basic Concepts and Processes for First-Time CubeSat Developers \cf12 NASA CubeSat Launch Initiative
\fs22\fsmilli11050 \cf2 CubeSat\
CubeSat\
101\
101\

\fs224 \cf3 2
\fs72 \cf2 Development\
Process Overview\

\fs22 IN THIS CHAPTER\

\fs20 \cf5 2.1 
\fs16 \cf6 Concept Development\

\fs20 \cf5 2.2 
\fs16 \cf6 Securing Funding\

\fs20 \cf5 2.3 
\fs16 \cf6 Merit and Feasibility Reviews\

\fs67\fsmilli33624 T
\fs22 his chapter will tell you everything you need to accomplish and provide\
an estimated timeline of how long it may take to get your CubeSat from\
a concept to a functioning satellite in orbit. We may be focusing on what you\
need to do specifically for CSLI, but the process for any CubeSat 
\fs18 \cf7 mission
\fs22 \cf6  will\
be very similar. The overall timeframe can vary depending on the launch vehicle\
selected and what you are trying to accomplish with your CubeSat. A CubeSat\
can be designed, built, tested, and delivered in as little as 9 months, but typically\
takes 18 to 24 months to complete. Once your CubeSat is ready to be delivered,\
the typical time to launch is anywhere from a few months to a few years. This\
is obviously affected by the availability of launch opportunities, but also by the\
flexibility of your orbital requirements\'97the more flexible, the easier to manifest\
and therefore, the shorter wait. Launch vehicles will usually require you to deliver\
your finished CubeSat between 4 weeks and 6 months prior to launch; again,\
this depends on the launch vehicle provider and the organization sponsoring\
your launch.\
The project phases (and typical timeframes) are as follows:\

\fs18 \cf5 1. 
\fs22 \cf6 Concept Development 
\fs18 \cf10 (1\'966 months)\
\cf5 2. 
\fs22 \cf6 Securing Funding 
\fs18 \cf10 (1\'9612 months)\
\cf5 3. 
\fs22 \cf6 Merit and Feasibility Reviews 
\fs18 \cf10 (1\'962 months)\
\cf5 4. 
\fs22 \cf6 CubeSat Design 
\fs18 \cf10 (1\'966 months)\
\cf5 5. 
\fs22 \cf6 Development and Submittal of Proposal in Response to CSLI Call 
\fs18 \cf10 (3\'964 months)\

\fs20 \cf5 2.4 
\fs16 \cf6 CubeSat Design\

\fs20 \cf5 2.5 
\fs16 \cf6 Development and Submittal of\
Proposal in Response to CSLI Call\

\fs20 \cf5 2.6 
\fs16 \cf6 Selection and Manifesting\

\fs20 \cf5 2.7 
\fs16 \cf6 Mission Coordination\

\fs20 \cf5 2.8 
\fs16 \cf6 Regulatory Licensing\

\fs20 \cf5 2.9 
\fs16 \cf6 Flight Specific Documentation\
Development and Submittal\

\fs20 \cf5 2.10 
\fs16 \cf6 Ground Station Design,\
Development, and Testing\

\fs20 \cf5 2.11 
\fs16 \cf6 CubeSat Hardware Fabrication\
and Testing\

\fs20 \cf5 2.12 
\fs16 \cf6 Mission Readiness Reviews\

\fs20 \cf5 2.13 
\fs16 \cf6 CubeSat-to-Dispenser Integration\
and Testing\

\fs20 \cf5 2.14 
\fs16 \cf6 Dispenser-to-Launch Vehicle\
Integration\

\fs20 \cf5 2.15 
\fs16 \cf6 Launch\

\fs20 \cf5 2.16 
\fs16 \cf6 Mission Operations\

\fs18 \cf13 Pictured above:\

\fs17 \cf9 CSUNSat-1\cf8  Team (Adam Kaplan,\
James Flynn, Donald Eckels) working on\
their CubeSat. [CSU-Northridge]\

\fs20 \cf11 mission: 
\fs18 \cf2 This term is a somewhat\
generic, all-encompassing term that\
refers to the enterprise as a whole.\
It\'92s sometimes used interchange-\
ably with \'93project\'94 or \'93investiga-\
tion\'94 and includes all phases from\
development, testing, integration, to\
launch and operations.\
\cf11 CubeSat 101\cf2 : Basic Concepts and Processes for First-Time CubeSat Developers \cf12 NASA CubeSat Launch Initiative\

\fs26 \cf2 9
\fs22\fsmilli11050 CubeSat\
101\

\fs19 \cf11 CHAPTER 2\cf14  \cf2 Development Process Overview\

\fs18 \cf5 6. 
\fs22 \cf6 Selection and Manifesting 
\fs18 \cf10 (1\'9636 months)\
\cf5 7. 
\fs22 \cf6 Mission Coordination 
\fs18 \cf10 (9\'9618 months)\

\fs22 \cf6 Once this phase begins, a schedule will be provided by the integrator\
that will dictate hardware and documentation delivery dates, essentially\
providing the completion dates for the subsequent phases.\

\fs18 \cf5 8. 
\fs22 \cf6 Licensing 
\fs18 \cf10 (4\'966 months)\
\cf5 9. 10. 11. 
\fs22 \cf6 Flight-Specific Documentation Development and Submittal 
\fs18 \cf10 (10\'9612 months)\

\fs22 \cf6 Ground Station Design, Development, and Testing 
\fs18 \cf10 (2\'9612 months)\

\fs22 \cf6 CubeSat Hardware Fabrication and Testing 
\fs18 \cf10 (2\'9612 months)\
\cf5 12. 
\fs22 \cf6 Mission Readiness Reviews 
\fs18 \cf10 (half-day)\
\cf5 13. 14. 
\fs22 \cf6 CubeSat to Dispenser Integration and Testing 
\fs18 \cf10 (1 day)\

\fs22 \cf6 Dispenser to Launch Vehicle Integration 
\fs18 \cf10 (1 day)\
\cf5 15. 
\fs22 \cf6 Launch 
\fs18 \cf10 (1 day)\
\cf5 16. 
\fs22 \cf6 Mission Operations 
\fs18 \cf10 (variable, up to 20 years)\
\cf6 Note: \cf14 FIGURE 8\cf6  and \cf10 Appendix E\cf6  provide a notional timeline of events and deliverables.\
It will give you an idea of the timeframes that can overlap if your resources permit.\

\fs13\fsmilli6655 Concept Development\
Funding\
Merit/Feasibility Reviews\
Develop/Submit Proposal\
CSLI Selection Process\
Manifesting\
Mission Coordination\
Licensing\
Document Development/\
Submission\
Ground Station Development\
and Testing\
Flight Hardware Fabrication\
Readiness Reviews\
Dispenser Integration\
Launch Vehicle Integration\
Launch and Mission Operations\
Months\

\fs20 \cf14 FIGURE 8:
\fs17 \cf8  This notional timeline shows how these phases might come together for a project.\

\fs26 \cf2 10 
\fs18 \cf11 CubeSat 101\cf2 : Basic Concepts and Processes for First-Time CubeSat Developers \cf12 NASA CubeSat Launch Initiative
\fs22\fsmilli11050 \cf2 CubeSat\
101\

\fs19 \cf11 CHAPTER 2\cf14  \cf2 Development Process Overview\

\fs32 \cf14 2.1 \cf4 Concept Development (1\'966 months)\

\fs22 \cf3 > \cf2 FREE ADVICE\

\f2 \cf3 >\

\f0 \cf6 Okay, first things first: What do you want your CubeSat to do? As we mentioned\
in 
\fs18 \cf10 Chapter 1
\fs22 \cf6 , it is important to choose a mission goal in which the CSLI, that is,\
NASA, will be interested. You may also consider choosing a concept for which\
it will be easy to find funding. Many CubeSat missions are designed around the\
goals of a sponsor who will cover most of the development costs (more on that in\

\fs18 \cf10 Chapter 2.2
\fs22 \cf6 ). For your best chance of being selected by CSLI, check off as many\
\'93Keys to CSLI Selection\'94 (see the \'93Free Advice\'94 inset on the right) as you can.\
There\'92s no real time limit to this early concept development phase. Typically, a\
CubeSat developer will take anywhere from 1 to 6 months to plan the goals and\
basic details of the CubeSat concept.\
By the way, there\'92s no need to go it alone. Part of this conceptual development\
time will be spent in search of possible partners and collaborators who may have\
goals similar to your own. This is called 
\fs18 \cf7 strategic partnering
\fs22 \cf6 , and may provide\
you with extra funding or expertise, or both.\

\fs18 \cf14 FLEXIBILITY IS KEY. \cf8 Keep your\
mission as flexible as possible.\
CSLI may select your CubeSat\
mission because it has some\
great science goals, but that\
doesn\'92t guarantee you\'92ll get a\
launch right away. If you need\
special considerations like a very\
specific orbit or specific launch\
date, finding a launch could be\
tricky. Do your best to keep your\
requirements for launch as flexible\
as possible.\
\cf4 Keys to CSLI Selection\
\cf8 \'95\
Adequate funding\
\'95\
Great merit and feasibility\
reviews\
\'95\
Clear demonstration of benefit\
to NASA\

\fs32 \cf14 2.2 \cf4 Securing Funding (1\'9612 months)\
\cf14 WARNING!\

\fs18 \cf8 Under CSLI, NASA will cover all costs associated with the launch (up to\
$300,000, typically enough to launch a 3U into low-Earth orbit), but \cf14 CubeSat\
developers selected for a CSLI flight are responsible for any and all\
expenses related to the development and operation of the CubeSat\cf8 . This\
includes all materials and labor required to build the CubeSat, plus the testing\
expenses, ground station development and operational expenses, as well as\
travel costs for required CSLI meetings and delivery.\

\fs20 \cf11 strategic partnering:\

\fs18 \cf2 Sometimes a CubeSat mission\
is too ambitious for a single\
organization to undertake. In\
that case, a strategic partnership\
can combine the strengths and\
resources of multiple organizations\
to achieve greater goals. These\
strategic partnerships are typically\
formalized by some kind of formal\
agreement.\

\fs22 \cf6 Money is very important. Once your CubeSat is selected and manifested for a\
flight, CSLI will begin spending NASA dollars on your behalf. If you run out\
of funds and cannot complete your CubeSat, NASA may not be able to apply\
completed activities (\'93sunk costs\'94) to a replacement CubeSat. If this happens, a\
launch opportunity will have been lost and it could even cause the demanifest of\
other CubeSats co-manifested on the same launch. Additionally, the Cooperative\
Research and Development Agreement (CRADA) that you sign with NASA after\
being manifested requires you to reimburse NASA for any integration and launch\

\fs18 \cf11 CubeSat 101\cf2 : Basic Concepts and Processes for First-Time CubeSat Developers \cf12 NASA CubeSat Launch Initiative\

\fs26 \cf2 11
\fs22\fsmilli11050 CubeSat\
101\

\fs19 \cf11 CHAPTER 2\cf14  \cf2 Development Process Overview\

\fs22 \cf6 costs incurred if you don\'92t deliver your CubeSat on time. This hasn\'92t happened to\
anyone yet, but it could! Therefore, do not accept a launch opportunity until\
you are confident you can deliver your CubeSat on time. As part of your pro-\
posal to CSLI, you will need to provide enough budgetary information to prove\
that you\'92ve secured enough funding to get you across the finish line.\
That being said, there is plenty of money out there for CubeSat projects, you just\
need to know where to look. Let\'92s take a look at where you can get the money you\
need for your space mission!\
Designing a CubeSat around a specific mission you came up with on your own\
may be your dream, but it may be difficult to find funding. There are, however,\
requests for proposals (RFPs) sent out every year from organizations looking for\
people who can help them perform missions that would be perfect for a CubeSat.\
The National Science Foundation has funded a number of CubeSats in the past,\
as has NASA\'92s Earth Science Technology Office (ESTO). A simple Internet\
search could help you find similar organizations looking for a great team to help\
them out. These organizations would work with your team and cover some or all\
of the development costs. For university students interested in starting a CubeSat\
project, another option is to inquire with faculty and administrators at your col-\
lege or university. Someone there may think that funding your project would be\
an impressive feather in the university\'92s cap. In addition, every state has a NASA\

\fs18 \cf10 Space Grant Consortium
\fs22 \cf6 , which provides resources in support of students pur-\
suing careers in science, technology, engineering, and mathematics, or STEM.\
So, what\'92s the bottom line? How much is a CubeSat project going to cost?\
Unfortunately, there isn\'92t a standard price tag we can show you. The amount of\
funding you\'92re going to need to budget\
for depends on a number of different\
factors, the most important of which\
include the mission\'92s complexity, the\
experience level of your personnel, the\
project\'92s duration, and whether you\
need any specialized hardware (see\

\fs18 \cf14 FIGURE 9
\fs22 \cf6 ).\
Before you start searching for fund-\
ing, be sure to research the mission\'92s\
requirements and create a detailed cost\
estimate to avoid the pitfalls of being\

\fs17 \cf8 Students Alex Diaz and Riki\
Munakata of California Polytechnic\
State University testing the \cf9 LightSail\
\cf8 CubeSat. LightSail is a citizen-funded\
technology demonstration mission\
sponsored by the Planetary Society\
using solar propulsion for CubeSats.\
[The Planetary Society]\

\fs24 \cf10 Common Costs Associated\
with Developing a CubeSat\

\fs18 \cf6 Materials Labor Environmental\
Testing\
Travel\

\fs20 \cf14 FIGURE 9:
\fs17 \cf8  Common costs associated with developing a CubeSat.\

\fs26 \cf2 12 
\fs18 \cf11 CubeSat 101\cf2 : Basic Concepts and Processes for First-Time CubeSat Developers \cf12 NASA CubeSat Launch Initiative
\fs22\fsmilli11050 \cf2 CubeSat\
101\

\fs19 \cf11 CHAPTER 2\cf14  \cf2 Development Process Overview\

\fs22 DID YOU KNOW?\
\cf4 Crowdfunding\

\fs18 \cf8 It\'92s probably crossed your mind already, and yes, crowdfunding is an option.\
You may not be able to get all of the money you need through crowdfunding,\
but CubeSat developers have used this method in the past. Just be aware that\
what makes for a popular crowdfunding idea does not necessarily mean it is a\
good CSLI idea.\
One of the most successful crowdfunded CubeSats is LightSail, developed by\
The Planetary Society (TPS). Carl Sagan was one of the founding members of\
TPS, and now the famous science educator Bill Nye holds the reins as CEO.\
LightSail is their flagship project. It\'92s a 3U CubeSat that is designed to unfurl a\
32-square-meter sail, with the intent of propelling itself by sailing on the Sun\'92s\
radiation. So far, one LightSail CubeSat has been launched as a technology\
demonstration through CSLI. It\'92s an ambitious project\'97and according to\
the Kickstarter Web site, LightSail-2 has raised over $1.24 million. Your team\
might not have the media resources that TPS does (meaning you won\'92t get a\
million dollars), but other teams have acquired more realistic amounts through\
crowdfunding, so it could be a viable option for your team.\

\fs22 \cf4 Technology Demonstration Missions\

\fs18 \cf8 A number of CubeSat missions have been funded by Government agencies\
or commercial organizations to perform technology demonstrations. For\
example, say someone at NASA JPL is working on a $100 million satellite and\
will include some brand new technology that hasn\'92t been to space yet. To lower\
the risk to their own very expensive satellite mission, JPL will help someone\
else to incorporate this new component on a CubeSat platform to take it for\
an inexpensive test drive. This is an excellent option for newer organizations\
and universities that want to get experience building CubeSats, but don\'92t have\
significant resources.\

\fs17 \cf9 KickSat\cf8  is a technology\
demonstration mission designed\
by Zachary Manchester of Cornell\
University to demonstrate the\
deployment and operation of 104\
Sprite \'93ChipSats\'94 developed at the\
university. KickSat was funded by\
over 300 individual backers on the\
crowdfunding Web site KickStarter.\
KickSat was launched by NASA\'92s\
CubeSat Launch Initiative on the\
ELaNa V mission as an auxiliary\
payload aboard the SpaceX-3 Cargo\
Resupply Mission on April 18, 2014.\
[Cornell University]\

\fs22 \cf6 underfunded. To build a cost estimate, start by looking online for component\
suppliers. That will help you get an idea of the costs of materials. We\'92ll include\
more details about components in the design chapter (
\fs18 \cf10 Chapter 2.4
\fs22 \cf6 ). Funding will\
also need to cover your ground station (see 
\fs18 \cf10 Chapter 2.10
\fs22 \cf6 ) and any environmental\
testing, which can include vibration, thermal vacuum bakeout, shock, and elec-\
tromagnetic interference/electromagnetic compatibility (EMI/EMC) testing (See\

\fs18 \cf10 Chapter 6
\fs22 \cf6  for test descriptions), plus anything else the launch vehicle provider\
wants to throw at you. When possible, project reserves of at least 10% should be\
part of the budget to address any unexpected events. One common cost that is\
often overlooked is the cost for travel. CubeSat developers are typically required\
to travel to at least one review, and later to deliver the CubeSat for integration\

\fs18 \cf11 CubeSat 101\cf2 : Basic Concepts and Processes for First-Time CubeSat Developers \cf12 NASA CubeSat Launch Initiative\

\fs26 \cf2 13
\fs22\fsmilli11050 CubeSat\
101\

\fs19 \cf11 CHAPTER 2\cf14  \cf2 Development Process Overview\

\fs22 \cf6 into its dispenser. All of these items should be included in your cost estimate.\
CSLI will only cover the costs of the launch, which include the CubeSat dis-\
penser, the 
\fs18 \cf7 integration services
\fs22 \cf6 , and the launch itself. 
\fs32 \cf14 2.3 \cf4 Merit and Feasibility Reviews (1\'962 months)\

\fs20 \cf11 integration services:
\fs18 \cf2  This\
normally includes, at a minimum,\
review of your deliverables,\
the dispenser, integrating your\
CubeSat into the dispenser,\
any testing that is done on the\
dispenser/CubeSat system,\
and physically integrating the\
dispenser/CubeSat system onto\
the launch vehicle.\

\fs22 \cf6 As part of your proposal to CSLI, your team will be required to perform a merit\
review and a feasibility review. These reviews help assure mission stakeholders\
(and everyone else involved in the mission, i.e. CSLI, the launch vehicle provider,\
other sponsors, etc.) that your team or organization is capable of fulfilling your\
obligations and completing a successful and worthwhile mission. Your team will\
organize these reviews, and you will choose the reviewers. And to make sure\
everything is on the up-and-up, the review panel must be made up of individ-\
uals who are not on the project team. For the merit review, choose reviewers\
who have knowledge/experience with your focus area (science, technology and/\
or education) and that can assess why a flight opportunity is required. For the\
feasibility review, choose reviewers ideally with knowledge of space flight and\
spacecraft, but otherwise knowledgeable in various areas of hardware and project\
development and that can assess your team\'92s ability to deliver your spacecraft on\
time and on budget. If your focus area includes science or technology, be sure to\
include someone knowledgeable on that specific area. Keep in mind that you are\
not just trying to check a box; you want honest, valuable, and useful feedback to\
your objectives and design, so that you can improve your chances of a successful\
proposal and successful mission.\
The exact details for these reviews will be stated in CSLI\'92s official call for propos-\
als, but a basic synopsis is included here for your reference.\
\cf4 Merit Review\
\cf6 Before submitting your proposal to CSLI, your CubeSat\'92s intended\
mission must pass an intrinsic merit review. This review will assess\
the goals and objectives of the mission to determine the quality of its\
investigation in regard to science, education, and/or technology. It will\
also determine if the overall investigation supports one or more of the\
science, education, technology, and/or operations goals or objectives of\
the NASA Strategic Plan. The more closely your mission aligns with a\
goal or objective of the NASA Strategic Plan, the more likely it is that\
your CubeSat will be selected.\

\fs17 \cf8 Integration of the NRO\'92s Government\
Rideshare Advanced Concepts\
Experiment (GRACE) carrying\
multiple payloads, which were\
included as auxiliary payloads aboard\
NROL-55. GRACE contained 13\
CubeSats, including 4 of NASA\'92s\
CubeSat Launch Initiative CubeSats,\
as part of the ELaNa XII mission.\
[Cal Poly]\

\fs26 \cf2 14 
\fs18 \cf11 CubeSat 101\cf2 : Basic Concepts and Processes for First-Time CubeSat Developers \cf12 NASA CubeSat Launch Initiative
\fs22\fsmilli11050 \cf2 CubeSat\
101\

\fs19 \cf11 CHAPTER 2\cf14  \cf2 Development Process Overview\

\fs22 \cf4 Feasibility Review\
\cf6 In addition to the merit review, your team must also complete and\
pass a feasibility review prior to submitting the proposal. This review\
will judge whether your CubeSat\'92s mission is achievable with regard to\
\'93technical implementation,\'94 including feasibility, resiliency, risk, and\
the probability of success. Bottom line: Is this mission even possible,\
and can your team get it done?\
CSLI is not only interested in the outcomes of the merit and feasibility\
review but also how you addressed any findings from the reviews to resolve\
any issues or concerns identified by the reviewers.\

\fs32 \cf14 2.4 \cf4 CubeSat Design (1\'966 months)\

\fs22 \cf6 You will probably begin your design process with a lot of research. CubeSats\
have been around for a while now, and there are plenty of developers who have\
already made mistakes from which you can learn. Most of these developers are\
also very open and eager to share their successes and failures with others. There\
is plenty of material published online that may prove useful to you. We would\
also recommend attending one of the many annual conferences where you can\
meet and chat with members of the CubeSat community. A problem that may\
seem impossible to you might be old hat to someone who\'92s been working in this\
field for a while.\
You will also need to research which components will work best for your CubeSat\
system. Luckily for you, CubeSats have become increasingly popular, and the\
availability of commercial off-the-shelf parts has vastly increased. Although most\
popular components can now be purchased through commercial vendors, many\
educational organizations still try to build and design as many components as\
possible in-house in order to enhance the educational experience, as well as to\
keep costs low. Because new companies are entering the marketplace every year,\
we can\'92t give you a complete list of CubeSat component vendors, but an Internet\
search will reveal a number of useful suppliers. A list of companies that sup-\
ply CubeSat components can also be found at 
\fs18 \cf10 http://www.cubesat.org
\fs22 \cf6  on the\
Developer Resources page. The list on this page is updated regularly, but it isn\'92t\
meant to be a complete list of every vendor on the market.\

\fs17 \cf8 Students Sergei Posnov, David\
Einhorn, Thompson Cragwell, and\
Maria Kromis are working on the\
\cf9 ANDESITE \cf8 CubeSat from Boston\
University. ANDESITE will measure\
small-scale spatial magnetic features\
in the auroral current systems. The\
measurements will be made through\
a constellation of picosatellites\
deployed by the main payload and\
will communicate over a mesh\
network. [Boston University]\

\fs18 \cf11 CubeSat 101\cf2 : Basic Concepts and Processes for First-Time CubeSat Developers \cf12 NASA CubeSat Launch Initiative\

\fs26 \cf2 15
\fs22\fsmilli11050 CubeSat\
101\

\fs19 \cf11 CHAPTER 2\cf14  \cf2 Development Process Overview\

\fs22 \cf3 > \cf2 FREE ADVICE\

\f2 \cf3 >\

\f0\fs18 \cf14 KEEP IT SIMPLE.
\fs20  
\fs18 \cf8 Keep the design as simple as possible.\
CDS requirements are on the conservative side.\
The CDS prohibits pyrotechnics, and discourages\
a host of other cool stuff. Some violations would be\
unacceptable, but some may be waived or approved\
on a mission-by-mission basis. You will, however,\
be eligible for more launches if you adhere to these\
specifications. Things like a propulsion system may\
make the launch provider or their primary payload\
nervous, and some just choose not to carry CubeSats\
that have them. So CSLI may still select your CubeSat\
for launch but it may take longer to find a willing launch\
provider to give you a ride.\
\cf14 IMPORTANT COMPONENTS SHOULD BE ON THE EXTERIOR.
\fs20  
\fs18 \cf8 No\
matter how well you plan and design your CubeSat, it\'92s\
almost certain that something will break. Usually this\
happens during environmental testing (i.e., vibration/\
shock testing). This is normal for a new design, but\
there are things you can do to make the repair work\
simpler and quicker. Most of the time, if you need to fix\
something on the inside of your structure (i.e., remove\
panels and take things apart), you will be required to\
perform certain testing again. However, if you design\
your CubeSat so that important components are near\
the exterior and easy to access, then the rework may be\
simple and retest might not be necessary.\
\cf14 DO NOT DESIGN TO THE LIMITS OF THE ENVELOPE.
\fs20  
\fs18 \cf8 The\
CDS defines the standard CubeSat \'93envelope\'94\'97that\
is to say, the length, height, and width dimensions of\
the CubeSat body\'97very specifically. It\'92s extremely\
important that your CubeSat measurements fall\
within the tolerances set in the CDS. If your CubeSat\
doesn\'92t fit, it doesn\'92t fly. It\'92s a pretty terrible feeling\
to deliver your satellite and find out it won\'92t fit in the\
dispenser, so make sure your design targets the optimal\
dimension measurement, and the rest will be down to\
manufacturing. Pay attention to any planned protrusions\
as well. The CDS allows protrusions from the CubeSat\
body up to 6.5 mm from the surface. Most deployers\
can accommodate something a little longer, but that\'92s\
a dangerous path to walk. Simply put, as long as your\
CubeSat stays within the dimensional bounds of the\
CDS, there should be no problem when you deliver it.\
\cf14 DOUBLE UP ON THAT BURN WIRE. \cf8 You may not know what\
burn wire is yet, but don\'92t worry, it\'92s a very simple (and\
pretty reliable) method for constraining deployable\
components. A lot of CubeSats use deployable solar\
panels to increase their Sun exposure, and virtually all\
CubeSats use some form of deployable antenna. Before\
the CubeSat is released into orbit, these deployables\
need to be constrained. The most common method\
to constrain a deployable is to tie a fishing line to its\
component and route the other end around a simple\
resistor, also called the burn wire. When it\'92s time to\
release the deployables, a current is run through the\
resistor. When the resistor produces enough heat, the\
fishing line melts and releases the deployable. The\
only problem with this method is that sometimes the\
fishing line comes loose during vibration testing or\
ascent. Launch providers hate that. Use two separate\
burn wires to give yourself, and the launch providers,\
some peace of mind. It should reduce the likelihood of a\
deployable coming loose prematurely during testing.\
\cf14 USE FAMILIAR COMPONENTS.
\fs20  
\fs18 \cf8 Whenever possible, choose\
major components that have flown on CubeSats before.\
Major components include batteries, antennas, and\
attitude determination and control systems (\cf7 ADCS\cf8 ). You\
aren\'92t restricted to using components that have flight\
heritage, but it reduces the risk of failure and gives the\
launch provider more confidence that your CubeSat\
won\'92t create problems.\
\cf14 USE UL LISTED BATTERIES.
\fs20  
\fs18 \cf8 If a battery is \'93UL listed\'94 it\
means that the company UL, LLC, has given this battery\
its stamp of approval, which is recognized industrywide.\
UL puts batteries through a specific round of testing that\
shows the batteries are reliable and meet certain industry\
specifications (i.e., environmental, testing to predetermine\
levels). Developers across the board prefer to use\
UL-certified batteries. If you use a battery without the UL\
certification or try to make your own battery, the launch\
provider will require you to perform extra testing on your\
batteries to prove their robustness. The same goes if you\
tamper with a UL listed battery or its safety features.\
\cf14 USE OF HIGH-MELTING POINT MATERIALS.\cf8  (See inset in\
\cf10 Chapter 6.1\cf8 )\

\fs26 \cf2 16 
\fs18 \cf11 CubeSat 101\cf2 : Basic Concepts and Processes for First-Time CubeSat Developers \cf12 NASA CubeSat Launch Initiative
\fs22\fsmilli11050 \cf2 CubeSat\
101\

\fs19 \cf11 CHAPTER 2\cf14  \cf2 Development Process Overview\

\fs22 \cf6 You\'92ll want to get started on your design as soon as possible. Depending on the\
level of expertise of your team, you will encounter a number of setbacks during\
development, so it\'92s very prudent to give yourself as much time as possible.\
To help you avoid some of those setbacks, we\'92ve started a list of design consid-\
erations for you to check out. (See Free Advice on the preceding page.) Almost\
everything on this list is derived from real-world experiences and mishaps that\
have cost developers valuable time and have given everyone involved extra truck-\
loads of stress.\

\fs20 \cf11 ADCS:
\fs18 \cf2  The ADCS is the system\
designed to stabilize and orient\
the CubeSat toward a given\
direction. This is a critical system\
for mission success. If the satellite\
needs to point its solar panels\
toward the Sun to get the most\
power possible or if you are taking\
images of the Earth its attitude has\
to be set to the correct value.\

\fs32 \cf14 2.5 \cf4 Development and Submittal of Proposal in\
Response to CSLI Call (3\'964 months)\

\fs22 \cf6 We won\'92t get into too much detail about what needs to be in your proposal. The\
specific proposal instructions for any Announcement of 
\f1 Partnership\

\f0 Opportunity (A
\f1 oP
\f0 O) sent out by CSLI are detailed in the official\
announcement posted at 
\fs20 \cf10 https://sam.gov
\fs18  
\fs22 \cf6 or
\fs18 \cf10  http://go.nasa.gov/\
CubeSat_initiative
\fs22 \cf6 . Timelines may vary, but proposals are usually due within 4\
months of the AoPO being posted. Typically, the AoPO is posted in early\
August and the proposals are due in November. Instructions on how to submit\
the proposal are included in the AoPO. Typically, CSLI requests that the proposal\
be e-mailed to a specific NASA representative.\
It\'92s extremely important to follow the AoPO instructions, and to include all of\
the requested information in your proposal. If the CSLI proposal evaluation\
team finds that your proposal is not compliant with the AoPO, or is lacking\
any of the information required by the AoPO, then your proposal will be\
removed from consideration for that selection period. You will need to rework\
your proposal and resubmit it to a future AoPO in a subsequent year.\
Remember when writing your proposal to emphasize how your CubeSat mis-\
sion satisfies all of the points listed in Keys to CSLI Selection in 
\fs18 \cf10 Chapter 2.1
\fs22 \cf6 .\
When submitting your proposal to CSLI, you will be asked to denote your project\'92s\
focus area(s): science, technology investigation and/or education. If you choose to\
select more than one focus area, your proposal and reviews must address the goals\
and objectives you will be meeting for each focus area. For example, if you choose\
science and education, your proposal will be reviewed equally for the quality of\
your science investigation and your education outcomes described in your sub-\
mission. Using this example, a proposal with a strong science investigation could\

\fs17 \cf8 The \cf9 St. Thomas More Cathedral\
School (STM)Sat-1\cf8  mission is\
an education mission to provide\
hands-on, inquiry-based learning\
activities with an on-orbit mission\
to photograph Earth and transmit\
images. STMSat-1 was the first\
CubeSat launched for a primary\
school. It was launched by NASA\'92s\
CubeSat Launch Initiative on the\
December 6, 2015 ELaNa IX mission\
on the fourth Orbital-ATK Cygnus\
Commercial Resupply Services (CRS)\
to the Space Station and deployed\
on May 16, 2016. [St. Thomas More\
Cathedral School]\

\fs18 \cf11 CubeSat 101\cf2 : Basic Concepts and Processes for First-Time CubeSat Developers \cf12 NASA CubeSat Launch Initiative\

\fs26 \cf2 17
\fs22\fsmilli11050 CubeSat\
101\

\fs19 \cf11 CHAPTER 2\cf14  \cf2 Development Process Overview\

\fs22 \cf6 receive a substantially lower review if the proposal doesn\'92t contain an equally\
strong education plan. Therefore, choose wisely and conservatively.\
After the CubeSat has been selected it will be manifested on a mission. At that\
time NASA and the CubeSat developer will enter into a contract with a lot\
of legal jargon (e.g., liability, risk, data-sharing, etc.). This contract is called a\
CRADA, which stands for Cooperative Research And Development Agreement.\
NASA will write up this contract and send it to you, the CubeSat developer.\
But because there are real legal consequences involved with this contract, you\
are strongly advised to have a legal expert review it with you. Most CubeSat\
developers send it to their sponsoring institution\'92s legal department. In the case\
of university CubeSat projects, the university\'92s legal department typically reviews\
the agreement.\

\fs17 \cf8 A set of NanoRacks CubeSats is\
photographed by an Expedition 38\
crew member after the deployment\
by the Small Satellite Orbital Deployer\
(SSOD). [NASA]\

\fs32 \cf14 2.6 \cf4 Selection and Manifesting (1\'9636 months)\

\fs22 \cf6 Once proposals have been submitted, CSLI\'92s Selection Recommendation\
Committee will determine which proposals meet all of the standards outlined in\
the A
\f1 oP
\f0 O and will create a prioritized list of the qualifying CubeSat projects.\
How do you get your CubeSat to the top of the priority list? First, your merit and\
feasibility reviews need to look great. Second, make sure your proposal hits all\
of the points in 
\fs18 \cf10 Chapter 2.1 Keys to CSLI Selection
\fs22 \cf6 . Third, make sure your pro-\
posal clearly shows how you contribute to meeting one or more goals/objectives\
in the NASA Strategic Plan. Your proposal needs to be interesting and\'97if at all\
possible\'97groundbreaking.\
Having priority doesn\'92t mean you\'92ll be manifested on the next CSLI launch,\
because you still need to be matched with a launch that will work for your mission\
parameters. However, having priority over the other CubeSat teams means you\
get \'93dibs\'94 on the first launch that matches your criteria. NASA Launch Services\
Program (LSP) will pair the selected CubeSats with launch opportunities that are\
best suited for the CubeSats\'92 missions and completion dates, taking into account\
the planned orbit and any special constraints the CubeSat\'92s mission may have.\
Once the CubeSats are paired and manifested, an ELaNa mission number will\
be assigned.\
The prioritized selection list will be released approximately 12 to 16 weeks after\
the proposal deadline. Prior awards can be viewed at the NASA CSLI Web site.\

\fs20 \cf11 manifesting:
\fs18 \cf2  The process\
of assigning CubeSats to the\
available slots on a launch\
opportunity.\

\fs26 18 
\fs18 \cf11 CubeSat 101\cf2 : Basic Concepts and Processes for First-Time CubeSat Developers \cf12 NASA CubeSat Launch Initiative
\fs22\fsmilli11050 \cf2 CubeSat\
101\

\fs19 \cf11 CHAPTER 2\cf14  \cf2 Development Process Overview\

\fs32 \cf14 2.7 \cf4 Mission Coordination (9\'9618 months)\

\fs22 \cf6 Let\'92s talk about mission coordination. This is another term that\'92s very common in\
the aerospace industry, but not so much in other fields. When any undertaking\
involves more than one party, a certain amount of \'93coordination\'94 is required.\
CubeSat missions involve, at the very least, a CubeSat developer and an LV pro-\
vider. The missions that CSLI sponsors will typically include a 
\fs18 \cf7 mission inte-\
grator
\fs22 \cf6 , who is responsible for the coordination. A mission integrator is assigned\
once a launch opportunity is identified and one or more CubeSats are mani-\
fested to that opportunity. Note that the term \'93mission\'94 here is bigger than your\
CubeSat \'93mission.\'94 The mission now represents your CubeSat plus any other co-\
manifested CubeSats, the dispensers, the launch, and the deployment. This coor-\
dination includes managing integration schedules, deliverable documentation,\
and how the requirements will be verified. In other words: mission coordination\
is a catchall term for the overall mission planning and the submitting and keep-\
ing track of paperwork that will be required to pass between the LV provider and\
the CubeSat developer. The mission integrator will be responsible for the sched-\
ule and communication between the parties to make sure all CubeSat require-\
ments are verified on time.\
Mission coordination will begin about 18 months before the scheduled launch\
date. It will start with a \'93kickoff\'94 meeting between all of the developers on the\
mission and the mission integrator. Don\'92t worry, you shouldn\'92t need to travel any-\
where for this; the kickoff will be conducted over the phone as a teleconference\
(also called a \'93telecon\'94). The CubeSat developers aren\'92t expected to know all of\
the ins and outs of the requirement verification process, so the mission integrator\
will help guide the developers through the process. The mission integrator will\
supply the developer with a schedule for hardware and document 
\fs18 \cf7 deliverables
\fs22 \cf6 ,\
and document templates for each document deliverable. The mission integrator\
is also responsible for creating a mission-specific CubeSat-to-dispenser Interface\
Control Document (ICD)\'97check out the ICD in 
\fs18 \cf10 Chapter 4.1
\fs22 \cf6  for more details.\
This ICD is, essentially, the official rulebook for your CubeSat. You and the\
mission integrator will work together to show that your CubeSat meets every\
one of the requirements stated in the ICD. These requirements are derived from\
the CDS and the launch vehicle\'92s specific needs. The ICD will also specify the\
relevant environmental testing levels and durations to which your CubeSat will\
need to be tested. To help keep everyone on track, the mission integrator will\
organize regular telecons to discuss the current status of the mission, get CubeSat\
development updates, and provide technical assistance and guidance.\

\fs20 \cf11 mission integrator:
\fs18 \cf10  \cf2 You may be\
asking yourself why the mission\
integrator isn\'92t called the mission\
coordinator. Well, sometimes\
they are. The terms \'93integration\'94\
and \'93coordination\'94 when referring\
to a mission are commonly used\
interchangeably. For the purposes\
of this document, the person/\
organization responsible for the\
coordination will be referred to as\
\'93mission integrator,\'94 and we\'92ll use\
\'93mission coordination\'94 to refer to\
mission coordination activities.\

\fs20 \cf11 deliverables: 
\fs18 \cf2 A deliverable\
is anything that your team has\
agreed to submit to the mission\
integrator as part of your legal\
obligations under the CRADA.\
These deliverables will be used to\
verify that your CubeSat meets the\
requirements set in the mission\
ICD.\cf10  \cf11 Chapter 6 \cf2 describes the\
deliverables required on a typical\
CubeSat mission.\
\cf11 CubeSat 101\cf2 : Basic Concepts and Processes for First-Time CubeSat Developers \cf12 NASA CubeSat Launch Initiative\

\fs26 \cf2 19
\fs22\fsmilli11050 CubeSat\
101\

\fs19 \cf11 CHAPTER 2\cf14  \cf2 Development Process Overview\

\fs22 \cf6 During this mission coordination phase, your team will be working on hardware\
fabrication and design, testing, and the documentation you will be submitting to\
the mission integrator.\

\fs32 \cf14 2.8 \cf4 Regulatory Licensing (4\'966 months)\

\fs22 \cf6 We\'92ll go into much more detail about regulation-related licensing in 
\fs18 \cf10 Chapter\
5
\fs22 \cf6 , but we\'92ll explain the basics here. All CubeSats must go through a licensing\
process in order to transmit radio signals and a separate process to license the use\
of an imaging instrument such as a camera. Obtaining licenses for satellites\
can be a lengthy process. Prior to finalizing any system design and opera-\
tions plan and before submitting any application,\
you should understand regulatory constraints and\
clearly identify all necessary information required\
for licensing. Once all the necessary information\
is documented, you should submit your applica-\
tion, as soon as possible, preferably within 30 days\
after your CubeSat gets manifested or earlier. If you\
don\'92t have all of the necessary licenses in hand prior\
to your CubeSat\'92s final delivery date to the integra-\
tor, you risk your CubeSat being demanifested from\
the mission. This means you will be bumped from the\
launch. Don\'92t let that scare you too much; as long as\
you comply with regulatory rules, prepare a complete\
application, and get your paperwork started early, as\
recommended here, there should be time to get your\
license granted.\
More than likely, you will need to obtain a radio license because your CubeSat,\
like most other satellites, probably needs to transmit on a radio frequency (RF)\
to communicate with the ground and Federal law requires a radio license for\
that. Licenses to transmit RF to or from U.S. Government operated satellites are\
handled by the National Telecommunications and Information Administration\
(NTIA), while the Federal Communications Commission (FCC) handles all\
other non\'96Federal Government agency operated satellites. Before you get started,\
see 
\fs18 \cf10 Chapter 5
\fs22 \cf6  to help you determine which agency, and which license, is appro-\
priate for your CubeSat and its mission.\

\fs17 \cf8 Naia Butler-Craig, a systems engineer\
intern at NASA\'92s Glenn Research\
Center, works on assembling and\
testing the \cf9 Advanced Electrical\
Bus (ALBus) \cf8 CubeSat. The ALBus\
CubeSat is a pathfinder technology\
demonstration for high power density\
CubeSats. [NASA/Bridget Caswell,\
Alcyon Technical Services]\

\fs26 \cf2 20 
\fs18 \cf11 CubeSat 101\cf2 : Basic Concepts and Processes for First-Time CubeSat Developers \cf12 NASA CubeSat Launch Initiative
\fs22\fsmilli11050 \cf2 CubeSat\
101\

\fs19 \cf11 CHAPTER 2\cf14  \cf2 Development Process Overview\

\fs22 \cf6 The second license you may have to obtain is based on whether your CubeSat\
includes an imager, or camera. Anyone who intends to operate a non\'96Government\
owned U.S. CubeSat with an imager must contact the National Oceanic and\
Atmospheric Administration (NOAA) to find out whether a remote sensing\
license is necessary, and if it is, to get the application process started. This process\
can be lengthy, and the FCC will need to see your license from NOAA before it\
will finish processing your RF license. Many more details on obtaining a NOAA\
license can be found in Licensing Procedures (
\fs18 \cf10 Chapter 5
\fs22 \cf6 ).\

\fs32 \cf14 WARNING!\

\fs18 \cf8 Being demanifested for a licensing issue sounds scary, and it is. The\
regulatory agencies take this very seriously. There was a CubeSat on an early\
CSLI launch that had been integrated into the dispenser, and onto the launch\
vehicle, without an approved FCC RF license. CSLI and the integrator had\
assumed it would be granted before launch, but a few days before launch\
this still hadn\'92t occurred. There wasn\'92t time to remove the CubeSat from the\
dispenser, so the integrator was planning to go to the launch vehicle and\
disable the release mechanism, so that the CubeSat could not be released into\
orbit. Luckily for the CubeSat developer, the license came through just before it\
was too late. Otherwise, \cf14 not only would their mission have been scrubbed,\
but they also would have lost their CubeSat\cf8 !\

\fs32 \cf14 2.9 \cf4 Flight-Specific Documentation Development\
and Submittal (10\'9612 months)\

\fs22 \cf6 Once your CubeSat is manifested on a launch, the mission integrator will provide\
a list of deliverables (documents that CSLI and the mission integrator need from\
your team) that will need to be completed and submitted by a specified date.\
These documents will be used to verify that your CubeSat meets all safety and\
launch requirements set by the ICD. The first of these documents will likely be\
due shortly after your first kickoff meeting with the mission integrator. These\
deliverable documents will be discussed in more detail in the Flight Certification\
Documentation section (
\fs18 \cf10 Chapter 6
\fs22 \cf6 ) of this document.\

\fs18 \cf11 CubeSat 101\cf2 : Basic Concepts and Processes for First-Time CubeSat Developers \cf12 NASA CubeSat Launch Initiative\

\fs26 \cf2 21
\fs22\fsmilli11050 CubeSat\
101\

\fs19 \cf11 CHAPTER 2\cf14  \cf2 Development Process Overview\

\fs32 \cf14 2.10 \cf4 Ground Station Design, Development, and\
Testing (2\'9612 months)\

\fs22 \cf6 You will need a way to communicate with your CubeSat once it\'92s in space. For\
that you need a ground station. There are a lot of components required for a\
proper ground station, but two basic components you will need are a radio and\
an antenna. Your ground station should be built early in your project\'92s timeline.\
If your team isn\'92t experienced with CubeSat communications and the hardware\
required, building and testing your ground station will consume a lot of time\
and energy. Most teams prefer to use off-the-shelf amateur radio components,\
and there are typically local amateur radio club members willing (excited, even)\
to advise and help with building and commissioning the ground station. You can\
find these types of groups online (i.e. American Radio Relay League 
\fs18 \cf10 http://www.\
arrl.org/
\fs22 \cf6 ). Some good basic design information also can be found on 
\fs18 \cf10 http://www.\
cubesat.org
\fs22 \cf6 .\

\fs17 \cf8 Anthony Young works in the ground\
station at Santa Clara University,\
Santa Clara, Calif., in support\
of NASA\'92s \cf9 Organism/Organic\
Exposure to Orbital Stresses\
(O/OREOS) \cf8 CubeSat. [NASA]\

\fs22 \cf6 Thorough testing of the ground station is critical for your mission\'92s success. The\
ground station is used to locate the satellite as well as to send commands and to\
downlink data. Launching with an inadequate ground station is a mission killer.\
Your ground station should be tested early and often. By monitoring existing sat-\
ellites, your team can gain experience operating the equipment. This experience is\
invaluable in the satellite building process, particularly when writing the software\
and command structure. Additionally, it\'92s important to have your ground station\
in the loop during development. There are many satellites (CubeSats, amateur\
satellites, NOAA satellites, Space Station, etc.), which can be tracked, and even\
commanded if you coordinate with the satellite\'92s operators. Participating in such\
\cf3 > \cf2 FREE ADVICE\

\f2 \cf3 >\

\f0\fs18 \cf14 TROUBLESHOOTING BASICS. \cf8 The ground station has many components\
operating independently, any of which, if not working properly, can cause\
communication issues. When troubleshooting, take a systematic approach.\
Make sure antennas are pointing where expected by using calibration\
points like mountains, the Sun, or the Moon for azimuth and elevation.\
Use a vector network analyzer, if available, to check the impedance of the\
antenna, cables, and any adapters in the path to the radio. Also confirm that\
the radio is tuning to the expected frequency, is in the right mode, and that\
line levels are appropriately set between the radio and the \cf7 terminal node\
controller (TNC)\cf8 / computer. Software defined radios, particularly the small,\
less expensive options like the RTL2832 or FunCube, are an excellent way to\
capture and replay slices of RF spectrum for later decoding practice.\

\fs20 \cf11 terminal node controller\
(TNC): 
\fs18 \cf2 The TNC is a device used\
by amateur radio operators to\
participate in AX.25 packet radio\
networks. It will assemble the\
data into packets of information\
and key the transmitter to send\
the packets of data to the ground\
station. Once the ground station\
receives the packets, the packets\
are reassembled and encoded to\
a form that can be interpreted by\
your ground station.\

\fs26 22 
\fs18 \cf11 CubeSat 101\cf2 : Basic Concepts and Processes for First-Time CubeSat Developers \cf12 NASA CubeSat Launch Initiative
\fs22\fsmilli11050 \cf2 CubeSat\
101\

\fs19 \cf11 CHAPTER 2\cf14  \cf2 Development Process Overview\

\fs22 \cf6 activities can be valuable experience for your CubeSat team. (See 
\fs18 \cf10 Chapter 2.16 
\fs22 \cf6 for\
more on tracking satellites).\
Your team should become familiar with commonly tracked satellites and their\
operating modes and frequencies. In the 437 MHz (70 cm) band there are plenty\
of CubeSats with beacons strong enough to easily receive, but it is necessary\
to know which ones are active and which are not. As a rule of thumb, look for\
recently launched CubeSats, as those are most likely to be operating. Contact the\
organization that developed (and is most likely operating) the CubeSat, if nec-\
essary, to confirm operation. In the 140 MHz (2 m) band, the NOAA weather\
satellites are an excellent test object and produce interesting images.\
On your launch day, you\'92ll want to be as knowledgeable about CubeSat com-\
munications (CubeSat comms) and satellite tracking as humanly possible, so do\
as much research as you can. This includes contacting experienced university\
CubeSat programs, reading papers and presentations online, and going to small\
satellite conferences to chat with your fellow developers. With all of the resources\
available to you, you shouldn\'92t have too much trouble getting your team up to\
speed before launch.\

\fs20 \cf11 margin: 
\fs18 \cf2 This is a very common\
term in the engineering world\
specifically referring to the safety\
margin, but is more generally\
used to refer to extra anything that\
gives you peace of mind. When\
you\'92re talking about scheduling,\
you add time, or margin, in case\
you run into issues or just estimate\
incorrectly.\

\fs32 \cf14 2.11 \cf4 CubeSat Hardware Fabrication and Testing\
(2\'9612 months)\

\fs20 \cf11 ETU: 
\fs18 \cf2 An engineering test unit.\
An ETU is built like the flight unit,\
but is not intended for launch.\
Developers will typically use the\
ETU like a practice dummy. It can\
be used to practice putting the\
components together, fit checks,\
hardware and software testing,\
and anything else that you don\'92t\
want to try for the first time on\
your valuable flight unit.\

\fs22 \cf6 As mentioned in the CubeSat Design section (
\fs18 \cf10 Chapter 2.4
\fs22 \cf6 ), many hardware com-\
ponents may be purchased from commercial vendors, but fabricating in-house\
whenever possible can help keep costs down and, for educational CubeSat proj-\
ects, can increase learning opportunities. The timeframe for this part of the\
process varies greatly depending on how ambitious the design is and how expe-\
rienced your team is. Be conservative in planning and pad your build schedule\
with plenty of 
\fs18 \cf7 margin
\fs22 \cf6 .\
Keep in mind that it\'92s cheaper to build two satellites at once than to build one\
and later decide to build another. Launch opportunities are very fluid, and launch\
failures are always possible. If financially possible, it is extremely useful to build\
multiple units (e.g., one 
\fs18 \cf7 Engineering Test Unit\'97known as an ETU
\fs22 \cf6 , a 
\fs18 \cf7 FlatSat
\fs22 \cf6 ,\
and two flight units). Qualification testing and integrated development can be\
performed on the ETU, troubleshooting on the FlatSat, and final environmental\
testing can be done on the flight units. No two satellites are exactly the same, so\
building two flight units gives the option to fly the best hardware.\

\fs20 \cf11 FlatSat:
\fs18 \cf2  A FlatSat is exactly what\
it sounds like. It\'92s an engineering\
unit of the CubeSat that includes\
all of the components, except\
the structure. Typically, the\
components are mounted on\
some sort of flat board, hence\
the term FlatSat. Developers\
can use the FlatSat to test and\
troubleshoot the CubeSat\'92s\
systems without integrating\
everything onto the structure.\
\cf11 CubeSat 101\cf2 : Basic Concepts and Processes for First-Time CubeSat Developers \cf12 NASA CubeSat Launch Initiative\

\fs26 \cf2 23
\fs22\fsmilli11050 CubeSat\
101\

\fs19 \cf11 CHAPTER 2\cf14  \cf2 Development Process Overview\

\fs22 \cf6 During assembly of the flight satellites, developers are encouraged to take as\
many pictures as possible at regular intervals. Keeping detailed photo documen-\
tation during all phases of assembly, integration, and testing has saved some flight\
missions in the past. We can\'92t stress enough how important it is to keep good,\
detailed records of your successes and failures as you progress. One of the most\
common problems CubeSat teams have had is losing knowledge and expertise\
when team members move on and are replaced by new personnel. University\
CubeSat developers have the greatest problem with senior members graduating\
before the completion of the project.\
\cf3 > \cf2 FREE ADVICE\

\f2 \cf3 >\

\f0\fs18 \cf14 KEEP EXCELLENT RECORDS OF EVERYTHING YOU DO. \cf8 It is incredibly important\
to keep great records of the work your team has been doing. These\
records should be in the form of photographic evidence and thorough\
documentation. This is especially important for student organizations that\
will be losing senior team members as they graduate. Keeping records helps\
continuity within the project; you\'92ll avoid \'93reinventing the wheel\'94 over and\
over again.\

\fs17 Denise Thorsen and Jesse Frey from\
the University of Alaska Fairbanks\
are performing DITL testing on the\
\cf9 Alaska Research Center (ARC)\
\cf8 CubeSat. ARC was launched by\
NASA\'92s CubeSat Launch Initiative on\
the ELaNa XII mission as an auxiliary\
payload aboard the NROL-55 Mission\
on October 8, 2015. [University of\
Alaska, Fairbanks]\

\fs22 \cf6 There are two types of testing you will do for your CubeSat. The first type, devel-\
opment testing, is internal testing you\'92ll do for your own purposes. The second\
type, verification testing, you\'92ll do to prove to CSLI and the launch provider\
that your CubeSat is safe and sturdy. You can do as much development testing\
as you want, and no documentation will be due to CSLI. Once your CubeSat\
build is complete, you will be required to perform specific testing and submit test\
plans and reports to verify that the CubeSat meets the ICD requirements. After\
verification testing is performed, you cannot work on the CubeSat any longer,\
or you will be required to perform the verification testing again. Verification\
testing typically includes vibration and thermal vacuum tests, and in some cases\
shock, EMI/EMC, and static load tests, to ICD-prescribed levels. Day In The\
Life (DITL) testing is also required to show that 
\fs18 \cf7 electrical inhibits
\fs22 \cf6  and timers\
will function correctly.\
For vibration and shock testing, testing containers may be available for your\
CubeSat. This testing container is a simplified version of the actual flight dis-\
penser to act as a flight-like interface between your CubeSat and the testing appa-\
ratus. Ask your mission integrator if there are testing versions of your assigned\
dispenser available.\

\fs20 \cf11 electrical inhibit: 
\fs18 \cf2 An electrical\
inhibit is a physical device that\
interrupts the \'93power path\'94\
needed to turn on your CubeSat\
and/or other potentially hazardous\
devices.\

\fs26 24 
\fs18 \cf11 CubeSat 101\cf2 : Basic Concepts and Processes for First-Time CubeSat Developers \cf12 NASA CubeSat Launch Initiative
\fs22\fsmilli11050 \cf2 CubeSat\
101\

\fs19 \cf11 CHAPTER 2\cf14  \cf2 Development Process Overview\

\fs22 \cf3 > \cf2 FREE ADVICE\

\f2 \cf3 >\

\f0\fs18 \cf14 DEVELOPMENT TESTING. \cf8 \'93Test like you fly\'94 is a common mantra for CubeSat\
developers and applies to more than just final environmental testing.\
During electronic development, use evaluation and development kits and\
\cf7 breadboard\cf8  components before fabricating boards. Once the printed circuit\
boards (PCBs) are produced, test as many expected functions as possible\
before interfacing it with other systems. Keep the scope small with testing\
and add components systematically, testing them along the way. Never\
assume that boards or subsystems that work well during standalone testing\
will work well when integrated with other boards or subsystems.\
During mechanical development, it is useful to do thermal and vibration tests\
on individual subsystems prior to integrating all components. This often\
catches design issues early on and reduces over-test on the overall system.\

\fs20 \cf11 breadboard:
\fs18 \cf2  A breadboard\
is a board used to make\
an experimental model of\
components for testing.\

\fs22 \cf6 Testing should be completed with all documentation submitted to the mission\
integrator no later than 1 month prior to the readiness reviews.\

\fs32 \cf14 2.12 \cf4 Mission Readiness Reviews (Half-Day)\

\fs22 \cf6 The Mission Readiness Review (MRR) is a presentation that you\
will deliver to CSLI and the mission integrator summarizing all\
of the evidence you\'92ve provided to show that your CubeSat sat-\
isfies all of the requirements in the ICD. All of your deliverable\
documentation should be submitted to, and accepted by, the mis-\
sion integrator prior to this review. That means all testing should\
also have been completed, and your CubeSat should be com-\
pletely finished. This review cannot be completed by telephone;\
all CubeSat teams manifested on the mission are required to send\
at least one representative to present at the readiness review\'97so\
don\'92t forget to budget for travel! The location of the review will\
be determined by LSP and the mission integrator. An MRR out-\
line or template will be provided to each team by the mission\
integrator at least 1 month prior to the review. Your team will be\
required to submit a draft of the presentation 2 weeks or more\
before the review. This MRR pre-check of your draft is for your\
benefit as well as the reviewers. The mission integrator will be able\
to catch a lot of errors and ensure all information is covered so the\
actual MRR goes as smoothly as possible.\

\fs17 \cf9 SporeSat \cf8 undergoing vibration testing. SporeSat is\
a space biology science mission designed by Ames\
Research Center to gain a deeper knowledge of the\
mechanism and determine the threshold of cell gravity\
sensing. Launched by NASA\'92s CubeSat Launch Initiative\
on the ELaNa V mission as an auxiliary payload aboard\
the SpaceX-3 Cargo Resupply Mission on April 18, 2014.\
[NASA Ames Research Center]\

\fs18 \cf11 CubeSat 101\cf2 : Basic Concepts and Processes for First-Time CubeSat Developers \cf12 NASA CubeSat Launch Initiative\

\fs26 \cf2 25
\fs22\fsmilli11050 CubeSat\
101\

\fs19 \cf11 CHAPTER 2\cf14  \cf2 Development Process Overview\

\fs32 \cf14 2.13 \cf4 CubeSat-to-Dispenser Integration and Testing\
(2 days)\

\fs22 \cf6 It\'92s delivery day! You\'92ve completely finished your CubeSat\'97all testing is complete\
and all paperwork has been submitted. Now you get to deliver your CubeSat to\
the integration site, the location of which is determined by the mission inte-\
grator. When you arrive at the integration site you\'92ll unpack your CubeSat and\
move it into the integrator\'92s clean room. It\'92s not required, but the integrator may\
request that you help with the integration process. This means being responsible\
for positioning the CubeSat on the workbench while the integrator takes the pre-\
integration physical measurements. Some integrators\
will make a great effort to avoid handling the CubeSat.\
You may even get to insert your CubeSat into the dis-\
penser. In addition to integration activities, and assum-\
ing the integration facility allows cameras, there may be\
photo opportunities. These photos can be great publicity\
for your program\'97and for your scrapbook\'97so don\'92t\
forget to bring your pretty smiles! Once the dispenser\
door is closed, and all photos are taken, your job is done.\
The integrator will seal the dispenser and that typically\
concludes day 1.\
On day 2, the dispenser and CubeSat will go through\
a final vibration test as a single unit to make sure inte-\
gration was successful. And that\'92s it\'97the integrator will\
take it from there.\
Generally, the developers are required to attend integration. This is to ensure that\
if any issues arise they can be addressed real time and it is also the last time you\'92ll\
see your CubeSat.\
After integration to the dispenser is complete, you won\'92t have access to the\
CubeSat again. With prior approval, you may run system diagnostics or perform\
battery charging at the integration site before the CubeSat is buttoned up in the\
dispenser. However, in the event that there is a very long launch delay (e.g., if\
your launch is delayed by several months) the developers may have an opportu-\
nity to access their CubeSats again, but this is only in extreme circumstances and\
is by no means guaranteed.\

\fs17 \cf8 The \cf9 CSSWE (Colorado Student\
Space Weather Experiment)\
\cf8 CubeSat and PPOD just prior to\
integration. The CSSWE launched on\
September 13, 2012 as an auxiliary\
payload on the ELaNa VI mission\
aboard the NROL-36. [University of\
Colorado at Boulder]\

\fs26 \cf2 26 
\fs18 \cf11 CubeSat 101\cf2 : Basic Concepts and Processes for First-Time CubeSat Developers \cf12 NASA CubeSat Launch Initiative
\fs22\fsmilli11050 \cf2 CubeSat\
101\

\fs19 \cf11 CHAPTER 2\cf14  \cf2 Development Process Overview\

\fs22 \cf6 Any special accommodations (clean room, tem-\
perature, humidity, security, storage, etc.) that\
your CubeSat requires at the integration site\
should be requested at the start of the mission.\
Additionally, you will need to inform the inte-\
grators about any Ground Support Equipment\
(GSE) you plan to bring to the site, as well as\
any potential hazards to integration personnel.\
If the CubeSat has any possible hazards (e.g.,\
laser emitters), the CubeSat team will need to\
provide safety gear for the integration team\
(e.g., protective eyewear).\
After the CubeSat is integrated into the dis-\
penser, the mission integrator will inspect the loaded dispenser one more time.\
Then the dispenser will be packaged and shipped to the integration site where the\
loaded dispenser will be integrated onto the launch vehicle.\

\fs17 \cf8 Technicians integrating a PPOD\
containing CubeSats onto the Delta\
II launch vehicle as part of the ELaNa\
X mission that was launched as an\
auxiliary payload on NASA\'92s Soil\
Moisture Active Passive (SMAP)\
Mission. [NASA]\

\fs32 \cf14 2.14 \cf4 Dispenser-to-Launch Vehicle Integration\
(1 day)\

\fs22 \cf6 Dispenser-to-launch vehicle integration is the point at which the dispenser loaded\
with your CubeSat is attached to the rocket. This sounds pretty cool, and it is, but\
unfortunately, you aren\'92t invited. The launch vehicle providers are very protective\
of their rockets, so only essential personnel are permitted to participate. Essential\
personnel usually include LSP representatives, the mission integrator, and the\
launch provider\'92s technicians.\
The process only takes about a half-day to a day, depending on the launch vehicle.\
Not all missions are run the same way, but typically on the big day, the mission\
integrator will arrive at the launch vehicle site with the loaded dispenser. The LV\
technicians will lead the integrator to the location on the LV where the dispenser\
is to be affixed. After a final cleaning and inspection, the mission integrator will\
hand off the dispenser to the LV technicians. The technicians will follow a pre-\
scribed procedure to carefully attach the dispenser to the LV. Finally, photo-\
graphs will be taken as evidence that the integration was successful, and your\
CubeSat will be that much closer to space.\

\fs18 \cf11 CubeSat 101\cf2 : Basic Concepts and Processes for First-Time CubeSat Developers \cf12 NASA CubeSat Launch Initiative\

\fs26 \cf2 27
\fs22\fsmilli11050 CubeSat\
101\

\fs19 \cf11 CHAPTER 2\cf14  \cf2 Development Process Overview\

\fs22 \cf6 The integration to the LV typically occurs 2 weeks to 4 months prior to launch.\
It all depends on which LV your CubeSat is using. Each mission model is differ-\
ent and explained in more detail in the Mission Models section (
\fs18 \cf10 Chapter 3
\fs22 \cf6 ) of\
this document.\

\fs32 \cf14 2.15 \cf4 Launch (1 day)\

\fs22 \cf6 The launch location will depend on the pri-\
mary mission, and will be known well before\
the CubeSats are manifested. The launch\
date may change from the original timeline,\
but only the primary mission or launch vehi-\
cle can move the launch date. The CubeSats\
do not have any influence on the launch or\
launch window. If your project gets delayed\
for any reason, the launch will not be delayed.\
If your CubeSat is not delivered in time,\
the LV will definitely leave without your\
CubeSat onboard.\
While the CubeSat developers won\'92t have an\
active role in launch operations, you will usu-\
ally be invited to come to the launch site and\
watch the LV take off. Travel will be at your own expense, but most teams think\
it\'92s well worth it. While you\'92re there, LSP may ask that you participate in some\
public affairs and outreach events (e.g., NASA EDGE interviews, photos, etc.).\
Be aware that the launch date is subject to change at any time and day-of-launch\
scrubs are common due to weather and other factors. So, if you plan to travel to\
the launch, it may be wise to include some extra days in the event of a last-minute\
launch delay.\

\fs17 \cf8 Launch of ELaNa-II from Vandenberg\
Air Force Base, CA on December 6,\
2013. Four CubeSat Missions were\
deployed. [Corkery/ULA]\

\fs26 \cf2 28 
\fs18 \cf11 CubeSat 101\cf2 : Basic Concepts and Processes for First-Time CubeSat Developers \cf12 NASA CubeSat Launch Initiative
\fs22\fsmilli11050 \cf2 CubeSat\
101\

\fs19 \cf11 CHAPTER 2\cf14  \cf2 Development Process Overview\

\fs32 \cf14 2.16 \cf4 Mission Operations (variable, up to 20 years)\

\fs22 \cf6 Initial operations can be the most exciting part of a satellite mission, especially to\
first-time flyers; however, it can also be the most challenging. But not to worry,\
the mission integrator will work with your team to get communications up and\
running after launch.\
By now your team should have had plenty of practice using the ground station on\
engineering and/or flight versions of your own CubeSat, as well as some practice\
tracking existing CubeSats. You may have even been able to request permission\
from other CubeSat teams to uplink to their satellites. Having operations experi-\
ence during the development of your CubeSat is invaluable because it helps you\
decide what commands will work best when your CubeSat is in orbit. Existing\
satellites are a good starting point because the orbit and satellite behavior should\
be well established.\
\cf3 > \cf2 FREE ADVICE\

\f2 \cf3 >\

\f0\fs18 \cf14 HOW TO TRACK A SATELLITE. \cf8 To predict where any satellite is in orbit, \cf7 two-\
line element (TLE)\cf8  sets are entered into satellite tracking software that\
calculates the expected position of the satellite. TLEs can be generated from\
various sources; however, the most widely available and accurate TLEs are\
produced by the United States Air Force\'92s Joint Space Operations Center\
(JSpOC) at Vandenberg Air Force Base in California. The JSpOC publishes\
TLEs for most of the satellites currently in orbit on its Web site, \cf10 http://\
www.space-track.org\cf8 . The JSpOC Web site is also a great place to review\
satellite-tracking data, because their records go back to 1957, the beginning\
of the space program.\

\fs20 \cf11 two-line element (TLE):
\fs18 \cf2  A\
TLE is a data format encoding\
a list of orbital elements of an\
Earth-orbiting CubeSat for a given\
point in time, the epoch. Using a\
prediction formula, a TLE can be\
used to estimate the position and\
velocity in the past, present or\
future for your CubeSat.\
\cf8 0 CXBN-2\
1 42704U 98067LM 17304.55488591 .00021073 00000-0 25707-3 0 9994\
2 42704 51.6386 74.8642 0001580 42.1764 317.9350 15.60423680 26110\

\fs22 \cf6 Directly following a launch, the first challenge is determining which new object\
is your satellite. The launch provider usually provides preliminary state vectors\
before the launch date so the CubeSat developers can plan and schedule their\
operations. State Vectors specify the position and velocity of CubeSat relative to\
the Earth\'92s center of mass and are used to predict viewing times and the position\
of your CubeSat.\

\fs18 \cf11 CubeSat 101\cf2 : Basic Concepts and Processes for First-Time CubeSat Developers \cf12 NASA CubeSat Launch Initiative\

\fs26 \cf2 29
\fs22\fsmilli11050 CubeSat\
101\

\fs19 \cf11 CHAPTER 2\cf14  \cf2 Development Process Overview\

\fs17 \cf8 The University of Colorado at\
Boulder \cf9 Miniature X-ray Solar\
Spectrometer (MinXSS) \cf8 CubeSat\
followed by the University of Michigan\
CADRE CubeSat, are deployed from\
the Space Station on May 16, 2016\
on the ELaNa IX mission. The MinXSS\
mission is a science investigation\
to study solar flares, active regions,\
the quiescent Sun, and their impact\
on Earth\'92s upper atmosphere. The\
\cf9 CADRE\cf8  mission is a space weather\
investigation that will improve our\
understanding of the dynamics of\
the upper layers of our atmosphere:\
the thermosphere and ionosphere.\
[NASA]\

\fs22 \cf6 Right after the CubeSats are ejected into orbit on launch day, the launch provider\
will provide actual state vectors that can be converted into TLEs. It can take\
some time\'97from a couple days up to a week or so\'97for the JSpOC to produce\
rough TLEs. The accuracy of the TLEs will become more refined over the fol-\
lowing few weeks. During this time, the mission integrator will be working both\
with the JSpOC and the CubeSat teams to help determine which satellite belongs\
to which TLE. Some CubeSats carry GPS receivers, which helps identify each\
satellite by process of elimination. It\'92s not uncommon for it to take several weeks\
to confidently identify all of the satellites from a launch.\
If you\'92re planning to use a radio frequency in the amateur band (more fre-\
quency band details in 
\fs18 \cf10 Chapter 5.1
\fs22 \cf6 ), you can get help contacting your satellite\
from the amateur radio community. In the past, CubeSat developers have posted\
announcements online to get help from volunteer satellite trackers. These volun-\
teers have been very helpful identifying CubeSats. You can get more details by\
reaching out to fellow CubeSat teams online and at conferences.\
One more resource to help you out is the CubeSat Internet Relay Chat (IRC)\
channel. During and directly following launch, most of the active amateur sat-\
ellite-tracking enthusiasts meet on the CubeSat IRC channel to share observa-\
tions and work to identify each CubeSat. Most \'93first contacts\'94 occur on this IRC\
channel, and many are from other parts of the world. To join the CubeSat IRC\
channel, point your favorite IRC client to: 
\fs18 \cf10 irc.freenode.net
\fs22 \cf6  #cubesat\

\fs26 \cf2 30 
\fs18 \cf11 CubeSat 101\cf2 : Basic Concepts and Processes for First-Time CubeSat Developers \cf12 NASA CubeSat Launch Initiative
\fs22\fsmilli11050 \cf2 CubeSat\
101\

\fs224 \cf3 3
\fs78 \cf2 Mission Models\

\fs22 IN THIS CHAPTER\

\fs20 \cf5 3.1 
\fs16 \cf6 NASA-Procured Launch Vehicle\
Mission Model\

\fs20 \cf5 3.2 
\fs16 \cf6 Operationally Responsive Space\
(ORS) Rideshare Mission Model\

\fs20 \cf5 3.3 
\fs16 \cf6 National Reconnaissance Office\
(NRO) Rideshare Mission Model\

\fs20 \cf5 3.4 
\fs16 \cf6 Commercial Launch Service\
Through a Third-Party Broker\
Mission Model\

\fs20 \cf5 3.5 
\fs16 \cf6 International Space Station (ISS)\
Deployment Mission Model\

\fs67\fsmilli33624 W
\fs22 e know from 
\fs18 \cf10 Chapter 1
\fs22 \cf6  that CSLI has flown CubeSats on a number of\
different launch vehicles, but did you know that those launch vehicles\
were sponsored by different organizations? In this chapter we want to tell you\
about the different types of missions that CSLI CubeSats have been a part of.\
These organizations have a particular way they like to run their missions. These\
are called \'93mission models.\'94 That means your CubeSat team will work with\
requirements and organization structures specific to the type of mission your\
CubeSat is manifested on. To better prepare your team for what you can expect,\
we\'92ll go over the major differences in the mission models (listed below) that CSLI\
has worked with thus far.\

\fs18 \cf5 1. 2. 3. 4. 5. 
\fs22 \cf6 NASA-Procured Launch Vehicle Mission Model\
Operationally Responsive Space (ORS) Rideshare Mission Model\
National Reconnaissance Office (NRO) Rideshare Mission Model\
Commercial Launch Service through a Third-Party Broker Mission Model\
International Space Station (ISS) Deployment Mission Model\

\fs18 \cf13 Pictured above:\

\fs17 \cf9 IceCube\cf8  Team working at NASA\'92s\
Goddard Space Flight Center. The\
objective of the IceCube mission is\
to demonstrate the technology of\
a sub-millimeter-wave radiometer\
for future cloud ice sensing. This\
technology will enable cloud ice\
measurements to be taken in the\
intermediate altitudes (5 km\'9615 km),\
where no measurements currently\
exist. Launched by NASA\'92s CubeSat\
Launch Initiative on the May 24, 2017\
ELaNa XVII mission on the seventh\
Orbital-ATK Cygnus Commercial\
Resupply Services (OA-7) to the\
Space Station. [NASA]\

\fs18 \cf11 CubeSat 101\cf2 : Basic Concepts and Processes for First-Time CubeSat Developers \cf12 NASA CubeSat Launch Initiative\

\fs26 \cf2 31
\fs22\fsmilli11050 CubeSat\
101\

\fs19 \cf11 CHAPTER 3\cf14  \cf2 Mission Models\

\fs32 \cf14 3.1 \cf4 NASA-Procured Launch Vehicle Mission Model\

\fs22 \cf6 It\'92s no surprise that CSLI has placed CubeSats on launch vehicles being used\
for NASA missions. This is known as the NASA-Procured Launch Vehicle mis-\
sion model. Every year, NASA LSP procures launch vehicles for NASA and\
other civil U.S. Government agencies that will conduct missions to further sci-\
entific research or conduct technology demonstrations. When those missions\'92\
requirements allow for it, CSLI CubeSats are allowed to hitch a ride to orbit.\
The CubeSat requirements for these flights are based on LSP-REQ-317.01 and\
the CubeSat Design Specification (CDS), both of which are discussed in the\
Requirement Sources section (
\fs18 \cf10 Chapter 4
\fs22 \cf6 ).\
The organizational chart in 
\fs18 \cf14 FIGURE 10
\fs22 \cf6  outlines the organizations involved in\
NASA-Procured Launch Vehicle mission model. For CubeSat missions, NASA\
typically contracts mission coordination duties to an outside organization.\
Mission coordination duties can include the following: coordinating safety doc-\
umentation with 
\fs18 \cf7 range safety
\fs22 \cf6 , interfacing with the CubeSat developers, verify-\
ing ICD requirements, acting as the point of contact for the FCC and NOAA,\
performing CubeSat-to-dispenser integration and testing, and coordinating with\
the JSpOC to identify each CubeSat in orbit. Finally\'97and here\'92s the part that\

\fs20 \cf11 range safety: 
\fs18 \cf2 Range safety is\
the person designed to protect\
people and assets on both\
the rocket launch range and\
downrange in cases when a\
launch vehicle might expose them\
to danger.\

\fs16 \cf4 NASA Primary Mission\

\fs17 \cf13 Primary Mission Representative 
\fs16 \cf4 LV Provider\
NASA LSP\

\fs17 \cf13 Mission Management\

\fs16 \cf4 CSLI Mission Integrator\

\fs17 \cf13 Mission Coordination, Dispenser\
Integration, and Acceptance Testing\

\fs16 \cf4 CSLI\
CubeSats\

\fs20 \cf14 FIGURE 10:
\fs17 \cf8  NASA-Procured Launch Vehicle Mission Model Organizational Chart\
Launch of the ELaNa-X mission on\
January 31, 2015, as an auxiliary\
payload on NASA\'92s Soil Moisture\
Active Passive (SMAP) mission\
from Vandenberg Air Force Base,\
Calif. Three CSLI CubeSats were\
deployed: \cf9 FIREBIRD II A,B\cf8  from\
Montana State University, Bozeman,\
Mont.; \cf9 GRIFEX\cf8  from the Jet\
Propulsion Laboratory, Pasadena,\
Calif.; and \cf9 EXOCUBE\cf8  from Cal Poly,\
San Louis Obispo, Calif. [NASA]\

\fs26 \cf2 32\

\fs18 \cf11 CubeSat 101\cf2 : Basic Concepts and Processes for First-Time CubeSat Developers \cf12 NASA CubeSat Launch Initiative
\fs22\fsmilli11050 \cf2 CubeSat\
101\

\fs19 \cf11 CHAPTER 3\cf14  \cf2 Mission Models\

\fs17 \cf8 A Minotaur I rocket carrying, among\
other payloads, 11 small CubeSat\
research satellites as part of NASA\'92s\
fourth ELaNa mission, lifts off from\
Virginia\'92s Mid-Atlantic Regional\
Spaceport Pad 0B at NASA\'92s\
Wallops Flight Facility at 8:15 p.m.\
EST Nov. 19, 2013. This launch\
marked the launch of the first high-\
school-built cubesat, \cf9 TJ3Sat\cf8  built\
by Thomas Jefferson High School,\
Alexandria, VA. [NASA/Ali Stancil]\

\fs22 \cf6 affects your team\'97the mission integrator and/or NASA typically requires regu-\
lar mission tag-ups via telephone with the CubeSat developers. During these tag-\
ups the mission integrator will update the team on mission status and ask each\
developer to provide an update on their CubeSat status. You, as the developer,\
are expected to keep the mission integrator and NASA informed of your develop-\
ment status and any issues that might crop up.\
All of your deliverables will be submitted to and reviewed by the mission inte-\
grator and approved by NASA LSP. The mission integrator is responsible for rec-\
ommending to NASA LSP whether or not each CubeSat team is ready for flight.\
NASA will be responsible for ensuring that all CSLI CubeSats comply with\
NASA orbital debris mitigation requirements and will generate the Orbital\
Debris Assessment Report (see 
\fs18 \cf10 Chapter 6.1
\fs22 \cf6 ) for all CSLI CubeSats.\
In addition to the documentation, NASA also requires each team to present a\
readiness review in person to the mission integrator with NASA LSP as an advi-\
sor. This is the same readiness review we discussed in the Development Process\
Overview section (
\fs18 \cf10 Chapter 2.12
\fs22 \cf6 ).\

\fs18 \cf11 CubeSat 101\cf2 : Basic Concepts and Processes for First-Time CubeSat Developers \cf12 NASA CubeSat Launch Initiative\

\fs26 \cf2 33
\fs19 \cf11 CHAPTER 3\cf14  \cf2 Mission Models\

\fs32 \cf14 3.2 \cf4 Operationally Responsive Space (ORS)\
Rideshare Mission Model\

\fs22 \cf6 The Operational Responsive Space (ORS) Office isn\'92t as well known as NASA,\
but they\'92ve been very supportive of CubeSat missions. It\'92s a joint effort of mul-\
tiple agencies within the U.S. Department of Defense (DOD), and they have\
provided space on their launch vehicles to CubeSats in need of a ride to orbit.\
ORS launches have given rides to CSLI CubeSats as well as to other non\'96CSLI\
sponsored CubeSats.\
The organizational chart in 
\fs18 \cf14 FIGURE 11
\fs22 \cf6  outlines the ORS Rideshare Mission Model.\
ORS will contract with a mission integrator to oversee the development and inte-\
gration of the LV and payloads on the mission. As with the NASA mission model,\
these responsibilities may include coordinating safety documentation with range\
safety, interfacing with the CubeSat developers, verifying ICD requirements, act-\
ing as point of contact for the secondary missions with the FCC and NOAA,\
coordinating with the JSpOC for pre- and post-launch identification of objects,\
and managing the physical CubeSat-to-dispenser integration.\
In addition to the ORS mission integrator, there typically will be another mission\
integrator contracted by ORS to deal specifically with the CSLI CubeSat teams.\

\fs16 \cf4 ORS Office\
ORS Mission Integrator\
LV Provider\
NASA LSP\

\fs17 \cf13 Mission Management\

\fs16 \cf4 CSLI Mission\
Integrator\
CSLI\
CubeSats\
ORS\
CubeSats\

\fs20 \cf14 FIGURE 11:
\fs17 \cf8  ORS Rideshare Mission Model Organizational Chart\

\fs26 \cf2 34 
\fs18 \cf11 CubeSat 101\cf2 : Basic Concepts and Processes for First-Time CubeSat Developers \cf12 NASA CubeSat Launch Initiative
\fs19 \cf11 CHAPTER 3\cf14  \cf2 Mission Models\

\fs22 \cf6 The CSLI mission integrator will have scaled-back responsibilities compared to\
the equivalent role in the NASA-owned mission model, because the ORS mission\
integrator is responsible for a number of the tasks. The CSLI mission integrator\
will be limited to tasks related to tracking CubeSat development, performing ICD\
verification tasks, and providing relevant updates to the ORS mission integrator.\
This person will also participate in the ORS Mission tag-up meetings with ORS,\
and will speak on behalf of the CubeSat teams. The CSLI mission integrator will\
hold separate tag-ups for the CSLI CubeSats. Each CubeSat team will present a\
readiness review to the CSLI mission integrator and the ORS mission integrator\
with NASA LSP acting as an advisor. As with all mission models, CSLI CubeSat\
teams will be required to present in-person for their readiness review.\
You, as the CubeSat developer will submit all of your document deliverables to\
the CSLI mission integrator. So, from your point of view, everything is pretty\
much the same on an ORS mission as it is on a NASA mission: a member of\
your CubeSat team will have regular tag-up meetings with a mission integrator,\
submit all required documentation to an integrator, and participate in a readiness\
review for final launch approval.\
NASA will be responsible for ensuring that all CSLI CubeSats comply with\
NASA orbital debris mitigation requirements and will generate the Orbital\
Debris Assessment Report (see 
\fs18 \cf10 Chapter 6.1
\fs22 \cf6 ) for all CSLI CubeSats.\

\fs17 \cf8 Kathryn Clements and Mary Distler,\
students at St. Louis University, with\
the \cf9 Argus \cf8 CubeSat\cf9  \cf8 after completing\
pre-integration checkout. Launched by\
NASA\'92s CubeSat Launch Initiative on\
the ELaNa VII mission as an auxiliary\
payload aboard the U.S. Air Force-led\
Operationally Responsive Space (ORS-\
4) Mission on November 3, 2015. [St.\
Louis University]\

\fs32 \cf14 3.3 \cf4 National Reconnaissance Office (NRO)\
Rideshare Mission Model\

\fs22 \cf2 DID YOU KNOW?\
\cf6 The NRO has been a great supporter of CubeSat technologies and has flown a\
number of CubeSats as auxiliary payloads on their launch vehicles. CSLI has\
worked with the NRO for many years, and if your CubeSat mission is selected\
by CSLI to fly on a NRO mission, you will work primarily with the Auxiliary\
Payload Integration Contractor (APIC) team, which can be made up of multiple\
organizations and is contracted by the NRO.\
The chart in
\fs18 \cf14  FIGURE 12
\fs22 \cf6  shows all of the organizations involved in preparing\
CubeSats for flight on NRO-sponsored launches. The Office of Space Launch\
(OSL), located at the top of the chart, is the organization within the NRO that\
deals with launching satellites, as opposed to designing or operating them.\

\fs18 \cf4 The NRO\
\cf8 The National Reconnaissance\
Office (NRO) is an agency within\
the United States intelligence\
community. The NRO is responsible\
for designing, building, and operating\
the reconnaissance satellites for the\
United States Government. Although\
the NRO was established in 1961,\
its existence wasn\'92t declassified\
until 1992. If you\'92d like to know more\
about what the NRO does, their Web\
site, \cf10 http://www.nro.gov\cf8 , is a great\
place to start.\
\cf11 CubeSat 101\cf2 : Basic Concepts and Processes for First-Time CubeSat Developers \cf12 NASA CubeSat Launch Initiative\

\fs26 \cf2 35
\fs19 \cf11 CHAPTER 3\cf14  \cf2 Mission Models\

\fs16 \cf4 OSL\
Office of Space Launch\

\fs17 \cf13 (Under the National\
Reconnaissance Office)\

\fs16 \cf4 LV Provider\
APIC\
Auxiliary Payload Integration Contractor\

\fs17 \cf13 Mission Integration\

\fs16 \cf4 NASA LSP\

\fs17 \cf13 Mission Management\

\fs16 \cf4 CSLI\
CubeSats\
NRO\
CubeSats\

\fs20 \cf14 FIGURE 12:
\fs17 \cf8  NRO Mission Model Organizational Chart\

\fs22 \cf6 The APIC will be responsible for the mission integrator\'92s duties and will report\
regularly to the launch vehicle provider and OSL. For these reports and any\
readiness reviews to OSL, the APIC will need information and reports from the\
CubeSat teams; however, the CubeSat teams won\'92t need to participate in any\
of these meetings. Instead, the CubeSat teams will meet with the APIC team\
separately, typically in biweekly tag-ups via teleconference. At these tag-ups, the\
teams will provide status updates and alert the APIC to any issues that may affect\
the schedule or their ability to meet requirements.\
CubeSat teams will also be responsible for presenting a readiness review to the\
APIC, just like the other mission models. CSLI CubeSats will be required to\
present the review in-person to the APIC team, NASA LSP, and OSL.\
NASA will be responsible for ensuring that all CSLI CubeSats comply with\
NASA orbital debris mitigation requirements and will generate the Orbital\
Debris Assessment Report (see 
\fs18 \cf10 Chapter 6.1
\fs22 \cf6 ) for all CSLI CubeSats.\

\fs17 \cf8 This is the launch of ELaNa-XII on\
October 8, 2015, as an auxiliary\
payload on the NROL-55 mission from\
Vandenberg Air Force Base, Calif. Four\
CubeSat missions were deployed:\
\cf9 BisonSat \cf8 from Salish Kootenai College,\
Pablo, Mont.;\cf9  Fox-1\cf8  from AMSAT, The\
Radio Amateur Satellite Corporation,\
Kensington, Md.; \cf9 ARC-1\cf8  from the\
University of Alaska Fairbanks, Alaska;\
and \cf9 LMRSTSat\cf8  from the Jet Propulsion\
Laboratory, Pasadena, Calif. [ULA]\

\fs22 \cf6 All deliverables submitted by the CubeSat teams will be reviewed by the APIC.\
So, again, there isn\'92t much of a change for what your CubeSat team will need to\
do compared to the other mission models we\'92ve talked about so far: a member\
of your team will attend regular tag-up meetings with the APIC (the mission\
integrator), submit all required documentation to the APIC, and participate in a\
readiness review for final launch approval.\

\fs26 \cf2 36 
\fs18 \cf11 CubeSat 101\cf2 : Basic Concepts and Processes for First-Time CubeSat Developers \cf12 NASA CubeSat Launch Initiative
\fs22\fsmilli11050 \cf2 CubeSat\
101\

\fs19 \cf11 CHAPTER 3\cf14  \cf2 Mission Models\

\fs32 \cf14 3.4 \cf4 Commercial Launch Service Through a\
Third-Party Broker Mission Model\

\fs22 \cf6 CubeSat developers can purchase launches through third-party brokers on\
non-Government launches, usually on commercial or foreign missions. CSLI can\
also procure rides through a broker for payloads on commercial missions.\
The requirements for these missions will come from\
the LV provider via the broker (see 
\fs18 \cf14 FIGURE 13
\fs22 \cf6 ). NASA\
LSP will not verify the CubeSat requirements; instead,\
the broker will either serve as mission integrator or\
assign one. The mission integrator will work with the\
CubeSat and launch vehicle representatives to cre-\
ate the CubeSat-to-dispenser ICD and determine\
the appropriate schedule for document and hardware\
deliverables. The mission integrator role for third-party\
broker missions will be similar to that of the NASA\
missions. The mission integrator for these missions may\
not require readiness reviews, but may instead track the\
status of document and hardware deliverables to verify\
that the CubeSats are ready for flight.\
NASA will be responsible for ensuring that all CSLI CubeSats comply with\
NASA orbital debris mitigation requirements and will generate the Orbital\
Debris Assessment Report (see 
\fs18 \cf10 Chapter 6.1
\fs22 \cf6 ) for all CSLI CubeSats.\

\fs16 \cf4 Third-Party Broker\

\fs17 \cf13 Mission Manager 
\fs16 \cf4 LV Provider\
CSLI\
CubeSats\

\fs17 \cf8 During an event Oct. 14, 2015, at the\
Agency\'92s Kennedy Space Center\
in Florida, Garrett Skrobot, lead\
for the ELaNa missions for NASA\'92s\
Launch Services Program, shows\
the size of the CubeSats that will be\
launched under NASA\'92s contract\
award for the Venture Class Launch\
Services. Rocket Lab USA and Virgin\
Galactic were awarded contracts\
under the Venture Class Launch\
Services competition to send several\
CubeSats into space on flight profiles\
tailored to the needs of the CubeSats\
manifested on each launch. [NASA/\
Kim Shiflett]\

\fs20 \cf14 FIGURE 13:
\fs17 \cf8  Third-Party Broker Mission Model Organizational Chart\

\fs18 \cf11 CubeSat 101\cf2 : Basic Concepts and Processes for First-Time CubeSat Developers \cf12 NASA CubeSat Launch Initiative\

\fs26 \cf2 37
\fs22\fsmilli11050 CubeSat\
101\

\fs19 \cf11 CHAPTER 3\cf14  \cf2 Mission Models\

\fs32 \cf14 3.5 \cf4 International Space Station (ISS)\
Deployment Mission Model\

\fs22 \cf6 In addition to riding as auxiliary payloads mounted directly to launch vehicles,\
CubeSats can also be deployed from the Space Station (see 
\fs18 \cf14 FIGURE 14
\fs22 \cf6 ). For this\
type of mission, the CubeSats are integrated into dispensers on the ground, trans-\
ported to the ISS in a pressurized cargo vessel (e.g., SpaceX Dragon, Orbital ATK\'92s\
Cygnus, etc.), and hand carried onto the ISS from the cargo vessel. Astronauts\
aboard the ISS are responsible for deploying the CubeSats from the ISS typically\
1\'963 months after arrival.\
CubeSat mechanical and electrical requirements for ISS deployment are similar\
to those found in the CDS. For a list of requirements specific to ISS deploy-\
ment, please visit the NanoRacks Web site at 
\fs18 \cf10 http://nanoracks.com
\fs22 \cf6 . NanoRacks\
is currently the only commercial organization that can deploy CubeSats from\
the ISS. Any CubeSat using their services will need to comply with the current\
NanoRacks ICD. As with the other mission models, the CubeSats will submit\
flight safety review documents to the mission integrator, and the mission integra-\
tor will handle any reviews required by the ISS team.\
NASA will be responsible for ensuring that all CSLI CubeSats comply with\
NASA orbital debris mitigation requirements and will generate the Orbital\
Debris Assessment Report (see 
\fs18 \cf10 Chapter 6.1
\fs22 \cf6 ) for all CSLI CubeSats.\

\fs16 \cf4 NASA ISS LV Provider\
Mission Integrator\
\cf13 Mission Coordination,\
ISS Integration, and\
Acceptance Testing\
\cf4 NASA LSP\

\fs17 \cf13 Mission Management\

\fs16 \cf4 CSLI\
CubeSats\
Other\
CubeSats\

\fs20 \cf14 FIGURE 14:
\fs17 \cf8  ISS Mission Model Organizational Chart\

\fs26 \cf2 38\

\fs18 \cf11 CubeSat 101\cf2 : Basic Concepts and Processes for First-Time CubeSat Developers \cf12 NASA CubeSat Launch Initiative}