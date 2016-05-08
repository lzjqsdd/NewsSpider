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
		searchword = web.input().searchword
		newslist=list()
		if searchword:
			newslist = self.se.QueryPhrase(searchword,False)
		return render.header(searchword,newslist)
	
class news:
	def __init__(self):
		self.se = Search()
	def GET(self):
		searchword = web.input().searchword
		newslist=list()
		if searchword:
			newslist = self.se.QueryPhrase(searchword,False)
		return render.header(searchword,newslist)

if __name__ == "__main__":
	app = web.application(urls,globals())
	app.run()
