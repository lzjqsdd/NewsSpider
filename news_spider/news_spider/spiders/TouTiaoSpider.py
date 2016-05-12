#encoding=utf-8
import scrapy
from news_spider.items import NewsSpiderItem
import json
import time 
class TouTiaoSpider(scrapy.Spider):

	name = 'toutiao'
	allowed_domains = ["toutiao.com"]
	start_urls = [
	'http://toutiao.com/articles_news_society/p1'
	]
	base_class_url = 'http://toutiao.com/articles_news_society'
	base_url = 'http://toutiao.com'
#maxpage = 501;#允许爬的最大的页数
	maxpage = 5;#允许爬的最大的页数
	category = ['articles_news_society','articles_news_entertainment',
	'articles_movie','articles_news_tech','articles_digital',
	'articels_news_sports','articles_news_finance','articles_news_military',
	'articles_news_culture','articles_science_all'
	]

#请求每一个分类,按页数来
	def parse(self,response):
		for ctg in self.category:
			for page in range(0,self.maxpage):
				url = self.base_url+'/'+ctg+'/p'+str(page)
				yield scrapy.Request(url,self.parseNewsHref)

#解析每页新闻列表的地址
	def parseNewsHref(self,response):
		urls = response.xpath("//div[@class='info']//a/@href").extract()
		for url in urls:
			news_url = self.base_url+url
			yield scrapy.Request(news_url,self.parseNews)

#解析具体新闻内容 
	def parseNews(self,response):
		articles = response.xpath("//div[@id='pagelet-article']")
		item = NewsSpiderItem()
		title = articles.xpath("//div[@class='article-header']/h1/text()").extract()[0]
		tm = articles.xpath("//div[@id='pagelet-article']//span[@class='time']/text()").extract()[0]
		content = articles.xpath("//div[@class='article-content']//p/text()").extract()

		if(len(title)!=0 and len(tm)!=0 and len(content)!=0):
			item['title'] = title
			item['time'] = int(time.mktime(time.strptime(tm,'%Y-%m-%d %H:%M')))
			item['url'] = response.url
			cc=''
			if(len(content) != 0):
				for c in content:
					cc = cc+c+'\n'
				item['content'] = cc
				yield item

	def printC(self,text):
		for t in text:
			print t.encode('utf-8')
