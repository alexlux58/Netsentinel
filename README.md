# 🛡 NetSentinel Setup Guide

NetSentinel is a Django + DRF project using PostgreSQL for the backend database.  
This guide will walk you through local setup on macOS.

---

## 1️⃣ Create Project and Virtual Environment

```bash
mkdir netsentinel && cd netsentinel
python3 -m venv venv
source venv/bin/activate
```

---

## 2️⃣ Install Dependencies

```bash
pip install django djangorestframework psycopg2-binary requests pandas
```

---

## 3️⃣ Create Django Project

```bash
django-admin startproject netsentinel .
```

---

## 4️⃣ Install PostgreSQL (macOS)

Use Homebrew to install **PostgreSQL 15**:

```bash
brew install postgresql@15
brew services start postgresql@15
```

**Important:** PostgreSQL 15 is keg-only, so add it to your `PATH`:

```bash
echo 'export PATH="/usr/local/opt/postgresql@15/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

Verify installation:

```bash
psql --version
```

---

## 5️⃣ Create Database and User

Open PostgreSQL shell:

```bash
psql postgres
```

Run the following SQL commands:

```sql
CREATE DATABASE netsentinel;
CREATE USER netsentinel WITH PASSWORD 'password123';
GRANT ALL PRIVILEGES ON DATABASE netsentinel TO netsentinel;
\q
```

---

## 6️⃣ Configure Django Database Settings

In `netsentinel/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'netsentinel',
        'USER': 'netsentinel',
        'PASSWORD': 'password123',
        'HOST': 'localhost',
        'PORT': 5432,
    }
}
```

---

## 7️⃣ Apply Migrations and Create Admin User

```bash
source venv/bin/activate
python manage.py migrate
python manage.py createsuperuser
```

Follow the prompts to create an admin account.

---

## 8️⃣ Run Development Server

```bash
python manage.py runserver
```

- **Admin panel:** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
- **API root:** [http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/)

---

## 🔧 Troubleshooting

- **`psql: command not found`**  
  → Add PostgreSQL to your PATH as shown in step 4.

- **Authentication errors**  
  → Ensure the `USER` and `PASSWORD` in Django match the PostgreSQL user.

- **Migrations not applied**  
  → Run `python manage.py migrate` to create tables.

---

## ✅ Done!

You now have a fully working **Django + PostgreSQL** environment for **NetSentinel**.
