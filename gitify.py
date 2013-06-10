#!/usr/bin/python

#
# takes a list of folders
# rsync'es their respective contents with current folder's subfolder "git/"
# commits the git repository in "git/"
# removes the remaining empty directory
#

dry_run = False

import sys, os
from subprocess import Popen
from shlex import split

dirs = sys.argv[1:]
if len(dirs) == 0:
	for dir in sorted(os.listdir('.')):
		if os.path.isdir(dir) and len(dir) == 10 and dir.count('-') == 2: # e.g. 2013-05-06
		#if "Daten Carpe" in dir:
			dirs.append(dir)
print dirs

def run(cmd):
	print '$ '+cmd
	if dry_run:
		return 0
	else:
		return Popen(split(cmd)).wait()

# extract compressed archive
def extract(fname):
	pwd = os.getcwd()
	dn = os.path.dirname(fname)
	print '$ cd '+dn
	os.chdir(dn)
	fname = os.path.basename(fname)
	if fname[-3:] == '.7z':
		exitcode = run('7za x "'+fname+'"')
	elif fname[-7:] == '.tar.bz':
		exitcode = run('tar --no-same-owner -vxjf "'+fname+'"')
	if exitcode == 0:
		run('rm "'+fname+'"')
	print '$ cd '+pwd
	os.chdir(pwd)

def rsync(src, dst):
	# rsync content files and folder in src/ into dst/
	for content in os.listdir(src):
		content_path = os.path.join(src, content)

		# if 7z or tar.bz archive, extract first
		if content[-3:] == '.7z':
			extract(content_path)
			content_path = content_path[:-3]
		elif content[-7:] == '.tar.bz':
			extract(content_path)
			content_path = content_path[:-7]

		# rsync
		run('rsync -ar --remove-source-files --delete -i "'+content_path+'" "'+dst+'"')
		# remove empty folders (rsync wont' do that for us)
		run('find "'+content_path+'/" -type d -exec rmdir -p "{}" \;')
	run('rmdir "'+src+'"')

def commit(repodir, comment):
	print '$ cd '+repodir
	path = os.getcwd()
	os.chdir(repodir)
	run('git add .')
	run('git commit -am "'+comment+'"')
	print '$ cd '+path
	os.chdir(path)

# move content to git folder
gitrepo = "git/"
for dir in dirs:
	print 'committing the content files and folders in '+dir+' into '+gitrepo+' ...'
	rsync(dir, gitrepo)
	commit(gitrepo, "gitify "+dir)
	print ''
