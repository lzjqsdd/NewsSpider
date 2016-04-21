#!/usr/bin/python
import json
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

file = open(sys.argv[1])
data = json.load(file)

c = 0
for article in data:
	c+=1
	print article['time'],"--------",article['title']
#	print "[----Time-----]\n",article['time'],article['title']
#	print "[----Title----]\n",article['title']
#	print "[----Article--]\n",article['content'],"\n\n"
print c
