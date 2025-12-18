import streamlit as st

# ================================
# PAGE CONFIG
# ================================
st.set_page_config(
    page_title="Sistem Prediksi Risiko Diabetes",
    page_icon="🩺",
    layout="centered",
    initial_sidebar_state="expanded"  
)

from utils.ui import set_background

set_background()
# ================================
# SIDEBAR : MENU UTAMA & PETUNJUK
# ================================
with st.sidebar:
    st.markdown("""
    <style>
    .sidebar-title {
        font-size: 1.25rem;
        font-weight: 700;
        color: #0B3C5D;
        margin-bottom: 12px;
    }

    .sidebar-card {
        background: rgba(255,255,255,0.92);
        padding: 14px;
        border-radius: 14px;
        box-shadow: 0 6px 18px rgba(0,0,0,0.06);
        margin-bottom: 18px;
    }

    .sidebar-card ul {
        padding-left: 18px;
        margin-top: 10px;
    }

    .sidebar-card li {
        margin-bottom: 10px;
        font-size: 0.95rem;
        line-height: 1.4;
    }

    .sidebar-card small {
        color: #7F8C8D;
        font-size: 0.82rem;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown(
        '<div class="sidebar-title">📂 Menu Utama</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="sidebar-card">
        <b>🧭 Petunjuk Menu</b>
        <ul>
            <li>
                🩺 <b>Penilaian Risiko Diabetes</b><br>
                <small>Melakukan prediksi risiko berdasarkan data gaya hidup dan kesehatan</small>
            </li>
            <li>
                📘 <b>Edukasi Diabetes</b><br>
                <small>Informasi dasar mengenai diabetes dan faktor risikonya</small>
            </li>
            <li>
                🍎 <b>Rekomendasi Kesehatan</b><br>
                <small>Saran pola hidup sehat sesuai hasil prediksi</small>
            </li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

# ================================
# CUSTOM CSS
# ================================
st.markdown("""
<style>
.welcome-title {
    font-size: 2.9rem;
    font-weight: 800;
    color: #0B3C5D;
    margin-bottom: 6px;
}

.branding {
    font-size: 0.95rem;
    color: #7F8C8D;
    margin-bottom: 26px;
    letter-spacing: 0.4px;
}

.welcome-text {
    font-size: 1.08rem;
    line-height: 1.75;
    color: #34495E;
    margin-bottom: 24px;
}

.card {
    background: #F9FBFD;
    padding: 24px;
    border-radius: 18px;
    box-shadow: 0 10px 28px rgba(0,0,0,0.06);
    margin-top: 28px;
}

.card h4 {
    margin-bottom: 14px;
    color: #2C3E50;
    font-weight: 700;
}

.card ul {
    padding-left: 18px;
}

.card li {
    margin-bottom: 14px;
    font-size: 1rem;
}

.card small {
    color: #6C7A89;
}

.footer {
    margin-top: 42px;
    font-size: 0.85rem;
    color: #95A5A6;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# ================================
# HEADER
# ================================
st.markdown(
    '<div class="welcome-title">🩺 Prediksi Risiko Diabetes</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="branding">'
    'Machine Learning–Based Health Risk Assessment System<br>'
    'Developed by <b>Dian Anjani</b>'
    '</div>',
    unsafe_allow_html=True
)

# ================================
# DESCRIPTION
# ================================
st.markdown("""
<div class="welcome-text">
Aplikasi ini dirancang untuk membantu <b>deteksi dini risiko diabetes</b> dengan memanfaatkan pendekatan <b>Machine Learning</b>.<br><br>

Prediksi dilakukan berdasarkan kombinasi <b>usia, gaya hidup, dan riwayat kesehatan</b>,
sehingga pengguna dapat memperoleh gambaran awal kondisi kesehatannya secara cepat dan praktis,
<b>tanpa memerlukan pemeriksaan laboratorium</b>.
</div>
""", unsafe_allow_html=True)

# ================================
# MENU CARD
# ================================
st.markdown("""
<div class="card">
<h4>📌 Fitur Utama Aplikasi</h4>
<ul>
<li>
<b>🩺 Penilaian Risiko Diabetes</b><br>
<small>
Melakukan analisis dan prediksi tingkat risiko diabetes berdasarkan data kesehatan pengguna.
</small>
</li>

<li>
<b>📘 Edukasi Diabetes</b><br>
<small>
Menyediakan informasi dasar dan pemahaman umum terkait diabetes serta faktor risikonya.
</small>
</li>

<li>
<b>🍎 Rekomendasi Kesehatan</b><br>
<small>
Memberikan saran gaya hidup sehat yang disesuaikan dengan hasil prediksi risiko.
</small>
</li>
</ul>
</div>
""", unsafe_allow_html=True)

# ================================
# CALL TO ACTION
# ================================
st.info(
    "👉 Gunakan menu navigasi untuk mengakses fitur yang tersedia dan mulai melakukan penilaian risiko."
)

# ================================
# FOOTER
# ================================
st.markdown(
    '<div class="footer">© 2025 • Prediksi Risiko Diabetes • Dian Anjani</div>',
    unsafe_allow_html=True
)
