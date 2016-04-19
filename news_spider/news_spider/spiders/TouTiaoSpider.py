import scrapy
from news_spider.items import NewsSpiderItem
import json
import time 
class TouTiaoSpider(scrapy.Spider):

	name = 'toutiao'
	allowed_domains = ["toutiao.com"]
	start_urls = [
	'http://toutiao.com/articles_news_society'
	]
	base_class_url = 'http://toutiao.com/articles_news_society'
	base_url = 'http://toutiao.com'
	page = 1;

	def parse(self,response):
		print self.page
		urls = response.xpath("//div[@class='info']//a/@href").extract()
		for url in urls:
			news_url = self.base_url+url
			yield scrapy.Request(news_url,self.parseNews)
		self.page+=1
		if(self.page <=30):
			yield scrapy.Request(self.base_class_url+'/p'+str(self.page))
		 
	def parseNews(self,response):
		articles = response.xpath("//div[@id='pagelet-article']")
		for article in articles:
			item = NewsSpiderItem()
			item['title'] = article.xpath("//div[@class='article-header']/h1/text()").extract()[0]
			item['time'] = article.xpath("//div[@id='pagelet-article']//span[@class='time']/text()").extract()[0]
			content = article.xpath("//div[@class='article-content']//p/text()").extract()
#item['content'] = article.xpath("//div[@class='article-content']//p/text()").extract()
			cc=''
			if(len(content) != 0):
				for c in content:
					cc = cc+c
				item['content'] = cc
			yield item

	def printC(self,text):
		for t in text:
			print t.encode('utf-8')
