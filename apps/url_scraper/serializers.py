from urllib.parse import urlparse

from rest_framework import serializers

from apps.url_scraper.models import ScrapedURL, ScrapedUrlImage


class ScrapedUrlImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScrapedUrlImage
        fields = ['image_url', ]


class ScrapedURLSerializer(serializers.ModelSerializer):
    images = ScrapedUrlImageSerializer(many=True, read_only=True)
    url = serializers.URLField(required=True, allow_blank=False)
    domain_name = serializers.CharField(required=False)
    protocol = serializers.CharField(required=False)

    class Meta:
        model = ScrapedURL
        fields = '__all__'

    @staticmethod
    def validate_url(value):
        parsed_url = urlparse(value)
        if not parsed_url.scheme or not parsed_url.netloc:
            raise serializers.ValidationError("Invalid URL format.")
        return value


class CreateScrapedURLSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScrapedURL
        fields = '__all__'
