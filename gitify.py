#!/usr/bin/python

import os
from subprocess import Popen
from shlex import split

# find folders named after dates
dirs = []
for dir in sorted(os.listdir('.')):
	if os.path.isdir(dir) and len(dir) == 10 and dir.count('-') == 2: # e.g. 2013-05-06
		dirs.append(dir)

def run(cmd):
	print '$ '+cmd
	Popen(split(cmd)).wait()

def rsync(src, dst):
	for sub in os.listdir(src):
		subsrc = os.path.join(dir, sub)
		run('rsync -vr --remove-source-files --delete "'+subsrc+'" "'+dst+'"')
		run('rm -R "'+subsrc+'"')

def commit(repodir, comment):
	print '$ cd '+repodir
	path = os.getcwd()
	os.chdir(repodir)
	run('git add .')
	run('git commit -am "'+comment+'"')
	print '$ cd '+path
	os.chdir(path)

# move content to git folder
for dir in dirs:
	print 'syncing '+dir+' ...'
	rsync(dir, 'git/')
	commit('git/', dir)
	print ''
