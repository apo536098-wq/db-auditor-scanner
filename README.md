# 🛡️ DB-Auditor-Scanner (v1.0.0)

<p align="left">
  <img src="https://img.shields.io/badge/Security-Audit-red?style=flat-square&logo=kali-linux&logoColor=white" alt="Security"/>
  <img src="https://img.shields.io/badge/Language-Python%203-blue?style=flat-square&logo=python&logoColor=white" alt="Language"/>
  <img src="https://img.shields.io/badge/Database-SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white" alt="Database"/>
</p>

An automated, lightweight database security audit engine and relational schema constraint validation scanner. Designed to simulate adversarial database enumeration and validate core integrity rules.

---

## 🛰️ Tactical Core Modules

### 1. Schema Constraint Auditor (Integrity Defense)
* **Dynamic Rule Validation:** Audits `CHECK`, `NOT NULL`, and `PRIMARY KEY` behaviors against the relational model.
* **Exception Interception:** Tests the database engine's resilience against out-of-range payloads (e.g., simulating `CHECK (Sinif IN (1, 2))` boundary failures).

### 2. SQLi Simulation Engine (Vulnerability Assessment)
* **Authentication Bypass Simulation:** Tests input vectors using single-quote logical operations (`' OR '1'='1`).
* **Operational Logging:** Captures and prints raw data leakage tables or system exception trace logs inside the terminal.

---

## 📂 Repository Blueprint

```text
db-auditor-scanner/
├── database_setup.py   # Initializes the relational architecture & testbeds
├── audit_scanner.py    # The core analysis and security auditing script
└── README.md           # Deployment documentation
