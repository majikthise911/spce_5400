# MASTER CubeSat Mission Evaluation Methodology
**Created:** 2025-11-02
**Version:** 2.0 (Comprehensive Update)
**Purpose:** Complete methodology for evaluating CubeSat missions incorporating all lessons learned

---

## EXECUTIVE SUMMARY

This document provides the **complete, reproducible methodology** for evaluating CubeSat mission concepts. It evolved from initial CSLI-only evaluation to include problem validation, market research, novelty assessment, and domain alignment.

**Use this document to:**
1. Understand the complete evaluation framework
2. Reproduce the mission analysis process
3. Evaluate new mission concepts systematically
4. Make data-driven decisions about mission selection

---

## EVOLUTION OF METHODOLOGY

### Version 1.0 (Morning Session)
- **Focus:** CSLI requirements only
- **Problem:** Didn't validate if anyone actually needs the solution
- **Lessons:** High CSLI scores don't guarantee someone will fund/want the mission

### Version 2.0 (This Document)
- **Focus:** Multi-dimensional evaluation balancing ALL factors
- **Key Addition:** Problem validation through web research of agency stated needs
- **Philosophy:** Balance innovation with solving real problems

---

## PART 1: THE COMPREHENSIVE EVALUATION FRAMEWORK

### Overview of Evaluation Dimensions

The framework evaluates missions across **7 PRIMARY DIMENSIONS**:

1. **CSLI Selection Probability** (Will NASA select it for free launch?)
2. **Problem Validation** (Does someone explicitly need this?)
3. **Innovation/Novelty** (How unprecedented is this?)
4. **Transformative Impact** (How much does this change the world?)
5. **Domain Alignment** (Does it match your interests/expertise?)
6. **Funding Potential** (Are there RFPs or commercial opportunities?)
7. **Technical Feasibility** (Can it actually be built as a CubeSat?)

### Scoring Philosophy

**Balanced Approach:** No single dimension should dominate. A mission with perfect CSLI score but solving an imaginary problem = bad choice. A mission with 5/5 novelty but impossible to build = bad choice.

**Validation First:** Before scoring high on novelty or impact, **verify through web research** what currently exists and what agencies actually need.

---

## PART 2: DIMENSION 1 - CSLI SELECTION PROBABILITY

### Purpose
Evaluate likelihood NASA will select mission for CubeSat Launch Initiative (free launch worth ~$250k-$500k)

### Scoring Criteria (10 factors, 70 points total)

#### 1. NASA Strategic Plan Alignment (Weight: 2.0x)
**Score 1-5, multiply by 2.0**

- **5:** Directly advances multiple NASA strategic goals (Climate, Artemis, space weather, etc.)
- **4:** Strongly aligns with one major NASA priority
- **3:** Supports NASA goals but not primary focus
- **2:** Tangentially related to NASA mission
- **1:** No clear NASA alignment

**How to Evaluate:**
- Search: "NASA strategic plan 2024" + mission topic
- Check: NASA Science Mission Directorate priorities
- Verify: Recent NASA announcements mention this topic

#### 2. Mission Simplicity (Weight: 1.5x)
**Score 1-5, multiply by 1.5**

- **5:** Single primary objective, clear success criteria
- **4:** 2-3 related objectives, straightforward
- **3:** Multiple objectives, moderate complexity
- **2:** Many objectives, complex interdependencies
- **1:** Overly ambitious scope for CubeSat

**Red Flags:**
- "And also demonstrates..." multiple times
- Requires multiple complex subsystems to work perfectly
- Success depends on unproven technology chain

#### 3. Form Factor Compliance (Weight: 1.0x)
**Score 1-5, multiply by 1.0**

- **5:** 1U-3U, fits standard dispenser
- **4:** 6U, slightly larger but standard
- **3:** 12U, less common but available
- **2:** Custom size, non-standard
- **1:** Exceeds CubeSat standards

#### 4. Design Feasibility (Weight: 2.0x)
**Score 1-5, multiply by 2.0**

