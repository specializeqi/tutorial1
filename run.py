from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

settings = get_project_settings()
settings.set('FEED_URI', 'data/output.json')
settings.set('FEED_FORMAT', 'json')

process = CrawlerProcess(settings)
process.crawl('python_tutorial')
process.start()