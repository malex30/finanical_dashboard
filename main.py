import finnhub
import os
import pendulum
import pandas as pd
import pprint as pp
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

STOCK_MARKET_CLOSE = False

finnhub_api_key = os.getenv("FINNHUB_API_KEY")

# Create a proper client instance
finnhub_client = finnhub.Client(api_key=finnhub_api_key)

now = pendulum.now()
sunday = now.previous(pendulum.SUNDAY)
saturday = now.previous(pendulum.SATURDAY)
previous_sunday = sunday.subtract(days=7)
now = now.format("YYYY-MM-DD")
sunday = sunday.format("YYYY-MM-DD")
previous_sunday = previous_sunday.format("YYYY-MM-DD")
saturday = saturday.format("YYYY-MM-DD")
print(now, sunday, previous_sunday)

print(finnhub_client.market_status(exchange="US"))

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


df = pd.DataFrame(stocks_profiles)

pp.pprint(stocks_profiles)

stocks_df = pd.DataFrame.from_dict(stocks)
print(stocks_df.head(10))

news_df = pd.DataFrame.from_dict(news)
print(news_df.head(10))
