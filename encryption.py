#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from subprocess import Popen, PIPE
from shlex import split
import os

def encrypt(filename, recipient):
	gpgfname = filename+'.gpg'
	cmd = 'gpg --batch --encrypt="'+filename+'" --recipient="'+recipient+'" --output="'+gpgfname+'" --yes' # yes to overwrite
	print cmd
	p = Popen(split(cmd), stdin=PIPE, stdout=PIPE)
	p.stdin.write(open(filename).read())
	p.stdin.close()

	if p.wait() == 0:
		os.delete(filename)
		return True, gpgfname
	else:
		stdout = p.communicate()[0]
		print stdout
		return False, '$ '+cmd+'\n'+stdout

