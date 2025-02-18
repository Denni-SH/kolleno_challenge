from django.contrib import admin

from apps.url_scraper.models import ScrapedURL, ScrapedUrlImage

admin.site.register(ScrapedURL)
admin.site.register(ScrapedUrlImage)
