from datetime import datetime
from typing import Optional

class User:
    def __init__(self, user_id: int, name: str, email: str, password_hash: str, created_at: datetime = None):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password_hash = password_hash
        self.created_at = created_at or datetime.now()

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'name': self.name,
            'email': self.email,
            'created_at': self.created_at.isoformat() if isinstance(self.created_at, datetime) else self.created_at
        }

class Product:
    def __init__(self, product_id: int, name: str, description: str, price: float, 
                 image_url: str, stock: int, category: str, created_at: datetime = None):
        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price
        self.image_url = image_url
        self.stock = stock
        self.category = category
        self.created_at = created_at or datetime.now()

    def to_dict(self):
        return {
            'product_id': self.product_id,
            'name': self.name,
            'description': self.description,
            'price': float(self.price),
            'image_url': self.image_url,
            'stock': self.stock,
            'category': self.category,
            'created_at': self.created_at.isoformat() if isinstance(self.created_at, datetime) else self.created_at
        }

class Order:
    def __init__(self, order_id: int, user_id: int, total_amount: float, created_at: datetime = None):
        self.order_id = order_id
        self.user_id = user_id
        self.total_amount = total_amount
        self.created_at = created_at or datetime.now()

    def to_dict(self):
        return {
            'order_id': self.order_id,
            'user_id': self.user_id,
            'total_amount': float(self.total_amount),
            'created_at': self.created_at.isoformat() if isinstance(self.created_at, datetime) else self.created_at
        }

class OrderItem:
    def __init__(self, order_item_id: int, order_id: int, product_id: int, quantity: int, price: float):
        self.order_item_id = order_item_id
        self.order_id = order_id
        self.product_id = product_id
        self.quantity = quantity
        self.price = price

    def to_dict(self):
        return {
            'order_item_id': self.order_item_id,
            'order_id': self.order_id,
            'product_id': self.product_id,
            'quantity': self.quantity,
            'price': float(self.price)
        }
