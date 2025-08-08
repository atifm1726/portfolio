import streamlit as st

st.set_page_config(page_title="Projects", layout="wide")

st.title("💼 Projects Showcase")
st.markdown("Explore some of my most impactful data-driven projects.")

st.subheader("🗺️ US Census Data Explorer")
st.write("""
An interactive web app that visualizes U.S. Census data by **state**, **year**, **gender**, and **metric**.
- Built using **Streamlit**, **Plotly**, and the **U.S. Census API**
- 3D bar maps, line charts, and dropdowns for real-time exploration
- Designed for users with no coding experience to intuitively navigate census statistics
""")

st.subheader("😄 Emotion Detection System")
st.write("""
A real-time emotion recognition system using **DeepFace** and **OpenCV**.
- Detects facial expressions through webcam feed
- Identifies emotions like *happy*, *sad*, *angry*, etc.
- Useful in **mental health tracking**, **interactive systems**, and **security tools**
""")

st.subheader("🧠 Mental Health Prediction in Tech")
st.write("""
A machine learning model trained on a Kaggle survey dataset to predict the likelihood of seeking mental health support.
- Techniques: **Logistic Regression**, **SVM**, and **Decision Trees**
- Evaluated using **accuracy**, **precision**, **recall**, and **F1-score**
- Goal: help companies understand what factors influence mental health openness
""")

# Go Back Button
if st.button("⬅️ Go Back to Home"):
    st.switch_page("home.py")
