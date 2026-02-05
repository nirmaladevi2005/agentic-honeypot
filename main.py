from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
from typing import Optional, Dict
import re

app = FastAPI(title="Agentic Honeypot API")

# -------- Agent Memory --------
agent_state: Dict[str, int] = {
    "risk_score": 0
}

conversation_summary: list[str] = []

# -------- Request Schema --------
class MessageData(BaseModel):
    message: str

# -------- Root Health Check --------
@app.get("/")
def health():
    return {"status": "Agentic Honey-Pot is running"}

# -------- Agentic Honeypot Endpoint --------
@app.post("/agent-chat/{session_id}")
def agent_chat(
    session_id: str,
    data: MessageData,
    x_api_key: Optional[str] = Header(None)
):
    if not x_api_key or x_api_key.strip() != "test123":
        raise HTTPException(status_code=401, detail="Invalid API key")

    msg = data.message.lower()

    upi_matches = re.findall(r"\b[\w.-]+@upi\b", msg)
    links = re.findall(r"https?://\S+", msg)

    scam_detected = bool(upi_matches or links)

    if scam_detected:
        agent_state["risk_score"] += 1

    conversation_summary.append(data.message)

    return {
        "session_id": session_id,
        "scam_detected": scam_detected,
        "agent_state": agent_state,
        "conversation_summary": conversation_summary[-3:],  # last 3
        "extracted_intelligence": {
            "upi_ids": upi_matches,
            "phishing_links": links
        }
    }
