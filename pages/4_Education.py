import streamlit as st

st.set_page_config(page_title="Education", layout="wide")

st.title("🎓 Education")
st.write("Here's my academic background, including degrees, coursework, and certifications.")

st.subheader("📘 Master of Science in Data Analytics")
st.write("""
**Institution:** University of Illinois Springfield  
**GPA:** 4.0 / 4.0  
**Duration:** 2023 – Present (Expected Graduation: May 2025)

**Relevant Coursework:**
- Machine Learning & Predictive Modeling
- Statistical Inference and Regression Analysis
- Big Data Tools (Hadoop, Spark)
- Data Visualization with Python & R
- Business Analytics and Reporting

**Projects:**
- Mental Health ML Classifier
- Big Data Pipeline using PySpark
- Streamlit dashboard for survey analysis
""")

st.subheader("📗 Bachelor of Science (Optional Entry)")
st.write("""
If you want to include bachelor's or any certification (Coursera, Udemy, etc.), let me know and I’ll format this section too.
""")

# Back button
if st.button("⬅️ Go Back to Home"):
    st.switch_page("home.py")
