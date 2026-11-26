# Executive Presentation Outline: "Is That College Worth the Fees?"
## A Power BI Value-for-Money Analytics Framework for NIRF 2025 Engineering Colleges

**PowerPoint File:** [`NIRF_PowerBI_Presentation.pptx`](NIRF_PowerBI_Presentation.pptx)  
**Target Audience:** Prospective Engineering Students, Middle-Class Families & Academic Evaluators  
**Length:** 10 Slides (Widescreen 16:9)

---

### Slide 1: Title & Framing
* **Title:** Is That College Worth the Fees?
* **Subtitle:** A Power BI Value-for-Money Analytics Framework for NIRF 2025 Engineering Colleges
* **Key Context:**
  - Stakeholder: Middle-Class Indian Families deciding on 4-year engineering admissions.
  - Core Dilemma: Balancing ₹15L–₹20L tuition exposure against realistic placement returns.
  - Deliverables: 5-Page Power BI Report, DAX Analytics Engine, and Merged Audited Dataset.

### Slide 2: The Problem: Brand Prestige vs. Crushing Tuition Debt
* **The Family Dilemma:** Over 1.2 million students evaluate engineering admissions yearly, assuming higher NIRF rank guarantees higher salary and safer financial security.
* **The Hidden Market Variance:** Tuition fees vary by over 130× across the Top 100 NIRF colleges (₹14,110 to ₹19.5 Lakhs), while median placement packages range from ₹3.36 LPA to ₹22.50 LPA.
* **The Analytics Solution:** An objective Value-for-Money index that calculates the exact years of gross salary needed to pay back total 4-year academic dues, cutting through marketing spin.

### Slide 3: Core Metric & The Hardest Data Engineering Problem
* **Formula:** $\text{Fee-to-Salary Ratio} = \frac{\text{Total 4-Year Mandatory Academic Fees}}{\text{Annual Median Placement Salary}}$
* **The NIRF Data Blindspot:** NIRF DCS reports student intake, graduated cohorts, and placement numbers, but completely omits student tuition fees. Expenditure figures in NIRF represent institutional operational budgets, NOT student tuition liability.
* **Audited Solution:** Built an automated Python pipeline downloading all 100 DCS PDFs in 29.6 seconds. Audited 100 official institutional fee circulars (JoSAA, state counselling authorities, university notifications) for General-Category Indian students.

### Slide 4: Power BI Report Architecture (5 Purpose-Built Pages)
1. **Page 1: Executive Overview (3 Visuals)** — Multi-Row KPI card, Fees vs Salary scatter bubble plot with State Play Axis, and 224x recovery disparity bar chart.
2. **Page 2: The Mid-Tier Trap (4 Visuals)** — Multi-Row card, City tech-hub slicer, dual-axis Combo chart (Fees/Salary vs Ratio), and Rank Band matrix table.
3. **Page 3: Geographic ROI (3 Visuals)** — Custom India TopoJSON shape map, state recovery bar ranking, and interactive 3-tier Decomposition Tree.
4. **Page 4: Capital Risk & Placement (3 Visuals)** — 4-Quadrant scatter plot (Placement % vs Fees), Institution Type donut chart, and Danger Zone watchlist table.
5. **Page 5: College Explorer (2 Visuals)** — Multi-hierarchy Rank Band & State slicer with full-width 1920px master searchable college explorer table.

