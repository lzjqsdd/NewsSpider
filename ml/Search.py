# -*- coding: utf-8 -*- 
import sys
import json
reload(sys)
sys.path.append("..")
sys.setdefaultencoding('utf-8')
from Cut import Cut
import tools.Global as Global

class Search:
	def __init__(self):
		self.kw_id = self.loadKW_ID()

	def loadKW_ID(self):
		f = open(Global.inverse_dir+'id.txt')
		line = f.readline()
		kw_id = json.loads(line, encoding='utf-8')
		kwid = dict()
		for ki in kw_id:
			kwid[ki.encode('utf-8')] = kw_id[ki]
		for i in kwid:
		 	print i,kwid[i]
		return kwid


	def getQueryItem(self,searchWord):
		idx = self.kw_id[searchWord]
		cut = Cut()
		line = cut.getRow(idx,Global.cutnews_origin_dir,Global.filesize)
		data = json.loads(line)
		print data['title'],'\n',data['time'],'\n',data['content'],'\n'

	def getInverseRecord(self,item):
		pass

	def mergeInverseRecord(self,RecordList):
		pass

search = Search()
search.getQueryItem(sys.argv[1].decode('utf-8'))
