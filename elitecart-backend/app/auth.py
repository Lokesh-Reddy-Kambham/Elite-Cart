from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash
import os
from datetime import timedelta

def hash_password(password):
    """Hash a password using werkzeug"""
    return generate_password_hash(password)

def verify_password(password, hash):
    """Verify a password against its hash"""
    return check_password_hash(hash, password)

def create_token(user_id, user_email):
    """Create JWT token"""
    from flask_jwt_extended import get_jwt
    expires = timedelta(hours=24)
    # Use string identity for JWT subject to satisfy PyJWT expectations
    access_token = create_access_token(
        identity=str(user_id),
        additional_claims={'email': user_email},
        expires_delta=expires
    )
    return access_token

def get_current_user():
    """Get current user from JWT token"""
    return get_jwt_identity()
