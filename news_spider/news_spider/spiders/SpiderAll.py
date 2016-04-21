import scrapy
from scrapy.crawler import CrawlerProcess
from TouTiaoSpider import TouTiaoSpider
from NetEase import NetEaseSpider

process = CrawlerProcess()
process.crawl(TouTiaoSpider)
process.crawl(NetEaseSpider)
process.start()

