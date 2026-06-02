# 🛡️ DB-Auditor-Scanner (v1.1.0)

<p align="center">
  <img src="https://img.shields.io/badge/Security_Level-Tactical_SOC-red?style=for-the-badge&logo=kali-linux&logoColor=white" alt="SOC Status"/>
  <img src="https://img.shields.io/badge/Core_Engine-Python_3.11-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python Engine"/>
  <img src="https://img.shields.io/badge/Storage-SQLite3-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="Database"/>
</p>

<p align="center">
  <b>An automated database security audit suite, schema constraint enforcement engine, and reactive cyber threat log parser.</b>
</p>

---

## ⚡ System Architecture & Data Flow



Proje, ilişkisel veritabanı bütünlük kurallarını (Relational Integrity Constraints) siber zafiyet test modelleriyle birleştiren hibrit bir yapıya sahiptir. Süreç akışı şu şekildedir:

```text
  [ Network Traffic ] ──► [ log_analyzer.py ] ──► ( Regex Inspection Engine )
                                                          │
   ┌──────────────────────────────────────────────────────┴─────────┐
   ▼ (Malicious Payloads)                                           ▼ (Valid Operations)
[ SecurityLogs Table ]                                      [ database_setup.py ]
   │                                                                │
   ▼                                                                ▼
[ Threat Telemetry ] ◄── [ audit_scanner.py ] ◄────────────── [ cyber_university.db ]
                      (Constraint / SQLi Auditing)
