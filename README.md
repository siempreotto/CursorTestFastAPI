# FastAPI Restaurant API

A modern REST API built with FastAPI for managing restaurant dishes (platos).

## 🚀 Features

- **CRUD Operations** for restaurant dishes
- **Pydantic Data Validation** with comprehensive schemas
- **Interactive API Documentation** with Swagger UI
- **CORS Support** for frontend integration
- **Health Check Endpoint** for monitoring
- **Type Hints** throughout the codebase
- **Comprehensive Error Handling**

## 📋 Requirements

- Python 3.13+
- FastAPI
- Uvicorn
- Pydantic Settings

## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/fastapi-project.git
   cd fastapi-project
   ```

2. **Create and activate virtual environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   # OR if using uv:
   uv sync
   ```

## 🚀 Running the Application

### Development Mode
```bash
python main.py
```

### Using Uvicorn directly
```bash
uvicorn main:app --reload --host 127.0.0.1 --port 9500
```

The API will be available at:
- **Main API:** http://127.0.0.1:9500
- **Interactive Docs:** http://127.0.0.1:9500/docs
- **Alternative Docs:** http://127.0.0.1:9500/redoc

## 📚 API Endpoints

### Basic Endpoints
- `GET /` - Root endpoint with API information
- `GET /health` - Health check endpoint
- `GET /api/v1/test` - Test endpoint

### Platos (Dishes) CRUD
- `GET /api/v1/platos` - Get all dishes
- `GET /api/v1/platos/{id}` - Get dish by ID
- `POST /api/v1/platos` - Create new dish
- `PUT /api/v1/platos/{id}` - Update dish (complete)
- `PATCH /api/v1/platos/{id}` - Update dish (partial)
- `DELETE /api/v1/platos/{id}` - Delete dish

## 🧪 Example Usage

### Get all dishes
```bash
curl http://127.0.0.1:9500/api/v1/platos
```

### Create a new dish
```bash
curl -X POST http://127.0.0.1:9500/api/v1/platos \
  -H "Content-Type: application/json" \
  -d '{"name": "Tacos al Pastor", "precio": 9.99}'
```

### Update a dish
```bash
curl -X PATCH http://127.0.0.1:9500/api/v1/platos/1 \
  -H "Content-Type: application/json" \
  -d '{"precio": 16.99}'
```

## 📁 Project Structure

```
fastapi-project/
├── main.py              # Main FastAPI application
├── settings.py          # Configuration settings
├── schemas.py           # Pydantic schemas
├── pyproject.toml       # Project dependencies
├── .env                 # Environment variables (optional)
├── .gitignore          # Git ignore rules
└── README.md           # Project documentation
```

## ⚙️ Configuration

The application can be configured through environment variables or a `.env` file:

```env
PROJECT_NAME="FastAPI Restaurant API"
VERSION="0.1.0"
HOST=127.0.0.1
PORT=9500
DEBUG=true
ENVIRONMENT=development
```

## 🧪 Testing

Visit the interactive documentation at http://127.0.0.1:9500/docs to test all endpoints directly in your browser.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🔧 Development

### Code Style
- Follow PEP 8 guidelines
- Use type hints throughout
- Write comprehensive docstrings
- Keep functions focused and small

### Adding New Features
1. Create new schemas in `schemas.py`
2. Add endpoints in `main.py`
3. Update documentation
4. Test thoroughly

## 📞 Support

If you have any questions or issues, please open an issue on GitHub.

---

Built with ❤️ using FastAPI
