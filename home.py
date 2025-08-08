import streamlit as st

st.set_page_config(page_title="Atif Aziz Memon - Portfolio", layout="wide")

# Title and subtitle
st.markdown("<h1 style='font-size: 3rem;'>👋 Hello, I'm Atif Aziz Memon</h1>", unsafe_allow_html=True)
st.markdown("### 📊 Data Analyst | 🎓 MS in Data Analytics (4.0 GPA) | 🧠 AI/ML Explorer")
st.markdown("---")

# About Me section
st.subheader("🔍 About Me")
st.write("""
I'm a passionate data analyst and machine learning enthusiast currently pursuing my Master's in Data Analytics at the **University of Illinois Springfield** (GPA 4.0).

I thrive on turning raw data into impactful insights and building tools that make complex data accessible to everyone.
""")

st.markdown("**🔑 Key Skills:**")
st.markdown("""
- 🐍 Python, SQL, R  
- 📊 Data Visualization (Plotly, Streamlit, Power BI)  
- 🤖 Machine Learning (scikit-learn, DeepFace)  
- 🗃️ Database Management (Oracle, PostgreSQL, PL/SQL)  
""")

st.markdown("**🏢 Previously at NayaPay** — I managed financial databases, automated ETL pipelines, and optimized queries as a **Database Administrator**.")

st.markdown("---")

# Navigation buttons
st.subheader("📂 Explore More:")
col_a, col_b, col_c, col_d = st.columns(4)

with col_a:
    if st.button("💼 Projects"):
        st.switch_page("pages/1_Projects.py")

with col_b:
    if st.button("🧑‍💼 Experience"):
        st.switch_page("pages/2_Experience.py")

with col_c:
    if st.button("🎓 Education"):
        st.switch_page("pages/4_Education.py")

with col_d:
    if st.button("📫 Contact"):
        st.switch_page("pages/3_Contact.py")

st.markdown("---")

with open("atif_memon_resume.pdf", "rb") as file:
    resume_bytes = file.read()

st.download_button(
    label="📄 Download My Resume",
    data=resume_bytes,
    file_name="Atif_Memon_Resume.pdf",
    mime="application/pdf"
)



