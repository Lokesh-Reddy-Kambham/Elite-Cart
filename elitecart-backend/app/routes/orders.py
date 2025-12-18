from flask import Blueprint, request, jsonify
from app.database import fetch_one, fetch_all, insert_record, update_record
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from mysql.connector import Error

orders_bp = Blueprint('orders', __name__, url_prefix='/api/orders')

@orders_bp.route('', methods=['POST'])
@jwt_required()
def create_order():
    """Create a new order"""
    try:
        current_user_id = get_jwt_identity()
        # identity was stored as string in JWT, convert to int
        try:
            current_user_id = int(current_user_id)
        except Exception:
            pass
        user_id = current_user_id
        data = request.get_json()
        
        if not data or not data.get('items') or len(data['items']) == 0:
            return jsonify({'error': 'No items in order'}), 400
        
        # Calculate total amount
        total_amount = 0
        order_items = []
        
        for item in data['items']:
            product_id = item.get('product_id')
            quantity = item.get('quantity')
            
            if not product_id or not quantity or quantity <= 0:
                return jsonify({'error': 'Invalid item data'}), 400
            
            # Get product details
            product = fetch_one("SELECT * FROM products WHERE product_id = %s", (product_id,))
            if not product:
                return jsonify({'error': f'Product {product_id} not found'}), 404
            
            if product['stock'] < quantity:
                return jsonify({'error': f'Insufficient stock for product {product_id}'}), 400
            
            total_amount += product['price'] * quantity
            order_items.append({
                'product_id': product_id,
                'quantity': quantity,
                'price': product['price']
            })
        
        # Create order
        order_id = insert_record(
            "INSERT INTO orders (user_id, total_amount) VALUES (%s, %s)",
            (user_id, total_amount)
        )
        
        # Create order items
        for item in order_items:
            insert_record(
                "INSERT INTO order_items (order_id, product_id, quantity, price) VALUES (%s, %s, %s, %s)",
                (order_id, item['product_id'], item['quantity'], item['price'])
            )
            
            # Update product stock
            update_record(
                "UPDATE products SET stock = stock - %s WHERE product_id = %s",
                (item['quantity'], item['product_id'])
            )
        
        return jsonify({
            'message': 'Order created successfully',
            'order_id': order_id,
            'total_amount': total_amount,
            'items_count': len(order_items)
        }), 201
    
    except Error as err:
        return jsonify({'error': str(err)}), 500

@orders_bp.route('/user/<int:user_id>', methods=['GET'])
@jwt_required()
def get_user_orders(user_id):
    """Get all orders for a specific user"""
    try:
        current_user_id = get_jwt_identity()
        try:
            current_user_id = int(current_user_id)
        except Exception:
            pass

        # Users can only see their own orders
        if current_user_id != user_id:
            return jsonify({'error': 'Unauthorized'}), 403
        
        # Get orders
        orders = fetch_all(
            "SELECT * FROM orders WHERE user_id = %s ORDER BY created_at DESC",
            (user_id,)
        )
        
        if not orders:
            return jsonify({'orders': [], 'count': 0}), 200
        
        # Get order items for each order
        for order in orders:
            items = fetch_all(
                "SELECT * FROM order_items WHERE order_id = %s",
                (order['order_id'],)
            )
            order['items'] = items
        
        return jsonify({
            'orders': orders,
            'count': len(orders)
        }), 200
    
    except Error as err:
        return jsonify({'error': str(err)}), 500

@orders_bp.route('/<int:order_id>', methods=['GET'])
@jwt_required()
def get_order_details(order_id):
    """Get details of a specific order"""
    try:
        current_user_id = get_jwt_identity()
        try:
            current_user_id = int(current_user_id)
        except Exception:
            pass

        # Get order
        order = fetch_one("SELECT * FROM orders WHERE order_id = %s", (order_id,))
        
        if not order:
            return jsonify({'error': 'Order not found'}), 404
        
        # Check authorization
        if current_user_id != order['user_id']:
            return jsonify({'error': 'Unauthorized'}), 403
        
        # Get order items
        items = fetch_all(
            "SELECT * FROM order_items WHERE order_id = %s",
            (order_id,)
        )
        order['items'] = items
        
        return jsonify(order), 200
    
    except Error as err:
        return jsonify({'error': str(err)}), 500
