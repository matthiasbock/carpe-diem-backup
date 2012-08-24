#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from robot import Robot
from htmlparser import between

def External_IP():
	r = Robot()
	r.GET("http://www.wieistmeineip.de/")
	ip = between(r.Page, 'CopyToClipboard(\'', '\'')
	if ip == '':
		ip = between(r.Page, '<h1 class="ip">', '</h1>')
	return ip

