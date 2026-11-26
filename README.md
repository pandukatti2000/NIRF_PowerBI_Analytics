# NIRF 2025 Engineering College Value-for-Money (VFM) Power BI Analytics

> **AccioJob · Spin Build Pitch · Data Analytics · Project DA-16**  
> *"Is that college worth the fees?" — A Comprehensive 5-Page Power BI Analytics & Reporting Solution*

[![Power BI](https://img.shields.io/badge/Power_BI-Desktop-F2C811?logo=powerbi&logoColor=black)](https://powerbi.microsoft.com/)
[![Dashboard File](https://img.shields.io/badge/Report-NIRF__Engineering__VFM__Analytics.pbix-orange.svg)](NIRF_Engineering_VFM_Analytics.pbix)
[![Dataset](https://img.shields.io/badge/Dataset-colleges__final.csv-blue.svg)](data/colleges_final.csv)
[![Presentation](https://img.shields.io/badge/PowerPoint-10--Slide_Deck-D24726?logo=microsoftpowerpoint&logoColor=white)](NIRF_PowerBI_Presentation.pptx)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](#license)

---

## 1. Project Overview & Stakeholder Decision

* **The Stakeholder:** A prospective Indian engineering student and their family evaluating admission offers across top NIRF-ranked institutions.
* **The Decision:** Determining which engineering institution delivers the highest financial return relative to mandatory four-year academic fees, balancing brand prestige against family capital outlays and educational loan burdens.
* **The Core Value Metric:**
  $$\text{Fee-to-Salary Ratio} = \frac{\text{Total 4-Year Mandatory Academic Fees (General Category)}}{\text{Annual Median Placement Salary}}$$
  *(Represents the equivalent years of gross first-year median salary required to pay back total 4-year tuition and academic dues. Lower values represent superior financial value.)*

---

## 2. Power BI Dashboard Architecture (`.pbix`)

The interactive dashboard file is **`NIRF_Engineering_VFM_Analytics.pbix`** (1920×1080 Widescreen). It contains **5 purpose-built analytical pages** designed with maximum clarity and 2 to 4 high-impact visuals per page:

```text
├── Page 1: Executive Overview (3 Visuals)
│   ├── Top Multi-Row Card: 97 Eligible Colleges, ₹8.43L Avg Fees, ₹11.14 LPA Avg Salary, 0.90 yrs Avg Recovery
│   ├── Scatter Bubble Plot: Fees vs. Salary (Sized by Placed Volume, colored by Institution Type, with State Play Axis)
│   └── Clustered Bar Chart: Highlighting the 224× recovery disparity (Jadavpur 0.013 yrs vs SRM 2.919 yrs)
│
├── Page 2: The Mid-Tier Trap (4 Visuals)
│   ├── Multi-Row Card: Rank Band Performance Metrics
│   ├── City Slicer: Interactive dropdown for tech hubs (Pune, Chennai, Delhi, etc.)
│   ├── Dual-Axis Combo Line/Column Chart: Columns show Fees & Salary; Line shows Recovery Years across Rank Bands
│   │   → Proves: Moving from Band 1 (Ranks 1–25) to Band 2 (Ranks 26–50) increases fees by 6.8% while salary drops by 28.5%!
│   └── Rank Band Matrix Table: Drill-down from Rank Band to individual institutions
│
├── Page 3: Geographic ROI (3 Visuals)
│   ├── Custom India Shape Map: Colored by Fee-Salary Ratio gradient using embedded TopoJSON map
│   ├── Clustered Horizontal Bar Chart: States ranked ascending by Recovery Time (West Bengal 5.0 mo vs Uttarakhand 22.7 mo)
│   └── Decomposition Tree: Interactive root-cause breakdown (Avg Ratio → State → Institution Type → College)
│
├── Page 4: Capital Risk & Placement (3 Visuals)
│   ├── 4-Quadrant Scatter Plot: Placement % (0–100%) vs 4-Year Fees (0–22 Lakhs)
│   │   → Exposes the "Danger Zone": Colleges charging >₹10L with <50% placement success
│   ├── Donut Chart: Breakdown of ranked colleges by Institution Type
│   └── Watchlist Table: Pinpointing high-risk colleges like KIIT (34.9% placed) and Graphic Era (49.3% placed)
│
└── Page 5: College Explorer (2 Visuals)
    ├── Multi-Hierarchy Slicer: Filter dynamically by Rank Band and State
    └── Full-Width Master Table (1920px): Searchable grid displaying Rank, College, City, State, Fees, Salary, Ratio, and Placement %
```

---

## 3. Data Model & DAX Formulas

### Primary Table: `colleges_final.csv` (100 Rows)
* `data/colleges_final.csv`: Joins NIRF DCS placement figures (AY 2023–24) with audited mandatory 4-year academic dues.

### Calculated Columns
```dax
Rank_Band = 
SWITCH(
    TRUE(),
    colleges_final[nirf_rank] <= 25, "Band 1 (Ranks 1-25)",
    colleges_final[nirf_rank] <= 50, "Band 2 (Ranks 26-50)",
    colleges_final[nirf_rank] <= 75, "Band 3 (Ranks 51-75)",
    "Band 4 (Ranks 76-100)"
)
```

```dax
Institution_Type = 
SWITCH(
    TRUE(),
    CONTAINSSTRING(colleges_final[college_name], "Indian Institute of Technology") || CONTAINSSTRING(colleges_final[college_name], "IIT"), "IIT",
    CONTAINSSTRING(colleges_final[college_name], "National Institute of Technology") || CONTAINSSTRING(colleges_final[college_name], "NIT"), "NIT",
    CONTAINSSTRING(colleges_final[college_name], "Jadavpur") || 
    CONTAINSSTRING(colleges_final[college_name], "Jamia") || 
    CONTAINSSTRING(colleges_final[college_name], "Anna") || 
    CONTAINSSTRING(colleges_final[college_name], "Delhi Technological") || 
    CONTAINSSTRING(colleges_final[college_name], "Netaji Subhas") || 
    CONTAINSSTRING(colleges_final[college_name], "College of Engineering, Pune") || 
    CONTAINSSTRING(colleges_final[college_name], "Aligarh") ||
    CONTAINSSTRING(colleges_final[college_name], "Madan Mohan") ||
    CONTAINSSTRING(colleges_final[college_name], "AU College"), "Premier State/Central Govt",
    "Private / Deemed"
)
```

### Core DAX Measures (`_Measures` table)
```dax
Eligible_Colleges = 
CALCULATE(COUNTROWS(colleges_final), colleges_final[placement_extraction_status] = "SUCCESS")

Avg_4Yr_Fees_Lakhs = 
CALCULATE(AVERAGE(colleges_final[total_4yr_academic_fees_lpa]), colleges_final[placement_extraction_status] = "SUCCESS")

Avg_Median_Salary_LPA = 
CALCULATE(AVERAGE(colleges_final[median_salary_lpa]), colleges_final[placement_extraction_status] = "SUCCESS")

Avg_Fee_Salary_Ratio = 
CALCULATE(AVERAGE(colleges_final[fee_salary_ratio]), colleges_final[placement_extraction_status] = "SUCCESS")

Avg_Recovery_Months = [Avg_Fee_Salary_Ratio] * 12

Avg_Placement_Rate = 
CALCULATE(AVERAGE(colleges_final[placement_percentage]), colleges_final[placement_extraction_status] = "SUCCESS")
```

---

## 4. Key Numerical Findings

1. **Public Subsidies Deliver up to 224× Faster Capital Recovery:**
   - **Jadavpur University** (NIRF #18) charges **₹14,110** total academic fees over four years against a median placement salary of **₹10.50 LPA**, recovering academic dues in **0.013 years** (~5 days of gross pay) with a **91.01%** placement rate.
   - **Jamia Millia Islamia** (NIRF #24) costs **₹0.66L** for a **₹13.78 LPA** median salary (**0.048 years** / 18 days; 84.6% placed).
   - In contrast, private universities like **SRM IST** (NIRF #14) charge **₹18.10L** in fees for a **₹6.20 LPA** median salary (**2.919 years** / 35 months), taking **224.5× longer** to recover fees than Jadavpur despite holding a higher NIRF rank.
2. **The "Mid-Tier Trap" (Ranks 26–75):**
   - **Band 1 (Ranks 1–25):** Mean Fee **₹8.63L** | Mean Salary **₹15.05 LPA** | Recovery **0.68 yrs** (8.2 mo) | Placed **79.72%**
   - **Band 2 (Ranks 26–50):** Mean Fee **₹9.22L** (+6.8%) | Mean Salary **₹10.76 LPA** (-28.5%) | Recovery **0.99 yrs** (11.9 mo) | Placed **71.39%**
   - **Band 3 (Ranks 51–75):** Mean Fee **₹9.10L** | Mean Salary **₹10.40 LPA** (-30.9%) | Recovery **0.968 yrs** (11.6 mo) | Placed **72.37%**
   - **Band 4 (Ranks 76–100):** Mean Fee **₹6.75L** | Mean Salary **₹8.17 LPA** | Recovery **0.982 yrs** (11.8 mo) | Placed **64.27%**
3. **Geographic Distribution:**
   - **Top Value States:** **West Bengal** (0.420 yrs avg ratio, ₹12.50 LPA salary) and **Delhi** (0.602 yrs avg ratio across 6 colleges with the country's highest state average salary: **₹16.08 LPA**).
   - **Least Value States:** **Uttarakhand** (1.889 yrs avg ratio) and **Karnataka** (1.339 yrs avg ratio, driven by high private tuition fees).

---

## 5. Repository Artifacts

* **Power BI File:** [`NIRF_Engineering_VFM_Analytics.pbix`](NIRF_Engineering_VFM_Analytics.pbix) (Widescreen 1080p 5-page report).
* **PowerPoint Presentation:** [`NIRF_PowerBI_Presentation.pptx`](NIRF_PowerBI_Presentation.pptx) (10 widescreen slides).
* **Slide Notes & Outline:** [`PRESENTATION_OUTLINE.md`](PRESENTATION_OUTLINE.md).
* **Visualization Blueprint:** [`POWERBI_BLUEPRINT.md`](POWERBI_BLUEPRINT.md) (Complete field mappings and DAX library).
* **Source Citations Log:** [`fee_sources.md`](fee_sources.md) (Audited references for all 100 institutions).
* **India TopoJSON Map:** [`india_states_powerbi.topojson`](india_states_powerbi.topojson) (Boundary definitions for India state visual).

---

## License

This project is licensed under the MIT License. Academic data sources belong to the Ministry of Education (NIRF) and respective universities.
