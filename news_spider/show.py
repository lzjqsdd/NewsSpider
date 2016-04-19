#!/usr/bin/python
import json

file = open('ne.json')
data = json.load(file)

for article in data:
	print "[----Time-----]\n",article['time']
	print "[----Title----]\n",article['title']
	print "[----Article--]\n",article['content'],"\n\n"
