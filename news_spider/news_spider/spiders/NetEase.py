#encoding=utf-8
import scrapy
from news_spider.items import NewsSpiderItem
import json
import time 
import re

class NetEaseSpider(scrapy.Spider):

	start_urls = ['http://snapshot.news.163.com/wgethtml/http+!!news.163.com!/2016-04/17/12.html']
	name='netease'
	allowed_domains=['news.163.com']

	base_url = 'http://snapshot.news.163.com/wgethtml/http+!!news.163.com!'
#	year = ['2016','2015']
#	month = ['12','11','10','09','08','07','06','05','04','03','02','01']
#	day = ['31','30','29','28','27','26','25','24','23','22','21',
#	   '20','19','18','17','16','15','14','13','12','11','10',
#		   '09','08','07','06','05','04','03','02','01']
	year = ['2016']
	month = ['03']
	day = ['31','30','29','28','27','26','25','24','23','22','21']

	def parse(self,response):
		for y in self.year:
			for m in self.month:
				for d in self.day:
					url = self.base_url+'/'+y+'-'+m+'/'+d+'/12.html'
					yield scrapy.Request(url,self.parseList)

	
	def parseList(self,response):
		urls = response.xpath("//a/@href").extract()
		for url in urls:
			yield scrapy.Request(url,self.parseNews)

	def parseNews(self,response):
		data = response.xpath("//div[@class='post_content_main']")
		item = NewsSpiderItem()
		timee = data.xpath("//div[@class='post_time_source']/text()").extract()
		title = data.xpath("//h1/text()").extract()
		content = data.xpath("//div[@class='post_text']/p/text()").extract()

		time_pattern = re.compile("[0-9]{4}-[0-9]{2}-[0-9]{2}\s[0-9]{2}:[0-9]{2}")
		if(len(timee)!=0 and len(title)!=0 and len(content)!=0):
			tm = time_pattern.findall(timee[0])[0]
			item['time'] = int(time.mktime(time.strptime(tm,'%Y-%m-%d %H:%M')))
			item['title'] = title[0]
			item['url'] = response.url
			cc=''
			if(len(content)!=0):
				for c in content:
					cc = cc+c+'\n'
			item['content'] = cc
			yield item
