#encoding=utf-8
import jieba



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
			print seg_list
