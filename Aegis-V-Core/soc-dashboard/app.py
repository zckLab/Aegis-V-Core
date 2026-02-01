import streamlit as st
import requests
import pandas as pd
import plotly.graph_objects as go
import time
from crypto_utils import AegisCrypto

st.set_page_config(page_title="AEGIS-V | CORE", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&family=JetBrains+Mono&display=swap');
    
    html, body, [data-testid="stAppViewContainer"] {
        background-color: #000000;
        color: #ffffff;
        font-family: 'Inter', sans-serif;
    }
    
    footer {visibility: hidden;}
    [data-testid="stHeader"] {background: rgba(0,0,0,0);}

    .hero-title {
        font-size: 80px; font-weight: 800; text-align: center;
        background: linear-gradient(180deg, #ffffff 40%, #222 100%);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        letter-spacing: -4px; margin-bottom: 0px;
    }

    /* Infinite Carrossel */
    @keyframes scroll {
        0% { transform: translateX(0); }
        100% { transform: translateX(calc(-250px * 5)); }
    }
    .slider {
        background: transparent;
        height: 300px; margin: auto; overflow: hidden;
        position: relative; width: 100%;
    }
    .slider::before, .slider::after {
        background: linear-gradient(to right, #000 0%, rgba(0,0,0,0) 100%);
        content: ""; height: 300px; position: absolute; width: 200px; z-index: 2;
    }
    .slider::after { right: 0; top: 0; transform: rotateZ(180deg); }
    .slider::before { left: 0; top: 0; }
    .slide-track {
        animation: scroll 30s linear infinite;
        display: flex; width: calc(250px * 10);
    }
    .slide {
        background: rgba(255,255,255,0.02);
        border: 1px solid rgba(255,255,255,0.05);
        border-radius: 20px; margin: 10px;
        height: 250px; width: 250px;
        padding: 20px; transition: 0.3s;
        flex-shrink: 0;
    }
    .slide:hover { border-color: #00ff41; background: rgba(0,255,65,0.02); }
    .slide img { width: 50px; margin-bottom: 15px; filter: grayscale(1) invert(1); }

    .stButton>button {
        background: #ffffff; color: #000; border-radius: 50px;
        padding: 15px 50px; font-weight: 800; border: none;
        transition: 0.4s; display: block; margin: 0 auto;
    }
    .stButton>button:hover { transform: scale(1.05); box-shadow: 0 0 50px rgba(255,255,255,0.1); }

    .log-box {
        background: rgba(10,10,10,0.8); border: 1px solid #1a1a1a;
        border-radius: 15px; padding: 20px; font-family: 'JetBrains Mono';
        font-size: 12px; color: #444; height: 380px; overflow-y: auto;
    }
    .neon-text { color: #00ff41; text-shadow: 0 0 10px rgba(0,255,65,0.5); }
    </style>
    """, unsafe_allow_html=True)

if 'logs' not in st.session_state: st.session_state.logs = []
if 'crypto' not in st.session_state: st.session_state.crypto = AegisCrypto(None)

api_active = False
try: 
    if requests.get("http://127.0.0.1:8080/api/health", timeout=0.2).status_code == 200: api_active = True
except: pass

st.markdown("<h1 class='hero-title'>Aegis-V Core</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#555; font-size:20px; margin-bottom:40px;'>High-Performance Hardware Security Mesh</p>", unsafe_allow_html=True)

if st.button("ENTER THE MCP ENGINE"):
    try:
        res = requests.get("http://127.0.0.1:8080/unlock", headers={"X-Aegis-Signature": st.session_state.crypto.get_signature()})
        if res.status_code == 200:
            data = res.json()
            st.session_state.last_res = data
            st.session_state.logs.append(f"[{time.strftime('%H:%M:%S')}] AUTH_GRANTED: {data['core']}")
            st.toast("Access Authorized")
    except: st.error("Engine Offline")

st.write("###")


features = [
    ("https://cdn-icons-png.flaticon.com/512/2092/2092663.png", "C++ Core", "Low-level bit manipulation."),
    ("https://cdn-icons-png.flaticon.com/512/6124/6124995.png", "Assembly", "Otimized cipher rounds."),
    ("https://cdn-icons-png.flaticon.com/512/2592/2592317.png", "MOSFET", "PWM Gate control monitoring."),
    ("https://cdn-icons-png.flaticon.com/512/2716/2716612.png", "C-Security", "Zero-Trust Protocol."),
    ("https://cdn-icons-png.flaticon.com/512/919/919853.png", "Go Engine", "High-concurrency proxy.")
]
slide_html = "".join([f"<div class='slide'><img src='{img}'><h4>{title}</h4><p style='color:#555;font-size:12px;'>{desc}</p></div>" for img, title, desc in features*2])
st.markdown(f"<div class='slider'><div class='slide-track'>{slide_html}</div></div>", unsafe_allow_html=True)

st.write("---")


if api_active:
    col_left, col_right = st.columns([2, 1])
    
    with col_left:
        st.markdown("### 📡 Live Entropy Spectrum")
        metrics = requests.get("http://127.0.0.1:8080/api/metrics").json()
        fig = go.Figure()
        fig.add_trace(go.Scatter(y=metrics, fill='tozeroy', line=dict(color='#00ff41', width=2), fillcolor='rgba(0,255,65,0.05)'))
        fig.update_layout(
            paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
            margin=dict(l=0, r=0, t=0, b=0), height=380,
            xaxis=dict(showgrid=False, visible=False), 
            yaxis=dict(showgrid=True, gridcolor="#111", color="#444", range=[0, 100]),
            dragmode='zoom' # Habilita zoom
        )
        st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': True, 'modeBarButtonsToRemove': ['select2d', 'lasso2d']})
        st.caption("Pinch to zoom. Use the camera icon to reset view.")

    with col_right:
        st.markdown(f"### ⚙️ {st.session_state.get('last_res', {}).get('node', 'Standby Node')}")
        st.markdown("<div class='log-box'>", unsafe_allow_html=True)
        if 'last_res' in st.session_state:
            st.markdown(f"<p class='neon-text'>● STATUS: AUTHORIZED</p>", unsafe_allow_html=True)
            st.markdown(f"<p style='color:#888;'>LOAD: {st.session_state.last_res['load']}</p>", unsafe_allow_html=True)
        
        log_html = "".join([f"<div style='margin-bottom:5px;'>{l}</div>" for l in st.session_state.logs[::-1]])
        st.markdown(f"<div style='margin-top:20px;'>{log_html}</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
else:
    st.markdown("<div style='text-align:center; padding:100px; border:1px solid #111; border-radius:30px; color:#333;'>WAITING FOR AEGIS-V ENGINE...</div>", unsafe_allow_html=True)