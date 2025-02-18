import finnhub
import os
import pendulum
import psycopg2
from icecream import ic
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

# Establish the connection
conn = psycopg2.connect(
    host=DB_HOST, port=DB_PORT, dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD
)


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


for company, ticker in stocks.items():
    profile = finnhub_client.company_profile2(symbol=ticker)
    ic(company, profile)


for company, ticker in stocks.items():
    news = finnhub_client.company_news(symbol=ticker, _from=previous_sunday, to=sunday)
    ic(company, ticker, news)
