import random
import time, requests
from celery import shared_task
from parser.config import EXCHANGERATE_API_KEY
from parser.models import ParsingResult


@shared_task
def make_request_to_exchangerate_api(code: str = "RUB"):
    if not isinstance(code, str):
        raise TypeError(f"parameter 'code' must be string not {type(code)}")

    while True:
        url = f"https://v6.exchangerate-api.com/v6/{EXCHANGERATE_API_KEY}/latest/USD"

        for i in range(10):
            response = requests.get(url)
            if response.status_code != 200:
                time.sleep(2)

            data = response.json()
            if data is None:
                continue

            conversion_rates: dict = data.get("conversion_rates")
            if conversion_rates is None:
                continue

            base_code = data["base_code"] #usd
            currency_value = conversion_rates[f"{code.upper()}"]
            if currency_value is None:
                return

            pv = ParsingResult(base_currency=base_code, to_currency=code, currency_value=currency_value)
            pv.save()
            time.sleep(random.uniform(0.33, 0.78))
        time.sleep(10)