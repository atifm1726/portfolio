import streamlit as st

st.set_page_config(page_title="Contact", layout="wide")

st.title("📫 Contact Me")
st.write("Let’s connect! I’m open to collaborations, mentorship, and project opportunities.")

st.markdown("""
- 📧 **Email:** [atifm1726@gmail.com](mailto:atifm1726@gmail.com)  
- 💼 **LinkedIn:** [linkedin.com/in/atif-memon1726](https://www.linkedin.com/in/atif-memon1726)  
- 📱 **Phone:** +1 (217) 553-1338  
""")

st.markdown("---")
st.subheader("📬 Contact Form (Coming Soon)")
st.write("This section will soon support contact messages directly from the page.")

# Back button
if st.button("⬅️ Go Back to Home"):
    st.switch_page("home.py")
