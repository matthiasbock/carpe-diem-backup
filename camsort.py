#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from sys import argv

if len(argv) > 1:
	today = argv[1].split('-')
else:
	from datetime import date
	today = date.today().timetuple()

year = today[0].zfill(4)
month = today[1].zfill(2)
day = today[2].zfill(2)
date_i = year+month+day
date_o = year+'.'+month+'.'+day
wildcard = 'ipcam'+date_i+'*.jpg'
outfile = date_o+'.avi'

# create video from single JPEGs
from subprocess import Popen
from shlex import split
Popen( split('mencoder mf://'+wildcard+' -mf fps=10:type=jpg -ovc copy -oac copy -o '+outfile) ).wait()

# remove JPEGs
#from os.path import exists
#if exists(outfile):
#	Popen( split('rm '+wildcard) ).wait()
