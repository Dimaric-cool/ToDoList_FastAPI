from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, ForeignKey, Date
from sqlalchemy.dialects.postgresql import ARRAY
from datetime import datetime
from app.database import Base

class TodoModel(Base):
    """SQLAlchemy модель для работы с базой данных PostgreSQL."""
    __tablename__ = "todo"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=True, index=True)
    title = Column(String(100), nullable=False, index=True)
    description = Column(Text)
    tags = Column(ARRAY(Text), nullable=True)
    completed = Column(Boolean, nullable=False, default=False, index=True)
    due_date = Column(Date, nullable=True, index=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow, index=True)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
