from default.libraries.api_service import ApiService
class BitfinexApi:
	def get_ticker_api():
		return "https://api.bitfinex.com/v1/pubticker"

	def get_default_headers():
		return {}

	def ticker_api(crypto_currency):
		if crypto_currency is None:
			raise Exception("Crypto currency can't be empty")

		url = ("%s/%s" % (BitfinexApi.get_ticker_api(), crypto_currency))

		response = ApiService.call("GET", url, BitfinexApi.get_default_headers(), None)
		return response