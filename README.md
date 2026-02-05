# 🛡️ Agentic Honey-Pot

An **Agentic AI–inspired cybersecurity honeypot system** designed to detect, engage, and analyze scammer behavior through intelligent interaction and adaptive reasoning.

---

## 🚨 Problem Statement

Online scams using fake UPI IDs, phishing links, and social engineering tactics are increasing rapidly.  
Traditional systems detect threats but lack adaptive intelligence and reasoning.

---

## 💡 Solution

**Agentic Honey-Pot** is a smart honeypot system that:
- Lures attackers using a fake conversational endpoint
- Detects scam patterns in messages
- Maintains agent state and conversation memory
- Adapts responses based on risk level

---

## 🤖 Why Agentic AI?

Unlike rule-based systems, this project:
- Maintains an **agent_state**
- Shows **intent awareness**
- Keeps **conversation memory**
- Performs **autonomous threat reasoning**
- Dynamically adapts behavior

---

## ✨ Features

- Fake login / chat honeypot
- Scam and phishing detection
- UPI ID & malicious link identification
- Risk scoring & threat levels
- Agent state tracking
- Conversation summarization
- REST APIs using FastAPI
- Swagger UI for testing

---

## 🧠 Tech Stack

- Python  
- FastAPI  
- Pydantic  
- Regex-based intelligence extraction  
- Swagger UI (OpenAPI)

---

## 🚀 Deployed Application

- **Base URL:**  
  https://agentic-honeypot-cze1.onrender.com

- **API Documentation (Swagger):**  
  https://agentic-honeypot-cze1.onrender.com/docs

> ⚠️ Note: Opening the base URL directly may show `Method Not Allowed`.  
> This is expected because the application is API-based.

---

## 🔐 API Authentication

All protected endpoints require an API key.

**Header:**
x-api-key: test123


---

## 🧪 Honeypot Testing Endpoint

**Method:** `POST`  
**Endpoint:**


/agent-chat/{session_id}


**Example Full URL:**


https://agentic-honeypot-cze1.onrender.com/agent-chat/test-session


**Required Header:**


x-api-key: test123


---

## 📥 Example Honeypot Response



Scammer
URGENT: Your SBI account has been compromised.
Your account will be blocked in 2 hours.
Share your account number and OTP immediately.


---

## 💻 Run Locally

```bash
python -m venv venv
venv\Scripts\activate
pip install fastapi uvicorn
uvicorn main:app --reload


Open in browser:

http://127.0.0.1:8000/docs

---

## 📂 GitHub Repository
https://github.com/nirmaladevi2005/agentic-honeypot