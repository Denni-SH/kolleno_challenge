from rest_framework import serializers


class CryptoRatesSerializer(serializers.Serializer):
    bitcoin_eur = serializers.FloatField(required=False)
    eur_to_gbp = serializers.FloatField(required=False)
    bitcoin_gbp = serializers.FloatField(required=False)
