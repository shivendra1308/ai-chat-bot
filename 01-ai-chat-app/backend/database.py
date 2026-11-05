# database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLite database file
# Like connection string in Prisma!
DATABASE_URL = "sqlite:///./chat.db"

# Create engine
# Like creating DB connection!
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
    # check_same_thread only needed for SQLite!
)

# Session factory
# Like a DB transaction manager!
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base class for all models
Base = declarative_base()

# Dependency — gives us DB session per request
# Like middleware in Express!
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()