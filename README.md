# Enterprise Applied Analytics Pipeline (Python & SQLite)

An end-to-end data engineering pipeline designed to ingest, clean, and analyze distributed customer transactional data. This project implements modular engineering principles, parameterized relational queries to calculate key performance indicators (KPIs), and automated testing architectures to guarantee data integrity and security.

## 🛠️ Architecture & Core Features
- **ETL Ingestion Engine (`src/etl_load_sqlite.py`):** Automatically extracts multi-source relational records from flat files (`customers_raw.csv`), applies schema validation, and structures it into a transactional SQLite database layer.
- **Parametric KPI Engine (`src/kpi_city.py`):** Dynamically computes cross-sectional performance metrics localized by city hubs. Built explicitly with parameterized interfaces to optimize query execution and eliminate vulnerabilities.
- **Robust Testing & Security Framework (`tests/test_kpi_city.py`):** Orchestrates robust verification suites utilizing `pytest`. Includes regression testing for operational lookups and deterministic security tests validating absolute immunity against SQL Injection payloads.

## 📁 Repository Structure
├── data/raw/         # Raw immutable data landing zone
├── src/              # Production pipeline codebase
│   ├── etl_load_sqlite.py
│   └── kpi_city.py
├── tests/            # Automated test vectors and assertions
└── requirements.txt  # Environment dependencies (Pandas, PyTest)

## 🚀 Execution & Setup
1. Clone the environment:
   ```bash
   git clone https://github.com/BARANEEDHARAN-S/Applied_Analytics.git
   cd Applied_Analytics
   ```
2. Provision system requirements:
   ```bash
   python -m pip install -r requirements.txt
   ```
3. Execute the ETL Pipeline & Compute KPIs:
   ```bash
   python src/etl_load_sqlite.py
   python src/kpi_city.py
   ```
4. Trigger unit test validation workflows:
   ```bash
   python -m pytest
   ```
