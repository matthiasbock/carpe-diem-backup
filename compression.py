#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import os
from subprocess import Popen, PIPE
from shlex import split
from os import chdir

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

def name_without_path(folder):
	s = folder.split('/')
	return s[len(s)-1]

def getpath(folder):
	s = folder.split('/')
	return '/'.join(s[:-1])

def tar_bzip(folder):
	name = name_without_path(folder)
	filename = name+'.tar.bz'
	chdir( getpath(folder) )
	Popen(split('/bin/tar --remove-files -cjf '+filename+' '+name)).wait()
	chdir('/home/code/carpe-diem-backup')
	return filename

#
# requires p7zip-full to be installed
#

def sevenzip(folder):
	name = name_without_path(folder)
	filename = name+'.7z'
	path = getpath(folder)
#	print path
	chdir(path)
	cmd = '7za a '+filename+' '+name
#	print cmd
	exitstatus = Popen(split(cmd)).wait()
	if exitstatus == 0 and name != '' and (not '*' in name):	# remove
		Popen(split('rm -R '+name)).wait()
	chdir('/home/code/carpe-diem-backup')
	return filename

