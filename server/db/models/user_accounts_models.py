from pydantic import BaseModel


class NewAccountForm(BaseModel):
    email: str
    password: str
