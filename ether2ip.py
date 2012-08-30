#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from subprocess import Popen, PIPE
from shlex import split

def resolve(find_ether):	# string of 6 chars
	from utils import between
	netmask = '192.168.3'
	reply = Popen(split('nmap -sP '+netmask+'.1-245'), stdout=PIPE).communicate()[0]
	for line in reply.split('\n'):
		if 'appears to be up' in line:
			ip = ''.join([chr(int(e)) for e in between(line, '(', ')').split('.')])
		elif 'MAC Address:' in line:
			ether = ''.join([chr(int(e,16)) for e in between(line, ': ', ' ').split(':')])
			if ether == find_ether:
				return ip	# returns string of 4 chars

if __name__ == '__main__':
	from utils import ip2str
	print ip2str( resolve('\x00\x1d\x19\xb5\x06\xd0') )

