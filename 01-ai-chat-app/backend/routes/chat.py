# routes/chat.py
# All chat routes live here!

from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session
from database import get_db
from services.groq_service import get_groq_stream, get_available_models
import crud
import json
from pydantic import BaseModel

# APIRouter = mini Express router!
# Like: const router = express.Router()
router = APIRouter(prefix="/chat", tags=["chat"])

class ChatRequest(BaseModel):
    message: str
    user_id: str = "default_user"

# ===== STREAMING CHAT =====
@router.post("/stream")
async def chat_stream(
    request: ChatRequest,
    db: Session = Depends(get_db)
):
    # Save user message to DB
    crud.save_message(
        db=db,
        user_id=request.user_id,
        role="user",
        content=request.message
    )

    # Get history from DB
    history = crud.get_chat_history(
        db=db,
        user_id=request.user_id,
        limit=20
    )

    # Convert to Groq format
    messages_for_groq = [
        {"role": msg.role, "content": msg.content}
        for msg in history
    ]

    async def generate():
        full_response = ""

        stream = get_groq_stream(messages_for_groq)

        for chunk in stream:
            if chunk.choices[0].delta.content:
                text = chunk.choices[0].delta.content
                full_response += text
                yield f"data: {json.dumps({'text': text})}\n\n"

        # Save AI response to DB
        crud.save_message(
            db=db,
            user_id=request.user_id,
            role="assistant",
            content=full_response
        )

        yield f"data: {json.dumps({'done': True})}\n\n"

    return StreamingResponse(
        generate(),
        media_type="text/event-stream"
    )

# ===== GET HISTORY =====
@router.get("/history/{user_id}")
def get_history(
    user_id: str,
    db: Session = Depends(get_db)
):
    messages = crud.get_chat_history(db, user_id)
    return {
        "user_id": user_id,
        "messages": [
            {
                "role": msg.role,
                "content": msg.content,
                "created_at": str(msg.created_at)
            }
            for msg in messages
        ],
        "total": len(messages)
    }

# ===== CLEAR HISTORY =====
@router.delete("/history/{user_id}")
def clear_history(
    user_id: str,
    db: Session = Depends(get_db)
):
    return crud.clear_chat_history(db, user_id)