#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import sys, os
home = sys.argv[1]
os.chdir(home)

def make_mjpeg(files, moviename):
	from subprocess import Popen
	from shlex import split
	from shutil import move
	print str(len(files))+' jpegs'
	os.mkdir('tmp')
	for file in files:
		move(file, 'tmp/')
	os.chdir('tmp')
	Popen(split('mencoder mf://*.jpg -mf fps=1:type=jpg -ovc copy -oac copy -o ../'+moviename)).wait()
	os.chdir('..')
	if os.path.exists(moviename) and os.path.getsize(moviename) > 0:
		for file in files:
			os.remove('tmp/'+file)
		os.rmdir('tmp')

jpegs = []
threshold = 10 # sec
last_timestamp = 0

def cut():
	if len(jpegs) > 0:
		_file = jpegs[0].replace('s','')
		year = _file[5:9]
		month = _file[9:11]
		day = _file[11:13]
		hour = _file[13:15]
		min = _file[15:17]
		sec = _file[17:19]
		make_mjpeg(jpegs, year+'-'+month+'-'+day+'_'+hour+'-'+min+'-'+sec+'.mjpg')

for file in sorted(os.listdir(home)):
	if file[:5] == 'ipcam' and file[-4:].lower() == '.jpg':
		timestamp = int(file.replace('s','')[5:19])
		if timestamp - last_timestamp > threshold:
			cut()
			jpegs = []

#		timestamp = file[5:13] # date
#		if last_timestamp != timestamp:
#			cut()
#			jpegs = []

		jpegs.append(file)
		last_timestamp = timestamp
cut()
