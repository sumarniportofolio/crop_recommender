import streamlit as st
from src.train import predict_crop

# Page config
st.set_page_config(
    page_title="Smart Agricultural Crop Optimizer",
    page_icon="🌱",
    layout="wide"
)

# Header
st.markdown("""
    <div style="background-color:#4CAF50;padding:10px;border-radius:10px">
    <h1 style="color:white;text-align:center;">Smart Agricultural Production Optimizing Engine</h1>
    <p style="color:white;text-align:center;">Masukkan parameter tanah untuk mendapatkan rekomendasi tanaman</p>
    </div>
    """, unsafe_allow_html=True)

st.write("")  # spasi

# Input layout dengan 2 kolom
col1, col2 = st.columns(2)

with col1:
    N = st.number_input("Nitrogen (N)", min_value=0, max_value=200, value=50)
    P = st.number_input("Phosphorus (P)", min_value=0, max_value=200, value=50)
    K = st.number_input("Potassium (K)", min_value=0, max_value=200, value=50)

with col2:
    Temperature = st.number_input("Temperature (°F)", min_value=30, max_value=120, value=70)
    Ph = st.number_input("pH", min_value=3.0, max_value=10.0, value=6.5)

st.write("")  # spasi

# Button prediksi dengan warna hijau
if st.button("Prediksi Tanaman 🌱"):
    crop = predict_crop(N, P, K, Temperature, Ph)
    st.markdown(f"""
        <div style="background-color:#e8f5e9;padding:20px;border-radius:10px;margin-top:10px">
        <h2 style="color:#2e7d32;text-align:center;">Rekomendasi tanaman: {crop}</h2>
        </div>
    """, unsafe_allow_html=True)

# Footer kecil
st.markdown("""
    <hr>
    <p style="text-align:center;color:gray;font-size:12px;">© 2026 Smart Agricultural Engine</p>
""", unsafe_allow_html=True)