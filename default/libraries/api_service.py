import requests

class ApiService:
	def call(method, url, headers, data):
		response = None
		if method == "GET":
			response = requests.get(url, headers=headers)
		elif method == "POST":
			response = requests.post(url, data = data, headers = headers)
		elif method == "PUT":
			response = requests.put(url, data = data, headers = headers)
		else:
			raise Exception("Unknown method: %r" % method)
		
		return response.json()