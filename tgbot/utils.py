"""модуль отвечающий за классы для bot.py"""

import requests
from config import CURRENCY as currency


class ConvertException(Exception):
    pass


class Convert:
    @staticmethod
    def convert(cu_fr: str, cu_to: str, amount: int):
        cu_fr_code = currency.get(cu_fr.lower())
        cu_to_code = currency.get(cu_to.lower())

        try:
            r = int(amount)
        except ValueError:
            raise ConvertException(f'Не удалось обработь количество валюты "{amount}"')

        if cu_to not in currency:
            raise ConvertException(f'Не удалось обработать валюту')

        if cu_fr_code == cu_to_code:
            raise ConvertException('Невозможно конвертировать 2 одинаковые валюты')

        url = f"https://api.apilayer.com/exchangerates_data/convert?to={cu_to_code}&from={cu_fr_code}&amount={amount}"
        headers = {
            "apikey": "w3uUpRnQhEF1GjtQ2Bim3VWSdycP9cNv"
        }
        response = requests.get(url, headers=headers)
        data = response.json()
        result = data.get('result')
        return result
