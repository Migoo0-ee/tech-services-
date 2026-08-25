# Tech Services API — Backend Core

A secure and fast backend API built with Django REST Framework to support mobile and web applications. Built as part of an IBM-affiliated training program.

---

## 🛠 Tech Stack

- **Framework:** Django & Django REST Framework (DRF)
- **Auth:** SimpleJWT (Token-based Authentication)
- **Architecture:** Clean Architecture
- **Database:** SQLite (dev) / PostgreSQL (prod)

---

## 🔗 API Endpoints

### Authentication
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/auth/signup/` | Register a new user |
| POST | `/auth/login/` | Login and receive JWT token |

### Templates
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/templates/all/` | List all templates |
| GET | `/templates/category/<category>/` | Filter by category |
| GET | `/templates/paid/<is_paid>/` | Filter free or paid templates |

---

## 🔐 Security

- JWT authentication via SimpleJWT
- 401 Unauthorized returned on failed auth attempts
- Django password validation enforced on signup

---

## 🚀 Installation

```bash
git clone https://github.com/Migoo0-ee/tech-services-
cd tech-services-
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

---

## 👤 Developer

**Abdallah Mohamed (Migo)** — Backend Developer & Security Researcher

LinkedIn => https://www.linkedin.com/in/abdallah-el-messiri-4a31b1320/
GitHub => https://github.com/Migoo0-ee
