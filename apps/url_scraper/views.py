from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.url_scraper.models import ScrapedURL
from apps.url_scraper.serializers import ScrapedURLSerializer
from apps.url_scraper.services import ScrapedURLService
from apps.url_scraper.tasks import scrape_url_task


class ScrapedURLViewSet(ModelViewSet):
    queryset = ScrapedURL.objects
    serializer_class = ScrapedURLSerializer
    http_method_names = ['get', 'post', 'delete', ]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        url = serializer.validated_data['url']

        scraped_url = ScrapedURLService.create_scraped_url(url)
        # TODO
        # scrape_url_task.delay(scraped_url.id)
        scrape_url_task(scraped_url.id)

        response_data = self.get_serializer(scraped_url).data
        return Response(response_data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['get'])
    def status(self, request, pk=None):
        scraped_url = get_object_or_404(ScrapedURL, pk=pk)
        return Response({"is_fully_processed": scraped_url.is_fully_processed})
