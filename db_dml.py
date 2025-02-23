import os
from dotenv import load_dotenv
import psycopg2

# Load environment variables from .env
load_dotenv()


# Connect to the database
try:
    # conn_string = f"postgresql://postgres:{os.getenv('DB_PASSWORD')}@db.zbpqescwaxctplgpgugz.supabase.co:5432/postgres"
    connection = psycopg2.connect(
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
    )
    print("Connection successful!")
    # conn = psycopg2.connect(conn_string)

    # Create a cursor to execute SQL queries
    cursor = connection.cursor()

    # Example query
    cursor.execute("SELECT NOW();")
    result = cursor.fetchone()
    print("Current Time:", result)

    cursor.execute("CREATE SCHEMA IF NOT EXISTS finnhub;")
    connection.commit()

    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS finnhub.stock_profile (
        id SERIAL PRIMARY KEY,
        country VARCHAR(255) NOT NULL,
        currency VARCHAR(255) NOT NULL,
        exchange VARCHAR(255) NOT NULL,
        ipo VARCHAR(255) NOT NULL,
        marketCapitalization DECIMAL(10,2) NOT NULL,
        name VARCHAR(255) NOT NULL,
        phone VARCHAR(255) NOT NULL,
        share_outstanding DECIMAL(10,2) NOT NULL,
        ticker VARCHAR(255) NOT NULL,
        website VARCHAR(255) NOT NULL,
        logo VARCHAR(255) NOT NULL
    )
    """
    )
    connection.commit()

    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS finnhub.news (
        category VARCHAR(255) NOT NULL,
        datetime VARCHAR(255) NOT NULL,
        headline VARCHAR(255) NOT NULL,
        id SERIAL PRIMARY KEY,
        image VARCHAR(255) NOT NULL,
        related VARCHAR(255) NOT NULL,
        source VARCHAR(255) NOT NULL,
        summary VARCHAR(255) NOT NULL,
        url VARCHAR(255) NOT NULL
    )
    """
    )
    connection.commit()

    # Close the cursor and connection
    cursor.close()
    connection.close()
    print("Connection closed.")

except Exception as e:
    print(f"Failed to connect: {e}")
