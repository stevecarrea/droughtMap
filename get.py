import urllib
import datetime
import os
import socket
socket.setdefaulttimeout(20)

path = "images"

date_list = []

start = datetime.datetime.strptime("2016-11-01", "%Y-%m-%d")
end = datetime.datetime.strptime("2017-04-05", "%Y-%m-%d")
date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]

for date in date_generated:
	date_list.append(date.strftime("%Y%m%d")) 

for i in date_list:
	url = 'http://droughtmonitor.unl.edu/data/jpg/{}/{}_total_date.jpg'.format(i, i)
	filename = '{}.jpg'.format(i)
	fullpath = os.path.join(path, filename)
	if os.path.isfile(fullpath):
		print 'file {} exists'.format(fullpath)
	else:
		ret = urllib.urlopen(url)
		if ret.code == 200:
			print 'saved {}'.format(filename)
			urllib.urlretrieve (url, fullpath)



