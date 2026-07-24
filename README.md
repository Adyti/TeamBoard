# TeamBoard Backend

A Django REST Framework backend application that provides user authentication, knowledge base search, and admin usage reporting.

## Features

- User Registration
- User Login with JWT Authentication
- Company auto-creation using Django Signals
- API Key generation
- Knowledge Base search
- Query logging
- Admin usage summary
- Role-based authorization
- PostgreSQL database
- Docker support

---

## Tech Stack

- Python 3
- Django
- Django REST Framework
- PostgreSQL
- Docker
- JWT Authentication
- Postman

---

## Project Structure

```
TeamBoard/
│
├── api/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── permissions.py
│   ├── serializers.py
│   ├── signals.py
│   ├── urls.py
│   └── views.py
│
├── teamboard/
├── docker-compose.yml
├── requirements.txt
├── .env.example
├── TeamBoard_API.postman_collection.json
├── manage.py
└── README.md
```

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/<repository-name>.git
cd TeamBoard
```

---

### 2. Create a virtual environment

Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure environment variables

Create a `.env` file in the project root using the values from `.env.example`.

Example:

```env
SECRET_KEY=your-secret-key
DEBUG=True

DB_NAME=teamboard_db
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

---

### 5. Start PostgreSQL using Docker

```bash
docker-compose up -d
```

Verify the container is running:

```bash
docker ps
```

---

### 6. Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 7. Create a superuser

```bash
python manage.py createsuperuser
```

---

### 8. Run the development server

```bash
python manage.py runserver
```

Open:

```
http://127.0.0.1:8000/
```

---

## Seed Knowledge Base Entries

1. Open Django Admin:

```
http://127.0.0.1:8000/admin/
```

2. Log in with your superuser account.

3. Navigate to **KB Entries**.

4. Add sample knowledge base records.

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/auth/register/` | Register a new user |
| POST | `/api/auth/login/` | Login and receive a JWT token |
| POST | `/api/kb/query/` | Search the knowledge base (JWT required) |
| GET | `/api/admin/usage-summary/` | View usage statistics (Admin only) |

---

## Postman Collection

The repository includes:

```
TeamBoard_API.postman_collection.json
```

---

## Author

**Aditi Sawant**