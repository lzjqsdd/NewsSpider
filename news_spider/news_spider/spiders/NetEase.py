#encoding=utf-8
import scrapy
from news_spider.items import NewsSpiderItem
import json
import time 

class NetEaseSpider(scrapy.Spider):

	start_urls = ['http://snapshot.news.163.com/wgethtml/http+!!news.163.com!/2016-04/17/12.html']
	name='netease'
	allowed_domains=['news.163.com']

	base_url = 'http://snapshot.news.163.com/wgethtml/http+!!news.163.com!'

	def parse(self,response):
		count = 1
		urls = response.xpath("//a/@href").extract()
		for url in urls:
			yield scrapy.Request(url,self.parseNews)

	def parseNews(self,response):
		data = response.xpath("//div[@class='post_content_main']")
		item = NewsSpiderItem()
		time = data.xpath("//div[@class='post_time_source']/text()").extract()
		title = data.xpath("//h1/text()").extract()
		content = data.xpath("//div[@class='post_text']/p/text()").extract()

		if(len(time)!=0 and len(title)!=0 and len(content)!=0):
			item['time'] = time[0][13:-5]
			item['title'] = title[0]
			cc=''
			if(len(content)!=0):
				for c in content:
					cc = cc+c+'\n'
			item['content'] = cc
			yield item

