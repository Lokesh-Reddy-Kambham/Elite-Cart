import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

load_dotenv()

class Database:
    _connection = None
    
    @classmethod
    def get_connection(cls):
        if cls._connection is None or not cls._connection.is_connected():
            try:
                cls._connection = mysql.connector.connect(
                    host=os.getenv('DB_HOST', 'localhost'),
                    user=os.getenv('DB_USER', 'root'),
                    password=os.getenv('DB_PASSWORD', ''),
                    database=os.getenv('DB_NAME', 'elitecart'),
                    port=int(os.getenv('DB_PORT', 3306))
                )
                print("Database connection successful")
            except Error as err:
                print(f"Error: {err}")
                raise
        return cls._connection
    
    @classmethod
    def close_connection(cls):
        if cls._connection is not None and cls._connection.is_connected():
            cls._connection.close()
            print("Database connection closed")

def execute_query(query, params=None):
    """Execute a single query and return results"""
    connection = Database.get_connection()
    cursor = connection.cursor(dictionary=True)
    try:
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        connection.commit()
        return cursor
    except Error as err:
        connection.rollback()
        print(f"Query Error: {err}")
        raise

def fetch_one(query, params=None):
    """Fetch a single record"""
    connection = Database.get_connection()
    cursor = connection.cursor(dictionary=True)
    try:
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        result = cursor.fetchone()
        return result
    finally:
        cursor.close()

def fetch_all(query, params=None):
    """Fetch all records"""
    connection = Database.get_connection()
    cursor = connection.cursor(dictionary=True)
    try:
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        results = cursor.fetchall()
        return results
    finally:
        cursor.close()

def insert_record(query, params):
    """Insert a record and return the last insert ID"""
    connection = Database.get_connection()
    cursor = connection.cursor(dictionary=True)
    try:
        cursor.execute(query, params)
        connection.commit()
        last_id = cursor.lastrowid
        return last_id
    except Error as err:
        connection.rollback()
        print(f"Insert Error: {err}")
        raise
    finally:
        cursor.close()

def update_record(query, params):
    """Update records"""
    connection = Database.get_connection()
    cursor = connection.cursor(dictionary=True)
    try:
        cursor.execute(query, params)
        connection.commit()
        rows_affected = cursor.rowcount
        return rows_affected
    except Error as err:
        connection.rollback()
        print(f"Update Error: {err}")
        raise
    finally:
        cursor.close()

def delete_record(query, params):
    """Delete records"""
    connection = Database.get_connection()
    cursor = connection.cursor(dictionary=True)
    try:
        cursor.execute(query, params)
        connection.commit()
        rows_affected = cursor.rowcount
        return rows_affected
    except Error as err:
        connection.rollback()
        print(f"Delete Error: {err}")
        raise
    finally:
        cursor.close()
