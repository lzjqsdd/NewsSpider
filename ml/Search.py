# -*- coding: utf-8 -*- 
import sys
import json
reload(sys)
sys.path.append("..")
sys.setdefaultencoding('utf-8')
from Cut import Cut
import tools.Global as Global
import jieba

class Search:
	def __init__(self):
		self.kw_id = self.loadKW_ID()

	def loadKW_ID(self):
		f = open(Global.inverse_dir+'id.txt')
		line = f.readline()
		kw_id = json.loads(line, encoding='utf-8')
		return kw_id


	def getQueryItem(self,searchWord):
		idx = self.kw_id[searchWord.decode('utf-8')]
		cut = Cut()
		ii_line = cut.getInverseIndexRow(idx,Global.inverse_dir,Global.filesize)
		record =json.loads(ii_line)
		for rec in record:
			line = cut.getRow(int(rec),Global.cutnews_origin_dir,Global.filesize)
			data = json.loads(line)
			print data['title'],'\n',data['time'],'\n',data['content'],'\n'
		


	def getInverseRecord(self,item):
		pass

	def mergeInverseRecord(self,RecordList):
		pass

search = Search()
search.getQueryItem(sys.argv[1])
