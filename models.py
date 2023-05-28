from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(length=30), unique=True, index=True)
    password = Column(String(length=8))
    is_active = Column(Boolean, default=True)

    posts = relationship("Post", back_populates="user")


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(length=50), index=True)
    description = Column(String(length=256), index=True)
    location = Column(String(length=100))
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="posts")