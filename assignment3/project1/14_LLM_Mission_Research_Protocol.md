# LLM MISSION RESEARCH PROTOCOL
**For CubeSat Mission Concept Generation & Evaluation**

**Created:** 2025-11-02  
**Version:** 1.0  
**Companion to:** 13_MASTER_Evaluation_Methodology.md

---

## PURPOSE

This document provides **explicit execution instructions** for LLMs to research, evaluate, and rank CubeSat mission concepts using the comprehensive methodology. 

**Goal:** Generate a ranked list of viable mission concepts for a Masters in Space Operations CubeSat course project.

---

## USER CONTEXT & CONSTRAINTS

### Academic Requirements
- **Program:** Masters in Engineering - Space Operations
- **Course:** CubeSat Systems
- **Deliverable:** Single mission concept to develop through course
- **Timeline:** ~4-6 months for mission design (typical semester)
- **Resources:** University-level (limited budget, access to standard CubeSat components)

### User's Preferred Mission Domains (Priority Order)
1. **Space Weather & Geospace** ⚡ (HIGHEST INTEREST)
2. **Space Domain Awareness** 🛰️
3. **Technology Demonstration** 🔬
4. **Deep Space** 🚀
5. **Astrophysics** ⭐
6. **Novel/Cross-Domain** 🎯

**Special Note:** Earth Observation missions are ONLY of interest if they enable planetary/asteroid applications (e.g., testing sensors for future asteroid prospecting).

### User's Priorities
1. **Innovation/Novelty** - Most important (25% weight)
2. **Transformative Impact** - Second priority (20% weight)
3. **Problem Validation** - Critical to avoid "building what nobody wants" (20% weight)
4. **Domain Alignment** - Must match interests (15% weight)

---

## EXECUTION PROTOCOL

### PHASE 1: MISSION CONCEPT GENERATION

**Task:** Generate 8-12 mission concepts across preferred domains

**Instructions:**
1. Generate 2-3 concepts per top domain (Space Weather, SDA, Tech Demo, Deep Space)
2. Ensure diversity of approaches within each domain
3. Focus on missions that could realistically be:
   - Designed in 4-6 months
   - Built with university resources + CSLI support
   - Launched via NASA CSLI (LEO missions only)

**Output Format for Each Concept:**
```
MISSION NAME: [Catchy, descriptive name]
DOMAIN: [Primary domain]
ONE-LINE DESCRIPTION: [Elevator pitch]
PRIMARY OBJECTIVE: [What it does]
KEY INNOVATION: [What's novel]
```

---

### PHASE 2: PRELIMINARY FILTERING

**Before detailed evaluation, filter out missions that:**
- ❌ Require beyond-LEO launch (CSLI only does LEO)
- ❌ Need technology at TRL 1-2 (too risky for masters project)
- ❌ Are pure Earth observation with no space exploration connection
- ❌ Duplicate well-established commercial capabilities with no innovation

**Action:** Eliminate obviously infeasible missions. Document why eliminated.

---

### PHASE 3: SYSTEMATIC EVALUATION

For each remaining mission, execute the following research and scoring process:

### STEP 1: PROBLEM VALIDATION RESEARCH

**Objective:** Verify someone explicitly needs this capability

**Required Searches (perform ALL of these):**

```
Search 1: "[Primary Agency] [mission domain] capability gap 2024"
Example: "NOAA space weather capability gap 2024"

Search 2: "[Primary Agency] strategic plan [domain] 2025"
Example: "Space Force space domain awareness strategic plan 2025"

Search 3: "[Primary Agency] [domain] solicitation funding"
Example: "NASA space weather solicitation funding"

Search 4: "[mission domain] current missions 2024"
Example: "space weather monitoring current missions 2024"

Search 5: "[mission domain] commercial providers"
Example: "space weather data commercial providers"
```

**What to Look For:**
- ✅ **Tier 1 (Score 5):** Agency explicitly uses words "critical gap," "urgent need," "severely limit," with recent dates (2023-2025)
- ✅ **Tier 2 (Score 4):** Agency states as "priority area," active research programs, some gaps remain
- ✅ **Tier 3 (Score 3):** General interest, part of broader priority, "nice to have"
- ❌ **Tier 4 (Score 2):** Only tangential mentions, no recent agency statements
- ❌ **Tier 5 (Score 1):** No evidence anyone needs this

**CRITICAL:** Document actual quotes from agency documents with dates and sources.

**Assign Validation Score:** 1-5 based on tier

---

