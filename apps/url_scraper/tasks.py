from celery import shared_task

from apps.url_scraper.models import ScrapedURL
from apps.url_scraper.services import ScrapedURLService


@shared_task
def scrape_url_task(scraped_url_id):
    scraped_url = ScrapedURL.objects.get(id=scraped_url_id)

    try:
        html_content = ScrapedURLService.fetch_url_data(scraped_url.url)
        title, images, stylesheets = ScrapedURLService.parse_html(html_content)
        ScrapedURLService.complete_scraped_url(scraped_url, title, stylesheets, images)
    except Exception as e:
        print(f"Error processing {scraped_url.url}: {e}")
