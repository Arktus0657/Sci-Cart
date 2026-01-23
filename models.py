from pydantic import BaseModel 

class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float
    quantity: int

class User(BaseModel):
    id: int
    username: str
    email: str
    full_name: str