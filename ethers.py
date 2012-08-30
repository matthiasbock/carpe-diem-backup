#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from subprocess import Popen, PIPE
from shlex import split

def ether2ip(find_ether):
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

def update_fstab(ip, smbname):
	fstab = open('/etc/fstab').read()
	
ethers = open('/etc/ethers').read()

for line in ethers.split('\n'):
	if len(line) > 6*2+5+2 and '\t' in line:
		s = line.split('\t')
		ether = s[0]
		smbname = s[1]
		ip = ether2ip(ether)
		update_fstab(ip, smbname)
		print smbname+' is at '+ip

