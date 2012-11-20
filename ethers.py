#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

#
# reads all mac addresses in /etc/ethers
# and adds/updates the corresponding hostnames (smbhostnames) to/in hosts
#

from subprocess import Popen, PIPE
from shlex import split
from utils import between

def getIP():
	output = Popen(['ifconfig'], stdout=PIPE).communicate()[0]
	return between( between(output, 'eth0', '\n\n'), 	'inet addr:', ' ' )

def ether2ip(find_ether):
	find_ether = find_ether.upper()
	netmask = '.'.join( getIP().split('.')[0:3] )
	reply = Popen(split('nmap -sP '+netmask+'.1-245'), stdout=PIPE).communicate()[0]
	for line in reply.split('\n'):
		if 'Host ' in line and ' up' in line:
			ip = between(line, '(', ')')
		elif 'MAC Address:' in line:
			ether = between(line, ': ', ' ')
			if ether.upper() == find_ether:
				return ip
	return None

def update_hosts(ip, smbname):
	hosts = open('/etc/hosts').read().split('\n')
	found = False
	for i in range(len(hosts)):
		if smbname.upper() in hosts[i].upper():
			hosts[i] = ip+'\t'+smbname
			found = True
			break
	hosts = '\n'.join(hosts)
	if not found:
		hosts += '\n'+ip+'\t'+smbname
	open('/etc/hosts', 'w').write(hosts)
	
ethers = open('/etc/ethers').read()

for line in ethers.split('\n'):
	if len(line) > 6*2+5+1 and '\t' in line:
		s = line.split('\t')
		ether = s[0].strip()
		smbname = ' '.join(s[1:])
		ip = ether2ip(ether)
		if ip is not None:
			update_hosts(ip, smbname)
			print smbname+' is at '+ip
		else:
			print 'could not resolve '+ether+' ('+smbname+')'

