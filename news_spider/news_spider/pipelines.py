# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json
from items import TitleSpiderItem
import threading


class NewsSpiderPipeline(object):
	lock = threading.Lock()
	file = open('../data/news.json','a')
	
	def __init__(self):
		pass

	def process_item(self,item,spider):
		line = json.dumps(dict(item))+'\n'
		try:
			NewsSpiderPipeline.lock.acquire()	
			NewsSpiderPipeline.file.write(line)
		except:
			pass
		finally:
		 	NewsSpiderPipeline.lock.release()
		return item
	def spider_closed(self,spider):
		pass


class TitlePipeline(object):
	lock = threading.Lock()
	file_title = open('../data/title.json','a')

	def __init__(self):
		pass
	def process_item(self,item,spider):
		title_item = TitleSpiderItem()
		title_item['title'] = item['title']
		title_item['time'] = item['time']
		title_item['url'] = item['url']
		line = json.dumps(dict(title_item))+'\n'

		try:
			TitlePipeline.lock.acquire()
			TitlePipeline.file_title.write(line)
		except:
			pass
		finally:
			TitlePipeline.lock.release()
		return item

	def spider_closed(self,spider):
		pass
