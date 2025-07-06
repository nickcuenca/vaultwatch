# VaultWatch 🔐

**VaultWatch** is a backend security alert system that logs user activity, detects behavioral anomalies, and sends real-time email alerts for events like geo-IP mismatches, brute-force login attempts, and failed 2FA verifications.

> 🚨 Built to simulate the defensive systems used in modern cybersecurity-aware applications.

![Build](https://github.com/nickcuenca/vaultwatch/actions/workflows/python-app.yml/badge.svg)
[![codecov](https://codecov.io/gh/nickcuenca/vaultwatch/branch/main/graph/badge.svg)](https://codecov.io/gh/nickcuenca/vaultwatch)

---

## 🛠️ Tech Stack

- **FastAPI** – High-performance Python web framework
- **PostgreSQL** – Secure relational database for audit logging
- **Celery + Redis** – Async job queue for email alerts
- **AWS SES** – Email delivery service
- **Docker** – Containerized deployment
- **GitHub Actions** – CI/CD with testing & build automation

---

## 🔐 Key Features

- ✅ JWT authentication & RBAC
- ✅ Real-time login logging (IP, timestamp, outcome)
- ✅ Behavior-based anomaly detection:
  - Repeated failed logins
  - Geo-IP deviation
  - Suspicious session patterns
- ✅ Asynchronous email alerts via AWS SES
- ✅ Modular rule engine for custom detection logic
- ✅ Dockerized backend with NGINX reverse proxy & HTTPS

---

## 🚀 Getting Started

Clone the repo, install dependencies, and launch:

```bash
git clone https://github.com/nickcuenca/vaultwatch.git
cd vaultwatch
pip install -r requirements.txt
uvicorn app.main:app --reload
```

---

## ✅ Testing

- Built with `pytest` and `httpx` for full test coverage  
- Code coverage: **95%+**  
- CI pipeline runs automatically on push via GitHub Actions

To run tests locally:
```bash
pytest -v --cov=app
```