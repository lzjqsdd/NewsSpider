# -*- coding: utf-8 -*- 
import jieba
import json
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

class DivideWord:
	def __init__(self):
		pass
	def parse(self):
		file = open('../news_spider/title.json')

		while True:
			line = file.readline()
			if not line:
				break
			data = json.loads(line)
			seg_list = list(jieba.cut(data['title'], cut_all=True))
			for w in seg_list:
				print w.encode('utf-8'),
			print '\n'

dw = DivideWord()
dw.parse()
