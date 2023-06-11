from typing import List, Union, Dict
from datetime import datetime

from pydantic import BaseModel


class UserBase(BaseModel):
    email: str
    username: str
    fullname: str
    title: str
    skills: list
    address: str
    job_type: Union[str, None] = ""


class UserCreate(UserBase):
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class User(UserBase):
    id: int
    is_active: bool
    followers: list
    followings: list
    # Posts: List[Post] = []

    class Config:
        orm_mode = True


class PostBase(BaseModel):
    title: str
    description: Union[str, None] = None
    location: str
    title: str
    job_type: str
    pay_rate_per_hr_dollar: float
    description: str
    skills: list
    liked_by: list
    viewed_by: list


class PostCreate(PostBase):
    pass


class Post(PostBase):
    id: int
    user_id: int
    post_by_username: str
    post_by_fullname: str
    post_date: datetime
    comments: Union[list, None] = []

    class Config:
        orm_mode = True
