from sqlalchemy import Column, Integer, String, DateTime, func, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(50), default='')
    first_name = Column(String(50), default='')
    last_name = Column(String(50), default='')
    created_at = Column(DateTime(timezone=False), server_default=func.now())

    messages = relationship("Message", back_populates="user", cascade="all, delete-orphan")

class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    text = Column(String(4096), nullable=False)
    message_type = Column(String(20), nullable=False)
    created_at = Column(DateTime(timezone=False), server_default=func.now())

    user = relationship("User", back_populates="messages")