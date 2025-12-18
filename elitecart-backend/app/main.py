from flask import Flask, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Import blueprints
from app.routes.auth import auth_bp
from app.routes.products import products_bp
from app.routes.orders import orders_bp

def create_app():
    """Create and configure Flask app"""
    app = Flask(__name__)
    
    # Configure JWT
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'your-secret-key-change-in-production')
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 86400  # 24 hours
    
    # Initialize JWT Manager
    jwt = JWTManager(app)
    
    # Enable CORS
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    
    # Register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(products_bp)
    app.register_blueprint(orders_bp)
    
    # Health check endpoint
    @app.route('/api/health', methods=['GET'])
    def health_check():
        return jsonify({'status': 'healthy', 'service': 'EliteCart API'}), 200
    
    # Error handlers
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({'error': 'Endpoint not found'}), 404
    
    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({'error': 'Internal server error'}), 500
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)
