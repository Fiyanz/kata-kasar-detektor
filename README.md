# 🛡️ Deteksi Kata Kasar (Indonesia)

Aplikasi berbasis Machine Learning untuk mendeteksi ujaran kasar, kekerasan, pelecehan, atau rasisme dalam teks Bahasa Indonesia.  
Model dilatih menggunakan SVM + TF-IDF, dan diimplementasikan ke dalam antarmuka web interaktif menggunakan Streamlit.

🔗 **Live Demo App**: [Klik untuk membuka aplikasi Streamlit](https://kata-kasar-detektor.streamlit.app)

---

## 🎯 Tujuan Proyek

Proyek ini bertujuan untuk:
- Mengklasifikasikan teks ke dalam 4 kategori: `neutral`, `violence`, `racist`, dan `harassment`
- Melatih model dari dataset percakapan bahasa Indonesia yang telah dibersihkan
- Menyediakan antarmuka pengguna (UI) sederhana dan responsif untuk pengujian model

---


## 🧪 Contoh Penggunaan

Teks masukan:

```txt
"dasar cina"
```
Output:
```txt

🟡 Rasisme
```

---

## 🚀 Cara Menjalankan Aplikasi

1. Clone repositori ini:
```bash
git clone https://github.com/username/kata-kasar-detektor.git
cd kata-kasar-detektor
```
2. Install dependensi:
```bash
pip install -r requirements.txt
```
3. Run app
```bash
streamlit run app.py
```

---

## 🧠 Teknologi yang Digunakan

- Python 3.x
- Scikit-learn
- TfidfVectorizer
- Support Vector Machine (SVM)
- Streamlit
- Google Colab (untuk pelatihan model)

---

## 📊 Sumber Dataset

Dataset yang digunakan dalam proyek ini berasal dari Kaggle:

📦 **Indonesian Chat Dataset**  
oleh: [@jprestiliano](https://www.kaggle.com/jprestiliano)  
🔗 [https://www.kaggle.com/datasets/jprestiliano/indonesian-chat-dataset](https://www.kaggle.com/datasets/jprestiliano/indonesian-chat-dataset)

Dataset ini berisi contoh percakapan dalam Bahasa Indonesia yang telah dikategorikan ke dalam label seperti `neutral`, `violence`, `racist`, dan `harassment`.


---

## 👨‍💻 Pengembang

**Fiyanz**  
Ilmu Komputer  



