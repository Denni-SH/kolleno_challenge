from django.db import models


class ScrapedURLManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().prefetch_related('images')

    def create_initial_url(self, url, domain_name, protocol):
        scraped_url = self.create(
            url=url,
            domain_name=domain_name,
            protocol=protocol,
            title="Processing...",
            stylesheets=0,
            is_fully_processed=False,
        )

        return scraped_url


class ScrapedURLImageManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().select_related('scraped_url')

    def create_images(self, scraped_url, images):
        if images:
            from apps.url_scraper.models import ScrapedUrlImage
            self.bulk_create(
                [ScrapedUrlImage(scraped_url=scraped_url, image_url=img) for img in images]
            )
