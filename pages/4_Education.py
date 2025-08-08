import streamlit as st

st.set_page_config(page_title="Education", layout="wide")

st.title("🎓 Education")
st.write("Here's my academic background, including degrees, coursework, and certifications.")

st.subheader("📘 Master of Science in Data Analytics")
st.write("""
**Institution:** University of Illinois Springfield  
**GPA:** 4.0 / 4.0  
**Duration:** 2024 – Present (Expected Graduation: May 2026)

**Relevant Coursework:**
- Machine Learning 
- Advanced Statistical Methods
- Big Data 
- Data Visualization with Python & R


**Projects:**
- Mental Health ML Classifier
- Streamlit dashboard for survey analysis
""")

st.subheader("📗 Bachelor of Science (Optional Entry)")
st.write("""
If you want to include bachelor's or any certification (Coursera, Udemy, etc.), let me know and I’ll format this section too.
""")

# Back button
if st.button("⬅️ Go Back to Home"):
    st.switch_page("home.py")
