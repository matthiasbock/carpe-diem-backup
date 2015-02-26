#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from httpclient import HttpClient
from htmlparser import between

def External_IP():
	r = HttpClient()
	r.GET("http://www.wieistmeineip.de/")
	ip = between(r.Page, '<strong>', '</strong>')
	return ip

if __name__=='__main__':
	print External_IP()

