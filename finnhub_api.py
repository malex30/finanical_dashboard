import ratelimit
import finnhub
import os
import pendulum
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

finnhub_api_key = os.getenv("FINNHUB_API_KEY")
# Create a proper client instance
finnhub_client = finnhub.Client(api_key=finnhub_api_key)

# Global rate limiter
rate_limiter = ratelimit.RateLimiter(max_calls=30, period=1)


# Decorator to wrap API calls
def rate_limited(func):
    def wrapper(*args, **kwargs):
        if rate_limiter.is_rate_limited():
            # Introduce a delay or raise an exception
            pendulum.sleep(1 / 30)
        return func(*args, **kwargs)

    return wrapper


@rate_limited
def get_company_news(ticker, start_date, end_date) -> dict:
    """
    Args:
      symbol REQUIRED
      Company symbol.

      from REQUIRED
      format is YYYY-MM-DD.

      to REQUIRED
      format is YYYY-MM-DD.

      Returns:
        List latest company news by symbol
    """
    return finnhub_client.company_news(symbol=ticker, _from=start_date, _to=end_date)


@rate_limited
def get_company_profile(ticker) -> dict:
    """
    Args:
      symbol optional
      Symbol of the company: AAPL e.g.

      isin optional
      ISIN

      cusip optional
      CUSIP

    Examples:
      /stock/profile2?symbol=AAPL
      /stock/profile2?isin=US5949181045
      /stock/profile2?cusip=023135106

    Returns:
      company profile

    """
    return finnhub_client.company_profile2(symbol=ticker)
