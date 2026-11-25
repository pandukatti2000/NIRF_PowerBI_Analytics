# Complete 5-Page Power BI Analytics & Visualization Blueprint
## NIRF 2025 Engineering College Value-for-Money (VFM) Project
**Project ID:** AccioJob DA-16 (*"Is that college worth the fees?"*)  
**Primary Dataset to Load:** `data/colleges_final.csv` (100 Institutions, 97 Eligible 4-Yr UG Programs)

---

## 1. Data Model & Preparation in Power BI

### Step 1: Ingest Data
1. Open **Power BI Desktop**.
2. Click **Get Data** $\rightarrow$ **Text/CSV** $\rightarrow$ select `data/colleges_final.csv`.
3. In the Power Query Transform window:
   - Ensure the first row is used as headers.
   - Filter `placement_extraction_status` = `"SUCCESS"` for VFM calculations (or leave all and filter using DAX measures to keep all 100 rows).
   - Verify column data types:
     - `nirf_rank`: Whole Number
     - `intake_count`, `graduated_count`, `placed_count`, `higher_studies_count`: Whole Number
     - `total_4yr_academic_fees_inr`, `median_salary_inr`: Decimal / Currency
     - `total_4yr_academic_fees_lpa`, `median_salary_lpa`, `fee_salary_ratio`, `placement_percentage`: Decimal Number
     - `state`, `city`, `college_name`, `fee_category_quota`: Text
4. Click **Close & Apply**.

---

## 2. Complete DAX Formulas Library

Create a dedicated Measures Table (Home $\rightarrow$ Enter Data $\rightarrow$ Table Name: `_Measures`).

### A. Core Aggregation Measures

```dax
Total_Colleges = COUNTROWS(colleges_final)
```

```dax
Eligible_Colleges = 
CALCULATE(
    COUNTROWS(colleges_final),
    colleges_final[placement_extraction_status] = "SUCCESS"
)
```

```dax
Avg_4Yr_Fees_Lakhs = 
CALCULATE(
    AVERAGE(colleges_final[total_4yr_academic_fees_lpa]),
    colleges_final[placement_extraction_status] = "SUCCESS"
)
```

```dax
Avg_Median_Salary_LPA = 
CALCULATE(
    AVERAGE(colleges_final[median_salary_lpa]),
    colleges_final[placement_extraction_status] = "SUCCESS"
)
```

```dax
Avg_Fee_Salary_Ratio = 
CALCULATE(
    AVERAGE(colleges_final[fee_salary_ratio]),
    colleges_final[placement_extraction_status] = "SUCCESS"
)
```

```dax
Avg_Recovery_Months = [Avg_Fee_Salary_Ratio] * 12
```

```dax
Avg_Placement_Rate = 
CALCULATE(
    AVERAGE(colleges_final[placement_percentage]),
    colleges_final[placement_extraction_status] = "SUCCESS"
)
```

```dax
Total_Graduated_Students = 
CALCULATE(
    SUM(colleges_final[graduated_count]),
    colleges_final[placement_extraction_status] = "SUCCESS"
)
```

```dax
Total_Placed_Students = 
CALCULATE(
    SUM(colleges_final[placed_count]),
    colleges_final[placement_extraction_status] = "SUCCESS"
)
```

```dax
Cohort_Placement_Percentage = 
DIVIDE([Total_Placed_Students], [Total_Graduated_Students], 0) * 100
```

```dax
Realistic_Payback_Years = 
DIVIDE([Avg_Fee_Salary_Ratio], 0.35, 0)
// Assumes a graduate saves 35% of gross salary after taxes and living costs
```

---

### B. Calculated Columns (Add to `colleges_final` table)

#### 1. Rank Band Grouping
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