- **5:** All components COTS or flight-proven, straightforward integration
- **4:** Mostly COTS, minor customization needed
- **3:** Mix of COTS and custom, moderate development
- **2:** Significant custom development required
- **1:** Requires breakthrough technology

**How to Evaluate:**
- Search: [component type] + "CubeSat" + "flight proven"
- Check: NanoAvionics, Clyde Space, AAC Clyde catalogs
- Verify: Similar missions flown successfully

#### 5. Funding Realism (Weight: 1.5x)
**Score 1-5, multiply by 1.5**

- **5:** Under $50k (highly realistic for university)
- **4:** $50k-$100k (feasible with grants)
- **3:** $100k-$200k (requires multiple funding sources)
- **2:** $200k-$500k (challenging for university)
- **1:** Over $500k (unrealistic without major sponsor)

#### 6. Launch Flexibility (Weight: 1.0x)
**Score 1-5, multiply by 1.0**

- **5:** Any launch, any inclination, any time (LEO mission)
- **4:** Standard orbits (SSO, ISS), flexible timing
- **3:** Specific orbit requirements, somewhat flexible
- **2:** Narrow orbit window, limited options
- **1:** Requires dedicated launch or beyond-LEO (disqualifying for CSLI)

**Automatic Disqualifiers:**
- Mars orbit, lunar orbit, deep space (CSLI doesn't support)
- Requires specific constellation position

#### 7. Component Heritage & Availability (Weight: 1.5x)
**Score 1-5, multiply by 1.5**

- **5:** All components commercially available with flight heritage
- **4:** Mostly available, minor modifications
- **3:** Some custom components, development needed
- **2:** Significant custom hardware development
- **1:** Unproven technology, high development risk

**How to Verify:**
- Search: "CubeSat [component name] flight heritage"
- Check: Gunter's Space Page for similar missions
- Verify: Component manufacturer spec sheets

#### 8. Testing Requirements (Weight: 1.0x)
**Score 1-5, multiply by 1.0**

- **5:** Standard environmental testing only
- **4:** Standard plus minor additional tests
- **3:** Some specialized testing required
- **2:** Extensive specialized testing
- **1:** Testing beyond typical university capability

#### 9. Licensing Feasibility (Weight: 1.0x)
**Score 1-5, multiply by 1.0**

- **5:** No special licenses required
- **4:** Standard amateur radio license
- **3:** Commercial frequency coordination needed
- **2:** Complex regulatory approvals
- **1:** Requires international treaties or restricted technology

**Red Flags:**
- Quantum encryption (ITAR restrictions)
- Powerful lasers (weapons concerns)
- Active debris removal (international law issues)

#### 10. Ground Station Feasibility (Weight: 1.5x)
**Score 1-5, multiply by 1.5**

- **5:** Amateur radio frequencies, existing university station
- **4:** Standard commercial ground station services available
- **3:** Requires ground station network, available commercially
- **2:** Custom ground station development needed
- **1:** Requires dedicated global ground infrastructure

**How to Verify:**
- Check: Amazon Ground Station, KSAT, Infostellar coverage
- Verify: Amateur satellite frequencies sufficient for data rate

### CSLI Score Calculation

**Total Possible:** 70 points
**Percentage:** (Total Score / 70) × 100%

**Interpretation:**
- **85-100%:** Excellent CSLI probability
- **75-84%:** Good CSLI probability
- **65-74%:** Moderate CSLI probability
- **50-64%:** Low CSLI probability
- **<50%:** Very unlikely for CSLI

### Additional CSLI Qualitative Factors

Beyond the scored criteria, CubeSat 101 emphasizes these factors:

#### Keys to CSLI Selection Success:
□ Adequate funding secured for development
□ Great merit and feasibility reviews
□ Clear demonstration of benefit to NASA
□ Maximum flexibility in orbital requirements and launch dates

#### Mission Category Alignment:
- **Science missions:** 50% of CSLI selections
- **Technology development:** 66% of CSLI selections (overlap with science)
- **Education missions:** Also represented

**Note:** Most missions are dual-purpose (science + technology demo)

#### CubeSat 101 Best Practices:

**Design Principles:**
□ Components on exterior for easy access
□ Don't design to envelope limits - leave margin (mass, volume, power)
□ Double up on burn wires for deployables
□ Use high-melting point materials (avoid Teflon, nylon near heat sources)
□ Plan to build multiple units: ETU (engineering test unit), FlatSat, 2+ flight units

**Testing Philosophy:**
□ "Test like you fly" approach
□ Extensive photo documentation throughout development
□ All testing complete 1 month before readiness review

**Timeline Realism:**
- Concept to delivery: 9-24 months (realistic range)
- Ground station development: 2-12 months
- Hardware fabrication: 2-12 months
- Start licensing within 30 days of manifesting (4-6 month process)

#### Critical Risk Factors:

□ **Team expertise:** Relevant skills or access to mentors identified
□ **Student projects:** Plan for graduation/turnover, document everything
□ **Licensing:** Start early - no license = automatic DEMANIFEST
□ **Budget reserve:** Include 10%+ contingency for unexpected events
□ **Ground station:** Test before launch - inadequate station = mission killer

#### Automatic Disqualifiers (From CubeSat 101):

❌ Pyrotechnics (prohibited)
❌ No mechanism to obtain RF license
❌ Requires beyond-LEO launch for CSLI (Mars, lunar, deep space)
❌ Cannot complete required testing
❌ No clear NASA benefit

#### Discouraged Features (Reduce Selection Probability):

⚠️ Propulsion systems (increase complexity)
⚠️ Complex deployable mechanisms
⚠️ Inter-satellite operations
⚠️ Custom/novel batteries (use UL-listed to avoid extensive testing)
⚠️ Many interdependent systems

---

## PART 3: DIMENSION 2 - PROBLEM VALIDATION

### Purpose
Verify that the mission solves a problem someone explicitly stated they need (avoid "building what nobody wants")

### Methodology: Web Research for Stated Needs

**Critical Philosophy:** Don't assume people need your solution. **VERIFY** through research.

### Step 1: Identify the Problem Domain

**Question:** What problem does this mission claim to solve?

Examples:
- Space weather forecasting
- Wildfire detection
- Asteroid resource assessment
- GPS accuracy
- Climate data continuity

### Step 2: Research Agency Stated Needs

**Search Strategy:**

```
Search Pattern 1: "[Agency] [domain] capability gap 2024"
Example: "NOAA space weather capability gap 2024"

Search Pattern 2: "[Agency] strategic plan [domain]"
Example: "Space Force space domain awareness strategic plan"

Search Pattern 3: "[Agency] congressional report [domain]"
Example: "NASA Earth observation congressional report"

Search Pattern 4: "[Agency] [domain] solicitation funding"
Example: "NOAA space weather solicitation funding"
```

**Key Documents to Find:**
- Congressional budget justifications
- Strategic plans (agency-level, 5-year plans)
- GAO reports on capability gaps
- Industry days / pre-solicitation notices
- Academic workshops (Decadal Surveys for NASA)

### Step 3: Look for Explicit Statements

**What to Look For:**

✅ **STRONG VALIDATION:**
- "Critical gap"
- "Severely limit capability"
- "Urgent need"
- "Currently seeking"
- "Actively buying data"
- Specific dollar amounts committed

✅ **MODERATE VALIDATION:**
- "Priority area"
- "Of interest"
- "Under study"
- "Future capability"

❌ **WEAK/NO VALIDATION:**
- No mentions found
- Only general interest statements
- "Could be useful" (not "is needed")

### Step 4: Check for Existing Solutions

**Critical Question:** If this problem is so important, what currently exists?

**Search Pattern:**
```
"[problem domain] current missions 2024"
"[problem domain] operational satellites"
"[problem domain] commercial providers"
```

**Red Flags:**
- Multiple operational solutions exist but no stated gap
- Problem hasn't been mentioned in recent (2023-2025) documents
- Only found in old (pre-2020) documents

### Step 5: Validation Tier Assignment

**Tier 1 (⭐⭐⭐⭐⭐) - CRITICAL VALIDATED NEED:**
- Agency explicitly stated problem in recent (2023-2025) document
- Used words like "critical," "urgent," "severely limit"
- Agency actively funding solutions or buying data
- Clear capability gap with aging/expiring systems

**Tier 2 (⭐⭐⭐⭐) - STRONG VALIDATED NEED:**
- Agency stated this as priority area
- Problem identified in strategic plans
- Some existing capabilities but gaps remain
- Active research programs in this area

**Tier 3 (⭐⭐⭐) - MODERATE VALIDATION:**
- Problem acknowledged in literature
- General interest but no urgent statements
- Part of broader priority area
- "Nice to have" vs. "must have"

**Tier 4 (⭐⭐) - WEAK VALIDATION:**
- No recent agency statements found
- Only tangential mentions
- Solution in search of a problem
- Might be useful but no one asked for it

**Tier 5 (⭐) - NO VALIDATION:**
- No evidence anyone needs this
- Contradicts stated priorities
- Solution already widely available

### Scoring for Problem Validation

**Convert Tier to Score (1-5):**
- Tier 1 = 5 points
- Tier 2 = 4 points
- Tier 3 = 3 points
- Tier 4 = 2 points
- Tier 5 = 1 point

### Example: NOAA Space Weather (Tier 1 Validation)

**Search Performed:**
- "NOAA space weather capability gap 2024"

**Document Found:**
- NOAA Space Weather Next Program Congressional Report (Sept 2024)

**Explicit Statement:**
> "Current space weather missions have greatly exceeded their engineering life expectancy. There is a growing likelihood of a continuity gap in space weather data in the near future, which would severely limit NOAA's forecasting capability."

**Additional Evidence:**
- NOAA Commercial Space Weather Data Pilot actively buying data
- Specific solicitations for ionospheric observations
- Budget line items for space weather

**Validation Score:** 5/5 (Tier 1)

---

## PART 4: DIMENSION 3 - INNOVATION/NOVELTY

### Purpose
Assess how unprecedented the technology or approach is (avoid inflated self-assessment)

### Critical Lesson Learned
**ALWAYS RESEARCH WHAT EXISTS** before claiming high novelty. Ground-based versions, previous missions, and existing commercial solutions often exist.

### Methodology: Honest Novelty Assessment

### Step 1: Break Down the Innovation Claims

**Question:** What specifically is claimed to be novel?

Example - CRYPTO-SAT:
- Claim: "First space-based quantum random number generator"
- Components: (1) Quantum RNG, (2) In space, (3) Providing randomness

### Step 2: Research Each Component

**Search Pattern:**
```
"quantum random number generator" (general tech)
"quantum random number generator space" (space application)
"space-based random number generation" (alternate phrasing)
"[Country] quantum satellite" (international missions)
"micius satellite quantum" (specific known missions)
```

### Step 3: Identify What Actually Exists

**For CRYPTO-SAT Example:**
- ✅ Ground-based QRNGs: Widely available commercially
- ✅ Space-based quantum: China's Micius (2016) demonstrated quantum key distribution
- ✅ Random number generation: Standard spacecraft function
- ❌ Space-based QRNG for commercial distribution: Not found

**Conclusion:** Technology exists (ground), space quantum exists (Micius), but specific combo is new.

### Step 4: Assess Innovation Level

**5/5 - Revolutionary:**
- Technology has NEVER been demonstrated anywhere (ground or space)
- No similar approaches found in literature
- Creates entirely new capability
- **Verification:** Multiple search strategies found nothing similar

**Examples:**
- First-ever CubeSat (2003)
- First interplanetary CubeSat (MarCO 2018)
- Novel physics experiment never done before

**4/5 - Highly Innovative:**
- Technology demonstrated on ground but never in space
- Novel combination of existing technologies
- Significantly advances state-of-art
- **Verification:** Found ground demonstrations but no space missions

**Examples:**
- First AI onboard processing on CubeSat (Phi-Sat-1, 2024)
- First distributed CubeSat constellation with autonomous coordination
- Novel sensor miniaturization achieving 10x improvement

**3/5 - Moderately Novel:**
- Technology exists elsewhere but new application
- Incremental improvement to existing capability
- Different methodology for known problem
- **Verification:** Similar missions exist but approach differs

**Examples:**
- Hyperspectral imaging (exists) applied to asteroid prospecting (new application)
- ML wildfire prediction (exists for terrestrial data) using satellite data (adaptation)

**2/5 - Incremental:**
- Similar missions have flown
- Improvement to existing capability
- Different platform for existing tech
- **Verification:** Multiple similar missions found

**Examples:**
- Another Earth observation imager (many exist)
- Quantum satellite (Micius already flew)
- Space weather monitoring (SOHO, ACE, DSCOVR exist)

**1/5 - Not Novel:**
- Widely available capability
- Many operational missions doing this
- Standard CubeSat application
- **Verification:** Numerous existing examples

**Examples:**
- Basic communications relay (Iridium, others)
- Simple Earth photography (Planet, others)
- Amateur radio transponder (many exist)

### Step 5: Honest Self-Assessment Checklist

Before assigning novelty score, ask:

□ Did I search for ground-based versions of this technology?
□ Did I search for international missions (China, ESA, Russia)?
□ Did I check recent CubeSat launches (2020-2025)?
□ Did I search with alternate terminology?
□ Am I confusing "new for CubeSats" with "new in general"?
□ Am I calling incremental improvements "revolutionary"?

**If you answered NO to any:** Do more research before scoring.

### Novelty Score Calculation

**Score:** 1-5 based on honest assessment above

**Documentation Required:**
- What searches were performed
- What existing solutions were found
- Why the claimed novelty level is justified
- What specifically is novel vs. what exists

---

## PART 5: DIMENSION 4 - TRANSFORMATIVE IMPACT

### Purpose
Assess the real-world effect if the mission succeeds perfectly

### Methodology

### Step 1: Identify the Impact Claim

**Question:** If this mission succeeds, what changes?

### Step 2: Assess Scale of Impact

**5/5 - Revolutionary Impact:**
- Enables entirely new industry
- Saves many lives or prevents catastrophe
- Fundamentally changes how we understand the universe
- Multi-billion dollar economic impact
- Affects billions of people

**Examples:**
- GPS (enabled trillion-dollar industries)
- Asteroid mining validation (enables space economy)
- Early earthquake warning (saves thousands of lives)

**4/5 - High Impact:**
- Significantly improves existing capability
- Clear economic benefit ($100M+ value)
- Protects critical infrastructure
- Affects millions of people
- Advances major scientific field

**Examples:**
- Improved space weather forecasting (protects power grid, satellites)
- Wildfire early detection (saves property, lives)
- Climate monitoring (informs policy)

**3/5 - Moderate Impact:**
- Useful improvement to current systems
- Economic benefit ($10M-$100M)
- Regional or sectoral impact
- Advances specific research area

**Examples:**
- Improved crop monitoring (helps farmers)
- Debris tracking (satellite protection)
- Educational outreach (inspires students)

**2/5 - Limited Impact:**
- Niche application
- Small user base
- Incremental improvement
- Primarily academic interest

**Examples:**
- Specific astrophysics measurement
- Technology demonstration for future use
- Data for single research paper

**1/5 - Minimal Impact:**
- No clear application
- Duplicates existing capability
- Interest only to mission team
- No follow-on potential

### Step 3: Validate Impact Claims

**Questions to Ask:**

□ Is the impact mechanism clearly explained?
□ Are there actual users/customers identified?
□ Has anyone asked for this capability?
□ What happens if this mission never flies?
□ Is the impact direct or requires many other things to happen first?

**Red Flags for Inflated Impact:**
- "Could revolutionize..." without mechanism
- Impact requires multiple future breakthroughs
- No identified users or beneficiaries
- Circular reasoning ("important because space")

### Impact Score Calculation

**Score:** 1-5 based on honest assessment

**Documentation Required:**
- Who specifically benefits
- How the impact mechanism works
- Scale of effect (people/dollars/capability)
- Why this impact is realistic

---

## PART 6: DIMENSION 5 - DOMAIN ALIGNMENT

### Purpose
Ensure mission aligns with your interests, expertise, and goals

### User's Stated Preferred Domains:

1. **Space Weather & Geospace** ⚡
2. **Space Domain Awareness** 🛰️
3. **Technology Demonstration** 🔬
4. **Deep Space** 🚀
5. **Astrophysics** ⭐
6. **Novel/Cross-Domain** 🎯

### Additional Interest:
- **Earth Observation ONLY IF** it enables planetary/asteroid applications (e.g., LITHIUM HUNTER)

### Scoring for Domain Alignment

**5/5 - Perfect Match:**
- Directly in preferred domain
- Combines multiple interests
- Clear pathway to future applications in preferred areas

**Examples:**
- Space weather monitoring with AI (space weather + technology demo)
- Asteroid prospecting using hyperspectral (enables space mining interest)

**4/5 - Strong Match:**
- In preferred domain
- Aligns with stated interests

**Examples:**
- Deep space CubeSat demonstration
- Astrophysics measurement

**3/5 - Moderate Match:**
- Partially aligns with interests
- Has elements of preferred domains

**Examples:**
- Earth observation with novel technology demonstration component

**2/5 - Weak Match:**
- Tangentially related to interests
- Requires justification for alignment

**1/5 - No Match:**
- Outside preferred domains
- No clear connection to interests

**Examples (for you specifically):**
- Pure Earth observation with no planetary application
- Standard communications relay
- Agricultural monitoring without space exploration connection

### Domain Alignment Score

**Score:** 1-5 based on match to your preferences

---

## PART 7: DIMENSION 6 - FUNDING POTENTIAL

### Purpose
Assess likelihood of securing development funding beyond CSLI launch

### Methodology: Research Funding Opportunities

### Step 1: Identify Potential Funding Sources

**Government Sources:**
- NASA CSLI (free launch)
- NASA ROSES (research grants)
- NSF (research + education)
- DoD/Space Force (military applications)
- NOAA (weather/climate)
- DOE (energy-related)

**Commercial Sources:**
- Venture capital (if commercial application)
- Industry partnerships (if industry benefit)
- Licensing/data sales (if revenue model)

### Step 2: Research Active Opportunities

**Search Patterns:**
```
"NASA ROSES 2025 [domain]"
"NSF solicitation [domain] 2024"
"Space Force small satellite [domain]"
"[Agency] RFP CubeSat [domain]"
```

**Key Sites to Check:**
- grants.gov
- beta.sam.gov
- nspires.nasaprs.com (NASA)
- nsf.gov/funding
- SpaceNews.com (announcements)

### Step 3: Assess Funding Likelihood

**5/5 - Strong Funding Probability:**
- Active RFP explicitly seeking this capability
- Agency currently buying this data/service
- Multiple funding sources available
- Clear revenue model (if commercial)

**Evidence:**
- Open solicitation with upcoming deadline
- Agency budget documents mention this need
- Recent awards in this area

**4/5 - Good Funding Probability:**
- Strong alignment with agency priorities
- Recent solicitations in this area (even if currently closed)
- Demonstrated funding history
- Potential commercial interest

**3/5 - Moderate Funding Probability:**
- General alignment with agency missions
- Competitive programs available
- Requires strong proposal to win
- Uncertain commercial market

**2/5 - Low Funding Probability:**
- Limited funding sources
- Highly competitive with many proposals
- Requires multiple grants to fully fund
- No commercial path identified

**1/5 - Minimal Funding Probability:**
- No identified funding sources beyond CSLI
- Outside agency priorities
- No commercial viability
- Would require self-funding

### Funding Score Calculation

**Score:** 1-5 based on research

**Documentation:**
- Specific funding sources identified
- Evidence of recent awards in area
- Commercial viability assessment
- Realistic funding timeline

---

## PART 8: DIMENSION 7 - TECHNICAL FEASIBILITY

### Purpose
Realistic assessment of whether mission can be built and flown

### Assessment Criteria

**5/5 - Highly Feasible:**
- All technology at TRL 7-9 (flight-proven)
- COTS components available
- Similar missions successfully flown
- Low technical risk

**How to Verify:**
- Search: "CubeSat [technology] flight heritage"
- Check: Similar successful missions
- Verify: Component availability from suppliers

**4/5 - Feasible:**
- Mostly TRL 6-9
- Minor development required
- Similar missions succeeded with some lessons learned
- Moderate technical risk

**3/5 - Challenging:**
- Mix of TRL 4-6
- Significant development effort
- Some similar attempts with mixed results
- Substantial technical risk

**2/5 - High Risk:**
- Technology at TRL 3-4
- Major development required
- Few similar attempts, unclear if feasible
- High technical risk

**1/5 - Speculative:**
- Technology at TRL 1-2
- Requires breakthroughs
- Never demonstrated
- Very high risk / likely infeasible

### Technical Feasibility Score

**Score:** 1-5 based on TRL and heritage

---

## PART 9: COMPREHENSIVE SCORING SYSTEM

### Weighting Strategy

Based on your priorities:
1. Innovation/Novelty - Most important
2. Impact - Second most important
3. Problem Validation - Critical (avoid building what nobody wants)
4. Domain Alignment - Must match interests
5. CSLI Probability - Necessary for selection
6. Funding Potential - Important for development
7. Technical Feasibility - Gating factor

### Proposed Weights (Total = 100%)

| Dimension | Weight | Rationale |
|-----------|--------|-----------|
| **Innovation/Novelty** | 25% | Your #1 priority |
| **Impact** | 20% | Your #2 priority |
| **Problem Validation** | 20% | Critical lesson learned today |
| **Domain Alignment** | 15% | Must match your interests |
| **CSLI Probability** | 10% | Necessary but not sufficient |
| **Funding Potential** | 5% | Nice to have |
| **Technical Feasibility** | 5% | Gating factor (score <3 disqualifies) |

### Calculation Method

**Step 1:** Score each dimension (1-5)

**Step 2:** Normalize CSLI score (convert percentage to 1-5 scale)
- 85-100% → 5
- 75-84% → 4
- 65-74% → 3
- 50-64% → 2
- <50% → 1

**Step 3:** Apply weights and calculate total

```
Total Score = (Novelty × 0.25) + (Impact × 0.20) + (Validation × 0.20) +
              (Domain × 0.15) + (CSLI × 0.10) + (Funding × 0.05) +
              (Feasibility × 0.05)
```

**Step 4:** Convert to 100-point scale

```
Final Score = Total Score × 20
```

**Interpretation:**
- **90-100:** Exceptional mission candidate
- **80-89:** Excellent mission candidate
- **70-79:** Good mission candidate
- **60-69:** Acceptable mission candidate
- **<60:** Reconsider or significantly revise

### Gating Factors (Automatic Disqualification)

Regardless of total score, mission is disqualified if:

□ Technical Feasibility < 3 (too risky)
□ Domain Alignment < 2 (doesn't match interests)
□ CSLI Probability < 2 AND Funding Potential < 3 (no path to launch/funding)
□ Problem Validation = 1 AND Novelty < 4 (solving imaginary problem with existing tech)

---

## PART 10: DOCUMENTATION REQUIREMENTS

### For Each Mission Evaluation, Document:

**1. CSLI Evaluation:**
- Score for each of 10 criteria
- Total score and percentage
- Key strengths and weaknesses

**2. Problem Validation:**
- Search queries performed
- Documents found (with dates)
- Explicit agency quotes
- Validation tier assignment
- Existing solutions identified

**3. Novelty Assessment:**
- Innovation claims broken down
- Search results for each claim
- What exists vs. what's new
- Honest novelty score with justification

**4. Impact Assessment:**
- Impact mechanism explained
- Beneficiaries identified
- Scale of effect estimated
- Validation of impact claims

**5. Domain Alignment:**
- Which preferred domains matched
- Rationale for score

**6. Funding Research:**
- Funding sources identified
- RFPs/solicitations found (with deadlines)
- Commercial viability assessment

**7. Technical Feasibility:**
- TRL assessment for key technologies
- Similar missions referenced
- Component availability verified
- Risk assessment

**8. Final Calculation:**
- All scores tabulated
- Weights applied
- Final score calculated
- Recommendation with rationale

---

## PART 11: REPRODUCIBILITY CHECKLIST

To reproduce this analysis:

□ Read NASA CSLI CubeSat 101 (Ch 1-3)
□ Use 10-criteria CSLI rubric with weights
□ Perform web searches for agency stated needs (document searches used)
□ Research existing solutions (document what was found)
□ Assess novelty honestly (show work for each innovation claim)
□ Evaluate impact realistically (identify actual beneficiaries)
□ Check domain alignment against user preferences
□ Research funding opportunities (record sources found)
□ Verify technical feasibility (cite similar missions)
□ Apply weighted scoring formula
□ Check gating factors
□ Document everything

---

## PART 12: METHODOLOGY VALIDATION

### How to Validate This Methodology Works:

**Test Case 1: Known Good Mission**
- Take successful CubeSat mission (e.g., Planet Labs imaging)
- Score using this methodology
- Should score high (80+)

**Test Case 2: Known Failed Selection**
- Take mission rejected by CSLI
- Score using methodology
- Should identify weaknesses

**Test Case 3: "Product Nobody Wants"**
- Take technically feasible but unsolicited idea
- Score using methodology
- Should score low on Problem Validation, hurting total score

### Self-Correction Mechanisms:

1. **Web Research Requirement:** Forces validation vs. assumptions
2. **Honest Novelty Assessment:** Multiple searches required before claiming novelty
3. **Problem Validation Tier:** Can't score high without evidence
4. **Gating Factors:** Prevents one high score from masking critical weaknesses
5. **Documentation:** Requires showing work, catches hand-waving

---

## PART 13: NEXT STEPS - APPLYING THIS METHODOLOGY

### Step 1: Filter Missions by Domain
Identify missions that match your preferred domains:
- Space Weather & Geospace
- Space Domain Awareness
- Technology Demonstration
- Deep Space
- Astrophysics
- Novel/Cross-Domain
- Earth Observation (ONLY if enables planetary applications)

### Step 2: Re-evaluate Filtered Missions
Apply complete 7-dimension evaluation to remaining missions

### Step 3: Rank by Comprehensive Score
Sort missions by final weighted score

### Step 4: Deep Dive Top 3-5
Perform detailed analysis on top candidates

### Step 5: Make Final Selection
Choose mission balancing all factors

---

## CONCLUSION

This methodology evolved from painful lessons:
1. High CSLI scores don't mean anyone wants it (CRYPTO-SAT)
2. Novelty claims need verification (CRYPTO-SAT, LITHIUM HUNTER)
3. Innovation alone isn't enough (EMERGENCY-MESH)
4. Must balance novelty with problem validation

**The Sweet Spot:** Missions that solve explicitly stated agency needs while adding genuine innovation beyond what currently exists.

**Use this document** as the master reference for all future mission evaluations. It's comprehensive, reproducible, and battle-tested through today's analysis.

---

*Methodology Version 2.0 - Created 2025-11-02*
*Ready for application to mission selection*
