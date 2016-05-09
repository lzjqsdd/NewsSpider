# -*- coding: utf-8 -*- 
import sys
import json
reload(sys)
sys.path.append("..")
sys.setdefaultencoding('utf-8')
from Cut import Cut
import tools.Global as Global
import jieba
import time

class Search:
	def __init__(self):
		self.kw_id = self.loadKW_ID()

	def loadKW_ID(self):
		f = open(Global.inverse_dir+'id.txt')
		line = f.readline()
		kw_id = json.loads(line, encoding='utf-8')
		return kw_id


	#返回文档号
	def QuerySingle(self,searchWord,ishow):
		if self.kw_id.has_key(searchWord.decode('utf-8')):
			idx = self.kw_id[searchWord.decode('utf-8')]
			cut = Cut()
			ii_line = cut.getInverseIndexRow(idx,Global.inverse_dir,Global.filesize)
			record =json.loads(ii_line)
			if ishow:
				for rec in record:
					line = cut.getRow(int(rec),Global.cutnews_origin_dir,Global.filesize)
					data = json.loads(line)
					print data['title'],'\n',data['time'],'\n',data['content'],'\n'
		#返回单个词项对应的倒排记录表
			return record
		else:
			if isshow:
				print 'Not Exists Record!'
			#调用该函数后需要对结果进行判断
			return dict()
		
	
	#'与'查询：先分词，再合并倒排记录,不考虑权重,返回文档号
	def QueryPhrase(self,searchPhrase,isshow = True):
		words = jieba.cut(searchPhrase.decode('utf-8'),cut_all=False)
		cut = Cut()
		result = set(range(1,100000))
		for word in words:
			if not self.kw_id.has_key(word):
				print 'Not Exist Record'
				return set()
			idx = self.kw_id[word]
			ii_line = cut.getInverseIndexRow(idx,Global.inverse_dir,Global.filesize)
			record =json.loads(ii_line)
			re = set()
			for rec in record:
				re.add(int(rec))
			result = result & re
		if len(result) == 0:
			print 'Not Exists Record!'
		newslist=list()
		count = 0
		for rst in result:
		  	count+=1
		  	if count > Global.listsize:
		  		break
			line = cut.getRow(int(rst),Global.cutnews_origin_dir,Global.filesize)
			data = json.loads(line)
			if isshow:
				print data['title'],'\n',data['time'],'\n',data['content'],'\n'
			tm = time.localtime(int(data['time']))
			data['time'] = time.strftime('%Y-%m-%d %H:%M:%S',tm)
			data['content'] = data['content'][0:Global.snippetsize]
			data['id'] = rst
			newslist.append(data)
		return newslist

	#返回热点新闻
	def QueryHotNews(self):
		pass

	#返回最新新闻
	def QueryByTime(self,searchPhrase):
		newslist = self.QueryPhrase(searchPhrase,False)
		return sorted(newslist,lambda x,y:cmp(y['time'],x['time']))

	def QueryById(self,no):
		no = int(no.decode('utf-8'))
		default = dict()
		default['title'] = "No Such News"
		default['time']=''
		default['content'] = "Oh No!"
		default['url'] = "#"
		if not no:
			return default
		cut = Cut()
		line = cut.getRow(no,Global.cutnews_origin_dir,Global.filesize)
		if line:
			data = json.loads(line)
			return data
		else:
			return default

	
#search = Search()
#search.QueryPhrase(sys.argv[1])
#search.QueryPhrase(sys.argv[1])
