# NIRF 2025 Engineering College Value-for-Money (VFM) Power BI Analytics

> **AccioJob · Spin Build Pitch · Data Analytics · Project DA-16**  
> *"Is that college worth the fees?" — A Comprehensive 5-Page Power BI Analytics & Reporting Solution*

[![Power BI](https://img.shields.io/badge/Power_BI-Desktop-F2C811?logo=powerbi&logoColor=black)](https://powerbi.microsoft.com/)
[![Dataset](https://img.shields.io/badge/Dataset-colleges__final.csv-blue.svg)](data/colleges_final.csv)
[![Presentation](https://img.shields.io/badge/PowerPoint-10--Slide_Deck-D24726?logo=microsoftpowerpoint&logoColor=white)](NIRF_PowerBI_Presentation.pptx)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](#license)

---

## 1. Project Overview & Stakeholder Problem

* **The Stakeholder:** A prospective Indian engineering student and their family choosing among engineering college admission offers.
* **The Decision:** Determining which engineering institution delivers the highest financial return relative to mandatory four-year academic fees, balancing brand prestige against family capital outlays and educational loan burdens.
* **The Core Value Metric:**
  $$\text{Fee-to-Salary Ratio} = \frac{\text{Total 4-Year Mandatory Academic Fees (General Category)}}{\text{Annual Median Placement Salary}}$$
  *(Represents the equivalent years of gross first-year median salary required to pay back total 4-year tuition and academic dues. Lower values represent superior financial value.)*

---

## 2. Primary Dataset to Use

Load **`data/colleges_final.csv`** directly into Power BI Desktop.

It contains all **100 Top NIRF 2025 Engineering Colleges** joined with audited 4-year academic fees and placement outcomes:
* `institute_id`: Official NIRF institute identifier (e.g., `IR-E-U-0456`).
* `college_name`: Full institutional name.
* `nirf_rank`: NIRF 2025 official rank (1 to 100).
* `nirf_score`: Total NIRF evaluation score.
* `city`, `state`: Geographic location.
* `graduated_count`, `placed_count`, `placement_percentage`: Official placement volume and percentage for the graduating cohort (Academic Year 2023–24).
* `median_salary_inr`, `median_salary_lpa`: Median placement package reported in NIRF DCS.
* `total_4yr_academic_fees_inr`, `total_4yr_academic_fees_lpa`: Audited mandatory 4-year academic dues for General-Category Indian students.
* `fee_salary_ratio`: Standardized value metric (Fees / Salary).
* `placement_extraction_status`: Status flag (`SUCCESS` for 97 eligible 4-year UG colleges; `PG_ONLY_NO_UG4` for 3 postgraduate-only institutes).

---

## 3. The 5-Page Power BI Report Blueprint

Detailed step-by-step layout and visual configuration are documented in [`POWERBI_BLUEPRINT.md`](POWERBI_BLUEPRINT.md).

```text
├── Page 1: Executive KPI & Strategic Value Overview
│   ├── 5 Top KPI Cards (Eligible Colleges, Avg Fees, Avg Salary, Avg Recovery, Avg Placement)
│   ├── Fees vs. Salary Bubble Scatter Plot (Sized by Placed Count, colored by Institution Type)
│   └── Top 5 Best Value vs. Top 5 Highest Capital Burden Tables
│
├── Page 2: The "Mid-Tier Trap" — NIRF Rank Band Dissection
│   ├── Clustered Column & Line Combo Chart (Average Fees & Salary on Left Axis; Recovery Years on Right Axis)
│   ├── 4 Rank Band Performance Cards (Bands 1 to 4)
│   └── Drill-Down Rank Band Matrix with Conditional Formatting
│
├── Page 3: Geographic & State-Level Return on Investment
│   ├── Filled / Shape Map of India colored by Fee-Salary Ratio gradient
│   ├── Horizontal Clustered Bar Chart of States sorted by Payback Time
│   └── State Decomposition Tree (State → Public/Private → College)
│
├── Page 4: Placement Reliability vs Capital Exposure
│   ├── 4-Quadrant Matrix (Placement % on X-Axis vs 4-Yr Fees on Y-Axis)
│   ├── Donut Chart of Colleges by Placement Reliability Tier
│   └── Danger Zone Alert Table (Colleges with <50% Placement & >₹10L Fees)
│
└── Page 5: Interactive College Explorer & Loan Simulator
    ├── Side-by-Side Multi-College Comparison Selector
    ├── What-If Parameter Sliders: Loan Financing % & Disposable Salary Savings %
    └── Complete Searchable College Explorer Matrix with Source URL Links
```

---

## 4. DAX Measures & Calculated Columns Library

Create a dedicated table named `_Measures` in Power BI:

### Core DAX Measures
```dax
Total_Colleges = COUNTROWS(colleges_final)

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

### Calculated Columns (Add to `colleges_final`)
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
Recovery_Category = 
SWITCH(
    TRUE(),
    ISBLANK(colleges_final[fee_salary_ratio]), "N/A (PG Only)",
    colleges_final[fee_salary_ratio] < 0.5, "1. Exceptional Value (< 6 Months)",
    colleges_final[fee_salary_ratio] <= 1.0, "2. High Value (6 - 12 Months)",
    colleges_final[fee_salary_ratio] <= 2.0, "3. Moderate Burden (1 - 2 Years)",
    "4. Severe Debt Risk (> 2 Years)"
)
```

---

## 5. Key Numerical Findings

1. **Public Subsidies Deliver up to 224× Faster Capital Recovery:**
   - **Jadavpur University** (NIRF #18) charges **₹14,110** total academic fees over four years against a median placement salary of **₹10.50 LPA**, recovering academic dues in **0.013 years** (~5 days of gross pay) with a **91.01%** placement rate.
   - **Jamia Millia Islamia** (NIRF #24) costs **₹0.66L** for a **₹13.78 LPA** median salary (**0.048 years** / 18 days; 84.6% placed).
   - In contrast, private universities like **SRM IST** (NIRF #14) charge **₹18.10L** in fees for a **₹6.20 LPA** median salary (**2.919 years** / 35 months), taking **224.5× longer** to recover fees than Jadavpur despite holding a higher NIRF rank.
2. **The "Mid-Tier Trap" (Ranks 26–75):**
   - **Band 1 (Ranks 1–25):** Mean Fee **₹8.63L** | Mean Salary **₹15.05 LPA** | Recovery **0.68 yrs** (8.2 mo) | Placed **79.72%**
   - **Band 2 (Ranks 26–50):** Mean Fee **₹9.22L** (+6.8%) | Mean Salary **₹10.76 LPA** (-28.5%) | Recovery **0.99 yrs** (11.9 mo) | Placed **71.39%**
   - **Band 3 (Ranks 51–75):** Mean Fee **₹9.10L** | Mean Salary **₹10.40 LPA** (-30.9%) | Recovery **0.97 yrs** (11.6 mo) | Placed **72.37%**
   - **Band 4 (Ranks 76–100):** Mean Fee **₹6.75L** | Mean Salary **₹8.17 LPA** | Recovery **0.98 yrs** (11.8 mo) | Placed **64.27%**
3. **Geographic Distribution:**
   - **Top Value States:** **West Bengal** (0.420 yrs avg ratio, ₹12.50 LPA salary) and **Delhi** (0.602 yrs avg ratio across 6 colleges with the country's highest state average salary: **₹16.08 LPA**).
   - **Least Value States:** **Uttarakhand** (1.889 yrs avg ratio) and **Karnataka** (1.339 yrs avg ratio, driven by high private tuition fees).

---

## 6. Project Artifacts & Presentations

* **PowerPoint Presentation:** [`NIRF_PowerBI_Presentation.pptx`](NIRF_PowerBI_Presentation.pptx) (10 widescreen slides ready for demo day presentation).
* **Slide Notes & Outline:** [`PRESENTATION_OUTLINE.md`](PRESENTATION_OUTLINE.md).
* **2-Minute Video Pitch Script:** [`VIDEO_SCRIPT_POWERBI.md`](VIDEO_SCRIPT_POWERBI.md) (Second-by-second timed script: 0:00–0:15 hook, 0:15–1:15 dashboard walkthrough, 1:15–1:45 data engineering, 1:45–2:00 family recommendation).
* **Source Citations Log:** [`fee_sources.md`](fee_sources.md) (Audited references for all 100 institutions).

---

## 7. How to Push this Repository to GitHub

To publish this project to GitHub under a new repository (e.g. `NIRF_PowerBI_Analytics`):

```bash
cd "c:\Users\pkatt\OneDrive\Desktop\Projects\NIRF_PowerBI_Analytics"

# Initialize git
git init
git add .
git commit -m "feat: complete NIRF 2025 Power BI analytics project with 5-page blueprint, DAX library, and presentation deck"

# Using GitHub CLI:
gh repo create NIRF_PowerBI_Analytics --public --source=. --remote=origin --push

# Or using standard Git with a pre-created repository:
git branch -M main
git remote add origin https://github.com/<your-username>/NIRF_PowerBI_Analytics.git
git push -u origin main
```

---

## License

This project is licensed under the MIT License. Academic data sources belong to the Ministry of Education (NIRF) and respective universities.
