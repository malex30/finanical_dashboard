import finnhub
import os
from icecream import ic
from dotenv import load_dotenv

load_dotenv()

finnhub_api_key = os.getenv("FINNHUB_API_KEY")

# Create a proper client instance
finnhub_client = finnhub.Client(api_key=finnhub_api_key)

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
    quote = finnhub_client.quote(ticker)
    ic(company, quote)
