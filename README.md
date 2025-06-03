# VaultWatch 🔐

**VaultWatch** is a security alert backend system that logs user activity, detects behavioral anomalies, and sends real-time email alerts for suspicious events such as geo-IP mismatches, brute-force login attempts, and failed 2FA verifications.

This project blends modern backend software engineering practices with cybersecurity principles to simulate active monitoring and defense of user-authenticated systems.

---

## 🛠️ Tech Stack

- **FastAPI** – High-performance Python web framework (for APIs)
- **PostgreSQL** – Relational database for secure audit logging
- **Celery + Redis** – Asynchronous task queue for email alerts
- **AWS SES** – Cloud email service for secure notifications
- **Docker** – Containerized deployment
- **GitHub Actions** – CI/CD for automated testing and deployment

---

## 🔐 Key Features

- ✅ JWT-based authentication and role-based access control (RBAC)
- ✅ Real-time login activity logging (IP address, timestamp, outcome)
- ✅ Anomaly detection for:
  - Repeated failed logins
  - Geo-IP deviation
  - Suspicious session patterns
- ✅ Automated email alerts via AWS SES
- ✅ Modular rule engine for defining and customizing detection logic
- ✅ Deployed with Docker & secured with NGINX reverse proxy + TLS

---

## 📦 Setup Instructions

1. **Clone the repo**
   ```bash
   git clone https://github.com/nickcuenca/vaultwatch.git
   cd vaultwatch
   ```

2. **Create `.env` file**
   ```env
   DATABASE_URL=postgresql://postgres:password@localhost:5432/vaultwatch_db
   AWS_SES_ACCESS_KEY_ID=your_key
   AWS_SES_SECRET_ACCESS_KEY=your_secret
   EMAIL_SENDER=youremail@example.com
   ```

3. **Run FastAPI server**
   ```bash
   uvicorn app.main:app --reload
   ```

4. **Start Celery worker**
   ```bash
   celery -A app.tasks worker --loglevel=info
   ```

---

## 🧪 Coming Soon

- Admin dashboard to view triggered alerts
- Web UI for managing users and sessions
- Docker Compose for full-service orchestration
- CI/CD pipeline with GitHub Actions

---

## 📄 License

MIT License

---

## 👨‍💻 Author

**Nicolás Cuenca**  
[LinkedIn](https://www.linkedin.com/in/nicolaswcuenca/) · [GitHub](https://github.com/nickcuenca)