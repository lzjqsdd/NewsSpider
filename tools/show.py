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
		f = open(Global.content_dir,'r')
		c=0
		while True:
			line = f.readline()
			if not line:
				break
			c+=1
		f.close()
		print c
		return c

	def showitem(self,line):
		data = json.loads(line)
		print "-->",data['time'],data['title'],data['url'],data['content']

	
	def showKeyWord(self):
		f = open(Global.inverse_dir+'id.txt','r')
		line = f.readline()
		data = json.loads(line)
		print 'load keyword done.'
		print type(data)
		print len(data)
#		for k in data.keys():
#			print k,data[k]

