# -*- coding: utf-8 -*- 
import json
import sys
sys.path.append("..")
import tools.Global as Global
import os
import linecache
import jieba

class Cut:
	def __init__(self):
		pass

	def cutfile(self,path,fliename,size):
		file_data = open(fliename,'r')
		num = 0
		flag = 0
		while True:
			if flag == 1:
				break
			if not os.path.exists(path):
				os.makedirs(path)
			cutfilename = path+'/'+str(num)+'.txt'
			cut_file = open(cutfilename,'wb')
			print 'Generate:'+cutfilename+'...'
			for i in range(0,size):
				line = file_data.readline()
				if not line:
					flag = 1
					break
				data = json.loads(line)
				seg_list = jieba.cut(data['content'],cut_all=False)
				result = ' '.join(seg_list)
				data['content'] = result
				cut_file.write(json.dumps(data)+'\n')
			cut_file.close()
			num+=1

	def cutfileWithoutCut(self,path,fliename,size):
		file_data = open(fliename,'r')
		num = 0
		flag = 0
		while True:
			if flag == 1:
				break
			if not os.path.exists(path):
				os.makedirs(path)
			cutfilename = path+'/'+str(num)+'.txt'
			cut_file = open(cutfilename,'wb')
			print 'Generate:'+cutfilename+'...'
			for i in range(0,size):
				line = file_data.readline()
				if not line:
					flag = 1
					break
				cut_file.write(line)
			cut_file.close()
			num+=1
	
	def getInverseIndexRow(self,recordnum,path,size):
		filenum = (recordnum-1)/size
		linenum = (recordnum-1)%size+1
		cutfilename = path+'/'+str(filenum)+'.txt'
		print cutfilename,linenum
		linecache.clearcache()
		line = linecache.getline(cutfilename,linenum)
		linecache.clearcache()
		data = json.loads(line)
		return line

	def getRow(self,recordnum,path,size):
		filenum = (recordnum-1)/size
		linenum = (recordnum-1)%size+1
		cutfilename = path+'/'+str(filenum)+'.txt'
		print cutfilename,linenum
		linecache.clearcache()
		line = linecache.getline(cutfilename,linenum)
		linecache.clearcache()
		data = json.loads(line)
		return line

#test cutfile
#c = Cut()
#c.cutfileWithoutCut(Global.cutnews_origin_dir,Global.content_dir,Global.filesize)
#c.cutfile(Global.cutnews_dir,Global.content_dir,Global.filesize)

#test getRow
#c = Cut()
#c.getRow(200,Global.cutnews_dir,Global.filesize)
