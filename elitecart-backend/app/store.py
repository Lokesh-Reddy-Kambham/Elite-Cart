from datetime import datetime
from threading import RLock
import os

_store_lock = RLock()
_initialized = False

_users = []
_products = []
_orders = []
_order_items = []

_next_user_id = 1
_next_product_id = 1
_next_order_id = 1
_next_order_item_id = 1


def is_memory_mode():
    """Use in-memory store on Vercel by default, or when explicitly enabled."""
    return os.getenv('USE_IN_MEMORY_STORE') == '1' or bool(os.getenv('VERCEL'))


def _now():
    return datetime.utcnow().isoformat() + 'Z'


def _seed_products():
    return [
        {
            'name': 'Premium Sneaker',
            'description': 'High quality running sneaker with excellent comfort',
            'price': 99.99,
            'image_url': '/images/sneaker.jpg',
            'stock': 50,
            'category': 'Men',
        },
        {
            'name': 'Casual T-Shirt',
            'description': 'Comfortable cotton t-shirt for everyday wear',
            'price': 29.99,
            'image_url': '/images/tshirt.jpg',
            'stock': 100,
            'category': 'Men',
        },
        {
            'name': 'Elegant Dress',
            'description': 'Beautiful evening dress perfect for special occasions',
            'price': 149.99,
            'image_url': '/images/dress.jpg',
            'stock': 30,
            'category': 'Women',
        },
        {
            'name': 'Running Shorts',
            'description': 'Breathable shorts designed for active sportspeople',
            'price': 49.99,
            'image_url': '/images/shorts.jpg',
            'stock': 75,
            'category': 'Men',
        },
        {
            'name': 'Sports Bra',
            'description': 'High support sports bra for intense workouts',
            'price': 69.99,
            'image_url': '/images/sportsbra.jpg',
            'stock': 40,
            'category': 'Women',
        },
        {
            'name': 'Jeans',
            'description': 'Classic blue jeans with perfect fit',
            'price': 79.99,
            'image_url': '/images/jeans.jpg',
            'stock': 60,
            'category': 'Unisex',
        },
        {
            'name': 'Leather Jacket',
            'description': 'Premium leather jacket for a sophisticated look',
            'price': 199.99,
            'image_url': '/images/jacket.jpg',
            'stock': 25,
            'category': 'Men',
        },
        {
            'name': 'Yoga Pants',
            'description': 'Comfortable yoga pants with high waistband',
            'price': 59.99,
            'image_url': '/images/yogapants.jpg',
            'stock': 45,
            'category': 'Women',
        },
    ]


def initialize_store():
    global _initialized, _next_product_id
    if _initialized:
        return
    with _store_lock:
        if _initialized:
            return
        for p in _seed_products():
            create_product(p)
        _initialized = True


def find_user_by_email(email):
    initialize_store()
    email_normalized = (email or '').strip().lower()
    return next((u for u in _users if u['email'].lower() == email_normalized), None)


def get_user_by_id(user_id):
    initialize_store()
    return next((u for u in _users if u['user_id'] == user_id), None)


def create_user(name, email, password_hash):
    global _next_user_id
    initialize_store()
    with _store_lock:
        user = {
            'user_id': _next_user_id,
            'name': name,
            'email': (email or '').strip().lower(),
            'password_hash': password_hash,
            'created_at': _now(),
        }
        _users.append(user)
        _next_user_id += 1
        return user.copy()


def list_products(category=None, min_price=None, max_price=None, in_stock=False):
    initialize_store()
    results = [p.copy() for p in _products]
    if category:
        results = [p for p in results if p['category'] == category]
    if min_price is not None:
        results = [p for p in results if float(p['price']) >= float(min_price)]
    if max_price is not None:
        results = [p for p in results if float(p['price']) <= float(max_price)]
    if in_stock:
        results = [p for p in results if int(p['stock']) > 0]
    results.sort(key=lambda p: p['product_id'], reverse=True)
    return results


def get_product_by_id(product_id):
    initialize_store()
    product = next((p for p in _products if p['product_id'] == product_id), None)
    return product.copy() if product else None


def create_product(data):
    global _next_product_id
    with _store_lock:
        product = {
            'product_id': _next_product_id,
            'name': data['name'],
            'description': data['description'],
            'price': float(data['price']),
            'image_url': data['image_url'],
            'stock': int(data['stock']),
            'category': data['category'],
            'created_at': _now(),
        }
        _products.append(product)
        _next_product_id += 1
        return product.copy()


def update_product(product_id, updates):
    with _store_lock:
        product = next((p for p in _products if p['product_id'] == product_id), None)
        if not product:
            return None
        for key in ['name', 'description', 'price', 'image_url', 'stock', 'category']:
            if key in updates:
                if key == 'price':
                    product[key] = float(updates[key])
                elif key == 'stock':
                    product[key] = int(updates[key])
                else:
                    product[key] = updates[key]
        return product.copy()


def delete_product(product_id):
    with _store_lock:
        idx = next((i for i, p in enumerate(_products) if p['product_id'] == product_id), None)
        if idx is None:
            return False
        _products.pop(idx)
        return True


def create_order(user_id, total_amount):
    global _next_order_id
    with _store_lock:
        order = {
            'order_id': _next_order_id,
            'user_id': int(user_id),
            'total_amount': float(total_amount),
            'created_at': _now(),
        }
        _orders.append(order)
        _next_order_id += 1
        return order.copy()


def create_order_item(order_id, product_id, quantity, price):
    global _next_order_item_id
    with _store_lock:
        item = {
            'order_item_id': _next_order_item_id,
            'order_id': int(order_id),
            'product_id': int(product_id),
            'quantity': int(quantity),
            'price': float(price),
        }
        _order_items.append(item)
        _next_order_item_id += 1
        return item.copy()


def decrement_product_stock(product_id, quantity):
    with _store_lock:
        product = next((p for p in _products if p['product_id'] == product_id), None)
        if not product:
            return None
        if int(product['stock']) < int(quantity):
            return False
        product['stock'] = int(product['stock']) - int(quantity)
        return True


def get_orders_by_user(user_id):
    user_orders = [o.copy() for o in _orders if o['user_id'] == int(user_id)]
    user_orders.sort(key=lambda o: o['order_id'], reverse=True)
    return user_orders


def get_order_by_id(order_id):
    order = next((o for o in _orders if o['order_id'] == int(order_id)), None)
    return order.copy() if order else None


def get_order_items(order_id):
    return [i.copy() for i in _order_items if i['order_id'] == int(order_id)]