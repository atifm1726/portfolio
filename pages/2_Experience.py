import streamlit as st

st.set_page_config(page_title="Experience", layout="wide")

st.title("👨‍💼 Professional Experience")
st.markdown("Here’s an overview of my work experience and the impact I created.")

st.subheader("📌 NayaPay — Database Administrator")
st.write("""
**Location:** Karachi, Pakistan  
**Duration:** Jan 2022 – June 2023  

**Responsibilities:**
- Designed, maintained, and optimized relational databases (Oracle, MySQL, SQL Server)
- Wrote, debugged, and tuned complex SQL queries for high-volume financial transactions
- Collaborated with developers and QA teams on schema changes and deployment cycles
- Scheduled and managed daily backup routines using PL/SQL and cron jobs
- Performed root cause analysis of database issues and implemented preventive measures
- Analyzed slow-running queries and improved response time with indexing strategies
- Ensured data accuracy and consistency across production and reporting environments
- Audited data pipelines to detect anomalies and resolve duplicate/missing record issues
- Maintained staging and live environments, ensuring availability and failover readiness
- Built scripts to automate reporting tasks using PL/SQL functions and procedures
- Documented and maintained detailed technical logs and change requests
- Conducted weekly data validation checks and resolved discrepancies with business teams
- Assisted compliance team with data extractions for audits and financial reports

**Key Achievements:**
- Reduced query load time by 45% across financial reconciliation reports
- Improved system uptime from ~97% to over 99.9%
- Delivered monthly database cleanups that improved storage efficiency by 20%
- Acted as key point of contact for production DB issues, ensuring <15 min resolution time
- Led database optimization initiative, improving performance of over 60 reports
""")

# Back button
if st.button("⬅️ Go Back to Home"):
    st.switch_page("home.py")
