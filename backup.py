#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import os
import sys

from ConfigParser import RawConfigParser, NoOptionError
from datetime import datetime
from time import sleep
from subprocess import Popen, PIPE
from shlex import split

from compression import *
from mailer import MailTransport, Email
from mount import mount, umount

def mount_if_necessary(folder):
	if folder.strip() != '':
		return mount(folder)
	return True

def umount_if_necessary(folder):
	if folder.strip() != '':
		return umount(folder)
	return True

def backup_present(target):
	checks = [os.path.exists(test) for test in [target, target+'.tar.bz', target+'.tar.gz', target+'.7z', target+'.zip']]
	return True in checks

# read config file

conf = 'backup.conf'
today = datetime.today().strftime('%Y-%m-%d')
print 'Today is'
print today

if not os.path.exists(conf):
	print 'Error: '+conf+' not found'
	sys.exit(1)

parser = RawConfigParser()
parser.read(conf)
sections = parser.sections()
BackupJobs = []
for section in sections:
	d = {'section':section}
	for key in ['mount_source', 'source', 'mount_target', 'target', 'compress']:
		try:
			d[key] = parser.get(section, key).replace('{{today}}', today).rstrip('/')
		except NoOptionError:
			pass
	BackupJobs.append(d)

# for every Backup Job in the config file:

for job in BackupJobs:
	print 'Creating backup of '+job['source']+' ...'
	start = datetime.now()

	# mount source and target drives

	print '\tmounting '+job['mount_source']+' and '+job['mount_target']+' ...'
	if mount_if_necessary( job['mount_source'] ) and mount_if_necessary( job['mount_target'] ):
		if not backup_present( job['target'] ):
			t = job['target'].split('/')
			parent = '/'.join(t[:len(t)-1])
			print '\tcreating target parent '+parent+' ...'
			Popen(split('mkdir -p '+parent)).wait()
			Popen(split('mkdir -p /var/log/backups')).wait()

			# copy data

			cmd = 'cp -a "'+job['source']+'" "'+job['target']+'"'
			print '\t'+cmd
			open('/var/log/backups/'+today+'-'+job['section']+'.log', 'w').write(Popen(split(cmd), stdout=PIPE, stderr=PIPE).communicate()[0])
			print '\tdone.'
			sleep(10) # give it some time to complete the network transfer!

			# unmount source and target drives

			umount_if_necessary( job['mount_source'] )
			print '\tsource unmounted.'

			bsize = du(job['target'])
			if bsize == 0:
				print 'Something went wrong. The backup is empty ...'
				continue
			backupsize = str(bsize)+' '+job['target']
			print '\t\t'+backupsize
			compressedsize = backupsize
			if 'compress' in job.keys():
				if job['compress'] == 'tar.bz':
					print '\tCompressing ...'
					filename = tar_bzip(job['target'])
					cname = job['target']+'.tar.bz'
					sleep(5) # give it some time to complete the network transfer!
					compressedsize = str(du(cname))+' '+cname
					print '\t'+compressedsize
				elif job['compress'] == '7z':
					print '\tCompressing ...'
					filename = sevenzip(job['target'])
					cname = job['target']+'.7z'
					sleep(5) # give it some time to complete the network transfer!
					compressedsize = str(du(cname))+' '+cname
					print '\t'+compressedsize
				else:
					print 'Warning: Skipping unsupported compression method "'+job['compress']+'"'

			umount_if_necessary( job['mount_target'] )
			print '\ttarget unmounted.'

			# send a mail to the admin

			stop = datetime.now()
			runtime = str(stop-start)
			print 'Script runtime: '
			print runtime

			message = 'Runtime: '+runtime
			message += '\nBackup size: '+str(backupsize)
			if compressedsize != backupsize:
				message += '\nCompressed using '+job['compress']
				message += '\nCompressed size: '+str(compressedsize)

			Email(From='Kafka <carpediemd27@web.de>', To='cadibe-it@googlegroups.com', Subject='Backup erstellt: '+job['section'], Text=message).send( MailTransport(Account='carpediemd27@web.de') )
		else:
			print '\tBackup found. Skipping.'
	else:
		print '\tmount failed.'

print 'Backup routine completed.'

