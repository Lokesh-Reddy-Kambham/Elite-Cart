from flask import Blueprint, request, jsonify
from app.database import fetch_one, fetch_all, insert_record, update_record, delete_record
from flask_jwt_extended import jwt_required, get_jwt_identity
from mysql.connector import Error

products_bp = Blueprint('products', __name__, url_prefix='/api/products')

@products_bp.route('', methods=['GET'])
def get_products():
    """Get all products with optional filters"""
    try:
        # Get query parameters
        category = request.args.get('category')
        min_price = request.args.get('min_price', type=float)
        max_price = request.args.get('max_price', type=float)
        in_stock = request.args.get('in_stock', type=bool)
        
        # Build query
        query = "SELECT * FROM products WHERE 1=1"
        params = []
        
        if category:
            query += " AND category = %s"
            params.append(category)
        
        if min_price is not None:
            query += " AND price >= %s"
            params.append(min_price)
        
        if max_price is not None:
            query += " AND price <= %s"
            params.append(max_price)
        
        if in_stock:
            query += " AND stock > 0"
        
        query += " ORDER BY created_at DESC"
        
        products = fetch_all(query, params if params else None)
        
        return jsonify({
            'products': products,
            'count': len(products)
        }), 200
    
    except Error as err:
        return jsonify({'error': str(err)}), 500

@products_bp.route('/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """Get a specific product by ID"""
    try:
        product = fetch_one("SELECT * FROM products WHERE product_id = %s", (product_id,))
        
        if not product:
            return jsonify({'error': 'Product not found'}), 404
        
        return jsonify(product), 200
    
    except Error as err:
        return jsonify({'error': str(err)}), 500

@products_bp.route('', methods=['POST'])
@jwt_required()
def create_product():
    """Create a new product (Admin only)"""
    try:
        data = request.get_json()
        
        required_fields = ['name', 'description', 'price', 'image_url', 'stock', 'category']
        if not all(field in data for field in required_fields):
            return jsonify({'error': 'Missing required fields'}), 400
        
        product_id = insert_record(
            "INSERT INTO products (name, description, price, image_url, stock, category) VALUES (%s, %s, %s, %s, %s, %s)",
            (data['name'], data['description'], data['price'], data['image_url'], data['stock'], data['category'])
        )
        
        return jsonify({
            'message': 'Product created successfully',
            'product_id': product_id
        }), 201
    
    except Error as err:
        return jsonify({'error': str(err)}), 500

@products_bp.route('/<int:product_id>', methods=['PUT'])
@jwt_required()
def update_product(product_id):
    """Update a product (Admin only)"""
    try:
        # Check if product exists
        product = fetch_one("SELECT * FROM products WHERE product_id = %s", (product_id,))
        if not product:
            return jsonify({'error': 'Product not found'}), 404
        
        data = request.get_json()
        
        # Build update query
        update_fields = []
        params = []
        
        updatable_fields = ['name', 'description', 'price', 'image_url', 'stock', 'category']
        for field in updatable_fields:
            if field in data:
                update_fields.append(f"{field} = %s")
                params.append(data[field])
        
        if not update_fields:
            return jsonify({'error': 'No fields to update'}), 400
        
        params.append(product_id)
        query = f"UPDATE products SET {', '.join(update_fields)} WHERE product_id = %s"
        
        update_record(query, params)
        
        return jsonify({
            'message': 'Product updated successfully',
            'product_id': product_id
        }), 200
    
    except Error as err:
        return jsonify({'error': str(err)}), 500

@products_bp.route('/<int:product_id>', methods=['DELETE'])
@jwt_required()
def delete_product(product_id):
    """Delete a product (Admin only)"""
    try:
        # Check if product exists
        product = fetch_one("SELECT * FROM products WHERE product_id = %s", (product_id,))
        if not product:
            return jsonify({'error': 'Product not found'}), 404
        
        delete_record("DELETE FROM products WHERE product_id = %s", (product_id,))
        
        return jsonify({
            'message': 'Product deleted successfully'
        }), 200
    
    except Error as err:
        return jsonify({'error': str(err)}), 500
