#!/usr/bin/python
import json
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

file = open(sys.argv[1])
c=0
while 1:
	line = file.readline()
	if not line:
		break
	data = json.loads(line)
	c+=1
	print data['time'],data['title'],data['url']

#data = json.load(file)
#c = 0
#for article in data:
#	c+=1
#	print "[----Time-----]\n",article['time'],article['title']
#	print "[----Title----]\n",article['title']
#	print article['time'],article['title']
#	print "[----Article--]\n",article['content'],"\n\n"

print c
