import streamlit as st
import requests
import pandas as pd
import plotly.graph_objects as go
import time
from crypto_utils import AegisCrypto

st.set_page_config(page_title="AEGIS-V | CORE", layout="wide")

# CSS Avançado para Centralização e Estética Stealth
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;700;900&family=JetBrains+Mono&display=swap');
    
    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"] { 
        background-color: #000000 !important; 
        color: #ffffff !important; 
        font-family: 'Inter', sans-serif; 
    }

    .micro-line {
        width: 100%; height: 1px; 
        background: linear-gradient(90deg, rgba(255,255,255,0) 0%, rgba(255,255,255,0.1) 50%, rgba(255,255,255,0) 100%);
        margin: 10px 0;
    }

    .hero-title { 
        font-size: 80px; font-weight: 900; text-align: center; 
        background: linear-gradient(180deg, #ffffff 40%, #111 100%); 
        -webkit-background-clip: text; -webkit-text-fill-color: transparent; 
        letter-spacing: -5px; margin-bottom: 0;
    }

    /* Centralização Absoluta do Botão */
    .stButton { display: flex; justify-content: center; }
    .stButton>button { 
        background: #ffffff !important; color: #000000 !important; 
        border-radius: 2px !important; padding: 20px 80px !important; 
        font-weight: 800 !important; border: none !important; 
        text-transform: uppercase; transition: 0.4s;
    }
    .stButton>button:disabled { background: #111 !important; color: #333 !important; }

    /* Carrossel */
    @keyframes scroll { 0% { transform: translateX(0); } 100% { transform: translateX(calc(-300px * 5)); } }
    .slider { background: transparent; height: 350px; overflow: hidden; position: relative; width: 100%; }
    .slide-track { animation: scroll 40s linear infinite; display: flex; width: calc(300px * 10); }
    .slide { 
        background: rgba(255,255,255,0.01); border: 1px solid rgba(255,255,255,0.05); 
        border-radius: 4px; margin: 10px; height: 280px; width: 280px; 
        padding: 30px; flex-shrink: 0;
    }
    .slide img { width: 45px; height: 45px; margin-bottom: 20px; filter: brightness(2); }

    .log-box { 
        background: #050505; border: 1px solid #111; padding: 20px; 
        font-family: 'JetBrains Mono'; font-size: 11px; color: #444; 
        height: 400px; overflow-y: auto; 
    }
    </style>
    """, unsafe_allow_html=True)

# Lógica de Estado
if 'logs' not in st.session_state: st.session_state.logs = []
if 'last_handshake' not in st.session_state: st.session_state.last_handshake = 0

# Verificação de API
api_active = False
try:
    if requests.get("http://127.0.0.1:8080/api/health", timeout=0.2).status_code == 200:
        api_active = True
except: pass

st.markdown("<div class='micro-line'></div>", unsafe_allow_html=True)
st.markdown("<h1 class='hero-title'>AEGIS-V CORE</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#333; font-size:10px; letter-spacing:10px;'>SECURE HARDWARE INFRASTRUCTURE</p>", unsafe_allow_html=True)
st.markdown("<div class='micro-line'></div>", unsafe_allow_html=True)

st.write("###")

# Botão Centralizado com Trava de Segurança
btn_label = "Initialize MCP Handshake" if api_active else "System Offline - Backend Required"
if st.button(btn_label, disabled=not api_active):
    current_time = time.time()
    # Previne spam (1 handshake a cada 2 segundos)
    if current_time - st.session_state.last_handshake > 2:
        try:
            crypto = AegisCrypto(None)
            res = requests.get("http://127.0.0.1:8080/unlock", headers={"X-Aegis-Signature": crypto.get_signature()})
            if res.status_code == 200:
                data = res.json()
                st.session_state.last_res = data
                st.session_state.logs.append(f"[{time.strftime('%H:%M:%S')}] ACCESS_GRANTED: {data['core']}")
                st.session_state.last_handshake = current_time
                st.toast("Handshake Success", icon="🔒")
        except: st.error("Fatal: Connection Lost")
    else:
        st.toast("Rate Limit: Wait 2s", icon="⏳")

st.write("###")

# Carrossel com Ícones Corretos (Linguagens + Frameworks)
# Usando ícones da DevIcon para precisão
features = [
    ("https://raw.githubusercontent.com/devicons/devicon/master/icons/cplusplus/cplusplus-original.svg", "C++ CORE", "Register-level port manipulation and register-level scheduling."),
    ("https://cdn-icons-png.flaticon.com/512/2103/2103633.png", "ASSEMBLY", "Handshake encryption rounds optimized for AVR architecture."),
    ("https://raw.githubusercontent.com/devicons/devicon/master/icons/go/go-original.svg", "GO / GIN", "High-concurrency proxy gateway using the GIN framework."),
    ("https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg", "PYTHON / ST", "Reactive SOC dashboard built with Streamlit and Plotly."),
    ("https://cdn-icons-png.flaticon.com/512/3655/3655573.png", "HARDWARE", "Real-time monitoring of power-MOSFET electromechanical drive.")
]
slide_html = "".join([f"<div class='slide'><img src='{img}'><h3>{t}</h3><p style='color:#444; font-size:13px;'>{d}</p></div>" for img, t, d in features*2])
st.markdown(f"<div class='slider'><div class='slide-track'>{slide_html}</div></div>", unsafe_allow_html=True)

if api_active:
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown("### LIVE ENTROPY SPECTRUM")
        metrics = requests.get("http://127.0.0.1:8080/api/metrics").json()
        fig = go.Figure()
        fig.add_trace(go.Scatter(y=metrics, fill='tozeroy', line=dict(color='#00ff41', width=2), fillcolor='rgba(0,255,65,0.05)'))
        fig.update_layout(
            paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', 
            margin=dict(l=0,r=0,t=0,b=0), height=400, 
            xaxis=dict(showgrid=True, gridcolor="#111", visible=True), 
            yaxis=dict(showgrid=True, gridcolor="#111", visible=True, range=[0, 100])
        )
        st.plotly_chart(fig, use_container_width=True)
    with c2:
        st.markdown(f"### {st.session_state.get('last_res', {}).get('node', 'NODE_STANDBY')}")
        st.markdown("<div class='log-box'>", unsafe_allow_html=True)
        if 'last_res' in st.session_state:
            st.markdown(f"<p style='color:#00ff41; font-weight:900;'>● STATUS: AUTHORIZED</p>", unsafe_allow_html=True)
        logs_html = "".join([f"<div style='margin-bottom:5px;'>{l}</div>" for l in st.session_state.logs[::-1]])
        st.markdown(f"<div>{logs_html}</div></div>", unsafe_allow_html=True)
else:
    st.markdown("<div style='text-align:center; padding:100px; border:1px solid #111; border-radius:4px; color:#222;'>OFFLINE: INITIALIZE BACKEND TO START TELEMETRY</div>", unsafe_allow_html=True)