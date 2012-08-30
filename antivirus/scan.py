#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from sys import argv
from subprocess import Popen, PIPE
from shlex import split
from mailer import MailTransport, Email


# list files

files = Popen(split('find "'+argv[1]+'" -name "*.exe"'), stdout=PIPE).communicate()[0].strip()
open('exe.list','w').write(files)
files = files.split('\n')
for i in range(len(files)):
	if files[i] == '':
		files.pop(i)

# scan two files at once

def scan(filename):
	return Popen(split('clamscan --infected --no-summary "'+filename+'"'), stdout=PIPE)

def sendmail(log):
	Email(From='Kafka <carpediemd27@web.de>', To='cadibe-it@googlegroups.com', Subject='clamscan @ Kafka: FOUND', Text=log).send( MailTransport(Account='carpediemd27@web.de') )

log = ''
found = False
while len(files) > 0:
	p1 = scan(files.pop())
	p2 = None
	if len(files) > 0:
		p2 = scan(files.pop())
	p1.wait()
	result = p1.communicate()[0].strip()
	print result
	if 'FOUND' in result:
		found = True
		log += result+'\n'
	if p2 != None:
		p2.wait()
		result = p2.communicate()[0].strip()
		print result
		if 'FOUND' in result:
			found = True
			log += result+'\n'
	if len(log) > 5000:
		sendmail(log)
		log = ''

if log != '':
	sendmail(log)

if not found:
	Email(From='Kafka <carpediemd27@web.de>', To='cadibe-it@googlegroups.com', Subject='clamscan @ Kafka: clean', Text=argv[1]).send( MailTransport(Account='carpediemd27@web.de') )
