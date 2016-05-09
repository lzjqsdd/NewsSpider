import web
import sys
sys.path.append("..")
from ml.Search import Search

render = web.template.render('templates/')

urls=(
	"/","index",
	"/news","news"
)

app = web.application(urls,globals())

class index:
	def __init__(self):
		self.se = Search()
	def GET(self):
		data = web.input()
		if data:
			searchword = data.searchword
		else:
		 	searchword = ''
		newslist=list()
		if searchword:
			newslist = self.se.QueryByTime(searchword)
		return render.index(searchword,newslist)
	
class news:
	def __init__(self):
		self.se = Search()
	def GET(self):
		data = web.input()
		if data:
			ID = data.id
		else:
		 	ID=''
		news = self.se.QueryById(ID)
		return render.news(news)

if __name__ == "__main__":
	app = web.application(urls,globals())
	app.run()
