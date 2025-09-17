import streamlit as st
from utils.load_data import load_data

st.set_page_config(page_title="Home Credit Default Risk e Dashboard", page_icon="📊", layout="wide")

st.title("🛍 Home Credit Default Risk e Dashboard")

st.markdown("""
Welcome to the *Home Credit Default Risk Dashboard* built with *Streamlit*.  
Use the sidebar to navigate between different analysis modules:
* 📊 Overview & Data Quality
* 🎯 Target & Risk Segmentation
* 🏠 Demographics & Household Profile
* 💰 Financial Health & Affordability
* 🔍 Correlations, Drivers & Interactive Slice-and-Dice       
""")

st.markdown("---")
st.subheader("Upload / Use Default Dataset")

uploaded_file = st.file_uploader("Upload your application_train CSV file", type=["csv"])
if uploaded_file:
    df = load_data(uploaded_file)
else:
    df = load_data()

st.dataframe(df.head(10))