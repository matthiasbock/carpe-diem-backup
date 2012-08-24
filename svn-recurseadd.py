#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from subprocess import Popen, PIPE
from shlex import split
import sys



find = Popen(split('find . -name "*"'), stdout=PIPE).communicate()[0]

for filename in find.strip().split('\n'):
	if not '/.svn' in filename:
		Popen(split('svn add "'+filename+'"')).wait()