### Slide 5: Finding 1: Public Subsidies Deliver up to 224× Faster Capital Recovery
* **The Value Champion: Jadavpur University (NIRF #18):**
  - 4-Year Fees: ₹14,110 (₹2,400/yr tuition) | Median Salary: ₹10.50 LPA
  - Recovery Ratio: **0.013 Years (~5 Days)** | Placement: 91.01%
  - Other Public Champions: Jamia Millia (0.048 yrs / 18 days), Anna Univ (0.166 yrs / 2 months), AMU (0.186 yrs).
* **The Extreme Capital Burden: SRM IST (NIRF #14):**
  - 4-Year Fees: ₹18.10 Lakhs | Median Salary: ₹6.20 LPA
  - Recovery Ratio: **2.919 Years (35 Months)** — 224.5× longer than Jadavpur despite higher NIRF rank!
  - Other High-Debt Peers: Vignan's (2.887 yrs), UPES (2.585 yrs), Graphic Era (2.560 yrs), Vel Tech (2.500 yrs).

### Slide 6: Finding 2: The "Mid-Tier Trap" in NIRF Ranks 26–75
* **Band 1 (Ranks 1–25):** Mean Fee ₹8.63L | Mean Salary ₹15.05 LPA | Recovery **0.684 yrs** | 79.72% Placed
* **Band 2 (Ranks 26–50):** Mean Fee ₹9.22L (+6.8%) | Mean Salary ₹10.76 LPA (-28.5%) | Recovery **0.992 yrs** | 71.39% Placed
* **Band 3 (Ranks 51–75):** Mean Fee ₹9.10L | Mean Salary ₹10.40 LPA (-30.9%) | Recovery **0.968 yrs** | 72.37% Placed
* **Band 4 (Ranks 76–100):** Mean Fee ₹6.75L | Mean Salary ₹8.17 LPA | Recovery **0.982 yrs** | 64.27% Placed
* **Strategic Takeaway:** Colleges ranked 26–75 cost ₹50,000 to ₹60,000 *more* on average than top 25 colleges, yet yield ₹4.3L to ₹4.6L *lower* annual salaries.

### Slide 7: Finding 3: Geographic Clustering Dictates Educational Return
* **High Return States (Fastest Payback):**
  - West Bengal (4 Colleges): Avg Fee ₹5.20L | Avg Salary ₹12.50 LPA | Recovery: **0.420 Years (~5 Months)**
  - Madhya Pradesh (3 Colleges): Avg Fee ₹7.26L | Avg Salary ₹17.49 LPA | Recovery: **0.437 Years**
  - Delhi (6 Colleges): Avg Fee ₹9.86L | Avg Salary ₹16.08 LPA (Highest in India!) | Recovery: **0.602 Years**
* **Capital Exposure States (Slow Payback):**
  - Uttarakhand (3 Colleges): Avg Fee ₹12.83L | Avg Salary ₹9.50 LPA | Recovery: **1.889 Years (~23 Months)**
  - Karnataka (6 Colleges): Avg Fee ₹10.69L | Avg Salary ₹9.03 LPA | Recovery: **1.339 Years**
  - Tamil Nadu (14 Colleges): Anna Univ (0.16 yrs) vs SRM (2.92 yrs) and Vel Tech (2.50 yrs).

### Slide 8: Finding 4: The Double Penalty — High Fees Paired with Sub-50% Placement
* **The Denominator Trap:** NIRF median salary only counts placed students. Unplaced students earn ₹0.
* **Danger Zone Examples:**
  - KIIT (NIRF #36): ₹16.35L fees, ₹7.40 LPA salary, **34.9% placement** (over 65% unplaced!).
  - Vignan's (NIRF #80): ₹9.70L fees, ₹3.36 LPA salary, **43.4% placement**, 2.89 years recovery.
  - Graphic Era (NIRF #52): ₹12.80L fees, ₹5.00 LPA salary, **49.3% placement**, 2.56 years recovery.

### Slide 9: Actionable Decision Framework: 3 Golden Rules for Families
1. **Rule 1 (Unconditional Acceptance):** If admitted to an IIT, top NIT, or premier State University (Jadavpur, Anna Univ, DTU): Accept unconditionally. Subsidized fees (<₹8.8L) and high salaries (>₹12 LPA) ensure recovery in under 9 months.
2. **Rule 2 (The Mid-Tier Private Veto):** If choosing between a private college (Rank 26–75) costing >₹15 Lakhs and an accredited regional government college costing <₹4 Lakhs: Decline the private college unless confirmed in Computer Science/IT with >85% branch placement.
3. **Rule 3 (The Cost of Living Adjustment):** Always account for ₹1.2L–₹2.2L/year in residential hostel/mess expenses.

### Slide 10: Honest Analytical Limitations
1. **Branch-Wise Median Masking:** Campus median combines CS (₹18–₹24 LPA) with core branches (₹4.5–₹6.5 LPA).
2. **The Non-Placed Cohort (0 LPA):** Median applies only to students who received offers.
3. **Non-Academic Living Overhead:** Total 4-year living expenses add ₹4.8L to ₹8.8L to the cash requirement.
