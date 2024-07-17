import eda
import predict
import streamlit as st

navigation = st.sidebar.selectbox('Navigation', ['Exploratory Data Analysis', 'amazon sentiment analysis'])

import streamlit as st

# Judul sidebar
st.sidebar.title('mangenai amazon e-commerce')

# Deskripsi aplikasi
st.sidebar.markdown(
    "Selamat datang di aplikasi analisis ulasan Amazon! Di sini, Anda bisa menjelajahi berbagai" 
    "analisis teks yang kami lakukan terhadap jutaan ulasan produk di Amazon. Kami mengumpulkan"
    "data ini untuk membantu Anda memahami lebih dalam tentang apa yang dipikirkan konsumen tentang" 
    "berbagai produk."
)

# Fitur aplikasi
st.sidebar.subheader('Fitur Aplikasi:')
st.sidebar.markdown("- **Word Cloud:** representasi visual berdasarkan sentimen (positif, netral, negatif).")
st.sidebar.markdown("- **Analisis:** Analisis berdasarkan sentimen.")
st.sidebar.markdown("- **Prediksi:**  prediksi sentimen menggunakan model yang dilatih.")

# Panduan penggunaan
st.sidebar.subheader('Panduan Penggunaan:')
st.sidebar.markdown("1. **Unggah :** Unggah data untuk dianalisis.")
st.sidebar.markdown("2. **ExploreWord Cloud:** Jelajahi word cloud berdasarkan sentimen untuk melihat kata-kata kunci yang muncul dalam tweet.")
st.sidebar.markdown("3. **Prediction :** Masukkan teks tweet berdasarkan prediksi sentimen secara real-time.")

# Kontak atau informasi tambahan
st.sidebar.markdown(
    "Terima kasih telah menggunakan aplikasi analisis ulasan Amazon kami. Kami berharap aplikasi ini dapat membantu Anda dalam membuat keputusan pembelian yang lebih cerdas."
)

# Footer atau penutup sidebar
st.sidebar.markdown("**Terimakasih!**")

if navigation == 'Exploratory Data Analysis' :
    eda.run()
else:
    predict.run()