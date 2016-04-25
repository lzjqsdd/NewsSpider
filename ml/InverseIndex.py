#encoding=utf-8
import jieba
import json
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


file = open('../news_spider/title.json')
worddict = dict()
count=0
while True:
	line = file.readline()
	if not line:
		break
	data = json.loads(line)
	seg_list = list(jieba.cut(data['title'], cut_all=True))
	count+=1
	for w in seg_list:
		if w not in worddict:
			worddict[w] = []	
		worddict[w].append(count)

for i in worddict:
	print i
