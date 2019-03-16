import sys, os
from default.models import Crypto, Currency, CurrencyPrice
from default.libraries.bitfinex_api import BitfinexApi
from django.conf import settings

class CryptoCurrencyService:
	def add_crypto_currency(request_body):
		if 'crypto' not in request_body:
			raise Exception("Key 'crypto' not present")

		if 'currency' not in request_body:
			raise Exception("Key 'currency' not present")

		currencies = Currency.objects.filter(name=request_body['currency'])
		if len(currencies) == 0:
			currency = Currency()
			currency.name = request_body['currency']
			currency.save()

		cryptos = Crypto.objects.filter(name=request_body['crypto'])
		if len(cryptos) == 0:
			crypto = Crypto()
			crypto.name = request_body['crypto']
			crypto.save()

	def update_crypto(crypto_id, request_body):
		crypto = Crypto.objects.get(id = crypto_id)
		if crypto is None:
			raise Exception("Crypto not found")

		if "deleted" in request_body:
			crypto.deleted = request_body["deleted"]

		if "name" in request_body:
			crypto.name = request_body["name"]

		crypto.save()

	def get_supporter_crypto_currencies_and_run_task():
		scs = settings.VARIABLES['supported_crypto_currencies']
		for sc in scs:
			cryptos = Crypto.objects.filter(name = sc["crypto"])
			currencies = Currency.objects.filter(name = sc["currency"])

			if len(cryptos) == 1 and len(currencies) == 1:
				CryptoCurrencyService.fetch_and_save_crypto_currency_price(cryptos[0], currencies[0])
			else:
				raise Exception("Crypto/currency not found")

	def fetch_and_save_crypto_currency_price(crypto, currency):
		if crypto is None:
			raise Exception("Crypto not found")

		if currency is None:
			raise Exception("Currency not found")

		crypto_currency = ("%s%s" % (crypto.name, currency.name))
		response = BitfinexApi.ticker_api(crypto_currency)
		crypto_currency_prices = CurrencyPrice.objects.filter(crypto = crypto, currency = currency)
		crypto_currency_price = None

		if len(crypto_currency_prices) == 0:
			crypto_currency_price = CurrencyPrice()
			crypto_currency_price.crypto = crypto
			crypto_currency_price.currency = currency
			crypto_currency_price.price = float(response["last_price"])
			crypto_currency_price.low_price = float(response["low"])
			crypto_currency_price.high_price = float(response["high"])
			crypto_currency_price.bid_price = float(response["bid"])
			crypto_currency_price.ask_price = float(response["ask"])

			crypto_currency_price.save()
		elif len(crypto_currency_prices) == 1:
			crypto_currency_price = crypto_currency_prices[0]
			if float(crypto_currency_price.price) != float(response["last_price"]):
				crypto_currency_price.price = float(response["last_price"])
				crypto_currency_price.low_price = float(response["low"])
				crypto_currency_price.high_price = float(response["high"])
				crypto_currency_price.bid_price = float(response["bid"])
				crypto_currency_price.ask_price = float(response["ask"])

				crypto_currency_price.save()