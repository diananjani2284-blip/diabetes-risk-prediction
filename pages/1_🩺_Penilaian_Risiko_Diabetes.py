# ================================
# 1_🩺_Penilaian_Risiko_Diabetes.py
# ================================
import streamlit as st
import joblib
import pandas as pd
import numpy as np
import base64
import pickle
from utils.ui import set_background
set_background()

from datetime import datetime

# -------------------------------
# SESSION STATE (RIWAYAT)
# -------------------------------
if "prediction_history" not in st.session_state:
    st.session_state.prediction_history = []

# -------------------------------
# LOAD MODEL & ENCODER
# -------------------------------
MODEL_PATH = "model/full_diabetes_pipeline.pkl"
ENCODER_PATH = "model/target_encoders.pkl"

model = joblib.load(MODEL_PATH)

with open(ENCODER_PATH, "rb") as f:
    encoders = pickle.load(f)

target_encoder = encoders["diabetes_stage"]

# -------------------------------
# UI HEADER
# -------------------------------
st.title("🩺 Prediksi Risiko Diabetes")

st.markdown(""" 
Cukup isi data sederhana **tanpa pemeriksaan laboratorium**.
""")

# -------------------------------
# FORM INPUT USER
# -------------------------------
with st.form("form_diabetes"):
    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("Usia", min_value=10, max_value=100, value=30)
        gender = st.selectbox("Jenis Kelamin", ["Male", "Female"])

        berat = st.number_input(
            "Berat Badan (kg)",
            min_value=20.0,
            max_value=200.0,
            value=60.0
        )

        tinggi = st.number_input(
            "Tinggi Badan (cm)",
            min_value=100.0,
            max_value=220.0,
            value=165.0
        )

    # ======================
    # HITUNG BMI OTOMATIS
    # ======================
    bmi = round(berat / ((tinggi / 100) ** 2), 2)

    st.caption(
    f"📐 BMI otomatis dihitung: **{bmi}** — "
    "BMI (Body Mass Index) digunakan untuk menilai kategori berat badan berdasarkan tinggi dan berat badan."
)

    # ======================
    # KATEGORI BMI
    # ======================
    if bmi < 18.5:
        st.caption("🔍 Kategori BMI: Kurus")
    elif bmi < 25:
        st.caption("🔍 Kategori BMI: Normal")
    elif bmi < 30:
        st.caption("🔍 Kategori BMI: Overweight")
    else:
        st.caption("🔍 Kategori BMI: Obesitas")

    # ======================
    # INPUT LANJUTAN
    # ======================
    smoking_status = st.selectbox("Status Merokok", ["Never", "Former", "Current"])

    family_history = st.selectbox(
        "Riwayat Keluarga Diabetes",
        options=[0, 1],
        format_func=lambda x: "No" if x == 0 else "Yes"
    )

    with col2:
        alcohol = st.number_input("Konsumsi Alkohol / Minggu", min_value=0, max_value=50, value=0)
        activity = st.number_input("Aktivitas Fisik (menit/minggu)", min_value=0, max_value=1000, value=150)
        employment = st.selectbox("Status Pekerjaan", ["Employed", "Unemployed", "Retired", "Student"])
        diet_score = st.slider("Skor Pola Makan (1 = buruk, 10 = sehat)", 1.0, 10.0, 6.0)

    submitted = st.form_submit_button("🔍 Prediksi Risiko")

# -------------------------------
# PREDIKSI
# -------------------------------
if submitted:
    input_df = pd.DataFrame([{
        "Age": age,
        "gender": gender,
        "bmi": bmi,
        "smoking_status": smoking_status,
        "alcohol_consumption_per_week": alcohol,
        "physical_activity_minutes_per_week": activity,
        "family_history_diabetes": family_history, 
        "employment_status": employment,
        "diet_score": diet_score
    }])

    pred_class = model.predict(input_df)[0]
    pred_label = target_encoder.inverse_transform([pred_class])[0]

    # ---------------------------
    # SIMPAN RIWAYAT PREDIKSI
    # ---------------------------
    st.session_state.prediction_history.append({
        "Waktu": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "Usia": age,
        "Jenis Kelamin": gender,
        "BMI": bmi,
        "Merokok": smoking_status,
        "Alkohol/Minggu": alcohol,
        "Aktivitas (menit/minggu)": activity,
        "Riwayat Keluarga": "Yes" if family_history == 1 else "No",
        "Status Pekerjaan": employment,
        "Skor Pola Makan": diet_score,
        "Hasil Prediksi": pred_label,
    })

    # ---------------------------
    # OUTPUT UI
    # ---------------------------
    if pred_label == "No Diabetes":
        status_title = "Status Baik"
        status_icon = "✅"
        box_color = "#E8FFF1"
        border_color = "#2ECC71"
        message = (
            "Pertahankan gaya hidup sehat dan lakukan pemeriksaan rutin "
            "tahunan untuk memantau kondisi kesehatan Anda."
        )
    else:
        status_title = "Perlu Perhatian"
        status_icon = "⚠️"
        box_color = "#FFF6E5"
        border_color = "#F39C12"
        message = (
            "Disarankan untuk mulai memperbaiki pola hidup, menjaga pola makan, "
            "meningkatkan aktivitas fisik, dan berkonsultasi dengan tenaga medis."
        )

    st.markdown("## 🎉 **Prediksi Risiko Diabetes Anda**")

    if pred_label == "No Diabetes":
        st.success("🟢 Prediksi Risiko Rendah")
    else:
        st.warning("🟡 Prediksi Risiko Tinggi")

    st.markdown(
        f"""
        <div style="
            background-color:#EAFBF3;
            padding:25px;
            border-radius:12px;
            text-align:center;
            margin-top:15px;
            margin-bottom:15px;
        ">
            <h2 style="color:#1E8449; margin-bottom:5px;">{pred_label}</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div style="
            background-color:{box_color};
            border-left:6px solid {border_color};
            padding:18px;
            border-radius:10px;
            margin-top:15px;
        ">
            <h4>{status_icon} {status_title}</h4>
            <p style="margin-top:8px;">{message}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.info("Hasil ini merupakan **prediksi risiko awal**, bukan diagnosis medis.")

    # ---------------------------
    # RIWAYAT & EKSPOR DATA
    # ---------------------------
    st.markdown("## 🗂️ Riwayat Prediksi")

    df_history = pd.DataFrame(st.session_state.prediction_history)

    st.dataframe(df_history, use_container_width=True)

    col_export1, col_export2 = st.columns(2)

    with col_export1:
        st.download_button(
            "⬇️ Ekspor Riwayat (CSV)",
            df_history.to_csv(index=False),
            "riwayat_prediksi_diabetes.csv",
            "text/csv"
        )

    with col_export2:
        if st.button("🗑️ Hapus Riwayat"):
            st.session_state.prediction_history = []
            st.success("Riwayat prediksi berhasil dihapus.")


