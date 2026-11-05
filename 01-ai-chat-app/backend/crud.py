# crud.py
# CRUD = Create Read Update Delete
# Like your service layer!

from sqlalchemy.orm import Session
from models import Message, User

# ===== CREATE =====
def save_message(db: Session, user_id: str, role: str, content: str):
    message = Message(
        user_id=user_id,
        role=role,
        content=content
    )
    db.add(message)
    db.commit()
    db.refresh(message)
    return message

# ===== READ =====
def get_chat_history(db: Session, user_id: str, limit: int = 20):
    return db.query(Message)\
             .filter(Message.user_id == user_id)\
             .order_by(Message.created_at)\
             .limit(limit)\
             .all()

# ===== DELETE =====
def clear_chat_history(db: Session, user_id: str):
    db.query(Message)\
      .filter(Message.user_id == user_id)\
      .delete()
    db.commit()
    return {"message": "Chat history cleared!"}

# ===== GET MESSAGE COUNT =====
def get_message_count(db: Session, user_id: str):
    return db.query(Message)\
             .filter(Message.user_id == user_id)\
             .count()