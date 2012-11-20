#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from httpclient import HttpClient
from htmlparser import between

def External_IP():
	r = HttpClient()
	r.GET("http://www.wieistmeineip.de/")
	ip = between(r.Page, 'CopyToClipboard(\'', '\'')
	if ip == '':
		ip = between(r.Page, '<h1 class="ip">', '</h1>')
	return ip

if __name__=='__main__':
	print External_IP()

