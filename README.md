## 包含网站：
- 今日头条
- 网易新闻
- 腾讯新闻

## 主要功能
  - 新闻抓取
  - 索引构建
  - 前端搜索

### [整体结构](https://github.com/lzjqsdd/NewsSpider/blob/master/Frame.md)

## 运行

### 一键启动
  直接执行工程目录下的start.sh，可以启动抓取，索引和检索。可以修改tools/Global.py中的project_root路径，默认所有处理的数据均在该目录下

### 同时运行所有爬虫
```shell
git clone https://github.com/lzjqsdd/NewsSpider.git
cd NewsSpider/news_spider
scrapy crawlall
```

### 运行单个爬虫
```shell
scrapy crawl [toutiao|netease|tencent]
```

### 数据及注意事项
  - 抓取的新闻为utf-8格式的，并不是乱码
  - 网易新闻2015年的内容格式和2016的不一样，可以抓取，需要修改xpath解析方式
  - 默认参数可以抓取到13万条左右的数据，
   	- title.json(不含新闻内容)
   	- news.json(含新闻内容)，可以在setting.py中修改默认写入选项
   	- `news2db.py` 可以将json文件写入`sqlite3`数据库
  - 所有的数据配置均可以在tool/Global.py中修改

### TODO
  - 相似新闻推荐
  - 排序算法

### Demo展示
![Demo](https://github.com/lzjqsdd/NewsSpider/blob/master/data/show.png)
