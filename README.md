
# 📚 FastAPI Bookstore
> A modern, secure REST API for managing your digital bookstore

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-red?style=for-the-badge)
![JWT](https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=JSON%20web%20tokens)

## ✨ Features

🔐 **Secure Authentication**
- OAuth2 implementation with JWT tokens
- Password hashing using bcrypt
- Role-based access control

📚 **Book Management**
- Create, read, update, and delete books
- Search books by title
- Comprehensive book metadata

👥 **User Management**
- User registration and authentication
- Profile management
- Admin privileges

🧪 **Testing**
- Extensive pytest coverage
- Integration tests
- API endpoint testing

## 🚀 Quick Start

### Prerequisites

```bash
Python 3.11+
pip
Virtual environment
```

### 🛠️ Installation

1️⃣ Clone the repository
```bash
git clone <repository-url>
```

2️⃣ Set up virtual environment
```bash
python -m venv vir
source vir/bin/activate  # Windows: vir\Scripts\activate
```

3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 🌟 Running the API

```bash
uvicorn main:app --reload
```

## 🛣️ API Routes

### 👤 User Management
```http
POST /users/                 # Create new user
PUT /users/{user_id}        # Update user
DELETE /users/{user_id}     # Delete user
POST /token                 # Get access token
```

### 📚 Book Management
```http
GET /books/                 # Get all books
POST /books/               # Create new book
GET /books/{title}         # Get book by title
PUT /books/{title}         # Update book
DELETE /books/{title}      # Delete book
```

## 🏗️ Project Structure

```
📦 fastapi-bookstore
├── 📂 app1/
│   ├── 📜 models.py      # Data models
│   ├── 📜 crud.py       # Database operations
│   └── 📜 database.py   # Database configuration
├── 📂 routers/
│   ├── 📜 auth.py       # Authentication routes
│   └── 📜 books.py      # Book management routes
├── 📂 tests/
│   ├── 📜 test_auth.py  # Authentication tests
│   └── 📜 test_books.py # Book operations tests
├── 📜 main.py           # Application entry point
└── 📜 requirements.txt   # Dependencies
```

## 🔒 Authentication Flow

```mermaid
sequenceDiagram
    Client->>API: POST /token (username, password)
    API-->>Database: Validate credentials
    Database-->>API: User exists
    API->>Client: JWT access token
    Client->>API: Request with Bearer token
    API-->>Client: Protected resource
```

## 💡 Code Examples

### Creating a New Book
```python
POST /books/
{
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "price": 19.99,
    "stock": 50
}
```

### Authentication
```python
POST /token
{
    "username": "user@example.com",
    "password": "secure_password"
}
```

## 🧪 Testing

Run the test suite:
```bash
pytest
```

Generate coverage report:
```bash
pytest --cov=app tests/
```

## 🔐 Environment Variables

Create `.env` file:
```env
DATABASE_URL=postgresql://user:password@localhost/db_name
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

## 📈 Future Improvements

- [ ] Add book categories and tags
- [ ] Implement search functionality
- [ ] Add user reviews and ratings
- [ ] Integrate payment processing
- [ ] Add book image upload support

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">
Made with ❤️ and FastAPI
</div>
```
- Clear installation and setup instructions
- Comprehensive API route documentation
- Visual project structure tree

Would you like me to modify or enhance any particular section?
