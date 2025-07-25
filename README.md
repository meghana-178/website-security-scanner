# Placeholder for README.md
# 🔐 Website Security Scanner

A simple Flask-based web application to analyze basic website security parameters like HTTPS support, SSL certificate validity, security headers, and domain info.

## 🚀 Features
- ✅ Checks if HTTPS is enabled
- 🔐 Validates SSL certificate
- 📦 Extracts security headers (`HSTS`, `CSP`, `X-Frame-Options`)
- 🌍 Pulls domain details using WHOIS (creation, expiration, registrar)

## 🖥️ Tech Stack
- Python 3.x
- Flask
- Bootstrap (CDN)
- requests + whois module

## 🧪 Sample Scan
![screenshot](C:\Users\MEGHANA\Downloads\website-security-scanner\app\templates\scan-result.png)

## 🛠️ Installation
```bash
git clone https://github.com/meghana-178/website-security-scanner.git
cd website-security-scanner
pip install -r requirements.txt
python run.py
