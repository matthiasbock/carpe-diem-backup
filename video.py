#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from subprocess import Popen
from shlex import split

def make(files, type, fps=1):
	Popen(split('rm output.avi '+files)).wait()
	Popen(split('mencoder mf://'+files+' -mf w=640:h=480:fps='+str(fps)+':type='+type+' -vf scale=640:480:1 -ovc lavc -lavcopts keyint=5 -oac copy -o output.avi')).wait()

