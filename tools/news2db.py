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
cursor = conn.execute("SELECT name FROM sqlite_master WHERE type='table';")
result = cursor.fetchall()
tables = [tables[0] for tables in result]
if 'news' not in tables:
    conn.execute("CREATE TABLE news (title, time, url)")
    conn.commit()

while 1:
	line = file.readline()
	if not line:
		break
	line = re.sub("'","’",line)
	data = json.loads(line)
	insertsql = "insert into news(title,time,url) values ('"+str(data['title']).decode('utf-8')+"','"+str(data['time']).decode('utf-8')+"','"+str(data['url']).decode('utf-8')+"')"
	print insertsql
	conn.execute(insertsql)
	conn.commit()

conn.close()
