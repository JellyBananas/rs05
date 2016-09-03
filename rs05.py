# -*- coding:utf-8-*-
import urllib
import urllib2
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class RS05:
	def __init__(self, baseurl):
		self.baseURL = baseurl
		self.urlstore   = []
		self.dloadURL   = []

	def getMSG(self):
		try:
		    request  = urllib2.Request(self.baseURL)
		    response = urllib2.urlopen(request)
		    content  = response.read().decode('utf-8')
		    pattern  = re.compile('<h2><a target="_blank.*?href="(.*?)">',re.S)
		    items    = re.findall(pattern,content)
		    for item in items:
		        self.urlstore.append("http://www.rs05.com/"+item)
		    return self.urlstore

		except urllib2.URLError, e:
		    if hasattr(e,"code"):
		        print e.code
		    if hasattr(e,"reason"):
		        print e.reason
	
	def getDload(self,urllist):
		for item in urllist:
			try:
				request  = urllib2.Request(item)
				response = urllib2.urlopen(request)
				content  = response.read().decode('utf-8')
				pattern  = re.compile('<h1>(.*?)</h1>.*?<a target="_self" href="(.*?)">',re.S)
				items    = re.findall(pattern,content)
				for downloadurl in items:
					self.dloadURL.append(downloadurl)

			except urllib2.URLError, e:
				if hasattr(e,"code"):
					print e.code
				if hasattr(e,"reason"):
					print e.reason
		return self.dloadURL

print u"请输入页码："
page 	 	= str(raw_input())
url_main    = 'http://www.rs05.com/'+page
rs05   		= RS05(url_main)
suburl 		= rs05.getMSG()
dlurl  		= rs05.getDload(suburl)

file = open(u"下载地址.txt","w")
for item in dlurl:
	file.write(str(item[0])+"\n")
	file.write(str(item[1])+"\n")
	file.write("\n")


