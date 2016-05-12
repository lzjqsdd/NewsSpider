# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sys
sys.path.append("..")
import tools.Global as Global
import os

#init project_root
print "Make Data Root Dir..."
if not os.path.exists(Global.project_root):
	os.makedirs(Global.project_root)
if not os.path.exists(Global.project_root+'data'):
	os.makedirs(Global.project_root+'data')
if not os.path.exists(Global.inverse_dir):
	os.makedirs(Global.inverse_dir)
print 'Done.'
print 'Create Data File...'
if not os.path.exists(Global.content_dir):
	f = open(Global.content_dir,'w')
	f.close()
if not os.path.exists(Global.title_dir):
	f = open(Global.title_dir,'w')
	f.close()
print 'Done.'
