# -*- coding: utf-8 -*- 
import jieba
import jieba.analyse as analyse
import json
import sys
reload(sys)
sys.path.append("..")
sys.setdefaultencoding('utf-8')
import tools.Global as Global
from Cut import Cut
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from tools.show import show
import numpy as np


class InverseIndex:

	def __init__(self):
		self.file_data= open(Global.title_dir)
		self.file_sw = open(Global.stopword_dir)
#self.ii = open(Global.inverse_dir,'wb')
		self.stopword=[]
		self.worddict = dict()

	#load stopword list
	def loadsw(self):
		while True:
			line = self.file_sw.readline()
			if not line:
				break
			self.stopword.append(line)
			print line,

	#load origin data:news.json,title.json
	def CalcInverseIndex(self):
		self.loadsw()
		count=0
		while True:
			line = self.file_data.readline()
			if not line:
				break
			data = json.loads(line)
			seg_list = list(jieba.cut(data['title'], cut_all=False))
			count+=1
			for w in seg_list:
				if w not in self.worddict:
					self.worddict[w] = []
				if w not in self.stopword:
					print w,
					self.worddict[w].append(count)

	def loadDataFromFile(self):
		doc = []
		f = open(Global.content_dir,'r')
		while True:
			line = f.readline()
			if not line:
				break
			data = json.loads(line)
			seg_list = list(jieba.cut(data['title'],cut_all=False))
			doc.append(seg_list)
		return doc


	def loadDataFromCutFile(self,totalnum):
		doc = []
		cut = Cut()
		for i in range(1,totalnum):
			line = cut.getRow(i,Global.cutnews_dir,Global.filesize)
			if not line:
				break
			data = json.loads(line)
			keyword = analyse.extract_tags(data['content'],topK=20)
			seg = " ".join(keyword)
			print seg
			doc.append(seg)
		return doc


	#calculate tf-idf
	def CalcTFIDF(self):
		sh = show()
		count = sh.showcount()
		docArray = self.loadDataFromCutFile(count)
        #docArray = self.loadDataFromCutFile(10)
		vectorizer = CountVectorizer()
		transformer = TfidfTransformer()
		tfidf = transformer.fit_transform(vectorizer.fit_transform(docArray))
		print 'done'
		#write index-doc to file
		i = 0
		indexdoc = dict()
		f = open(Global.inverse_dir+'id.txt','wb')
		word = vectorizer.get_feature_names()
		for name in vectorizer.get_feature_names():
			i+=1
			indexdoc[name] = i
		f.write(json.dumps(indexdoc))
		f.close()
		
		colnum = tfidf.shape[1]
		#for i in range(0,colnum):
		#	filename = Global.inverse_dir+str(i/Global.filesize)+'.txt'
		#	f = open(filename,'a')
		#	idx_list = dict()
		#	for j in range(0,row):
		#		val = tfidf[j,i]
		#		if val > 0:
		#			idx_list[j+1] = val
		#	f.write(json.dumps(idx_list)+'\n')
		#	f.close()
		#i表示词项的编号，row表示非零文档所在的行
		for i in range(0,colnum):
			filename = Global.inverse_dir+str(i/Global.filesize)+'.txt'
			coldata = tfidf.getcol(i)
			col_nonzero_index = np.nonzero(coldata)
			item_weight_dict = dict()
			for row in col_nonzero_index[0]:
				item_weight_dict[row+1] = coldata[row][0].data[0]
			f = open(filename,'a')
			f.write(json.dumps(item_weight_dict)+'\n')
			f.close()
			print 'item ',i,'calculate done'
			

	def WriteInverseIndex(self,mat):
		pass
		
		
#test
#ii = InverseIndex()
#ii.CalcTFIDF()
#ii.loadDataFromCutFile(20)
