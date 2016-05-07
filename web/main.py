import web
import sys
sys.path.append("..")
from ml.Search import Search

render = web.template.render('templates/')

urls=(
	'/(.*)','index'
)

app = web.application(urls,globals())

class index:
	def __init__(self):
		self.se = Search()
	def GET(self,searchword):
		newslist=list()
		if searchword:
			newslist = self.se.QueryPhrase(searchword,False)
		return render.header(searchword,newslist)
	def POST(self):
		searchword = web.input(searchword=[])
		if searchword:
			newslist = self.se.QueryPhrase(searchword,False)
		return render.header(searchword,newslist)
	
if __name__ == "__main__":
	app = web.application(urls,globals())
	app.run()
