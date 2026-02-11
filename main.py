from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
import re

app = FastAPI(title="Agentic Honey-Pot", version="1.0")

# -------------------------
# In-memory storage
# -------------------------
attack_logs = []
chat_sessions = {}

# -------------------------
# Schemas
# -------------------------
class LoginData(BaseModel):
    username: str
    password: str

class MessageData(BaseModel):
    message: str

# -------------------------
# Utility: Scam Detection
# -------------------------
def analyze_message(message: str):
    upi_pattern = r"\b[\w.-]+@[\w.-]+\b"
    link_pattern = r"http[s]?://\S+"

    upi_ids = re.findall(upi_pattern, message)
    phishing_links = re.findall(link_pattern, message)

    scam_detected = bool(upi_ids or phishing_links)
    risk_score = 0.8 if scam_detected else 0.1
    threat_level = "HIGH" if scam_detected else "LOW"

    reasoning = []
    if upi_ids:
        reasoning.append("UPI ID detected")
    if phishing_links:
        reasoning.append("Suspicious link detected")

    return {
        "scam_detected": scam_detected,
        "risk_score": risk_score,
        "threat_level": threat_level,
        "reasoning": reasoning,
        "extracted_intelligence": {
            "upi_ids": upi_ids,
            "phishing_links": phishing_links
        }
    }

# -------------------------
# Agentic Intelligence
# -------------------------
def build_agent_state(message, detection_result):
    return {
        "risk_level": detection_result["threat_level"],
        "confidence": detection_result["risk_score"],
        "intent": "warn_user" if detection_result["scam_detected"] else "monitor",
        "detected_entities": detection_result["extracted_intelligence"],
        "last_action": "Threat flagged" if detection_result["scam_detected"] else "No action",
        "timestamp": datetime.utcnow().isoformat()
    }

def generate_conversation_summary(message, agent_state):
    return (
        f"Message analyzed. "
        f"Risk level: {agent_state['risk_level']}. "
        f"Agent intent: {agent_state['intent']}."
    )

# -------------------------
# Routes
# -------------------------
@app.get("/")
def home():
    return {"status": "Agentic Honey-Pot is running"}

# Fake Login Endpoint (Honeypot)
@app.post("/login")
def fake_login(data: LoginData):
    attack_logs.append({
        "username": data.username,
        "password": data.password,
        "time": datetime.utcnow().isoformat()
    })

    return {
        "status": "error",
        "message": "Login failed. Please try again."
    }

# View Attack Logs
@app.get("/attack-logs")
def get_logs():
    return {
        "total_attacks": len(attack_logs),
        "logs": attack_logs
    }

# Agent Chat Endpoint
@app.post("/agent-chat/{session_id}")
def agent_chat(session_id: str, data: MessageData):
    result = analyze_message(data.message)

    agent_state = build_agent_state(data.message, result)
    conversation_summary = generate_conversation_summary(data.message, agent_state)

    if session_id not in chat_sessions:
        chat_sessions[session_id] = 0
    chat_sessions[session_id] += 1

    return {
        "session_id": session_id,
        "conversation_turns": chat_sessions[session_id],
        "scam_detected": result["scam_detected"],
        "risk_score": result["risk_score"],
        "threat_level": result["threat_level"],
        "reasoning": result["reasoning"],
        "agent_state": agent_state,
        "conversation_summary": conversation_summary,
        "extracted_intelligence": result["extracted_intelligence"],
        "agent_reply": "Monitoring activity and adapting defenses"
    }
