# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json
from items import TitleSpiderItem
import fcntl


class NewsSpiderPipeline(object):
	
	def __init__(self):
		self.file = open('news.json','wb')

	def process_item(self,item,spider):
		fcntl.flock(self.file,fcntl.LOCK_EX)
		line = json.dumps(dict(item))+'\n'
		self.file.write(line)
		fcntl.flock(self.file,fcntl.LOCK_UN)
		return item


class TitlePipeline(object):
	def __init__(self):
		file_title = open('title.json','wb')

	def process_item(self,item,spider):
		fcntl.flock(file_title,fcntl.LOCK_EX)
		title_item = TitleSpiderItem()
		title_item['title'] = item['title']
		title_item['time'] = item['time']
		title_item['url'] = item['url']
		line = json.dumps(dict(title_item))+'\n'
		file_title.write(line)
		fcntl.flock(file_title,fcntl.LOCK_UN)
		return item
