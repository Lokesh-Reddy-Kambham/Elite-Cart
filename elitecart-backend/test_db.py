#!/usr/bin/env python
"""Test database connection"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.database import Database

try:
    conn = Database.get_connection()
    if conn.is_connected():
        print("✅ Database connection successful!")
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SHOW TABLES;")
        tables = cursor.fetchall()
        print(f"✅ Tables found: {tables}")
        cursor.close()
    else:
        print("❌ Database connection failed")
except Exception as e:
    print(f"❌ Error: {e}")
