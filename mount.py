#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from subprocess import Popen
from shlex import split
from time import sleep

def mounted(folder):
	for line in open('/etc/mtab').readlines():
#		print line.split(' ')[1]
		if line.split(' ')[1] == folder:
			return True
	return False

def mount(folder):
	if mounted(folder):
		return True
	Popen(split('mount '+folder)).wait()
	return mounted(folder)

def umount(folder):
	Popen(split('umount -l '+folder)).wait()
	sleep(3)
	return not mounted(folder)

