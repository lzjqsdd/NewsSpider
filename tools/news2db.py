# -*- coding: utf-8 -*- 
#!/usr/bin/python
import json
import re
import sqlite3
import sys
import Global
reload(sys)
sys.setdefaultencoding('utf-8')

file = open(Global.content_dir)
conn = sqlite3.connect('news.db')

# Check table is exist
# Method 1
# cursor = conn.execute("SELECT count(*) FROM sqlite_master WHERE type='table' AND name='news';")
# result = cursor.fetchone()[0]
# Method 2
conn.execute("CREATE TABLE IF NOT EXISTS news (title, content, time, url)")
conn.commit()

while 1:
	line = file.readline()
	if not line:
		break
	line = re.sub("'","’",line)
	data = json.loads(line)
	insertsql = "insert into news(title,content,time,url) values ('"+str(data['title']).decode('utf-8')+"','"+str(data['content'])+"','"+str(data['time']).decode('utf-8')+"','"+str(data['url']).decode('utf-8')+"')"
	print data['title'].decode('utf-8')
	conn.execute(insertsql)
	conn.commit()

conn.close()
