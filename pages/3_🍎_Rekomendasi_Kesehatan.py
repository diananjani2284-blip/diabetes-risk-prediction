# =========================================================
# pages/3_🍎_Rekomendasi_Kesehatan.py
# =========================================================
import streamlit as st
from utils.ui import set_background

set_background()

st.title("🍎 Rekomendasi Kesehatan")

st.caption(
    "Panduan gaya hidup sehat ini disusun sebagai upaya promotif dan preventif "
    "untuk membantu menjaga kesehatan serta menurunkan risiko penyakit metabolik, "
    "termasuk diabetes."
)

st.markdown("""
### Rekomendasi Gaya Hidup Sehat

Menerapkan pola hidup sehat secara konsisten dapat membantu menjaga
kadar gula darah tetap stabil serta meningkatkan kualitas hidup secara keseluruhan.
Berikut beberapa rekomendasi umum yang dapat diterapkan dalam kehidupan sehari-hari:

- 🥗 **Pola makan seimbang**  
  Konsumsi makanan dengan gizi seimbang yang terdiri dari sayur, buah,
  protein tanpa lemak, serta karbohidrat kompleks. Batasi makanan tinggi gula,
  garam, dan lemak jenuh.

- 🏃 **Aktivitas fisik rutin**  
  Lakukan aktivitas fisik intensitas sedang seperti jalan cepat,
  bersepeda, atau berenang setidaknya **150 menit per minggu**
  untuk membantu mengontrol berat badan dan meningkatkan sensitivitas insulin.

- 🚭 **Hindari rokok dan alkohol berlebih**  
  Merokok dan konsumsi alkohol berlebihan dapat meningkatkan risiko
  gangguan metabolik serta penyakit kardiovaskular.

- 😴 **Istirahat cukup dan kelola stres**  
  Tidur yang cukup (7–9 jam per hari) serta pengelolaan stres yang baik
  berperan penting dalam menjaga keseimbangan hormon dan kesehatan metabolik.

---

📌 **Catatan Penting**  
Rekomendasi ini bersifat **umum** dan bertujuan sebagai edukasi kesehatan.
Setiap individu memiliki kondisi kesehatan yang berbeda, sehingga disarankan
untuk menyesuaikan penerapan rekomendasi ini dengan kebutuhan pribadi
atau berkonsultasi dengan tenaga kesehatan profesional.
""")
