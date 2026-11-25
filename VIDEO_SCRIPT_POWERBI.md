# 2-Minute Video Presentation Script: Power BI Value-for-Money Analytics

**Project:** NIRF 2025 Engineering Value-for-Money Analytics  
**Target Duration:** Exactly 120 seconds (2 minutes · ~300 words spoken at 150 wpm)  
**Deliverable:** Spoken video pitch with second-by-second timestamps and Power BI screen cues.

---

## Timed Script & Visual Walkthrough

### [0:00 – 0:15] The Hook & Stakeholder Framing
* **Screen Cue:** Open on Slide 1 / Power BI Page 1 Title Banner (*"Is That College Worth the Fees?"*).
* **Spoken Pitch (15 seconds · 38 words):**  
  > *"Every admission season, over a million Indian families borrow heavily to fund their child’s engineering degree, believing that a higher NIRF rank guarantees financial security. Today, we answer one urgent question: **Which college actually gives you the best return for the fees you pay?**"*

---

### [0:15 – 1:15] The Power BI Report Walkthrough (Real Numbers & Revelations)
* **Screen Cue [0:15–0:35]:** Switch to **Page 1 (Executive KPI & Scatter Bubble Chart)**. Point to the KPI cards and hover over Jadavpur vs. SRM bubbles.
* **Spoken Pitch (20 seconds · 55 words):**  
  > *"We modeled all top 100 NIRF colleges in Power BI using our core metric: **Fee-to-Salary Ratio**—the years of gross median salary needed to recover 4 years of academic fees.*  
  >  
  > *Public universities dominate the top value rankings. **Jadavpur University** costs just **₹14,110** for 4 years against a **₹10.5 LPA** median salary. You recover your fees in **0.013 years**—less than one week of work!*  
  >  
  > *Hover over **SRM IST** at rank 14: fees jump to **₹18.1 Lakhs** for a **₹6.2 LPA** salary—taking **2.92 years** to recover. That is **224 times longer** than Jadavpur!"*

* **Screen Cue [0:35–0:55]:** Switch to **Page 2 (The Mid-Tier Trap Combo Chart)**.
* **Spoken Pitch (20 seconds · 48 words):**  
  > *"Now look at Page 2: the **'Mid-Tier Trap'**.  
  > When moving from Rank Band 1 to Band 2 and 3, average fees actually **rise** from ₹8.6 Lakhs to over **₹9.2 Lakhs**, while median salaries **plummet by 29%**. Private colleges in ranks 26 to 75 charge premium tuition without delivering premium placement."*

* **Screen Cue [0:55–1:15]:** Switch to **Page 4 (Placement Risk vs Capital Matrix)**.
* **Spoken Pitch (20 seconds · 46 words):**  
  > *"On Page 4, we expose the danger zone. NIRF median salaries only count placed students. At colleges like **KIIT**, fees exceed **₹16 Lakhs**, but the placement rate drops to **34.9%**—meaning over 65% of the graduating class received **₹0** in campus offers."*

---

### [1:15 – 1:45] DAX Architecture & The Hardest Data Problem
* **Screen Cue:** Show the Power BI Data Model, DAX Measures table (`_Measures`), and the CSV dataset.
* **Spoken Pitch (30 seconds · 72 words):**  
  > *"How did we build this? NIRF’s institutional data files report student intake and operating expenditures, but completely omit student tuition fees.*  
  >  
  > *To solve this, we engineered a Python pipeline that concurrently parsed all 100 official NIRF PDFs, then audited 100 independent institutional fee circulars and JoSAA notifications. We modeled dynamic DAX measures for recovery months, placement reliability tiers, and simulated loan payoff timelines."*

---

### [1:45 – 2:00] Actionable Family Recommendation & Close
* **Screen Cue:** Switch to **Page 5 (Interactive Loan Simulator)** or Slide 9 (3 Golden Rules).
* **Spoken Pitch (15 seconds · 41 words):**  
  > *"Our recommendation to families: Unconditionally accept premier public institutions and subsidized NITs. Reject mid-tier private universities costing over ₹15 Lakhs unless admitted to Computer Science.  
  >  
  > Explore our Power BI dashboard and make data-driven decisions!"*

---

## Pacing Checklist for Recording

| Timestamp | Target Words | Content / Focus | Visual on Screen |
| :---: | :---: | :--- | :--- |
| **0:00 – 0:15** | 38 | The Family Dilemma & Decision Question | Title Slide / Page 1 Header |
| **0:15 – 0:35** | 55 | Page 1: KPIs, Scatter Bubble Chart (Jadavpur vs SRM) | Bubble Scatter Plot |
| **0:35 – 0:55** | 48 | Page 2: The Mid-Tier Trap (Fee Spike vs Salary Drop) | Combo Column & Line Chart |
| **0:55 – 1:15** | 46 | Page 4: Capital Exposure vs Placement Reliability | 4-Quadrant Risk Matrix |
| **1:15 – 1:45** | 72 | Data Pipeline, NIRF Fee Omission & DAX Modeling | Data Model & DAX Formulas |
| **1:45 – 2:00** | 41 | Strategic Family Recommendation & Call to Action | Simulator / 3 Golden Rules |
| **Total** | **300** | **Strict 120-Second Cap (2 Minutes)** | **5-Page Power BI Walkthrough** |
