#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import sys, os
from datetime import date
from shutil import move
debug = False


# sort file by date

today = date.today().strftime('%Y%m%d')
home = '/media/Thecus/IPCam'

files = os.listdir(home)

def sort_into_folder(today):
	global debug

	datedir = os.path.join(home, today[:4]+'-'+today[4:6]+'-'+today[6:8])

	if not os.path.exists(datedir):
		os.mkdir(datedir)

	for f in files:
		if f.find('ipcam'+today) == 0 and f[-4:] in ['.jpg', '.JPG']:
			new = os.path.join(datedir, f)
			if debug:
				print f+' -> '+new
			move(os.path.join(home, f), new)

if len(sys.argv) < 2:
	sort_into_folder(today)
else:
	for arg in sys.argv[1:]:
		sort_into_folder(arg)


# sort events with different timestamps

def separate_events(today):
	global debug

	datedir = os.path.join(home, today[:4]+'-'+today[4:6]+'-'+today[6:8])
	files = sorted(os.listdir(datedir))

	lasttimestamp = 0
	trigger = 2000

	for f in files:
		if f.find('ipcam'+today) == 0 and f[-4:] in ['.jpg', '.JPG']:
			timestamp = f[13:-4]
			if int(timestamp) - int(lasttimestamp) > trigger:
				subdir = os.path.join(datedir, timestamp[:2]+':'+timestamp[2:4]+':'+timestamp[4:6])
				if not os.path.exists(subdir):
					os.mkdir(subdir)
			lasttimestamp = timestamp

			new = os.path.join(subdir, f)
			if debug:
				print f+' -> '+new
			move(os.path.join(datedir, f), new)

if len(sys.argv) < 2:
	separate_events(today)
else:
	for arg in sys.argv[1:]:
		separate_events(arg)


# make a video ...

