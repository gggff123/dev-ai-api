<div align="center">

# ⚡ DevAI API

### 🧠 AI-Powered Developer Assistant (GPT4Free + FastAPI)

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&pause=1000&color=00F7FF&center=true&vCenter=true&width=650&lines=AI+Backend+For+Developers;Explain+Errors+Instantly;Generate+Unit+Tests;Explain+Code+Clearly;Deployed+on+Render" />

<br/>

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-High%20Performance-009688?style=for-the-badge&logo=fastapi)
![Render](https://img.shields.io/badge/Hosted%20on-Render-46E3B7?style=for-the-badge&logo=render)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

</div>

---

# 🚀 What Is DevAI API?

DevAI API is a lightweight REST API built using **FastAPI** and powered by **GPT4Free**.

It helps developers:

- 🤖 Ask AI programming questions  
- 🐛 Explain error messages  
- 📖 Explain source code  
- 🧪 Generate unit tests  
- ⚡ Get fast JSON responses  

It is designed to be:

- Free  
- Simple  
- Easy to integrate into apps or tools  

---

# 🧠 How It Works

### 1️⃣ Client Sends Request  
A user sends a POST request to the API.

### 2️⃣ FastAPI Receives Request  
FastAPI:
- Parses JSON body  
- Validates input  
- Routes to correct endpoint  

### 3️⃣ GPT4Free Processes Prompt  
The backend sends the prompt to a GPT4Free provider which:
- Generates AI response  
- Returns text output  

### 4️⃣ API Returns JSON  

```json
{
  "success": true,
  "prompt": "Explain async in Python",
  "response": "Async allows non-blocking execution..."
}
```

---

# 🌍 Live API

https://dev-ai-api.onrender.com

---

# 📘 Interactive Documentation

https://dev-ai-api.onrender.com/docs

---

# 📡 API Endpoints

## 1️⃣ Ask AI

**POST** `/ask`

```json
{
  "prompt": "Explain REST API"
}
```

---

## 2️⃣ Explain Error

**POST** `/explain-error`

```json
{
  "error": "TypeError: list indices must be integers"
}
```

---

## 3️⃣ Explain Code

**POST** `/explain-code`

```json
{
  "code": "def add(a,b): return a+b"
}
```

---

## 4️⃣ Generate Unit Tests

**POST** `/generate-tests`

```json
{
  "code": "def multiply(a,b): return a*b"
}
```

---

# 🐍 Python Usage Example

```python
import requests

url = "https://dev-ai-api.onrender.com/ask"
data = {"prompt": "Explain decorators in Python"}

response = requests.post(url, json=data)
print(response.json())
```

---

# 🌐 JavaScript Usage Example

```javascript
fetch("https://dev-ai-api.onrender.com/ask", {
  method: "POST",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    prompt: "Explain closures"
  })
})
.then(res => res.json())
.then(data => console.log(data));
```

---

# 📦 Requirements

```
fastapi
uvicorn
g4f
```

---

# 🚀 Deploy on Render

### Build Command
```
pip install -r requirements.txt
```

### Start Command
```
uvicorn app:app --host 0.0.0.0 --port $PORT
```

---

# ⚠ Disclaimer

GPT4Free providers may change, rate-limit, or become unavailable.

This project is for educational and experimental purposes.

---

<div align="center">

⭐ Star this repo if you like it  
🚀 Built for developers  

</div>
