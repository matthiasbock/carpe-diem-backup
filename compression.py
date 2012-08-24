#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import os
from subprocess import Popen, PIPE
from shlex import split

def du(folder):
	cmd = 'du -sb "'+folder+'"'
	print '\t'+cmd
	try:
		out = Popen(split(cmd), stdout=PIPE).communicate()[0].split('\t')[0]
		print '\t'+out
		s = int(out)
	except:
		s = 0
	return s

def tar_bzip(folder):
	s = folder.split('/')
	folder = '/'.join(s[:-1])
	name = s[len(s)-1]
	filename = name+'.tar.bz'
	from os import chdir
	chdir(folder)
	Popen(split('/bin/tar --remove-files -cjf '+filename+' '+name)).wait()
#	if name != '' and (not '*' in name):
#		Popen(split('rm -R '+name)).wait()
	chdir('/home/code/carpe-diem-backup')
	return filename

