# 📡 [SYSTEM ACCESS: GRANTED] // CODE: DB-AUDITOR-SCANNER

<p align="center">
  <img src="https://blog.malwarebytes.com/wp-content/uploads/2018/10/network-recon-gif.gif" width="100%" alt="Cyber Security Operations Center Stream"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Security_Level-Tactical_SOC-red?style=for-the-badge&logo=kali-linux&logoColor=white" alt="SOC Status"/>
  <img src="https://img.shields.io/badge/Core_Engine-Python_3.11-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python Engine"/>
  <img src="https://img.shields.io/badge/Storage-SQLite3-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="Database"/>
</p>

---

## ⚡ TARGET SYSTEM ARCHITECTURE & EXPLOIT FLOW

```text
 [ INCOMING NETWORK TRAFFIC ]
             │
             ▼
   [ log_analyzer.py ] ───( REGEX SIGNATURE ENGINE )───┐
             │                                         │
             ├─► [MATCH: MALICIOUS PAYLOAD]            ├─► [MATCH: COMPLIANT TRAFFIC]
             │   (Classification: HIGH/MEDIUM)         │   (Classification: LOW)
             ▼                                         ▼
   { SecurityLogs Telemetry }                 { database_setup.py }
             │                                         │
             │                                         ▼
             └─────────────────────────────────► [ cyber_university.db ]



🛰️ RECONNAISSANCE & TACTICAL CORE MODULES
🎛️ MODULE 0x01 // Relational Schema Auditor (audit_scanner.py)
INTEGRITY-CHECK: CHECK, NOT NULL ve PRIMARY KEY kısıtlamalarını programatik olarak test eder.

CONSTRAINT-BYPASS-TEST: CHECK (Sinif IN (1, 2)) kuralını ihlal eden Class: 3 gibi geçersiz girdiler göndererek sistemin fırlattığı IntegrityError çıktılarını yakalar.

🎛️ MODULE 0x02 // SQLi Adversarial Simulator (audit_scanner.py)
AUTH-BYPASS-VECTOR: Tek tırnak manipülasyonu kullanarak mantıksal kimlik doğrulama bypass adımlarını (' OR '1'='1) simüle eder.

DATA-LEAK-MAPPER: Input validation (girdi doğrulama) kırıldığında oluşan sızıntıları terminale döker.

🎛️ MODULE 0x03 // Threat Log Intelligence Parser (log_analyzer.py)
SIGNATURE-DETECTION: Ağ günlüklerindeki UNION, -- ve zararlı SQL enjeksiyon izlerini imza tabanlı regex ile tarar.

💻 DEPLOYMENT & CORE INJECTION VECTORS (KALI LINUX)
Bash
python3 database_setup.py
python3 audit_scanner.py
python3 log_analyzer.py
📊 LIVE TERMINAL TELEMETRY // SOC OPERATIONS STREAM
Kod snippet'i
[=] ADIM 1: VERİTABANI KISITLAMA DENETİMİ BAŞLADI [=]
[✅ GÜVENLİ] Veritabanı CHECK kısıtlaması ihlali yakaladı: CHECK constraint failed: Ogrenci

[=] ADIM 2: SQL INJECTION TACTICAL SCAN [=]
[*] Test Edilen Girdi: Kadir' OR '1'='1
[(1, 'Kadir', 2), (2, 'Murat', 1), (3, 'Elif', 2)]

---

## 🚀 QUICK START // HOW TO RUN THIS SUITE

If you want to pull this automated security engine and run it inside your local Kali Linux machine, execute these commands sequentially in your terminal:

```bash
# 1. Clone the secure repository directly to your workspace
git clone [https://github.com/apo536098-wq/db-auditor-scanner.git](https://github.com/apo536098-wq/db-auditor-scanner.git)

# 2. Enter the active deployment directory
cd db-auditor-scanner

# 3. Fire up the relational base setup, the scanner, and the log intelligence system
python3 database_setup.py && python3 audit_scanner.py && python3 log_analyzer.py