### STEP 2: NOVELTY ASSESSMENT RESEARCH

**Objective:** Honestly assess how unprecedented the technology/approach is

**Required Searches (perform ALL of these):**

```
Search 1: "[core technology]" (general)
Example: "quantum random number generator"

Search 2: "[core technology] space" (space application)
Example: "quantum random number generator space"

Search 3: "[mission objective] satellite" (similar missions)
Example: "space-based random number generation satellite"

Search 4: "[technology] CubeSat flight heritage"
Example: "quantum sensor CubeSat flight heritage"

Search 5: "[country] [technology] satellite" (international missions)
Example: "China quantum satellite" or "ESA quantum mission"
```

**What to Document:**
- What exists on ground
- What exists in space (any platform)
- What exists on CubeSats specifically
- International missions (China, ESA, Russia often ahead in some areas)

**Scoring Rubric:**
- **5/5 - Revolutionary:** Never demonstrated anywhere, creates entirely new capability
- **4/5 - Highly Innovative:** Demonstrated on ground but never in space, or novel combination
- **3/5 - Moderately Novel:** New application of existing tech, incremental advancement
- **2/5 - Incremental:** Similar missions exist, improvement to existing capability
- **1/5 - Not Novel:** Widely available, many operational missions doing this

**Assign Novelty Score:** 1-5 based on research

---

### STEP 3: CSLI PROBABILITY ASSESSMENT

**Objective:** Calculate likelihood NASA CSLI will select this mission

**Use the 10-criteria rubric from master methodology:**
1. NASA Strategic Plan Alignment (Weight: 2.0x) - Score 1-5
2. Mission Simplicity (Weight: 1.5x) - Score 1-5
3. Form Factor Compliance (Weight: 1.0x) - Score 1-5
4. Design Feasibility (Weight: 2.0x) - Score 1-5
5. Funding Realism (Weight: 1.5x) - Score 1-5
6. Launch Flexibility (Weight: 1.0x) - Score 1-5
7. Component Heritage & Availability (Weight: 1.5x) - Score 1-5
8. Testing Requirements (Weight: 1.0x) - Score 1-5
9. Licensing Feasibility (Weight: 1.0x) - Score 1-5
10. Ground Station Feasibility (Weight: 1.5x) - Score 1-5

**Calculate CSLI Total:** Sum of (Score × Weight) = X out of 70 points

**Convert to Percentage:** (X / 70) × 100%

**Convert to 1-5 Scale for Final Scoring:**
- 85-100% → 5
- 75-84% → 4
- 65-74% → 3
- 50-64% → 2
- <50% → 1

**Assign CSLI Score:** 1-5 based on conversion

---

### STEP 4: IMPACT ASSESSMENT

**Objective:** Assess real-world effect if mission succeeds

**Key Questions:**
- Who specifically benefits? (Name agencies, industries, or populations)
- How does the impact mechanism work?
- What's the scale? (Lives saved? $ value? People affected?)
- What happens if this never flies?

**Scoring Rubric:**
- **5/5 - Revolutionary:** Enables new industry, saves many lives, affects billions, multi-billion $ impact
- **4/5 - High Impact:** Significantly improves capability, $100M+ value, protects infrastructure, affects millions
- **3/5 - Moderate Impact:** Useful improvement, $10M-$100M value, regional impact, advances specific research
- **2/5 - Limited Impact:** Niche application, small user base, incremental improvement
- **1/5 - Minimal Impact:** No clear application, duplicates existing, interest only to team

**Assign Impact Score:** 1-5 based on honest assessment

---

### STEP 5: DOMAIN ALIGNMENT

**Objective:** Check fit with user's interests

**Scoring:**
- **5/5:** Directly in top 3 preferred domains, combines multiple interests
- **4/5:** In preferred domain, clear alignment
- **3/5:** Partially aligns, has elements of preferred domains
- **2/5:** Tangentially related, requires justification
- **1/5:** Outside preferred domains, no clear connection

**Assign Domain Score:** 1-5 based on match

---

### STEP 6: FUNDING POTENTIAL RESEARCH

**Objective:** Assess likelihood of securing development funding

**Required Searches:**
```
Search 1: "NASA ROSES 2025 [domain]"
Search 2: "NSF solicitation [domain] 2024"
Search 3: "[relevant agency] RFP CubeSat [domain]"
Search 4: "[domain] commercial satellite data market"
```

