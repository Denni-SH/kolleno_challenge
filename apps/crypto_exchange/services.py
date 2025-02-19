import requests

from apps.crypto_exchange.constants import BITCOIN_RATE_API_REQUEST_URL, CURRENCY_EXCHANGE_API_REQUEST_URL
from apps.url_scraper.constants import URL_REQUEST_TIMEOUT_IN_SECONDS


class ExchangeRateService:
    @staticmethod
    def get_bitcoin_price():
        url = BITCOIN_RATE_API_REQUEST_URL

        try:
            response = requests.get(url, timeout=URL_REQUEST_TIMEOUT_IN_SECONDS)
            response.raise_for_status()
            data = response.json()
            return data.get("last_trade_price")
        except requests.RequestException:
            return None

    @staticmethod
    def get_eur_to_gbp_rate():
        url = CURRENCY_EXCHANGE_API_REQUEST_URL

        try:
            response = requests.get(url, timeout=URL_REQUEST_TIMEOUT_IN_SECONDS)
            response.raise_for_status()
            data = response.json()
            eur_to_gbp = data.get("conversion_rates", {}).get("GBP")
            return eur_to_gbp

        except requests.RequestException as e:
            print(f"ExchangeRate API Error: {e}")
            return None

    @staticmethod
    def calculate_bitcoin_gbp(bitcoin_eur, eur_to_gbp):
        return bitcoin_eur * eur_to_gbp if bitcoin_eur and eur_to_gbp else None
