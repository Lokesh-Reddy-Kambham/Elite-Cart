from flask import Blueprint, request, jsonify
from app.database import fetch_one, insert_record
from app.auth import hash_password, verify_password, create_token
from app.store import is_memory_mode, find_user_by_email, create_user
from mysql.connector import Error

auth_bp = Blueprint('auth', __name__, url_prefix='/api/auth')


@auth_bp.route('/signup', methods=['POST'])
def signup():
    """Register a new user"""
    try:
        data = request.get_json()

        if not data or not data.get('name') or not data.get('email') or not data.get('password'):
            return jsonify({'error': 'Missing required fields'}), 400

        email = data['email'].strip().lower()

        if is_memory_mode():
            existing_user = find_user_by_email(email)
            if existing_user:
                return jsonify({'error': 'Email already registered'}), 409

            password_hash = hash_password(data['password'])
            user = create_user(data['name'], email, password_hash)
            token = create_token(user['user_id'], user['email'])

            return jsonify({
                'message': 'User registered successfully',
                'user_id': user['user_id'],
                'name': user['name'],
                'email': user['email'],
                'access_token': token,
            }), 201

        existing_user = fetch_one('SELECT * FROM users WHERE email = %s', (email,))
        if existing_user:
            return jsonify({'error': 'Email already registered'}), 409

        password_hash = hash_password(data['password'])
        user_id = insert_record(
            'INSERT INTO users (name, email, password_hash) VALUES (%s, %s, %s)',
            (data['name'], email, password_hash),
        )
        token = create_token(user_id, email)

        return jsonify({
            'message': 'User registered successfully',
            'user_id': user_id,
            'name': data['name'],
            'email': email,
            'access_token': token,
        }), 201

    except Error as err:
        print(f'Database error in signup: {err}')
        return jsonify({'error': 'Database error: ' + str(err)}), 500
    except Exception as err:
        print(f'Unexpected error in signup: {err}')
        return jsonify({'error': 'Unexpected error: ' + str(err)}), 500


@auth_bp.route('/login', methods=['POST'])
def login():
    """Login user"""
    try:
        data = request.get_json()

        if not data or not data.get('email') or not data.get('password'):
            return jsonify({'error': 'Missing email or password'}), 400

        email = data['email'].strip().lower()

        if is_memory_mode():
            user = find_user_by_email(email)
            if not user or not verify_password(data['password'], user['password_hash']):
                return jsonify({'error': 'Invalid email or password'}), 401

            token = create_token(user['user_id'], user['email'])
            return jsonify({
                'message': 'Login successful',
                'user_id': user['user_id'],
                'name': user['name'],
                'email': user['email'],
                'access_token': token,
            }), 200

        user = fetch_one('SELECT * FROM users WHERE email = %s', (email,))

        if not user or not verify_password(data['password'], user['password_hash']):
            return jsonify({'error': 'Invalid email or password'}), 401

        token = create_token(user['user_id'], user['email'])

        return jsonify({
            'message': 'Login successful',
            'user_id': user['user_id'],
            'name': user['name'],
            'email': user['email'],
            'access_token': token,
        }), 200

    except Error as err:
        return jsonify({'error': str(err)}), 500