**What to Look For:**
- Active RFPs with upcoming deadlines
- Recent awards in this area (shows funding availability)
- Commercial data buyers (e.g., NOAA commercial weather data pilot)
- Agency budget line items

**Scoring:**
- **5/5:** Active RFP seeking this capability, or agency currently buying data
- **4/5:** Strong alignment with agency priorities, recent solicitations
- **3/5:** General alignment, competitive programs available
- **2/5:** Limited funding sources, highly competitive
- **1/5:** No identified funding beyond CSLI

**Assign Funding Score:** 1-5 based on research

---

### STEP 7: TECHNICAL FEASIBILITY

**Objective:** Assess if mission can actually be built

**Required Search:**
```
Search: "CubeSat [key technology] flight heritage"
Search: "[similar mission name] CubeSat success"
```

**Scoring Based on TRL:**
- **5/5:** All tech TRL 7-9 (flight-proven), COTS available, similar missions succeeded
- **4/5:** Mostly TRL 6-9, minor development, similar missions with lessons learned
- **3/5:** Mix TRL 4-6, significant development, mixed results from similar attempts
- **2/5:** TRL 3-4, major development, few similar attempts
- **1/5:** TRL 1-2, requires breakthroughs, never demonstrated

**Assign Feasibility Score:** 1-5 based on TRL

---

### STEP 8: APPLY SCORING ADJUSTMENTS

#### Adjustment 1: "iPhone Exception" (Creating New Markets)

**Condition:** If (Novelty ≥ 4) AND (Validation ≤ 2) AND (Impact ≥ 4)

**Rationale:** Some innovations solve problems people don't know they have yet (e.g., iPhone)

**Action:** Add +0.5 to final weighted score (before converting to 100-point scale)

**Document:** Note "iPhone Exception Applied" in output

#### Adjustment 2: Masters Project Feasibility

**Condition:** If mission requires >$200k OR >12U OR TRL<3

**Action:** Add warning flag: "⚠️ HIGH RISK FOR MASTERS PROJECT"

**Rationale:** May not be completable within degree timeline/resources

---

### STEP 9: CALCULATE FINAL SCORE

**Weighted Score Formula:**
```
Total = (Novelty × 0.25) + (Impact × 0.20) + (Validation × 0.20) + 
        (Domain × 0.15) + (CSLI × 0.10) + (Funding × 0.05) + (Feasibility × 0.05)

[Apply iPhone Exception if applicable: Total = Total + 0.5]

Final Score = Total × 20  (converts to 100-point scale)
```

---

### STEP 10: CHECK GATING FACTORS

