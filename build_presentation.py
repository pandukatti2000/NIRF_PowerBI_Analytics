import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def create_deck():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    # Color Palette
    NAVY = RGBColor(15, 23, 42)       # Slate 900
    BLUE = RGBColor(30, 58, 138)      # Blue 900
    ACCENT_BLUE = RGBColor(37, 99, 235) # Blue 600
    TEAL = RGBColor(13, 148, 136)     # Teal 600
    RED = RGBColor(220, 38, 38)       # Red 600
    GREEN = RGBColor(22, 163, 74)     # Green 600
    WHITE = RGBColor(255, 255, 255)
    LIGHT_BG = RGBColor(248, 250, 252) # Slate 50
    TEXT_DARK = RGBColor(30, 41, 59)   # Slate 800
    TEXT_MUTED = RGBColor(100, 116, 139) # Slate 500
    CARD_BG = RGBColor(241, 245, 249)  # Slate 100

    def add_header(slide, title_text, category_text="ACCIOJOB DA-16 · VALUE-FOR-MONEY ANALYTICS"):
        # Header category
        cat_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(0.4))
        tf_cat = cat_box.text_frame
        tf_cat.word_wrap = True
        p_cat = tf_cat.paragraphs[0]
        p_cat.text = category_text.upper()
        p_cat.font.size = Pt(11)
        p_cat.font.bold = True
        p_cat.font.color.rgb = ACCENT_BLUE

        # Main Title
        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.7), Inches(11.7), Inches(0.8))
        tf_title = title_box.text_frame
        tf_title.word_wrap = True
        p_title = tf_title.paragraphs[0]
        p_title.text = title_text
        p_title.font.size = Pt(24)
        p_title.font.bold = True
        p_title.font.color.rgb = NAVY

    # ==========================================
    # SLIDE 1: Title Slide
    # ==========================================
    blank_layout = prs.slide_layouts[6]
    slide1 = prs.slides.add_slide(blank_layout)

    # Background shape
    bg = slide1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg.fill.solid()
    bg.fill.fore_color.rgb = NAVY
    bg.line.color.rgb = NAVY

    # Title box
    tbox = slide1.shapes.add_textbox(Inches(1.2), Inches(1.8), Inches(11.0), Inches(2.2))
    tf1 = tbox.text_frame
    tf1.word_wrap = True
    p1 = tf1.paragraphs[0]
    p1.text = "Is That College Worth the Fees?"
    p1.font.size = Pt(44)
    p1.font.bold = True
    p1.font.color.rgb = WHITE

    p1_sub = tf1.add_paragraph()
    p1_sub.text = "A Power BI Value-for-Money Analytics Framework for NIRF 2025 Engineering Colleges"
    p1_sub.font.size = Pt(20)
    p1_sub.font.color.rgb = RGBColor(147, 197, 253) # Light Blue
    p1_sub.space_before = Pt(14)

    # Metadata card
    meta_box = slide1.shapes.add_textbox(Inches(1.2), Inches(4.5), Inches(11.0), Inches(1.8))
    tf_meta = meta_box.text_frame
    p_meta1 = tf_meta.paragraphs[0]
    p_meta1.text = "Stakeholder: Middle-Class Indian Families & Prospective Engineering Students"
    p_meta1.font.size = Pt(14)
    p_meta1.font.color.rgb = RGBColor(226, 232, 240)

    p_meta2 = tf_meta.add_paragraph()
    p_meta2.text = "Core Decision: Balancing 4-Year Tuition Exposure Against Verified Placement Return"
    p_meta2.font.size = Pt(14)
    p_meta2.font.color.rgb = RGBColor(226, 232, 240)

    p_meta3 = tf_meta.add_paragraph()
    p_meta3.text = "Deliverable: 5-Page Interactive Power BI Report · DAX Engine · Master Merged Dataset"
    p_meta3.font.size = Pt(14)
    p_meta3.font.bold = True
    p_meta3.font.color.rgb = RGBColor(56, 189, 248)
    p_meta3.space_before = Pt(8)

    # ==========================================
    # SLIDE 2: The High-Stakes Decision Problem
    # ==========================================
    slide2 = prs.slides.add_slide(blank_layout)
    add_header(slide2, "The Problem: Brand Prestige vs. Crushing Tuition Debt")

    # 3 Cards Layout
    cards_data = [
        ("The Family Dilemma", "Every year, over 1.2 million families evaluate engineering admissions, routinely assuming a higher NIRF ranking guarantees higher salary and safer financial security.", NAVY),
        ("The Hidden Market Variance", "Tuition fees vary by over 130× within the Top 100 NIRF colleges (₹14,110 to ₹19.5 Lakhs), while median placement packages range from ₹3.36 LPA to ₹22.50 LPA.", ACCENT_BLUE),
        ("The Analytics Solution", "We built an objective Value-for-Money index that calculates the exact years of gross salary needed to pay back total 4-year academic dues, cutting through marketing spin.", TEAL)
    ]
    for i, (title, desc, color) in enumerate(cards_data):
        left = Inches(0.8 + i * 3.95)
        top = Inches(1.8)
        width = Inches(3.75)
        height = Inches(4.8)

        card = slide2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = CARD_BG
        card.line.color.rgb = RGBColor(203, 213, 225)

        t_box = slide2.shapes.add_textbox(left + Inches(0.2), top + Inches(0.3), width - Inches(0.4), height - Inches(0.6))
        tf = t_box.text_frame
        tf.word_wrap = True
        p_t = tf.paragraphs[0]
        p_t.text = title
        p_t.font.size = Pt(18)
        p_t.font.bold = True
        p_t.font.color.rgb = color

        p_d = tf.add_paragraph()
        p_d.text = desc
        p_d.font.size = Pt(14)
        p_d.font.color.rgb = TEXT_DARK
        p_d.space_before = Pt(14)

    # ==========================================
    # SLIDE 3: Methodology & Value Metric
    # ==========================================
    slide3 = prs.slides.add_slide(blank_layout)
    add_header(slide3, "Core Metric & The Hardest Data Engineering Problem")

    # Metric Banner
    metric_banner = slide3.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.8), Inches(11.7), Inches(1.4))
    metric_banner.fill.solid()
    metric_banner.fill.fore_color.rgb = BLUE
    metric_banner.line.color.rgb = BLUE

    mb_text = slide3.shapes.add_textbox(Inches(1.0), Inches(1.9), Inches(11.3), Inches(1.2))
    tf_mb = mb_text.text_frame
    p_mb = tf_mb.paragraphs[0]
    p_mb.text = "Fee-to-Salary Ratio = Total 4-Year Mandatory Academic Fees / Annual Median Salary"
    p_mb.font.size = Pt(18)
    p_mb.font.bold = True
    p_mb.font.color.rgb = WHITE
    p_mb.alignment = PP_ALIGN.CENTER

    p_mb_sub = tf_mb.add_paragraph()
    p_mb_sub.text = "Interpretation: Equivalent years of gross year-one salary required to recover academic dues. Lower = Superior Value."
    p_mb_sub.font.size = Pt(13)
    p_mb_sub.font.color.rgb = RGBColor(191, 219, 254)
    p_mb_sub.alignment = PP_ALIGN.CENTER

    # Two columns
    col1 = slide3.shapes.add_textbox(Inches(0.8), Inches(3.6), Inches(5.6), Inches(3.2))
    tf_c1 = col1.text_frame
    tf_c1.word_wrap = True
    p_c1_h = tf_c1.paragraphs[0]
    p_c1_h.text = "The NIRF Data Blindspot"
    p_c1_h.font.size = Pt(16)
    p_c1_h.font.bold = True
    p_c1_h.font.color.rgb = RED

    bullets_c1 = [
        "NIRF DCS reports student intake, graduated cohorts, and placement numbers, but completely omits student tuition fees.",
        "Expenditure figures in NIRF represent institutional operational budgets, NOT student tuition liability.",
        "Never guess or fabricate: Fee schedules had to be audited from independent official sources."
    ]
    for b in bullets_c1:
        p_b = tf_c1.add_paragraph()
        p_b.text = "• " + b
        p_b.font.size = Pt(13)
        p_b.font.color.rgb = TEXT_DARK
        p_b.space_before = Pt(6)

    col2 = slide3.shapes.add_textbox(Inches(6.8), Inches(3.6), Inches(5.7), Inches(3.2))
    tf_c2 = col2.text_frame
    tf_c2.word_wrap = True
    p_c2_h = tf_c2.paragraphs[0]
    p_c2_h.text = "Audited Dual-Pipeline Solution"
    p_c2_h.font.size = Pt(16)
    p_c2_h.font.bold = True
    p_c2_h.font.color.rgb = GREEN

    bullets_c2 = [
        "Automated Python downloader collected all 100 official DCS PDFs concurrently in 29.6 seconds.",
        "Audited 100 official fee circulars: JoSAA notifications for 22 IITs & 23 NITs, State counselling bulletins, and private fee orders.",
        "Standardized to 4-year academic dues for General-Category Indian students; flagged 3 PG-only institutions."
    ]
    for b in bullets_c2:
        p_b = tf_c2.add_paragraph()
        p_b.text = "• " + b
        p_b.font.size = Pt(13)
        p_b.font.color.rgb = TEXT_DARK
        p_b.space_before = Pt(6)

    # ==========================================
    # SLIDE 4: Power BI Report Architecture (5 Pages)
    # ==========================================
    slide4 = prs.slides.add_slide(blank_layout)
    add_header(slide4, "Power BI Report Architecture: 5 Purpose-Built Analytical Pages")

    pages = [
        ("Page 1: Executive KPI Overview", "Scatter & Bubble plot of Fees vs Salary, KPI cards, Top 5 Best & Least Value colleges.", ACCENT_BLUE),
        ("Page 2: The Mid-Tier Trap", "Combo chart comparing Rank Bands 1 to 4, demonstrating fee escalation alongside salary drops.", TEAL),
        ("Page 3: Geographic & State ROI", "India shape map, state bar rankings, and decomposition tree exposing regional tuition variations.", NAVY),
        ("Page 4: Placement Risk vs Capital", "4-Quadrant scatter plot identifying high-cost colleges with sub-50% placement success.", RED),
        ("Page 5: Interactive Decision Engine", "Multi-college side-by-side comparison, loan financing parameter simulator, and search matrix.", GREEN)
    ]
    for i, (title, desc, color) in enumerate(pages):
        top_pos = Inches(1.8 + i * 1.0)
        shape = slide4.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), top_pos, Inches(11.7), Inches(0.85))
        shape.fill.solid()
        shape.fill.fore_color.rgb = CARD_BG
        shape.line.color.rgb = color
        shape.line.width = Pt(2)

        tb = slide4.shapes.add_textbox(Inches(1.0), top_pos + Inches(0.08), Inches(11.3), Inches(0.7))
        tf = tb.text_frame
        p_t = tf.paragraphs[0]
        p_t.text = title
        p_t.font.size = Pt(14)
        p_t.font.bold = True
        p_t.font.color.rgb = color

        p_d = tf.add_paragraph()
        p_d.text = desc
        p_d.font.size = Pt(12)
        p_d.font.color.rgb = TEXT_DARK

    # ==========================================
    # SLIDE 5: Key Finding 1 — Public vs Private Disparity
    # ==========================================
    slide5 = prs.slides.add_slide(blank_layout)
    add_header(slide5, "Finding 1: Public Subsidies Deliver up to 224× Faster Capital Recovery")

    # Left: Jadavpur Case
    box_left = slide5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.8))
    box_left.fill.solid()
    box_left.fill.fore_color.rgb = RGBColor(240, 253, 244) # Emerald 50
    box_left.line.color.rgb = GREEN

    tb_l = slide5.shapes.add_textbox(Inches(1.0), Inches(2.0), Inches(5.2), Inches(4.4))
    tf_l = tb_l.text_frame
    tf_l.word_wrap = True
    p_lh = tf_l.paragraphs[0]
    p_lh.text = "THE VALUE CHAMPION: JADAVPUR UNIVERSITY"
    p_lh.font.size = Pt(16)
    p_lh.font.bold = True
    p_lh.font.color.rgb = GREEN

    points_l = [
        "NIRF Rank: #18 (Top 20 in India)",
        "4-Year Total Academic Fees: ₹14,110 (₹2,400/yr tuition)",
        "Annual Median Placement Salary: ₹10.50 LPA",
        "Fee-to-Salary Recovery Ratio: 0.013 Years (~5 Days)",
        "Cohort Placement Rate: 91.01% (718 of 789 placed)",
        "Other Public Champions: Jamia Millia (0.048 yrs / 18 days), Anna Univ (0.166 yrs / 2 months), AMU (0.186 yrs)."
    ]
    for pt in points_l:
        p = tf_l.add_paragraph()
        p.text = "✔ " + pt
        p.font.size = Pt(13)
        p.font.color.rgb = TEXT_DARK
        p.space_before = Pt(8)

    # Right: SRM Case
    box_right = slide5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.8), Inches(5.7), Inches(4.8))
    box_right.fill.solid()
    box_right.fill.fore_color.rgb = RGBColor(254, 242, 242) # Rose 50
    box_right.line.color.rgb = RED

    tb_r = slide5.shapes.add_textbox(Inches(7.0), Inches(2.0), Inches(5.3), Inches(4.4))
    tf_r = tb_r.text_frame
    tf_r.word_wrap = True
    p_rh = tf_r.paragraphs[0]
    p_rh.text = "THE EXTREME CAPITAL BURDEN: SRM IST"
    p_rh.font.size = Pt(16)
    p_rh.font.bold = True
    p_rh.font.color.rgb = RED

    points_r = [
        "NIRF Rank: #14 (Ranked higher than Jadavpur)",
        "4-Year Total Academic Fees: ₹18.10 Lakhs (₹4.5L/yr tuition)",
        "Annual Median Placement Salary: ₹6.20 LPA",
        "Fee-to-Salary Recovery Ratio: 2.919 Years (35 Months)",
        "Relative Payback Factor: 224.5× longer than Jadavpur!",
        "Other High-Debt Burden Peers: Vignan's (2.887 yrs), UPES (2.585 yrs), Graphic Era (2.560 yrs), Vel Tech (2.500 yrs)."
    ]
    for pt in points_r:
        p = tf_r.add_paragraph()
        p.text = "⚠ " + pt
        p.font.size = Pt(13)
        p.font.color.rgb = TEXT_DARK
        p.space_before = Pt(8)

    # ==========================================
    # SLIDE 6: Key Finding 2 — The Mid-Tier Trap
    # ==========================================
    slide6 = prs.slides.add_slide(blank_layout)
    add_header(slide6, "Finding 2: The 'Mid-Tier Trap' in NIRF Ranks 26–75")

    # Table of Rank Bands
    rows = 5
    cols = 6
    top_t = Inches(1.8)
    left_t = Inches(0.8)
    width_t = Inches(11.7)
    height_t = Inches(3.2)

    table_shape = slide6.shapes.add_table(rows, cols, left_t, top_t, width_t, height_t)
    table = table_shape.table

    headers = ["NIRF Rank Band", "Colleges", "Avg 4-Yr Fees", "Avg Median Salary", "Recovery Ratio", "Avg Placement"]
    for j, h in enumerate(headers):
        cell = table.cell(0, j)
        cell.text = h
        cell.fill.solid()
        cell.fill.fore_color.rgb = BLUE
        p = cell.text_frame.paragraphs[0]
        p.font.bold = True
        p.font.size = Pt(13)
        p.font.color.rgb = WHITE

    data_rows = [
        ("Band 1 (Ranks 1–25)", "25", "₹8.63 Lakhs", "₹15.05 LPA", "0.684 Years (8.2 mo)", "79.72%"),
        ("Band 2 (Ranks 26–50)", "25", "₹9.22 Lakhs (+6.8%)", "₹10.76 LPA (-28.5%)", "0.992 Years (11.9 mo)", "71.39%"),
        ("Band 3 (Ranks 51–75)", "23", "₹9.10 Lakhs", "₹10.40 LPA (-30.9%)", "0.968 Years (11.6 mo)", "72.37%"),
        ("Band 4 (Ranks 76–100)", "24", "₹6.75 Lakhs", "₹8.17 LPA", "0.982 Years (11.8 mo)", "64.27%")
    ]
    for i, row in enumerate(data_rows, 1):
        for j, val in enumerate(row):
            cell = table.cell(i, j)
            cell.text = val
            p = cell.text_frame.paragraphs[0]
            p.font.size = Pt(12)
            p.font.color.rgb = TEXT_DARK

    # Callout note below
    callout = slide6.shapes.add_textbox(Inches(0.8), Inches(5.3), Inches(11.7), Inches(1.5))
    tf_callout = callout.text_frame
    tf_callout.word_wrap = True
    p_co = tf_callout.paragraphs[0]
    p_co.text = "Strategic Takeaway for Families:"
    p_co.font.bold = True
    p_co.font.size = Pt(15)
    p_co.font.color.rgb = NAVY

    p_co_sub = tf_callout.add_paragraph()
    p_co_sub.text = "Institutions ranked 26–75 cost ₹50,000 to ₹60,000 MORE than top 25 colleges due to private tuition escalation (Thapar, KIIT, UPES, Manipal), yet yield ₹4.3L to ₹4.6L LOWER annual salaries. Never assume higher rank inside the top 100 implies lower fee burden!"
    p_co_sub.font.size = Pt(13)
    p_co_sub.font.color.rgb = TEXT_DARK
    p_co_sub.space_before = Pt(4)

    # ==========================================
    # SLIDE 7: Key Finding 3 — Geographic Hubs vs Risk Zones
    # ==========================================
    slide7 = prs.slides.add_slide(blank_layout)
    add_header(slide7, "Finding 3: Geographic Clustering Dictates Educational Return")

    # Left: Top States
    c_left = slide7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.8))
    c_left.fill.solid()
    c_left.fill.fore_color.rgb = CARD_BG
    c_left.line.color.rgb = GREEN

    tb_sl = slide7.shapes.add_textbox(Inches(1.0), Inches(2.0), Inches(5.2), Inches(4.4))
    tf_sl = tb_sl.text_frame
    tf_sl.word_wrap = True
    p_sl = tf_sl.paragraphs[0]
    p_sl.text = "HIGH RETURN STATES (FASTEST PAYBACK)"
    p_sl.font.bold = True
    p_sl.font.size = Pt(16)
    p_sl.font.color.rgb = GREEN

    points_sl = [
        "West Bengal (4 Colleges): Avg Fee ₹5.20L | Avg Salary ₹12.50 LPA | Recovery: 0.420 Years (~5 Months)",
        "Madhya Pradesh (3 Colleges): Avg Fee ₹7.26L | Avg Salary ₹17.49 LPA | Recovery: 0.437 Years",
        "Assam (2 Colleges): Avg Fee ₹7.34L | Avg Salary ₹15.24 LPA | Recovery: 0.493 Years",
        "Delhi (6 Colleges): Avg Fee ₹9.86L | Avg Salary ₹16.08 LPA (Highest in India!) | Recovery: 0.602 Years"
    ]
    for pt in points_sl:
        p = tf_sl.add_paragraph()
        p.text = "• " + pt
        p.font.size = Pt(13)
        p.font.color.rgb = TEXT_DARK
        p.space_before = Pt(8)

    # Right: Low Return States
    c_right = slide7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.8), Inches(5.7), Inches(4.8))
    c_right.fill.solid()
    c_right.fill.fore_color.rgb = CARD_BG
    c_right.line.color.rgb = RED

    tb_sr = slide7.shapes.add_textbox(Inches(7.0), Inches(2.0), Inches(5.3), Inches(4.4))
    tf_sr = tb_sr.text_frame
    tf_sr.word_wrap = True
    p_sr = tf_sr.paragraphs[0]
    p_sr.text = "CAPITAL EXPOSURE STATES (SLOW PAYBACK)"
    p_sr.font.bold = True
    p_sr.font.size = Pt(16)
    p_sr.font.color.rgb = RED

    points_sr = [
        "Uttarakhand (3 Colleges): Avg Fee ₹12.83L | Avg Salary ₹9.50 LPA | Recovery: 1.889 Years (~23 Months) - Dragged by UPES & Graphic Era.",
        "Karnataka (6 Colleges): Avg Fee ₹10.69L | Avg Salary ₹9.03 LPA | Recovery: 1.339 Years - High private fees at Manipal & RVCE.",
        "Andhra Pradesh (4 Colleges): Avg Fee ₹7.73L | Avg Salary ₹7.28 LPA | Recovery: 1.305 Years",
        "Tamil Nadu Bifurcation (14 Colleges): Anna Univ (0.16 yrs) vs SRM (2.92 yrs) & Vel Tech (2.50 yrs)."
    ]
    for pt in points_sr:
        p = tf_sr.add_paragraph()
        p.text = "• " + pt
        p.font.size = Pt(13)
        p.font.color.rgb = TEXT_DARK
        p.space_before = Pt(8)

    # ==========================================
    # SLIDE 8: Key Finding 4 — Placement Risk vs Capital
    # ==========================================
    slide8 = prs.slides.add_slide(blank_layout)
    add_header(slide8, "Finding 4: The Double Penalty — High Fees Paired with Sub-50% Placement")

    desc_box = slide8.shapes.add_textbox(Inches(0.8), Inches(1.8), Inches(11.7), Inches(1.0))
    tf_d = desc_box.text_frame
    tf_d.word_wrap = True
    p_dh = tf_d.paragraphs[0]
    p_dh.text = "NIRF median salary only counts students who actually received placement offers. A low median salary is doubly dangerous when coupled with a low placement rate!"
    p_dh.font.size = Pt(14)
    p_dh.font.color.rgb = TEXT_DARK

    # 3 Danger Zone Examples
    ex_data = [
        ("KIIT Bhubaneswar (NIRF #36)", "4-Yr Fees: ₹16.35 Lakhs\nMedian Salary: ₹7.40 LPA\nPlacement Rate: 34.9%\nOver 65% of the graduating cohort walked away with ₹0 campus job offers!", RED),
        ("Vignan's Foundation (NIRF #80)", "4-Yr Fees: ₹9.70 Lakhs\nMedian Salary: ₹3.36 LPA\nPlacement Rate: 43.4%\nTakes 2.89 years of gross salary to recover, with under half of students placed.", RED),
        ("Graphic Era (NIRF #52)", "4-Yr Fees: ₹12.80 Lakhs\nMedian Salary: ₹5.00 LPA\nPlacement Rate: 49.3%\nTakes 2.56 years to recover tuition fees with less than 50% placement success.", RED)
    ]
    for i, (title, details, col) in enumerate(ex_data):
        left = Inches(0.8 + i * 3.95)
        top = Inches(3.0)
        card = slide8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, Inches(3.75), Inches(3.8))
        card.fill.solid()
        card.fill.fore_color.rgb = CARD_BG
        card.line.color.rgb = col
        card.line.width = Pt(2)

        tb = slide8.shapes.add_textbox(left + Inches(0.2), top + Inches(0.2), Inches(3.35), Inches(3.4))
        tf = tb.text_frame
        tf.word_wrap = True
        p_t = tf.paragraphs[0]
        p_t.text = title
        p_t.font.bold = True
        p_t.font.size = Pt(15)
        p_t.font.color.rgb = col

        for line in details.split('\n'):
            p = tf.add_paragraph()
            p.text = line
            p.font.size = Pt(12)
            p.font.color.rgb = TEXT_DARK
            p.space_before = Pt(4)

    # ==========================================
    # SLIDE 9: Strategic Decision Framework for Families
    # ==========================================
    slide9 = prs.slides.add_slide(blank_layout)
    add_header(slide9, "Actionable Decision Framework: 3 Golden Rules for Families")

    rules = [
        ("Rule 1: Unconditional Acceptance for Subsidized Elite Institutions", "If admitted to an IIT, top 10 NIT (Trichy, Surathkal, Rourkela, Warangal), or premier State University (Jadavpur, Anna Univ, DTU): Accept unconditionally. Statutory tuition caps (₹5.0L–₹8.0L) paired with median salaries exceeding ₹12.0–₹22.5 LPA guarantee financial recovery in under 9 months.", GREEN),
        ("Rule 2: The 'Mid-Tier Private' Veto Rule (>₹15 Lakhs)", "If deciding between a mid-tier private university (Rank 26–75) costing >₹15 Lakhs and an accredited regional government college costing <₹4 Lakhs: Decline the private college unless the student has confirmed admission to CS/IT with documented >85% department placement.", ACCENT_BLUE),
        ("Rule 3: Check the Non-Placed Denominator & Living Overhead", "Always adjust the financial calculation for living expenses (adding ₹1.2L–₹2.2L/year for residential campuses) and verify the branch-specific placement rate. A ₹7 LPA median means nothing if your child's branch has a 40% placement record.", RED)
    ]
    for i, (title, desc, color) in enumerate(rules):
        top_pos = Inches(1.8 + i * 1.7)
        shape = slide9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), top_pos, Inches(11.7), Inches(1.45))
        shape.fill.solid()
        shape.fill.fore_color.rgb = CARD_BG
        shape.line.color.rgb = color
        shape.line.width = Pt(2)

        tb = slide9.shapes.add_textbox(Inches(1.0), top_pos + Inches(0.12), Inches(11.3), Inches(1.2))
        tf = tb.text_frame
        tf.word_wrap = True
        p_t = tf.paragraphs[0]
        p_t.text = title
        p_t.font.size = Pt(15)
        p_t.font.bold = True
        p_t.font.color.rgb = color

        p_d = tf.add_paragraph()
        p_d.text = desc
        p_d.font.size = Pt(12)
        p_d.font.color.rgb = TEXT_DARK
        p_d.space_before = Pt(4)

    # ==========================================
    # SLIDE 10: Limitations & Demo Day Defense
    # ==========================================
    slide10 = prs.slides.add_slide(blank_layout)
    add_header(slide10, "Honest Analytical Limitations: What the Data Cannot Tell You")

    limits = [
        ("1. Branch-Wise Median Masking", "NIRF aggregates all engineering branches into a single median. A ₹10 LPA campus median typically hides a bimodal split: Computer Science at ₹18–₹24 LPA vs Civil/Metallurgy at ₹4.5–₹6.5 LPA.", NAVY),
        ("2. The Non-Placed Cohort (0 LPA)", "NIRF calculates median salary exclusively for placed students. In institutions like KIIT or Vignan's, over 55% to 65% of students received ₹0 from campus recruitment.", RED),
        ("3. Non-Academic Living Overhead", "The metric focuses exclusively on mandatory academic tuition and fees. Mandatory hostel and food add ₹1.2L to ₹2.2L per year (₹4.8L to ₹8.8L over 4 years), increasing total family outlay.", TEAL)
    ]
    for i, (title, desc, color) in enumerate(limits):
        left = Inches(0.8 + i * 3.95)
        top = Inches(1.8)
        width = Inches(3.75)
        height = Inches(4.8)

        card = slide10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = CARD_BG
        card.line.color.rgb = color

        t_box = slide10.shapes.add_textbox(left + Inches(0.2), top + Inches(0.3), width - Inches(0.4), height - Inches(0.6))
        tf = t_box.text_frame
        tf.word_wrap = True
        p_t = tf.paragraphs[0]
        p_t.text = title
        p_t.font.size = Pt(17)
        p_t.font.bold = True
        p_t.font.color.rgb = color

        p_d = tf.add_paragraph()
        p_d.text = desc
        p_d.font.size = Pt(13)
        p_d.font.color.rgb = TEXT_DARK
        p_d.space_before = Pt(14)

    output_path = r"c:\Users\pkatt\OneDrive\Desktop\Projects\NIRF_PowerBI_Analytics\NIRF_PowerBI_Presentation.pptx"
    prs.save(output_path)
    print(f"[SUCCESS] PowerPoint presentation saved to {output_path}")

if __name__ == "__main__":
    create_deck()
