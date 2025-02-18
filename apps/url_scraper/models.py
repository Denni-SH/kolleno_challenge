from django.db import models

from apps.url_scraper.managers import ScrapedURLManager, ScrapedURLImageManager


class ScrapedURL(models.Model):
    url = models.URLField(max_length=2083)
    domain_name = models.CharField(max_length=255)
    protocol = models.CharField(max_length=5)
    title = models.CharField(max_length=255, null=True, blank=True)
    stylesheets = models.IntegerField(default=0)

    is_fully_processed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = ScrapedURLManager()

    class Meta:
        indexes = [
            models.Index(fields=['created_at'])
        ]
        ordering = ['-created_at', ]

    def __str__(self):
        return self.url

    def update_scraped_data(self, title, stylesheets):
        self.title = title
        self.stylesheets = stylesheets
        self.is_fully_processed = True
        self.save()


class ScrapedUrlImage(models.Model):
    scraped_url = models.ForeignKey(ScrapedURL, related_name="images", on_delete=models.CASCADE)
    image_url = models.URLField()

    objects = ScrapedURLImageManager()

    class Meta:
        indexes = [
            models.Index(fields=['scraped_url']),
        ]

    def __str__(self):
        return f'{self.scraped_url}: {self.image_url}'
