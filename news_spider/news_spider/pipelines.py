# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json


class NewsSpiderPipeline(object):
	
	def process_item(self,item,spider):
		return item


class TouTiaoPipeline(object):
	def __init__(self):
#		self.file = codecs.open('toutiao.json','wb',encoding='utf-8')
		self.file = open('toutiao.json','wb')

	def process_item(self,item,spider):
		line = json.dumps(dict(item))+'\n'
#		self.file.write(line.decode("unicode_escape"))
		self.file.write(line)
		return item
