#!/usr/bin/env python3
"""
Career-Ops Email Sender
Run this on your own machine to send all applications.

Usage:
    python3 send-applications.py

Requirements:
    - Python 3 (pre-installed on most systems)
    - Gmail App Password: hpor yokc divv mawk
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

SENDER_EMAIL = "batisbaro@gmail.com"
SENDER_NAME = "Bubacarr Barrow"
APP_PASSWORD = "hporyokcdivvmawk"  # Replace if needed

applications = [
    {
        "to": "luxembourg@roberthalf.com",
        "subject": "Finance & Accounting Professional seeking Luxembourg opportunities — Bubacarr Barrow",
        "body": """Dear Robert Half Luxembourg Team,

I am a Finance and Data Analytics professional with a BSc in Accountancy (University of The Gambia), an IPFM (UK) professional certification, and over three years of progressive experience in accounts receivable, accounts payable, credit control, procurement, and financial reporting.

I am actively seeking finance and accounting opportunities in Luxembourg, specifically roles such as:
- Accounts Payable / Receivable Officer
- Finance or Administrative Officer
- Staff Accountant / Junior Accountant
- Financial Analyst / Reporting Analyst

Key experience highlights:
- Reduced outstanding receivables by GMD 2M (GMD 11M → 9M) in 2 months at DK Telecom
- Full AP/AR cycle, year-end financial statements, and budget management at Comafrique Limited using Tally ERP
- Procurement cycle management (RFQs, RFPs, ITTs, vendor contracts) at DK Telecom
- Currently: Payment Admin Officer at Wave, managing payment files, compliance, and merchant operations

Technical skills: SQL · Power BI · Tableau · Advanced Excel · Tally ERP · QuickBooks
Certifications: Google Data Analytics Pro (2022) · McKinsey Forward Programme (2023) · IPFM UK

I am available to relocate to Luxembourg immediately and am open to permanent, fixed-term, or contract positions.

Please find my CV attached. I am happy to speak at your convenience.

Best regards,
Bubacarr Barrow
batisbaro@gmail.com
+220 3151153 / 6770865"""
    },
    {
        "to": "contact@lu.morganphilips.com",
        "subject": "Finance & Accounting Professional — Luxembourg Job Search — Bubacarr Barrow",
        "body": """Dear Morgan Philips Luxembourg Team,

I am writing to register my interest in finance and accounting opportunities in Luxembourg through Morgan Philips. I am a results-driven Accountancy graduate with an IPFM (UK) certification and over three years of experience in financial operations, credit control, procurement, and data analytics across fintech, telecoms, and agri-commodity sectors.

I am targeting mid-level roles in Luxembourg such as:
- Finance Officer / Financial Analyst
- Accounts Payable / Receivable Accountant
- Administrative & Finance Officer
- Reporting / Data Analyst (Finance)

Professional highlights:
- Wave (2026–present): Payment Admin Officer — financial file management, compliance administration, merchant contracts
- DK Telecom (2025–2026): AR & Credit Control Accountant — reduced receivables by GMD 2M in 2 months; Procurement Officer — full RFQ/RFP/ITT cycle
- Comafrique Limited (2023–2025): Unit Accountant & Administrator — AP/AR, year-end financials (Tally ERP), international export documentation (Maersk, CMA CGM, MSC)

Education & Certifications:
BSc Accountancy (University of The Gambia, 2024) · Cert. Accounting & Finance IPFM UK · Google Data Analytics Professional Certificate · McKinsey Forward Programme · SQL Mastery · Data Analyst in Power BI

Technical: SQL · Power BI · Tableau · Advanced Excel · Tally ERP · QuickBooks · Google Workspace

I am available to relocate to Luxembourg immediately. Please find my CV attached.

Best regards,
Bubacarr Barrow
batisbaro@gmail.com
+220 3151153 / 6770865"""
    },
    {
        "to": "recruitment@manpower.lu",
        "subject": "Application: Financial Operations Administrative Assistant (European Institution) — Bubacarr Barrow",
        "body": """Dear Talent Acquisition Team,

I am writing to express my interest in the Financial Operations Administrative Assistant position for a European institution in Luxembourg, starting April 2026. I am a finance and administrative professional with a BSc in Accountancy, an IPFM (UK) certification, and over three years of cross-sector experience in financial operations, data reporting, and administrative coordination.

In my current role as Payment Admin Officer at Wave, I manage inbound payment files, maintain accurate tracking dashboards, and support compliance and administrative operations across a distributed payments network.

Prior to Wave, I served as AR & Credit Control Accountant at DK Telecom, where I managed debtor ledgers, reconciled AR balances, and reduced outstanding receivables by GMD 2M in just two months. At Comafrique Limited, I held a combined Accountant and Administrator role — managing budgets, AP/AR, and year-end financials using Tally ERP, while also coordinating international export logistics with Maersk, CMA CGM, and MSC.

I am highly organised, detail-oriented, and experienced working in structured, compliance-driven environments. I am proficient in Microsoft Office Suite, Google Workspace, SQL, Power BI, and Advanced Excel.

I am fully available to relocate to Luxembourg and can begin promptly.

Best regards,
Bubacarr Barrow
batisbaro@gmail.com
+220 3151153 / 6770865"""
    },
    {
        "to": "eca-recruitment@eca.europa.eu",
        "subject": "Application: Finance / Administrative Assistant (AST level) — Bubacarr Barrow",
        "body": """Dear HR Team,

I am writing to express my interest in finance and administrative assistant positions at the European Court of Auditors. I hold a BSc in Accountancy from the University of The Gambia and a professional Cert. in Accounting & Finance from IPFM (United Kingdom). Over three years, I have built hands-on experience in financial reporting, AP/AR management, procurement, and operational administration.

Key highlights:
- Financial accuracy: Reconciled AR balances and maintained clean debtor ledgers at DK Telecom; prepared year-end financial statements, budgets, and cost analyses at Comafrique Limited using Tally ERP.
- Procurement & contracts: Managed full procurement cycles at DK Telecom including RFQs, RFPs, ITTs, and vendor contract negotiation.
- Reporting & analytics: Google-certified Data Analyst with SQL, Power BI, Tableau, and Advanced Excel proficiency.
- Administrative coordination: Currently supporting compliance projects, merchant contracts, and cross-team operational planning at Wave, a leading pan-African fintech.

I am available to relocate to Luxembourg and am eager to contribute to the ECA's mission.

Best regards,
Bubacarr Barrow
batisbaro@gmail.com
+220 3151153 / 6770865"""
    },
]

def send_email(to, subject, body):
    msg = MIMEMultipart()
    msg['From'] = f"{SENDER_NAME} <{SENDER_EMAIL}>"
    msg['To'] = to
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(SENDER_EMAIL, APP_PASSWORD)
        server.send_message(msg)

if __name__ == "__main__":
    print(f"Sending {len(applications)} applications from {SENDER_EMAIL}...\n")
    for i, app in enumerate(applications, 1):
        try:
            send_email(app['to'], app['subject'], app['body'])
            print(f"✅ {i}/{len(applications)} Sent → {app['to']}")
        except Exception as e:
            print(f"❌ {i}/{len(applications)} Failed → {app['to']}: {e}")
    print("\nDone.")
