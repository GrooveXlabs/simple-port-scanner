<div align="center">

<!-- Animated Typing Header -->
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=24&duration=2500&pause=700&color=00D4FF&center=true&vCenter=true&width=500&lines=GrooveXlabs+Port+Scanner;TCP+Recon+for+Learning" alt="Typing Animation" />

<br>

<!-- Cyberpunk Banner -->
<img src="https://capsule-render.vercel.app/api?type=venom&color=0:0f0c29,50:302b63,100:24243e&height=150&section=header&text=Simple%20Port%20Scanner&fontSize=35&fontColor=00d4ff&animation=fadeIn&fontAlignY=55&desc=Educational%20TCP%20port%20scanner%20written%20in%20Python&descSize=14&descAlignY=75&descColor=a8a8b3" width="100%" />

<br><br>

<!-- Badges -->
<a href="https://github.com/GrooveXlabs/simple-port-scanner">
  <img src="https://img.shields.io/badge/🔒%20Security-First-ff006e?style=for-the-badge&labelColor=0f0c29" />
</a>
<a href="https://github.com/GrooveXlabs/simple-port-scanner">
  <img src="https://img.shields.io/badge/🐍%20Python-3.10+-3776AB?style=for-the-badge&labelColor=0f0c29" />
</a>
<a href="https://github.com/GrooveXlabs/simple-port-scanner">
  <img src="https://img.shields.io/badge/🎓%20Educational-Only-ea4335?style=for-the-badge&labelColor=0f0c29" />
</a>
<a href="LICENSE">
  <img src="https://img.shields.io/badge/📜%20License-MIT-00d4ff?style=for-the-badge&labelColor=0f0c29" />
</a>

<br><br>

<!-- Divider -->
<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png" width="100%" />

</div>

## 🔍 Overview

**GrooveXlabs Simple Port Scanner** is a lightweight, educational TCP port scanner written in Python. It helps you understand network reconnaissance basics by scanning a range of ports on a target host to identify which services are listening.

> ⚠️ **For educational and authorized testing only.** Always obtain explicit permission before scanning any network or host you do not own.

---

## ✨ Features

- 🎯 **Single & Range Scanning** — Scan individual ports or full ranges (1–65535)
- ⚡ **Fast Timeouts** — 0.5s socket timeout for responsive feedback
- 🖥️ **Interactive CLI** — Simple prompts for host and port range
- 🛡️ **Input Validation** — Sanitizes port ranges and prevents invalid input
- 📋 **Clean Output** — Clearly lists all open ports found

---

## 🚀 Quick Start

```bash
# Clone the repo
git clone https://github.com/GrooveXlabs/simple-port-scanner.git
cd simple-port-scanner

# Run the scanner
python port_scanner.py
```

**Example:**
```bash
$ python port_scanner.py
=== Groovexlabs Simple Port Scanner ===

Enter host to scan (e.g. 127.0.0.1 or scanme.nmap.org): scanme.nmap.org
Enter start port (e.g. 1): 20
Enter end port (e.g. 1024): 25

Scanning scanme.nmap.org from port 20 to 25...

[+] Port 22 is OPEN

Scan complete. Open ports:
- 22
```

---

## 📁 File Structure

```
simple-port-scanner/
├── port_scanner.py    # Main scanner logic
├── README.md          # This file
└── LICENSE            # MIT License
```

---

## 🛡️ How It Works

```
┌─────────────┐     ┌──────────────┐     ┌─────────────────┐
│   Input     │────→│  TCP Socket  │────→│  Timeout/Result  │
│ Host + Port │     │  Connection  │     │  Open / Closed   │
└─────────────┘     └──────────────┘     └─────────────────┘
```

1. Creates a TCP socket (`socket.AF_INET`, `socket.SOCK_STREAM`)
2. Sets a 0.5-second timeout to avoid hanging
3. Attempts to connect to each port in the range
4. Prints open ports and summarizes results

---

## 🧠 Learning Path

1. **Run it locally** — Scan `127.0.0.1` to see your own services
2. **Try scanme.nmap.org** — A safe, authorized target for practice
3. **Read the code** — Understand sockets, timeouts, and exception handling
4. **Extend it** — Add banner grabbing, multithreading, or Nmap-style output

---

## ⚠️ Legal & Ethical Use

> This tool is intended for **educational purposes** and **authorized security testing only**.
> 
> - ✅ Scan your own machines and networks
> - ✅ Use `scanme.nmap.org` for safe practice
> - ❌ Never scan networks without explicit written permission
> - ❌ Do not use this tool for malicious purposes

**GrooveXlabs is not responsible for misuse of this tool.**

---

## 🗺️ Related GrooveXlabs Projects

| Repository | Description |
|---|---|
| [GrooveXlabs](https://github.com/GrooveXlabs/GrooveXlabs) | Password Strength Analyzer |
| [security-notes](https://github.com/GrooveXlabs/security-notes) | Curated cybersecurity learning notes |
| [redtrack](https://github.com/GrooveXlabs/redtrack) | Red Team Recon & Attack Path Mapping |

---

## 🤝 Contributing

PRs welcome! Ideas for improvement:
- Multithreading / async scanning for speed
- Service banner grabbing
- Output formats (JSON, CSV)
- SYN stealth scanning

---

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.

---

<div align="center">

<br>

<sub>🔒 Built with security in mind. Open source by conviction.</sub>
<br>
<sub>Maintained by <strong>GrooveXlabs</strong></sub>

</div>
