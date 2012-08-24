#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from sys import argv
from mount import *
from subprocess import Popen, PIPE
from shlex import split
from mailer import MailTransport, Email

target = argv[len(argv)-1]

umount(target)
mount(target)
files = Popen(split('find "'+target+'" -name "*.exe"'), stdout=PIPE).communicate()[1].strip()
open('exe.list','w').write(files)
files = files.split('\n')
log = ''
while len(files) > 0:
	p1 = scan(files.pop())
	p2 = None
	if len(files) > 0:
		p2 = scan(files.pop())
	p1.wait()
	result = p1.communicate()[1]
	if p2 != None:
		p2.wait()
		result += p2.communicate()[1]
	print result
	log += result

Email(From='Kafka <carpediemd27@web.de>', To='matthias.bock@hu-berlin.de', Subject='Virenscan', Text=log).send( MailTransport(Account='carpediemd27@web.de') )

