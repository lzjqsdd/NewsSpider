#encoding=utf-8
import scrapy
from news_spider.items import NewsSpiderItem
import json
import time 
import re

class NetEaseSpider(scrapy.Spider):

	start_urls = ['http://news.qq.com']
	name='tencent'
	allowed_domains=['news.qq.com']

	base_url = 'http://news.qq.com/b/history/index20160419am.shtml?'
	year = ['2016','2015']
	month = ['12','11','10','09','08','07','06','05','04','03','02','01']
	day = ['31','30','29','28','27','26','25','24','23','22','21',
		   '20','19','18','17','16','15','14','13','12','11','10',
		   '09','08','07','06','05','04','03','02','01']
	tp = ['am','pm']

	def parse(self,response):
		for y in self.year:
			for m in self.month:
				for d in self.day:
					for t in tp:
						url = self.base_url+y+m+d+t+'.shtml?'
						yield scrapy.Request(url,self.parseList)

	
	def parseList(self,response):
		urls = response.xpath("//a/@href").extract()
		for url in urls:
			yield scrapy.Request(url,self.parseNews)

	def parseNews(self,response):
		data = response.xpath("//div[@id='C-Main-Article-QQ']")
		item = NewsSpiderItem()
		time = data.xpath("//span[@class='article-time']/text()").extract()
		title = data.xpath("//div[@class='hd']//h1/text()").extract()
		content = data.xpath("//div[@class='post_text']/p/text()").extract()

		time_pattern = re.compile("[0-9]{4}-[0-9]{2}-[0-9]{2}\s[0-9]{2}:[0-9]{2}")
		if(len(time)!=0 and len(title)!=0 and len(content)!=0):
			item['time'] = time_pattern.findall(time[0])[0]
			item['title'] = title[0]
			cc=''
			if(len(content)!=0):
				for c in content:
					cc = cc+c+'\n'
			item['content'] = cc
			yield item
