import mysql.connector
from mysql.connector import errorcode

def create_database():
    try:
        # Connect to MySQL server (no database specified yet)
        conn = mysql.connector.connect(
            host="localhost",
            user="root",       # change if needed
            password=""        # add your password here
        )
        cursor = conn.cursor()

        # Try creating the database (won't fail if exists because of IF NOT EXISTS)
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

        print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("❌ Something is wrong with your user name or password.")
        else:
            print(f"❌ Failed to connect or create database: {err}")

    finally:
        # Cleanup: Close cursor and connection if they exist
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'conn' in locals() and conn.is_connected():
            conn.close()

if __name__ == "__main__":
    create_database()
