#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from sys import argv
from subprocess import Popen, PIPE
from shlex import split
from mailer import MailTransport, Email

files = Popen(split('find "'+argv[1]+'" -name "*.exe"'), stdout=PIPE).communicate()[0].strip()
open('exe.list','w').write(files)
files = files.split('\n')
for i in range(len(files)):
	if files[i] == '':
		files.pop(i)

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

Email(From='Kafka <carpediemd27@web.de>', To='cadibe-it@googlegroups.com', Subject='Ergebnisse Viren-Scan', Text=log).send( MailTransport(Account='carpediemd27@web.de') )

