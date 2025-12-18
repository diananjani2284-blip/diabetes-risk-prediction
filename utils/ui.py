import streamlit as st

def set_background():
    st.markdown("""
    <style>
    /* Background utama */
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(
            135deg,
            #EAF4FF 0%,
            #FDFEFF 50%,
            #F1F7FD 100%
        );
        font-family: 'Segoe UI', system-ui, -apple-system, BlinkMacSystemFont, sans-serif;
    }

    /* Container konten */
    .block-container {
        padding-top: 2.5rem;
        padding-bottom: 2rem;
    }

    /* Judul utama */
    h1, h2, h3 {
        color: #0B3C5D;
        font-weight: 700;
    }

    /* Paragraf */
    p, li, span {
        color: #2C3E50;
        line-height: 1.7;
    }

    /* Card umum */
    .custom-card {
        background: rgba(255,255,255,0.92);
        padding: 22px;
        border-radius: 16px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.06);
        margin-bottom: 20px;
    }

    /* Info box Streamlit */
    div[data-testid="stAlert"] {
        border-radius: 12px;
    }
    </style>
    """, unsafe_allow_html=True)
