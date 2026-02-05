# Agentic Honey-Pot 🛡️

## Problem Statement
Online scams using fake UPI IDs, phishing links, and social engineering are increasing rapidly.  
Traditional systems detect threats but do not adapt or reason like an intelligent agent.

## Solution
Agentic Honey-Pot is an **Agentic AI–based cybersecurity system** that:
- Lures attackers using a fake login (honeypot)
- Detects scam patterns in conversations
- Maintains agent state and reasoning
- Adapts its behavior based on risk level

## Why Agentic AI?
Unlike rule-based systems, this project:
- Maintains **agent_state**
- Has **intent awareness**
- Keeps **conversation memory**
- Performs **autonomous threat reasoning**

## Features
- Fake login honeypot
- Attack log collection
- Scam detection (UPI IDs, phishing links)
- Risk scoring & threat levels
- Agent state tracking
- Conversation summary
- REST APIs using FastAPI

## Tech Stack
- Python
- FastAPI
- Pydantic
- Regex-based intelligence extraction
- Swagger UI for testing

## How to Run
```bash
python -m venv venv
venv\Scripts\activate
pip install fastapi uvicorn
uvicorn main:app --reload
