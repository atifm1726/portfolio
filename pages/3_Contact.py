import streamlit as st

st.set_page_config(page_title="Contact", layout="wide")

st.title("📬 Contact Me")

st.markdown("""
Feel free to reach out via email or connect with me on LinkedIn and GitHub:

- 📧 Email: atifm1726@gmail.com  
- 💼 [LinkedIn](https://www.linkedin.com/in/atif-memon1726)  
- 🐙 [GitHub](https://github.com/atifm1726)
""")

st.markdown("---")
st.subheader("📨 Send Me a Message")

with st.form(key="contact_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")
    submit_button = st.form_submit_button(label="Send")

if submit_button:
    if name and email and message:
        st.success(f"Thanks {name}, your message has been sent!")
    else:
        st.error("Please fill out all fields before submitting.")
