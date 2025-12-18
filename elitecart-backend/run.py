#!/usr/bin/env python
"""Run the Flask application"""
import sys
import os

# Add the backend directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.main import create_app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)
