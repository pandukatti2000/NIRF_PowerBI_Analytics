# Complete 5-Page Power BI Analytics & Visualization Blueprint
## NIRF 2025 Engineering College Value-for-Money (VFM) Project
**Project ID:** AccioJob DA-16 (*"Is that college worth the fees?"*)  
**Active Report File:** `NIRF_Engineering_VFM_Analytics.pbix` (1920×1080 Widescreen)  
**Primary Dataset:** `data/colleges_final.csv` (100 Institutions, 97 Eligible 4-Yr UG Programs)

---

## 1. Data Model & Architecture

The report model is built on top of `data/colleges_final.csv` with a dedicated `_Measures` table.

### Calculated Columns in `colleges_final`
1. **`Rank_Band`**:
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
2. **`Institution_Type`**:
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

### Core DAX Measures in `_Measures`
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

## 2. Five-Page Report Layout & Visual Mapping

Every page is optimized for Full HD (1920×1080) with a clean, executive aesthetic.

---

### Page 1: `Executive Overview` (3 Visuals)
* **Goal:** High-level strategic briefing on national averages, value leaders, and debt burdens.
1. **Multi-Row Card Visual (Top Banner):**
   - **Fields:** `Eligible_Colleges` (97), `Avg_4Yr_Fees_Lakhs` (₹8.43L), `Avg_Median_Salary_LPA` (₹11.14 LPA), `Avg_Fee_Salary_Ratio` (0.90 yrs).
   - **Position:** (323, 0), Width: 904px, Height: 418px.
2. **Scatter / Bubble Chart (Center Left · Hero Visual):**
   - **X Axis:** `total_4yr_academic_fees_lpa` (Fees in Lakhs)
   - **Y Axis:** `median_salary_lpa` (Salary in LPA)
   - **Category:** `college_name`
   - **Size:** `placed_count` (Volume of placed students)
   - **Series / Legend:** `Institution_Type`
   - **Play Axis:** `state` (Enables interactive animated state-by-state playback!)
   - **Tooltips:** `nirf_rank`, `fee_salary_ratio`, `placement_percentage`.
3. **Clustered Bar Chart (Center Right):**
   - **Category:** `college_name`
   - **Y Axis (Value):** `fee_salary_ratio`
   - Highlights the 224× recovery gap between Jadavpur (0.013 yrs) and SRM IST (2.919 yrs).

---

### Page 2: `The Mid-Tier Trap` (4 Visuals)
* **Goal:** Exposes fee inflation in NIRF Ranks 26–75 paired with a 28.5% drop in placement salary.
1. **Multi-Row Card Visual (Top Banner):**
   - **Fields:** `Avg_4Yr_Fees_Lakhs`, `Avg_Median_Salary_LPA`, `Avg_Fee_Salary_Ratio`, `Avg_Placement_Rate`.
2. **City Slicer (Top Left):**
   - **Field:** `city` (Allows localized filtering by tech hub).
3. **Dual-Axis Combo Line & Clustered Column Chart (Bottom Left):**
   - **X Axis:** `Rank_Band`
   - **Column Y-Axis 1:** `Avg_4Yr_Fees_Lakhs` and `Avg_Median_Salary_LPA`
   - **Line Y-Axis 2:** `Avg_Fee_Salary_Ratio`
   - *Key Insight:* Visually proves that Band 2 fees rise to ₹9.22L while median salaries drop by 28.5% compared to Band 1.
4. **Rank Band Matrix / Pivot Table (Bottom Right):**
   - **Rows:** `Rank_Band`
   - **Values:** `Avg_4Yr_Fees_Lakhs`, `Avg_Median_Salary_LPA`, `Avg_Fee_Salary_Ratio`.

---

### Page 3: `Geographic ROI` (3 Visuals)
* **Goal:** State-by-state return on engineering education across India.
1. **India Shape Map (Top Center):**
   - **Location:** `state`
   - **Color Saturation:** `Avg_Fee_Salary_Ratio`
   - **Embedded Map File:** Custom India TopoJSON (`india_states_powerbi.topojson`).
   - *Insight:* West Bengal & Delhi highlight in green (fast recovery); Uttarakhand & Karnataka highlight in red.
2. **State Recovery Clustered Bar Chart (Bottom Left):**
   - **Category:** `state`
   - **Value:** `Avg_Fee_Salary_Ratio` (Sorted ascending by recovery time).
3. **Decomposition Tree (Bottom Right):**
   - **Analyze:** `Avg_Fee_Salary_Ratio`
   - **Explain By:** `state` $\rightarrow$ `Institution_Type` $\rightarrow$ `college_name`
   - *Interactive Drill-Down:* Evaluators can click any state to isolate public vs private performance.

---

### Page 4: `Capital Risk & Placement` (3 Visuals)
* **Goal:** Pinpoints colleges charging high fees despite sub-50% placement rates.
1. **Four-Quadrant Scatter Chart (Top Center):**
   - **X Axis:** `placement_percentage` (0% to 100%)
   - **Y Axis:** `total_4yr_academic_fees_lpa` (0 to 22 Lakhs)
   - **Category:** `college_name` | **Series:** `Institution_Type`
   - **Tooltips:** `nirf_rank`, `median_salary_lpa`.
   - *Danger Zone:* Top-left quadrant highlights colleges with low placement and high capital outlay.
2. **Institution Type Donut Chart (Bottom Left):**
   - **Category:** `Institution_Type` | **Values:** `Eligible_Colleges`.
3. **Watchlist Table (Bottom Right):**
   - **Columns:** `college_name`, `nirf_rank`, `fees`, `placement %`, `salary`.
   - Identifies high-risk institutions like KIIT (34.9% placed) and Graphic Era (49.3% placed).

---

### Page 5: `College Explorer` (2 Visuals)
* **Goal:** Full-width interactive decision engine for students and families.
1. **Multi-Hierarchy Slicer (Top Center):**
   - **Fields:** `Rank_Band`, `state`.
2. **Master Explorer Table (Full 1920px Width):**
   - **Columns:** `nirf_rank`, `college_name`, `city`, `state`, `fees`, `salary`, `fee_salary_ratio`, `placement_percentage`.
   - Full widescreen width provides seamless readability across all 8 columns without horizontal clipping.
