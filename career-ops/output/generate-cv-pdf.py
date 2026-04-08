from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable, Table, TableStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER

output_path = "/home/user/righteousheathen/career-ops/output/cv-bubacarr-barrow.pdf"

doc = SimpleDocTemplate(
    output_path,
    pagesize=A4,
    rightMargin=2*cm, leftMargin=2*cm,
    topMargin=2*cm, bottomMargin=2*cm
)

W = A4[0] - 4*cm

# Styles
heading_color = colors.HexColor("#111111")
muted = colors.HexColor("#555555")

name_style = ParagraphStyle("Name", fontName="Helvetica-Bold", fontSize=18, spaceAfter=2, textColor=heading_color)
contact_style = ParagraphStyle("Contact", fontName="Helvetica", fontSize=9, spaceAfter=2, textColor=muted)
section_style = ParagraphStyle("Section", fontName="Helvetica-Bold", fontSize=9.5, spaceBefore=10, spaceAfter=3, textColor=heading_color, textTransform="uppercase", letterSpacing=1)
job_title_style = ParagraphStyle("JobTitle", fontName="Helvetica-Bold", fontSize=10.5, spaceBefore=8, spaceAfter=1)
job_meta_style = ParagraphStyle("JobMeta", fontName="Helvetica-Oblique", fontSize=9.5, spaceAfter=3, textColor=muted)
body_style = ParagraphStyle("Body", fontName="Helvetica", fontSize=10, leading=14, spaceAfter=2)
bullet_style = ParagraphStyle("Bullet", fontName="Helvetica", fontSize=10, leading=14, leftIndent=14, firstLineIndent=-10, spaceAfter=2)
small_style = ParagraphStyle("Small", fontName="Helvetica", fontSize=10, leading=14, spaceAfter=2)

def hr():
    return HRFlowable(width="100%", thickness=0.7, color=colors.HexColor("#cccccc"), spaceAfter=4)

def section(title):
    items = []
    items.append(Spacer(1, 4))
    items.append(Paragraph(title.upper(), section_style))
    items.append(HRFlowable(width="100%", thickness=0.7, color=colors.HexColor("#cccccc"), spaceAfter=2))
    return items

def bullet(text):
    return Paragraph(f"• {text}", bullet_style)

story = []

# Header
story.append(Paragraph("BUBACARR BARROW", name_style))
story.append(Paragraph("Bijilo, The Gambia &nbsp;&nbsp;|&nbsp;&nbsp; batisbaro@gmail.com &nbsp;&nbsp;|&nbsp;&nbsp; +220 3151153 / 6770865", contact_style))
story.append(HRFlowable(width="100%", thickness=1.5, color=heading_color, spaceAfter=6))

# Summary
story += section("Professional Summary")
story.append(Paragraph(
    "Results-driven Accountancy graduate (BSc, IPFM UK certified) with proven experience in accounts receivable, "
    "credit control, procurement, and financial reporting across fintech, ISP, and agri-commodity sectors. "
    "Google-certified Data Analytics professional skilled in SQL, Power BI, and Tableau. McKinsey Forward Programme "
    "alumnus with strong analytical capabilities and a track record of measurable impact.",
    body_style
))

# Experience
story += section("Work Experience")

jobs = [
    {
        "title": "Payment Admin Officer",
        "company": "Wave · Gambia",
        "period": "Mar 2026 – Present",
        "bullets": [
            "Manage inbound payment files and maintain accurate tracking across dashboards.",
            "Support merchant recruitment, contracts, and system/device maintenance across the network.",
            "Key logistics contact for payments team; liaise with field teams on operational planning.",
            "Assist with compliance projects and administrative duties in the payments department.",
        ]
    },
    {
        "title": "AR & Credit Control Accountant",
        "company": "DK Telecom Ltd · Gambia",
        "period": "Dec 2025 – Mar 2026",
        "bullets": [
            "Reduced outstanding receivables from GMD 11M to GMD 9M within 2 months — a GMD 2M improvement.",
            "Reconciled AR balances and maintained clean debtor ledgers; enforced credit thresholds.",
            "Escalated 30+ day overdue accounts to Finance Manager and Credit & Asset Recovery Manager.",
            "Alerted Sales team of at-risk accounts, credit limit breaches, and payment behaviour trends.",
        ]
    },
    {
        "title": "Procurement Officer",
        "company": "DK Telecom Ltd · Gambia",
        "period": "Sep 2025 – Nov 2025",
        "bullets": [
            "Managed procurement of network hardware/software; issued RFQs, RFPs, and ITTs.",
            "Negotiated vendor contracts for cost savings; monitored performance and resolved disputes.",
            "Analysed procurement data and reported on budget adherence and savings realised.",
        ]
    },
    {
        "title": "Unit Accountant & Administrator",
        "company": "Comafrique Limited · Gambia",
        "period": "Sep 2023 – Aug 2025",
        "bullets": [
            "Managed budgets, AP/AR, and year-end financial statements using Tally ERP.",
            "Delivered CFR/CIF cost analysis to CEO, directly informing sesame and cashew pricing decisions.",
            "Coordinated exports with Maersk, CMA CGM, and MSC; oversaw full export documentation.",
            "Automated sales contracts, invoices, and packing lists in collaboration with Dubai teams.",
        ]
    },
    {
        "title": "Assistant Accounts & Admin Officer",
        "company": "Comafrique Limited · Gambia",
        "period": "Mar 2023 – Sep 2023",
        "bullets": [
            "Processed invoices, managed bank reconciliations, petty cash, and expense reports.",
            "Supported budgeting, forecasting, payroll preparation, and financial statement production.",
        ]
    },
    {
        "title": "Voter Registration Supervisor",
        "company": "Independent Electoral Commission · Gambia",
        "period": "2021",
        "bullets": [
            "Led voter registration operations with precision; served as primary media liaison.",
            "Produced weekly operational reports for the Deputy Chairperson.",
        ]
    },
]

for job in jobs:
    story.append(Paragraph(job["title"], job_title_style))
    story.append(Paragraph(f"{job['company']}  |  {job['period']}", job_meta_style))
    for b in job["bullets"]:
        story.append(bullet(b))

# Education
story += section("Education")
story.append(Paragraph("<b>BSc Accountancy</b> — University of The Gambia, 2024", small_style))
story.append(Paragraph("<b>Cert. Accounting &amp; Finance</b> — IPFM, United Kingdom, 2017", small_style))

# Certifications
story += section("Certifications")
certs = [
    "Google Data Analytics Professional Certificate · 2022",
    "McKinsey Forward Programme · 2023",
    "SQL Mastery — CodeWithMosh · 2023",
    "Data Analyst in Power BI · 2024",
    "Bookkeeping Basic — QuickBooks · 2021",
    "Binance Blockchain Deep Dive · 2025",
]
for c in certs:
    story.append(Paragraph(c, small_style))

# Skills
story += section("Skills")
story.append(Paragraph("<b>Accounting:</b> Tally ERP · QuickBooks · AP/AR · Bank Reconciliation · Financial Reporting", small_style))
story.append(Paragraph("<b>Data &amp; Analytics:</b> SQL · Power BI · Tableau · Advanced Excel · Google Sheets", small_style))
story.append(Paragraph("<b>Productivity:</b> Microsoft Office Suite · Google Workspace", small_style))
story.append(Paragraph("<b>Languages:</b> English — Full professional proficiency", small_style))

doc.build(story)
print(f"PDF saved to: {output_path}")
