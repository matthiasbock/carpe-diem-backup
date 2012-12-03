#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import os
import sys

sys.exit()



from ConfigParser import RawConfigParser
from subprocess import Popen
from shlex import split
import re

from mailer import MailTransport, Email
from wieistmeineip import External_IP

# setup
conf = 'expire.conf'
if not os.path.exists(conf):
	print 'Error: '+conf+' not found'
	sys.exit(1)

# config
parser = RawConfigParser()
parser.read(conf)
mailto = parser.get('logs', 'mailto')

# for every section in the config file:

def delete(backup):
	if len(backup) > len('/home/Backups/') and ('/home/Backups/' in backup or '/media/Thecus/Backups/' in backup):
		Popen(split('rm -fR '+backup)).wait()
		Email(To=mailto, Subject='Altes Backup geloescht: '+backup).send( MailTransport() )
	else:
		Email(To=mailto, Subject='GEFAEHRLICHER FEHLER: Fehlerhafter Loeschbefehl', Text='Path: '+backup).send( MailTransport() )

for section in parser.sections():
	if section != 'logs':
		folder = parser.get(section, 'target')
		expire = int(parser.get(section, 'expire'))
		print 'Checking: '+folder+' ...'
		if os.path.exists(folder):
			backups = []
			for backup in sorted(os.listdir(folder)):
				if re.match(r'[0-9]{4}-[0-9]{2}-[0-9]{2}', backup) != None:
					backups.append(os.path.join(folder,backup))
			print '\t'+str(len(backups))+' backups, '+str(expire)+' max.'
			if len(backups) > expire:
				for i in range(len(backups)-expire):
					print '\tdeleting '+backups[i]+' ...'
					delete(backups[i])
			

print 'Done.'
