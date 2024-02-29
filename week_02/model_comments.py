#pydantic data model for object Users
from pydantic import BaseModel

class User(BaseModel):
    username: str
    email: str
    password: str