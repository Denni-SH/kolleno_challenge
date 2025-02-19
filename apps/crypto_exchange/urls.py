from django.urls import path

from .views import CryptoRatesView

urlpatterns = [
    path("crypto_rates/", CryptoRatesView.as_view(), name="crypto-rates"),
]
