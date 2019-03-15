from django.urls import path

from . import views
from . import services

urlpatterns = [
    path('', views.index, name='index'),
    path('add_crypto_currency', views.add_crypto_currency, name='add_crypto_currency'),
    path('update_crypto/<int:crypto_id>', views.update_crypto, name='update_crypto'),
    path('fetch_crypto_currency_price', views.fetch_crypto_currency_price, name='fetch_crypto_currency_price'),
    path('trigger_price_fetch', views.trigger_price_fetch, name='trigger_price_fetch'),
]