# Altinity QA Automation - Proof of Work

[![ClickHouse QA Tests](https://github.com/shivam-sharma-03/Altinity-QA-Project/actions/workflows/qa-pipeline.yml/badge.svg?branch=main)](https://github.com/shivam-sharma-03/Altinity-QA-Project/actions/workflows/qa-pipeline.yml)

## Overview
This repository contains an automated API test suite built as a Proof of Work for the QA Engineer position at Altinity. It demonstrates backend API test automation against a ClickHouse database using Python and Pytest.

## Project Goals
* Spin up an isolated ClickHouse database instance using Docker.
* Authenticate and interact with the ClickHouse HTTP REST API.
* Ensure test idempotency (handling state leakage).
* Validate data ingestion and retrieval using JSON formatting.

## Technology Stack
* **Database:** ClickHouse (Dockerized)
* **Language:** Python 3.x
* **Testing Framework:** Pytest
* **HTTP Client:** Requests

## Test Scenarios Covered
1. **Connection Verification:** Validates the database is up and responding with a 200 OK.
2. **Table Creation (Idempotent):** Safely drops existing tables and creates a new `users` table using the `MergeTree` engine.
3. **Data Ingestion:** Inserts dummy user records into the database via SQL over HTTP POST.
4. **Data Validation:** Retrieves the inserted records in JSON format and validates specific row counts and data integrity.

## How to Run Locally

### 1. Start the ClickHouse Database
Run the following Docker command to start a ClickHouse container with a custom password:
```bash
docker run -d --name clickhouse-qa-server -e CLICKHOUSE_PASSWORD=qa_password -p 8123:8123 clickhouse/clickhouse-server
```

### 2. Setup Python Environment
```bash
python -m venv venv
# Activate the virtual environment:
# Windows: .\venv\Scripts\activate
# Mac/Linux: source venv/bin/activate

pip install -r requirements.txt
```

### 3. Execute Tests
Run the test suite to see the results:
```bash
pytest test_db.py -v
```
