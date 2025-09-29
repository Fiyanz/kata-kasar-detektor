import streamlit as st
import joblib
import base64

# Load model
model = joblib.load("model/svm_kata_kasar_model.pkl")

# ========== UI CONFIGURATION ==========
st.set_page_config(
    page_title="Kata Kasar Detektor",
    page_icon="🚨",
    layout="centered"
)

# ========== SIDEBAR ==========
with st.sidebar:
    st.title("💬 Info Aplikasi")
    st.markdown("""
    Aplikasi ini menggunakan model Machine Learning **(SVM)**  
    untuk mendeteksi apakah sebuah kalimat mengandung:
    - 🔴 Kekerasan (Violence)
    - 🟠 Pelecehan (Harassment)
    - 🟡 Rasisme (Racist)
    - 🟢 Netral (Neutral)
    
    Dibuat untuk keperluan tugas akhir/publikasi.
    """)
    st.markdown("---")
    st.caption("Made with ❤️ by Fiyanz")
    st.caption("[GitHub Repo](https://github.com/Fiyanz/kata-kasar-detektor)") 

# ========== MAIN ==========
st.title("🚨 Kata Kasar Detektor")
st.markdown("Masukkan teks pada kolom di bawah untuk mengetahui apakah mengandung ujaran kasar atau tidak.")

user_input = st.text_area("📝 Masukkan Kalimat:", height=150)

# Tombol prediksi
if st.button("🔍 Prediksi"):
    if user_input.strip() == "":
        st.warning("Silakan masukkan teks terlebih dahulu.")
    else:
        label = model.predict([user_input])[0]
        
        label_colors = {
            "neutral": "🟢",
            "violence": "🔴",
            "racist": "🟡",
            "harassment": "🟠"
        }

        color = label_colors.get(label, "❓")
        st.markdown(f"### Hasil Prediksi: {color} **{label.upper()}**")
