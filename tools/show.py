#!/usr/bin/python
import json
import sys
reload(sys)
import Global
sys.setdefaultencoding( "utf-8" )


class show:
	def shownews(self,type):
		f = open(Global.content_dir,'r')
		while True:
			line = f.readline()
			if not line:
				break
			data = json.loads(line)
			if type == 1:
				print "-->",data['time'],data['title'],data['url'],data['content']
			else:
				print "-->",data['time'],data['title'],data['url']
		f.close()

	def showcount(self):
		f = open(Global.title_dir,'r')
		c=0
		while True:
			line = f.readline()
			if not line:
				break
			c+=1
		f.close()
		print c

	def showitem(self,line):
		data = json.loads(line)
		print "-->",data['time'],data['title'],data['url'],data['content']

	
