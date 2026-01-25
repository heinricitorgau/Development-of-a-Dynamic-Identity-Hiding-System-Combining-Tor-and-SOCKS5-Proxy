# Dynamic Identity-Hiding System (Tor + SOCKS5)

A research-oriented project that implements an automated identity-hiding system by integrating the **Tor anonymity network** with a **SOCKS5 proxy**, enabling controllable IP rotation and quantitative analysis of anonymity-related performance.

This project focuses on **controllability, experimentation, and risk awareness**, rather than claiming absolute anonymity.

---

## Project Overview

As online tracking, censorship, and IP-based blocking become increasingly common, static IP usage poses significant privacy and security risks—especially in scenarios such as:

- Cybersecurity testing  
- Anonymous web crawling  
- Anti-tracking research  

This project designs a **dynamic identity-hiding framework** that allows programs to actively request Tor to rebuild circuits and rotate exit IP addresses using the `NEWNYM` signal via Tor’s ControlPort.

---

## Objectives

- Programmatically control Tor circuit rebuilding using **Tor ControlPort**
- Automate exit IP rotation with **Python + Stem**
- Route traffic through **SOCKS5 (socks5h)** to prevent DNS leaks
- Measure and analyze IP rotation latency using **MATLAB**
- Enhance censorship resistance using **obfs4 pluggable transport**
- Evaluate anonymity limitations and operational risks

---

## System Architecture

MATLAB
↓ (pyenv)
Python (ghost_mode3)
↓ (stem / NEWNYM)
Tor ControlPort (9151)
↓
Tor Network
↓
SOCKS5 Proxy (9150)
↓
External IP Verification API


- **Python** handles low-level Tor control and networking  
- **MATLAB** performs high-level data analysis and visualization  

---

## Key Components

### 1 Tor + ControlPort
- Uses Tor’s `NEWNYM` signal to request new circuits
- Enables **controllable and repeatable** IP rotation experiments

### 2 SOCKS5 Proxy
- Routes traffic via `socks5h://127.0.0.1`
- Ensures DNS queries are also proxied (prevents DNS leaks)

### 3 obfs4 (Pluggable Transport)
- Obfuscates Tor traffic to evade DPI and censorship
- Particularly useful in restricted or monitored networks

### 4 MATLAB Integration
- Python scripts are invoked via MATLAB `pyenv`
- Latency and success rates are analyzed and visualized
- Enables quantitative evaluation of anonymity trade-offs

---

## Experimental Results (Summary)

- Automated IP rotation succeeded with **measurable latency**
- Average IP rotation time: **~9–13 seconds** (environment dependent)
- Exit IPs changed across different countries and ISPs
- Latency variation reflects Tor circuit construction behavior
- Excessive IP switching may reduce reliability due to Tor rate-limiting

---

## Security Considerations & Limitations

This project **does not claim absolute anonymity**.

Potential risks include:
- Traffic correlation attacks
- Protocol and behavior fingerprinting
- Detection due to excessive or regular IP switching
- CAPTCHA or blocking by target websites

**Mitigation strategies**:
- Introduce randomized waiting intervals
- Limit IP switching to necessary operations
- Avoid routing all traffic through Tor unnecessarily

---

## Use Cases

V Suitable for:
- Cybersecurity and anonymity research  
- Anti-tracking experiments  
- Anonymous data collection (controlled environments)  

X Not suitable for:
- Real-time communication
- High-frequency or latency-sensitive services
- Scenarios requiring guaranteed anonymity

---

## Project Structure

.
├── ghost_mode3.py # Main IP rotation script
├── ghost_mode3_data.py # Logging & statistical analysis
├── ghost_mode3_geo.py # Exit IP geolocation analysis
├── anti_tracking_sender.py # Simulated anonymous requests
├── logs/
│ └── *.csv # Experimental results
└── README.md


---

## References

- Tor Project – Tor Manual  
  https://www.torproject.org/docs/tor-manual.html

- Stem – Tor Controller Library  
  https://stem.torproject.org/

- Dingledine et al. (2004). *Tor: The Second-Generation Onion Router*  
  USENIX Security Symposium

- Winter & Lindskog (2012). *How the Great Firewall of China is Blocking Tor*  
  USENIX FOCI

---

## 📄 Disclaimer

This project is intended **for academic research and educational purposes only**.  
Users are responsible for complying with local laws and ethical guidelines when using anonymity technologies.

---

## 👤 Author

**Gao En-Zai**  
Department of Computer Science  
Academic Year 114
