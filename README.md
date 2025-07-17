# 📈 Sector Market Analysis API

This FastAPI application generates markdown-based sector analysis reports using Gemini Pro. 

---

## 🚀 Features

- Accepts sector names and generates analysis reports
- Gemini integration via Google API
- API key-based authentication
- Markdown format output
- Simple and secure

---

## 🛠️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/your-username/sector-analysis-api.git
cd sector-analysis-api
```

### 2. Create and activate virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the FastAPI server
```bash
uvicorn main:app --reload
```
The API will be available at: http://127.0.0.1:8000/docs

## 🔐 Authentication
API requires an x-api-key header. Valid keys:

- guest123

- admin456

## 🧪 Sample cURL Request
```bash
curl -X POST "http://127.0.0.1:8000/analyze" \
     -H "Content-Type: application/json" \
     -H "x-api-key: guest123" \
     -d '{"sector": "finance"}'
```
## Screenshots

![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)
