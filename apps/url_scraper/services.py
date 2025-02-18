from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup
from rest_framework import serializers

from apps.url_scraper.constants import URL_REQUEST_TIMEOUT_IN_SECONDS, URL_REQUEST_USER_AGENT
from apps.url_scraper.models import ScrapedURL, ScrapedUrlImage


class ScrapedURLService:
    @staticmethod
    def fetch_url_data(url):
        try:
            response = requests.get(
                url, timeout=URL_REQUEST_TIMEOUT_IN_SECONDS, headers={"User-Agent": URL_REQUEST_USER_AGENT},
            )
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            raise serializers.ValidationError(f"Failed to fetch the URL: {str(e)}")

    @staticmethod
    def parse_html(html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        title = soup.title.string if soup.title else "No Title"
        images = [img["src"] for img in soup.find_all("img") if "src" in img.attrs][:20]
        stylesheets = len(soup.find_all("link", rel="stylesheet"))
        return title, images, stylesheets

    @staticmethod
    def create_scraped_url(url):
        parsed_url = urlparse(url)
        return ScrapedURL.objects.create_initial_url(url, parsed_url.netloc, parsed_url.scheme)

    @staticmethod
    def complete_scraped_url(scraped_url, title, stylesheets, images):
        scraped_url.update_scraped_data(title, stylesheets)
        ScrapedUrlImage.objects.create_images(scraped_url, images)
