from pydantic import BaseModel
from datetime import datetime


class NewAccountForm(BaseModel):
    email: str
    password: str


class UserAccountIdentifier(BaseModel):
    email: str


class UserAccount(BaseModel):
    email: str
    password: str | None
    salt: str | None
    name: str | None
    join_time: str
    # location, permissions, etc
