from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# ---------- CONFIG ----------
API_KEY = "test123"

# ---------- REQUEST MODEL ----------
class ChatRequest(BaseModel):
    message: Optional[str] = None

# ---------- ROOT ----------
@app.get("/")
def root():
    return {"status": "Agentic Honeypot running"}

# ---------- MAIN ENDPOINT ----------
@app.post("/agent-chat/{session_id}")
def agent_chat(
    session_id: str,
    data: Optional[ChatRequest] = None,
    x_api_key: str = Header(None)
):
    # API key validation
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")

    # If no body sent (API tester case)
    user_message = data.message if data and data.message else "No message provided"

    return {
        "session_id": session_id,
        "received_message": user_message,
        "honeypot_response": "Request logged successfully"
    }
