from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from default.services.crypto_currency_service import CryptoCurrencyService
from background_task import background

def index(request):
	return HttpResponse("Hello, world. You're at the polls index.")

@csrf_exempt
def add_crypto_currency(request):
	request_body = json.loads(request.body)
	CryptoCurrencyService.add_crypto_currency(request_body)
	return HttpResponse('')

@csrf_exempt
def update_crypto(request, crypto_id):
	request_body = json.loads(request.body)
	CryptoCurrencyService.update_crypto(crypto_id, request_body)
	return HttpResponse('')

def fetch_crypto_currency_price(request):
	CryptoCurrencyService.fetch_and_save_crypto_currency_price(3, 2)
	return HttpResponse('')

def trigger_price_fetch(request):
	schedule_task(repeat=3)
	return HttpResponse('')

@background(schedule=3)
def schedule_task():
	print ("Started")
	CryptoCurrencyService.fetch_and_save_crypto_currency_price(3, 2)
	print ("Done")
