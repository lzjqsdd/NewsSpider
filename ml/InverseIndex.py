#encoding=utf-8
import jieba
import json
import sys
import Global
reload(sys)
sys.setdefaultencoding('utf-8')


class InverseIndex:

	def __init__(self):
		self.file_data= open(Global.data_dir)
		self.file_sw = open(Global.stopword_dir)
		self.ii = open(Global.inverse_dir,'wb')
		self.stopword=[]
		self.worddict = dict()

	def loadsw(self):
		while True:
			line = self.file_sw.readline()
			if not line:
				break
			self.stopword.append(line)
			print line,

	def loaddata(self):
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

	def write2file(self):
		for w in self.worddict:
			ii.write(w+' '+str(worddict[w])+'\n')

ii = InverseIndex()
ii.loaddata()
ii.write2file()
