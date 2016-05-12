#!/usr/bin/python
import json
import sys
reload(sys)
sys.path.append("..")
import Global
sys.setdefaultencoding( "utf-8" )
from ml.Cut import Cut
from ml.InverseIndex import InverseIndex

print "Cut Data......."
cut = Cut()
cut.cutfileWithoutCut(Global.cutnews_origin_dir,Global.content_dir,Global.filesize)
cut.cutfile(Global.cutnews_dir,Global.content_dir,Global.filesize)
print "Done."

print "Create Invese Index"
ii = InverseIndex()
ii.CalcTFIDF()
print "Done."

