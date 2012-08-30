#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from subprocess import Popen, PIPE
from shlex import split

def resolve(find_ether):
	from utils import between
	find_ether = find_ether.upper()
	netmask = '192.168.3'
	reply = Popen(split('nmap -sP '+netmask+'.1-245'), stdout=PIPE).communicate()[0]
	for line in reply.split('\n'):
		if 'appears to be up' in line:
			ip = between(line, '(', ')')
		elif 'MAC Address:' in line:
			ether = between(line, ': ', ' ')
			if ether.upper() == find_ether:
				return ip
	return None

if __name__ == '__main__':
	print resolve('00:1d:19:b5:06:d0')

