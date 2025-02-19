from rest_framework.response import Response
from rest_framework.views import APIView

from apps.crypto_exchange.serializers import CryptoRatesSerializer
from apps.crypto_exchange.services import ExchangeRateService


class CryptoRatesView(APIView):
    @staticmethod
    def get(request):
        bitcoin_eur = ExchangeRateService.get_bitcoin_price()
        eur_to_gbp = ExchangeRateService.get_eur_to_gbp_rate()
        bitcoin_gbp = ExchangeRateService.calculate_bitcoin_gbp(bitcoin_eur, eur_to_gbp)

        serializer = CryptoRatesSerializer(
            {"bitcoin_eur": bitcoin_eur, "eur_to_gbp": eur_to_gbp, "bitcoin_gbp": bitcoin_gbp, }
        )
        return Response(serializer.data)
