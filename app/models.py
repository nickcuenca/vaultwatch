from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(String, default="user")  # roles: user, admin
    created_at = Column(DateTime, default=datetime.utcnow)

    logins = relationship("LoginLog", back_populates="user")


class LoginLog(Base):
    __tablename__ = "login_logs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    ip_address = Column(String, nullable=False)
    success = Column(Boolean, default=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
    location = Column(String)  # Optional: for Geo-IP analysis

    user = relationship("User", back_populates="logins")