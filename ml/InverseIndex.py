# -*- coding: utf-8 -*- 
import jieba
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
			seg_list = list(jieba.cut(data['title'], cut_all=True))
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
			seg_list = list(jieba.cut(data['title'],cut_all=True))
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
			seg_list = jieba.cut(data['content'],cut_all=True)
			for seg in seg_list:
				seg=''.join(seg.split())
				if(seg!='' and seg!="\n" and seg!="\n\n"):
					doc.append(seg)
		return doc


	#save inverse table to file
	def write2file(self):
		for w in self.worddict:
			ii.write(w+' '+str(worddict[w])+'\n')



	#calculate tf-idf
	def CalcTFIDF(self):
		docArray = self.loadDataFromCutFile(10000)
		vectorizer = CountVectorizer()
		transformer = TfidfTransformer()
		tfidf = transformer.fit_transform(vectorizer.fit_transform(docArray))
		print 'done'
		#write index-doc to file
		i = 0
		indexdoc = dict()
		f = open(Global.inverse_dir+'id.txt','wb')
		for name in vectorizer.get_feature_names():
			i+=1
			indexdoc[i] = name
		f.write(json.dumps(indexdoc))
		
#test
ii = InverseIndex()
ii.CalcTFIDF()
