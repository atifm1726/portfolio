import streamlit as st

st.set_page_config(page_title="Contact", layout="wide")
st.title("📬 Contact Me")

# Contact links
st.markdown("""
Feel free to connect with me or send a message using the form below:

- 📧 Email: [atifm1726@gmail.com](mailto:atifm1726@gmail.com)  
- 💼 [LinkedIn](https://www.linkedin.com/in/atif-memon1726)  
- 🐙 [GitHub](https://github.com/atifm1726)
""")

st.markdown("---")

# Custom styled contact form using HTML/CSS
st.markdown("""
<style>
    .contact-form {
        background-color: #1e1e1e;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 0 10px rgba(0,0,0,0.5);
        max-width: 600px;
        margin: auto;
    }
    .contact-form input, .contact-form textarea {
        width: 100%;
        padding: 12px;
        margin-bottom: 15px;
        border: none;
        border-radius: 10px;
        background-color: #2e2e2e;
        color: #ffffff;
    }
    .contact-form button {
        background-color: #4CAF50;
        color: white;
        padding: 12px 24px;
        border: none;
        border-radius: 10px;
        cursor: pointer;
    }
    .contact-form button:hover {
        background-color: #45a049;
    }
</style>

<div class="contact-form">
    <h3>📨 Send Me a Message</h3>
    <form action="https://formsubmit.co/atifm1726@gmail.com" method="POST">
        <input type="text" name="name" placeholder="Your Name" required>
        <input type="email" name="email" placeholder="Your Email" required>
        <textarea name="message" placeholder="Your Message Here" rows="6" required></textarea>
        <button type="submit">📤 Send Message</button>
    </form>
</div>
""", unsafe_allow_html=True)
