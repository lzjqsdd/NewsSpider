#encoding:utf8
import json
import sys
import Global

class Cut:
	def __init__(self):
#every 30 news in a flie
		self.size = 30
		self.file_data = open(Global.data_dir)

	def cutfile(self,file):
		
		num = 0
		While(True):
			line = self.file_data.readline()
			if not line:
				break

			num+=1
			filename = str(num/self.size)+'.txt'
			if num%self.size != 0:	
				
				
