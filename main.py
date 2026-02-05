from fastapi import FastAPI, Header
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
import re

app = FastAPI(title="Agentic Honey-Pot", version="1.0.0")

# -------------------------
# In-memory storage
# -------------------------
attack_logs = []
conversation_states = {}

# -------------------------
# Models
# -------------------------
class LoginData(BaseModel):
    username: str
    password: str

class MessageData(BaseModel):
    message: Optional[str] = None

# -------------------------
# Home
# -------------------------
@app.get("/")
async def home():
    return {"status": "Agentic Honey-Pot is running"}

# -------------------------
# Fake Login Honeypot
# -------------------------
@app.post("/login")
async def fake_login(data: LoginData):
    attack_logs.append({
        "username": data.username,
        "password": data.password,
        "time": datetime.utcnow().isoformat()
    })

    return {
        "message": "Login failed. Please try again.",
        "status": "error"
    }

# -------------------------
# Attack Logs
# -------------------------
@app.get("/attack-logs")
async def get_logs():
    return {
        "total_attacks": len(attack_logs),
        "logs": attack_logs
    }

# -------------------------
# Agentic Chat Endpoint (TESTER SAFE)
# -------------------------
@app.api_route("/agent-chat/{session_id}", methods=["POST", "GET"])
async def agent_chat(
    session_id: str,
    payload: Optional[MessageData] = None,
    x_api_key: Optional[str] = Header(None)
):
    # API key validation
    if x_api_key != "test123":
        return {"error": "Invalid API key"}

    # Initialize session state
    if session_id not in conversation_states:
        conversation_states[session_id] = {
            "turns": 0,
            "summary": ""
        }

    state = conversation_states[session_id]
    state["turns"] += 1

    # Handle missing body (tester case)
    message = payload.message if payload and payload.message else "Suspicious activity detected"

    # -------------------------
    # AI / Honeypot Intelligence
    # -------------------------
    upi_ids = re.findall(r'\b[\w.-]+@upi\b', message)
    links = re.findall(r'https?://\S+', message)

    scam_detected = bool(upi_ids or links)
    risk_score = 0.8 if scam_detected else 0.1
    threat_level = "HIGH" if scam_detected else "LOW"

    reasoning = []
    if upi_ids:
        reasoning.append("UPI ID detected")
    if links:
        reasoning.append("Suspicious link detected")

    # Update conversation summary
    state["summary"] += f" | Turn {state['turns']}: {threat_level}"

    return {
        "session_id": session_id,
        "conversation_turns": state["turns"],
        "conversation_summary": state["summary"].strip(" |"),
        "scam_detected": scam_detected,
        "risk_score": risk_score,
        "threat_level": threat_level,
        "reasoning": reasoning,
        "extracted_intelligence": {
            "upi_ids": upi_ids,
            "phishing_links": links
        },
        "agent_reply": "Monitoring activity and adapting defenses"
    }
