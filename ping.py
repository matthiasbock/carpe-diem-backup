#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from subprocess import Popen, PIPE
from shlex import split

def ping(host, timeout=2):
	return ( 'time=' in Popen(split('ping -c 1 -W '+str(timeout)+' '+host), stdout=PIPE).communicate()[0] )

