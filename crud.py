from sqlalchemy.orm import Session
from sqlalchemy.sql import func
import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(
        email=user.email,
        password=user.password,
        username=user.username,
        fullname=user.fullname,
        title=user.title,
        skills=user.skills,
        address=user.address,
        followers=[],
        followings=[],
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_posts(db: Session, skip: int = 0, limit: int = 100):
    return (
        db.query(
            models.Post.id,
            models.Post.title,
            models.Post.location,
            models.Post.job_type,
            models.Post.pay_rate_per_hr_dollar,
            models.Post.skills,
            models.Post.liked_by,
            models.Post.viewed_by,
            models.Post.user_id,
            models.Post.description,
            models.Post.created_at.label("post_date"),
            models.User.username.label("post_by_username"),
            models.User.fullname.label("post_by_fullname")
        )
        .join(models.User)
        .offset(skip)
        .limit(limit)
        .all()
    )


def create_user_post(db: Session, post: schemas.PostCreate, user_id: int):
    db_post = models.Post(**post.dict(), user_id=user_id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post
