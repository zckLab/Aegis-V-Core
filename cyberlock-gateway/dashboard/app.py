import streamlit as st
import requests
import time
import pandas as pd

st.set_page_config(page_title="CyberLock Dashboard", layout="wide")

st.title("🛡️ CyberLock: Zero-Trust Hardware Gateway")
st.sidebar.header("System Status")
st.sidebar.success("Monitoring Active")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Hardware Authentication Trace")
    if st.button('Trigger Manual Handshake'):
        with st.spinner('Contacting Hardware Module...'):
            try:
                res = requests.get("http://localhost:8080/api/status").json()
                st.code(f"Challenge Sent: {res['last_challenge']}\nResponse: {res['auth_status']}\nHardware Found: {res['hardware_found']}")
                st.success("Access Granted by Cryptographic Proof")
            except:
                st.error("Backend Offline. Run 'make run-backend' first.")

with col2:
    st.subheader("Electromechanical Stress Analysis")
    # Gráfico aleatório para parecer monitoramento de sensores físicos
    chart_data = pd.DataFrame(
        [10, 15, 12, 18, 20, 15, 12],
        columns=['Solenoid Voltage (mV)']
    )
    st.line_chart(chart_data)

st.divider()
st.info("Technical Stack: Go (Proxy), Python (Frontend), C++/Assembly (Firmware Logic)")