**Automatic Disqualification if ANY are true:**
- ❌ Technical Feasibility < 3 (too risky for masters project)
- ❌ Domain Alignment < 2 (doesn't match user interests)
- ❌ (CSLI < 2) AND (Funding < 3) - no path to launch/funding
- ❌ (Validation = 1) AND (Novelty < 4) - solving imaginary problem with existing tech

**If disqualified:** Mark as "ELIMINATED" and explain why

---

## STANDARDIZED OUTPUT FORMAT

### For Each Mission, Provide:

```markdown
## MISSION: [Name]

**Domain:** [Primary Domain]  
**Final Score:** [XX/100]  
**Recommendation:** [EXCELLENT / GOOD / ACCEPTABLE / ELIMINATED]

### Quick Summary
[2-3 sentence overview of mission and key innovation]

### Scoring Breakdown
| Dimension | Score | Weight | Contribution | Notes |
|-----------|-------|--------|--------------|-------|
| Novelty | X/5 | 25% | XX pts | [Key finding] |
| Impact | X/5 | 20% | XX pts | [Who benefits] |
| Validation | X/5 | 20% | XX pts | [Tier & evidence] |
| Domain | X/5 | 15% | XX pts | [Alignment] |
| CSLI | X/5 | 10% | XX pts | [XX% raw score] |
| Funding | X/5 | 5% | XX pts | [Sources] |
| Feasibility | X/5 | 5% | XX pts | [TRL & heritage] |
| **TOTAL** | | | **XX/100** | [Adjustments applied] |

### Problem Validation Evidence
- **Tier:** [1-5]
- **Key Sources:** [List documents with dates]
- **Explicit Quote:** "[Actual agency quote if Tier 1-2]"
- **Existing Solutions:** [What currently exists]

### Novelty Assessment
- **Claimed Innovation:** [What's supposedly novel]
- **Research Findings:** [What actually exists]
- **Honest Assessment:** [What's genuinely new]
- **Searches Performed:** [List key searches]

### Impact Mechanism
- **Beneficiaries:** [Specific users/agencies]
- **Scale:** [$ value or lives/people affected]
- **Pathway:** [How impact is realized]

### CSLI Viability
- **Total CSLI Score:** [XX/70 = YY%]
- **Strengths:** [Top scoring criteria]
- **Weaknesses:** [Low scoring criteria]
- **Selection Probability:** [High/Moderate/Low]

### Funding Opportunities
- **Sources Identified:** [List with dates]
- **Open Solicitations:** [Any current RFPs]
- **Commercial Path:** [If applicable]

### Technical Risk
- **TRL Range:** [X-Y]
- **Similar Missions:** [Examples]
- **Key Risks:** [Main technical challenges]
- **Masters Project Suitability:** [✅ Suitable / ⚠️ High Risk / ❌ Too Risky]

### Gating Factors
- [✅/❌] Feasibility ≥ 3
- [✅/❌] Domain ≥ 2  
- [✅/❌] Launch/Funding path exists
- [✅/❌] Not solving imaginary problem

### Overall Assessment
[2-3 paragraphs explaining why this score makes sense, key strengths, key weaknesses, and suitability for masters project]

---
```

---

## FINAL OUTPUT: RANKED COMPARISON TABLE

After evaluating all missions, provide summary table:

```markdown
# MISSION RANKING SUMMARY

| Rank | Mission Name | Total Score | Novelty | Impact | Validation | Domain | CSLI | Recommendation | Flags |
|------|--------------|-------------|---------|--------|------------|--------|------|----------------|-------|
| 1 | [Name] | XX/100 | X/5 | X/5 | X/5 | X/5 | X/5 | EXCELLENT | [iPhone / ⚠️ Risk / None] |
| 2 | [Name] | XX/100 | X/5 | X/5 | X/5 | X/5 | X/5 | EXCELLENT | |
| ... | | | | | | | | | |

## TOP 3 RECOMMENDATIONS

### 🥇 FIRST CHOICE: [Mission Name] (XX/100)
**Why:** [Key strengths - novelty, validation, fit, feasibility]
**Caution:** [Any concerns]

### 🥈 SECOND CHOICE: [Mission Name] (XX/100)
**Why:** [Key strengths]
**Caution:** [Any concerns]

### 🥉 THIRD CHOICE: [Mission Name] (XX/100)
**Why:** [Key strengths]
**Caution:** [Any concerns]

## STRATEGIC GUIDANCE

[1-2 paragraphs on which mission best balances innovation, problem validation, and masters project feasibility]
```

---

## EXECUTION CHECKLIST

Before submitting results, verify:

- [ ] All missions evaluated across all 7 dimensions
- [ ] Web searches performed and documented for Validation, Novelty, CSLI alignment, Funding
- [ ] Actual agency quotes included for Tier 1-2 validation
- [ ] Existing solutions researched and documented
- [ ] CSLI scores calculated using all 10 criteria with weights
- [ ] Gating factors checked for each mission
- [ ] iPhone Exception applied where appropriate
- [ ] Masters project suitability flagged
- [ ] Final scores calculated using weighted formula
- [ ] Missions ranked from highest to lowest score
- [ ] Top 3 recommendations provided with strategic rationale
- [ ] All sources cited with dates

---

## SPECIAL INSTRUCTIONS FOR LLM EXECUTION

1. **Be Thorough:** Don't skip searches. Perform ALL required searches for each mission.

2. **Be Honest:** Don't inflate novelty scores. If ground-based versions exist, acknowledge it.

3. **Show Your Work:** Document search queries, sources found, and reasoning for scores.

4. **Think Like a Reviewer:** NASA reviewers will check your claims. Make sure they hold up.

5. **Balance Innovation and Pragmatism:** The goal is a mission that's both exciting AND completable in a masters program.

6. **Flag Risks Early:** If a mission won't work for masters timeline/budget, say so upfront.

7. **Cite Sources with Dates:** Recent documents (2023-2025) count more than old ones (pre-2020).

8. **Don't Hallucinate Validation:** If you can't find agency statements, admit it. Don't invent needs.

---

## REFERENCE

**Full Methodology:** See 13_MASTER_Evaluation_Methodology.md for complete details on:
- Detailed scoring rubrics
- Examples for each score level
- Search pattern details
- Background philosophy

**This document provides:** Streamlined execution protocol for systematic mission research and ranking.

---

**Version:** 1.0  
**Created:** 2025-11-02  
**Ready for immediate LLM execution**
