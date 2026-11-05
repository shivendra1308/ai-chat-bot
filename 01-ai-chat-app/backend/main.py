# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine, Base
from routes import chat
from services.groq_service import get_available_models

# Create all DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI Chat App")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routes
# Like: app.use('/chat', chatRouter) in Express!
app.include_router(chat.router)

@app.get("/")
def home():
    return {"message": "AI Chat API is running!"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/models")
def models():
    return {"models": get_available_models()}