#### 2. Institution Type Classification
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
    "Private / Deemed / Autonomous"
)
```

#### 3. Capital Recovery Speed Category
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

#### 4. Placement Reliability Tier
```dax
Placement_Tier = 
SWITCH(
    TRUE(),
    ISBLANK(colleges_final[placement_percentage]), "N/A",
    colleges_final[placement_percentage] >= 85, "Tier 1: High Reliability (> 85%)",
    colleges_final[placement_percentage] >= 70, "Tier 2: Solid (70 - 85%)",
    colleges_final[placement_percentage] >= 50, "Tier 3: Moderate (50 - 70%)",
    "Tier 4: High Risk (< 50%)"
)
```

---

## 3. The 5-Page Power BI Visualizations Layout

---

### Page 1: Executive KPI & Strategic Value Overview

* **Page Purpose:** Gives students and parents an immediate high-level summary of the entire landscape: average fees, salaries, and who delivers extreme value vs who imposes extreme debt.
* **Header / Filter Bar:**
  - Title: **"NIRF 2025 Engineering Value-for-Money Landscape"**
  - Subtitle: *"Evaluating 4-Year Academic Fees Against Median Placement Salaries"*
  - Top Slicers: `Institution_Type` (Dropdown), `State` (Dropdown), `Rank_Band` (Horizontal Tiles).
* **Row 1: Five Core KPI Cards**
  1. Card 1: `Eligible_Colleges` $\rightarrow$ **97 Colleges** (Subtext: *3 PG-Only Excluded*)
  2. Card 2: `Avg_4Yr_Fees_Lakhs` $\rightarrow$ **₹8.43 Lakhs** (Avg 4-Year Fees)
  3. Card 3: `Avg_Median_Salary_LPA` $\rightarrow$ **₹11.14 LPA** (Avg Annual Placement Salary)
  4. Card 4: `Avg_Fee_Salary_Ratio` $\rightarrow$ **0.904 Years** (~10.8 Months)
  5. Card 5: `Avg_Placement_Rate` $\rightarrow$ **72.01%** (Average Placed)
* **Row 2: Primary Visual — Fees vs Salary Bubble Chart (Center Stage)**
  - **Visual Type:** Scatter Chart / Bubble Plot
  - **X-Axis:** `total_4yr_academic_fees_lpa` (Range: 0 to 22 Lakhs)
  - **Y-Axis:** `median_salary_lpa` (Range: 0 to 26 LPA)
  - **Size:** `placed_count` (Larger bubbles = more students placed)
  - **Legend:** `Institution_Type` (IIT: Dark Blue, NIT: Teal, Govt: Green, Private: Red)
  - **Tooltips:** `college_name`, `nirf_rank`, `fee_salary_ratio`, `placement_percentage`, `state`
  - **Reference Lines:** Add constant lines for X = 8.43L (Avg Fee) and Y = 11.14L (Avg Salary).
* **Row 3: Top 5 Best vs Top 5 Least Value Tables**
  - **Left Table:** *Top 5 Best Value (Lowest Recovery)*
    - Columns: `nirf_rank`, `college_name`, `total_4yr_academic_fees_lpa`, `median_salary_lpa`, `fee_salary_ratio`
    - Top rows: Jadavpur (0.013 yrs), Jamia (0.048 yrs), Anna Univ (0.166 yrs), AMU (0.186 yrs), MMMUT (0.275 yrs).
  - **Right Table:** *Top 5 Highest Debt Burdens (Longest Recovery)*
    - Top rows: SRM IST (2.919 yrs), Vignan's (2.887 yrs), UPES (2.585 yrs), Graphic Era (2.560 yrs), Vel Tech (2.500 yrs).

---

### Page 2: The "Mid-Tier Trap" — NIRF Rank Band Dissection

* **Page Purpose:** Answers whether families should pay higher fees for mid-tier institutions (Ranks 26–75) compared to top 25 or lower 75–100 colleges.
* **Row 1: Rank Band Summary KPI Cards (Horizontal comparison)**
  - Band 1 (1–25): Fee ₹8.63L | Salary ₹15.05 LPA | Ratio **0.68 yrs** | 79.7% Placed
  - Band 2 (26–50): Fee ₹9.22L | Salary ₹10.76 LPA | Ratio **0.99 yrs** | 71.4% Placed
  - Band 3 (51–75): Fee ₹9.10L | Salary ₹10.40 LPA | Ratio **0.97 yrs** | 72.4% Placed
  - Band 4 (76–100): Fee ₹6.75L | Salary ₹8.17 LPA | Ratio **0.98 yrs** | 64.3% Placed
* **Row 2: The Core Revelation Chart (Combo Chart)**
  - **Visual Type:** Line and Clustered Column Chart
  - **X-Axis:** `Rank_Band`
  - **Column Values (Left Y-Axis):** `Avg_4Yr_Fees_Lakhs` & `Avg_Median_Salary_LPA`
  - **Line Value (Right Y-Axis):** `Avg_Fee_Salary_Ratio`
  - *Key Visual Insight:* Columns vividly show salaries dropping by 29% from Band 1 to Band 2 while fees actually rise from ₹8.63L to ₹9.22L!
* **Row 3: Interactive Drill-Down Matrix**
  - **Visual Type:** Matrix Table
  - **Rows:** `Rank_Band` $\rightarrow$ `college_name`
  - **Values:** `nirf_rank`, `total_4yr_academic_fees_lpa`, `median_salary_lpa`, `fee_salary_ratio`, `placement_percentage`
  - **Conditional Formatting:** Green-Yellow-Red color gradient on `fee_salary_ratio`.

---

### Page 3: Geographic & State-Level Return on Investment

* **Page Purpose:** Pinpoints which Indian states offer the highest return on engineering education and which states suffer from inflated private fees.
* **Row 1: State ROI Map Visual**
  - **Visual Type:** Shape Map or Azure Map (India States)
  - **Location:** `state`
  - **Color Saturation:** `Avg_Fee_Salary_Ratio` (Inverted: Lower ratio = Vibrant Green, Higher ratio = Red)
  - **Tooltips:** State Name, Number of Ranked Colleges, Average Fees, Average Median Salary.
* **Row 2: State Ranking Bar Chart**
  - **Visual Type:** Clustered Horizontal Bar Chart
  - **Y-Axis:** `state` (Sorted ascending by `Avg_Fee_Salary_Ratio`)
  - **X-Axis:** `Avg_Fee_Salary_Ratio`
  - *Key Highlight:* West Bengal (0.420 yrs), MP (0.437 yrs), Assam (0.493 yrs), Delhi (0.602 yrs) at top; Uttarakhand (1.889 yrs) and Karnataka (1.339 yrs) at bottom.
* **Row 3: State Deep-Dive Decomposition Tree**
  - **Visual Type:** Decomposition Tree
  - **Analyze:** `Avg_Fee_Salary_Ratio`
  - **Explain by:** `state` $\rightarrow$ `Institution_Type` $\rightarrow$ `college_name`
  - *Interactive Feature:* Allows users to click on any state (e.g., Tamil Nadu) to see the split between Anna University (0.16 yrs) vs SRM (2.92 yrs) and Vel Tech (2.50 yrs).

---

### Page 4: Placement Reliability vs Capital Exposure

* **Page Purpose:** Exposes the "double penalty"—colleges that charge exorbitant fees while failing to place over 35%–55% of their graduating class.
* **Row 1: Placement vs Capital Exposure 4-Quadrant Matrix**
  - **Visual Type:** Scatter Chart
  - **X-Axis:** `placement_percentage` (0% to 100%) - Add constant reference line at 70%.
  - **Y-Axis:** `total_4yr_academic_fees_lpa` (0 to 22 Lakhs) - Add constant reference line at 10 Lakhs.
  - **Bubbles:** `college_name`, colored by `Placement_Tier`.
  - **Four Critical Quadrants:**
    1. **Bottom-Right (The Green Safe Haven):** Low Fees (<₹10L), High Placement (>70%) $\rightarrow$ Jadavpur, Jamia, DTU, NITs, IITs.
    2. **Top-Right (The High-Stakes Premium):** High Fees (>₹10L), High Placement (>70%) $\rightarrow$ BITS, Thapar, IIIT Hyderabad.
    3. **Bottom-Left (Moderate Risk / Budget):** Low Fees (<₹10L), Low Placement (<70%) $\rightarrow$ Regional government colleges.
    4. **Top-Left (The Danger Zone):** High Fees (>₹10L), Low Placement (<70%) $\rightarrow$ KIIT (34.9% placed, ₹16.35L fees), Graphic Era (49.3% placed, ₹12.80L fees), Vel Tech (49.2% placed, ₹10.0L fees).
* **Row 2: Risk Breakdown Visuals**
  - **Visual 1 (Donut Chart):** Distribution of colleges by `Placement_Tier`.
  - **Visual 2 (Table):** Colleges with Placement < 60% sorted by highest fees.

---

### Page 5: Interactive College Explorer & Loan Repayment Simulator

* **Page Purpose:** A practical, interactive tool where a prospective student selects 2–3 colleges they have offers from and simulates actual loan repayment timelines.
* **Left Column: Dynamic Slicers & Comparison Filters**
  - Slicer 1: `State`
  - Slicer 2: `Rank_Band`
  - Slicer 3: Multi-select dropdown for `college_name` (compare up to 3 colleges side by side).
* **Center: What-If Loan Payoff Simulator (Using Power BI What-If Parameters)**
  - Parameter 1: `Financed_by_Loan_Pct` (Slider: 0% to 100%, Default: 80%)
  - Parameter 2: `Annual_Disposable_Savings_Pct` (Slider: 15% to 50%, Default: 30%)
  - **Dynamic Simulated Payback Formula:**
    ```dax
    Simulated_Debt_Payoff_Years = 
    DIVIDE(
        [Avg_4Yr_Fees_Lakhs] * (SELECTEDVALUE('Loan_Pct_Parameter'[Value], 0.8)),
        [Avg_Median_Salary_LPA] * (SELECTEDVALUE('Savings_Pct_Parameter'[Value], 0.30)),
        0
    )
    ```
* **Right / Bottom: Master Explorer Table**
  - Search box enabled.
  - Columns: `nirf_rank`, `college_name`, `city`, `state`, `total_4yr_academic_fees_lpa`, `median_salary_lpa`, `fee_salary_ratio`, `placement_percentage`, `fee_category_quota`.
  - Web URL icon linking directly to `nirf_source_url` and `fee_source_url`.
