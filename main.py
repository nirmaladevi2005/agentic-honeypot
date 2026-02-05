from fastapi import FastAPI, Header, Request
from datetime import datetime
import re

app = FastAPI(title="Agentic Honeypot", version="1.0")

# -------------------------
# Memory
# -------------------------
attack_logs = []
sessions = {}

# -------------------------
# Root
# -------------------------
@app.get("/")
def root():
    return {"status": "running"}

# -------------------------
# Fake Login
# -------------------------
@app.post("/login")
async def fake_login(request: Request):
    data = await request.json()
    attack_logs.append({
        "username": data.get("username"),
        "password": data.get("password"),
        "time": datetime.utcnow().isoformat()
    })
    return {"message": "Login failed"}

# -------------------------
# Logs
# -------------------------
@app.get("/attack-logs")
def logs():
    return attack_logs

# -------------------------
# 🚨 TESTER-SAFE AGENT ENDPOINT
# -------------------------
@app.api_route("/agent-chat/{session_id}", methods=["GET", "POST"])
async def agent_chat(
    session_id: str,
    request: Request,
    x_api_key: str = Header(...)
):
    # API key check
    if x_api_key.strip() != "test123":
        return {"error": "Invalid API key"}

    # Session init
    if session_id not in sessions:
        sessions[session_id] = {
            "turns": 0,
            "summary": ""
        }

    sessions[session_id]["turns"] += 1

    # Safely read body ONLY if it exists
    try:
        body = await request.json()
        message = body.get("message", "")
    except Exception:
        message = ""

    # Simple agent intelligence
    upi_ids = re.findall(r'\b[\w.-]+@upi\b', message)
    links = re.findall(r'https?://\S+', message)

    scam = bool(upi_ids or links)
    threat = "HIGH" if scam else "LOW"

    sessions[session_id]["summary"] += f" Turn{sessions[session_id]['turns']}:{threat}"

    return {
        "session_id": session_id,
        "turns": sessions[session_id]["turns"],
        "threat_level": threat,
        "scam_detected": scam,
        "extracted": {
            "upi_ids": upi_ids,
            "links": links
        },
        "agent_reply": "Adaptive monitoring active"
    }
