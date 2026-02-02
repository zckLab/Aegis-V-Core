# 🛡️ AEGIS-V: Hardware-Enforced Security Mesh

[![Backend-Go](https://img.shields.io/badge/Backend-Go--Gin-00ADD8?style=for-the-badge&logo=go)](https://gin-gonic.com/)
[![Frontend-Python](https://img.shields.io/badge/Frontend-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit)](https://streamlit.io/)
[![Hardware-Assembly](https://img.shields.io/badge/Hardware-AVR--Assembly-white?style=for-the-badge&logo=microchip)](https://github.com/)

**AEGIS-V** is a high-integrity security gateway that implements **Clean Architecture** to bridge high-level cloud dashboards with low-level hardware root-of-trust.

---

## 📖 Project Overview

Modern security often fails because it stays strictly in the software layer. AEGIS-V moves the "Secret" to a physical **Smart Endpoint**. Using a **Dumb Pipe** philosophy for communication, the system ensures that business rules and cryptographic decisions are made at the edges (Hardware and Core Logic), keeping the transmission layer simple and secure.

### How it Works:
1. **The User** triggers a request via the **Python SOC Dashboard**.
2. **The Go Gateway** (using Gin) acts as an Interface Adapter, converting the request into a cryptographic challenge.
3. **The Hardware (Smart Producer)** receives the challenge, processes it via an **Assembly Cipher**, and decides if the physical lock (Solenoid) should be actuated.
4. **Clean Architecture** ensures that the core security rules are decoupled from the frameworks, allowing the system to run on different hardwares or cloud providers seamlessly.

---

## 🏗️ System Architecture

Our implementation follows the **Clean Architecture** circles to ensure maintainability and security:

- **Entities**: Pure Domain Objects representing sensor measurements and security states.
- **Use Cases**: Physical simulation logic and anomaly detection criteria.
- **Interface Adapters**: Go Gin routes and Python Streamlit connectors that translate external data to the Core.
- **Frameworks & Drivers**: The actual Hardware (ATmega328P), SQL/NoSQL databases, and the HTTP engine.

---

## 📸 Visual Showcase

### 1. General System Schematic
![GSS](Aegis-V-Core/assets/GSS.png)
> **Description:** A global view of the interaction between Clean Architecture layers and physical electromechanical components.

### 2. Operational SOC Dashboard
![OSD](Aegis-V-Core/assets/OSD.png)
> **Description:** Main interface for the Security Operations Center, featuring dark-mode industrial aesthetics.

### 3. Hardware Telemetry & Entropy Analysis
![HTEA](Aegis-V-Core/assets/HTEA.png)
> **Description:** Real-time Plotly charts monitoring hardware signal stability and side-channel entropy.

### 4. Core Module Matrix (Features)
![Demo do site](Aegis-V-Core/assets/demo.gif)
> **Description:** Dynamic feature matrix showcasing the integration of C++, Assembly, Go, and Python modules.

---

## 🔧 Installation Manual

### 1. Hardware Setup (Firmware)
- **Location**: `core-firmware/src/`
- **Instructions**: Flash `main.cpp` and `cipher.S` to your microcontroller using PlatformIO or Arduino IDE.
- **Pinout**: Digital Pin 12 (PB4) for Solenoid/MOSFET control.

### 2. Backend Engine (Go)
The engine manages the "Smart Endpoint" logic and security proxying.
```bash
cd gateway-proxy
go mod tidy
go run main.go
```
### 3. Frontend SOC (Python)
The dashboard for real-time monitoring and command execution.
```bash
cd soc-dashboard
pip install -r requirements.txt
streamlit run app.py
```

### 🛠️ Implementation Details
- **Zero-Trust:** No request is trusted without a physical hardware handshake.
- **Concurrency:** Go routines manage multiple hardware nodes simultaneously.
- **Low-Level Mastery:** Cryptographic rounds implemented in **AVR Assembly** to prevent side-channel timing attacks.
- **Electromechanics:**  Real-time MOSFET thermal tracking and solenoid pulse-width modulation (PWM).

### 👤 Author
Developed by **zckLab**

_"Securing the digital world by anchoring it in the physical reality."_
