import re
import time

timee = " - -- 2015-06-15 15:34   "

day = ['31','30','29','28','27','26','25','24','23','22','21',
	   '20','19','18','17','16','15','14','13','12','11','10',
	   '09','08','07','06','05','04','03','02','01']
pattern = re.compile("[0-9]{4}-[0-9]{2}-[0-9]{2}\s[0-9]{2}:[0-9]{2}")
#pattern = re.compile("[0-9]{4}-[0-9]{2}-[0-9]{2}")
#pattern = re.compile("[0-9]")
tm = pattern.findall(timee)[0]

a = time.mktime(time.strptime(tm,'%Y-%m-%d %H:%M'))
print int(a)
