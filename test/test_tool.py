import sys
sys.path.append("..")
from tools.show import show
import tools.Global as Global
from ml.Cut import Cut

s = show()
#s.showcount()
#s.shownews(1)
s.showKeyWord()
#s.showitem(2608)

#c = Cut()
#line = c.getRow(50,Global.cutnews_origin_dir,Global.filesize)
#s.showitem(line)
