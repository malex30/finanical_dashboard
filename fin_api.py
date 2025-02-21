import finnhub
import os
import pendulum
import psycopg2
from icecream import ic
from dotenv import load_dotenv

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

    cursor.execute("CREATE SCHEMA finnhub;")

    cursor.execute(
        """
    CREATE TABLE
    stocks (
        id SERIAL PRIMARY KEY,
        ticker VARCHAR(255) NOT NULL,
        name VARCHAR(255) NOT NULL,
        price DECIMAL(10,2) NOT NULL
    )
    """
    )
    cursor.execute(
        "SELECT * FROM information_schema.columns WHERE table_name = 'stocks';"
    )
    # Close the cursor and connection
    cursor.close()
    connection.close()
    print("Connection closed.")

except Exception as e:
    print(f"Failed to connect: {e}")

finnhub_api_key = os.getenv("FINNHUB_API_KEY")

# Create a proper client instance
finnhub_client = finnhub.Client(api_key=finnhub_api_key)

now = pendulum.now()
sunday = now.previous(pendulum.SUNDAY)
previous_sunday = sunday.subtract(days=7)
now = now.format("YYYY-MM-DD")
sunday = sunday.format("YYYY-MM-DD")
previous_sunday = previous_sunday.format("YYYY-MM-DD")
ic(now, sunday, previous_sunday)

print(type(finnhub_client))

stocks = {
    # Growth Stocks
    "NVIDIA": "NVDA",
    "Tesla": "TSLA",
    "Palantir Technologies": "PLTR",
    "Accolade Inc.": "ACCD",
    "Akero Therapeutics Inc.": "AKRO",
    "Tempus AI Inc.": "TEM",
    # Large-Cap Tech Stocks
    "Apple": "AAPL",
    "Microsoft": "MSFT",
    "Amazon": "AMZN",
    "Intuit": "INTU",
    "Booking Holdings": "BKNG",
    # Oil & Gas Companies
    "Chevron": "CVX",
    "Exxon Mobil": "XOM",
    "ConocoPhillips": "COP",
    "EOG Resources": "EOG",
    "Occidental Petroleum": "OXY",
    "TotalEnergies": "TTE",
    "BP": "BP",
    "Schlumberger": "SLB",
    "Hess Corporation": "HES",
    "Marathon Petroleum Corporation": "MPC",
    "Phillips 66": "PSX",
}


# for company, ticker in stocks.items():
#     profile = finnhub_client.company_profile2(symbol=ticker)
#     ic(company, profile)


# for company, ticker in stocks.items():
#     news = finnhub_client.company_news(symbol=ticker, _from=previous_sunday, to=sunday)
#     ic(company, ticker, news)
