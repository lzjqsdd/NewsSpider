#-*- coding: utf-8 -*- 

#项目根目录
project_root="../testdata/"
#project_root="../"
#抓取内容不包含新闻正文的数据文件
title_dir = project_root+"data/title.json"
#抓取内容包含新闻正文内容的数据文件
content_dir=project_root+"data/news.json"
#以sqlite文件存放的数据，暂未用到
db_dir = project_root+"data/news.db"
#停用词文件位置
#stopword_dir=project_root+"data/stopword.txt"
stopword_dir="stopword.txt"
#倒排索引的文件目录，以分块方式存储，包含的id.txt为字典
inverse_dir=project_root+"data/inversedata/"
#对抓取新闻分块切割，并提取关键词后的位置
cutnews_dir=project_root+"data/cutnews/"
#只做简单的分割，方便索引新闻的展示
cutnews_origin_dir=project_root+"data/orinews"
#每个分块文件记录的条数
filesize = 100
#控制摘要的大小
snippetsize = 500
#控制首页新闻的个数，避免加载过多
listsize = 15
