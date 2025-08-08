import streamlit as st

st.set_page_config(page_title="Contact", layout="wide")
st.title("📬 Contact Me")

st.markdown("""
Feel free to connect with me or send a message using the form below:

- 📧 Email: atifm1726@gmail.com  
- 💼 [LinkedIn](https://www.linkedin.com/in/atif-memon1726)  
- 🐙 [GitHub](https://github.com/atifm1726)
""")

st.markdown("---")
st.subheader("📨 Send Me a Message")

contact_form = """
<form action="https://formsubmit.co/atifm1726@gmail.com" method="POST">
     <input type="text" name="name" placeholder="Your Name" required><br><br>
     <input type="email" name="email" placeholder="Your Email" required><br><br>
     <textarea name="message" placeholder="Your Message Here" rows="6" required></textarea><br><br>
     <button type="submit">📤 Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)
