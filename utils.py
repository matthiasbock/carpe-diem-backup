#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

def ip2str(ip):
	n = []
	for i in range(4):
		n.append(str(ord(ip[i])))
	return '.'.join(n).rjust(4*3+3)

def between(hay, before, after, occurence=1, include=False, include_before=False, include_after=False): # return substring from haystack between "before" and "after"
	haystack = str(hay)
	start = 0
	for i in range(1, occurence):
		start = haystack.find(before, start)+1
	p = haystack.find(before, start)
	if p < 0:
		return ''
	if (not include) and (not include_before):
		p += len(before)
	q = haystack.find(after, p)
	if q < 0:
		q = len(haystack)-1
	else:
		if include or include_after:
			q += len(after)
	return haystack[p:q]

