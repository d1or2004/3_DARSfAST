from pydantic import BaseModel
from typing import Optional


class RegisterModel(BaseModel):
    id: Optional[int]
    first_name: str
    last_name: str
    username: str
    email: str
    password: str
    is_staff: bool
    is_active: bool

    class Config:
        orm_mode = True
        schemas_extra = {
            "example": {
                "first_name": "Diyorbek",
                "last_name": "Axmadjonov",
                "username": "Dior",
                "email": "dior@gmail.com",
                "password": "2004",
                "is_staff": True,
                "is_active": True
            }
        }


class LoginModel(BaseModel):
    username: str
    password: str

