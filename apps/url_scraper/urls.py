from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ScrapedURLViewSet

router = DefaultRouter()
router.register(r'urls', ScrapedURLViewSet, basename='scraped-url')


urlpatterns = [
    path('', include(router.urls)),
]
