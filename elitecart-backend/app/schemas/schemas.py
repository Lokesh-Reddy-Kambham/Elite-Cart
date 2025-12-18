from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UserSignup(BaseModel):
    name: str
    email: EmailStr
    password: str

    class Config:
        schema_extra = {
            "example": {
                "name": "John Doe",
                "email": "john@example.com",
                "password": "securepass123"
            }
        }

class UserLogin(BaseModel):
    email: EmailStr
    password: str

    class Config:
        schema_extra = {
            "example": {
                "email": "john@example.com",
                "password": "securepass123"
            }
        }

class UserResponse(BaseModel):
    user_id: int
    name: str
    email: str
    created_at: datetime

class ProductCreate(BaseModel):
    name: str
    description: str
    price: float
    image_url: str
    stock: int
    category: str

    class Config:
        schema_extra = {
            "example": {
                "name": "Premium Sneaker",
                "description": "High quality sneaker for running",
                "price": 99.99,
                "image_url": "https://example.com/sneaker.jpg",
                "stock": 50,
                "category": "Men"
            }
        }

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    image_url: Optional[str] = None
    stock: Optional[int] = None
    category: Optional[str] = None

class ProductResponse(BaseModel):
    product_id: int
    name: str
    description: str
    price: float
    image_url: str
    stock: int
    category: str
    created_at: datetime

class OrderItemCreate(BaseModel):
    product_id: int
    quantity: int

class OrderCreate(BaseModel):
    items: list[OrderItemCreate]

class OrderItemResponse(BaseModel):
    order_item_id: int
    product_id: int
    quantity: int
    price: float

class OrderResponse(BaseModel):
    order_id: int
    user_id: int
    total_amount: float
    created_at: datetime
    items: Optional[list[OrderItemResponse]] = None
