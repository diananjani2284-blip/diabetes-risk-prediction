import streamlit as st
from utils.ui import set_background

set_background()

st.title("📘 Edukasi Diabetes")

st.caption(
    "Informasi kesehatan ini disusun untuk membantu masyarakat memahami diabetes, "
    "faktor risikonya, serta langkah pencegahan yang dapat dilakukan sejak dini "
    "berdasarkan sumber medis dan praktik kesehatan yang umum digunakan."
)

st.markdown("""
### Apa itu Diabetes?
Diabetes adalah **penyakit kronis** yang terjadi ketika tubuh tidak mampu
mengatur kadar gula (glukosa) dalam darah secara optimal.
Kondisi ini dapat disebabkan oleh **gangguan produksi insulin**,
**resistensi insulin**, atau kombinasi keduanya.

Jika tidak dikendalikan dengan baik, diabetes dapat meningkatkan risiko
berbagai komplikasi kesehatan seperti **penyakit jantung, stroke,
gangguan ginjal, gangguan penglihatan**, serta **kerusakan saraf**.
Oleh karena itu, **deteksi dini dan pencegahan** sangat penting.

---

### Faktor Risiko Utama
Beberapa faktor yang dapat meningkatkan risiko seseorang mengalami diabetes meliputi:

- **Usia**: Risiko meningkat seiring bertambahnya usia
- **Kelebihan berat badan atau obesitas (BMI tinggi)**
- **Kurangnya aktivitas fisik** atau gaya hidup sedentari
- **Pola makan tidak seimbang**, terutama tinggi gula dan lemak
- **Riwayat keluarga** dengan diabetes
- **Tekanan darah tinggi** dan gangguan metabolisme lainnya

Memiliki satu atau lebih faktor di atas **tidak berarti pasti menderita diabetes**,
namun dapat meningkatkan kemungkinan terjadinya penyakit ini.

---

### Pencegahan dan Gaya Hidup Sehat
Diabetes, khususnya diabetes tipe 2, **dapat dicegah atau ditunda**
dengan menerapkan pola hidup sehat, antara lain:

- Melakukan **aktivitas fisik secara rutin** minimal 30 menit per hari
- Mengonsumsi **makanan bergizi seimbang**, kaya serat, dan rendah gula
- Menjaga **berat badan ideal**
- Mengurangi konsumsi makanan olahan dan minuman manis
- Melakukan **pemeriksaan kesehatan secara berkala**

Perubahan kecil yang dilakukan secara konsisten dapat memberikan
dampak besar terhadap kesehatan jangka panjang.
""")


