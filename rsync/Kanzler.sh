#!/bin/bash
#
# Kanzler-PC
#

# start time
date=$(echo -n $(date))
cd /home/Backups/Kanzler/git/

# mount Samba share
umount -fl /media/Kanzler/C
sleep 5
mount /media/Kanzler/C
sleep 2

rsync -ar --delete -i "/media/Kanzler/C/Users/Kanzler/AppData/Local/IM" . > rsync.log

rsync -ar --delete -i "/media/Kanzler/C/ProgramData/IncrediMail" . >> rsync.log

rsync -ar --delete -i "/media/Kanzler/C/Users/Kanzler/AppData/Local/Microsoft/Outlook" . >> rsync.log

rsync -ar --delete -i "/media/Kanzler/C/Users/Kanzler/Documents/Outlook-Dateien" . >> rsync.log

rsync -ar --delete -i "/media/Kanzler/C/ProgramData/StarMoney 8.0" . >> rsync.log

rsync -ar --delete -i "/media/Kanzler/C/ProgramData/StarMoney 9.0" . >> rsync.log

umount -fl /media/Kanzler/C

git add .
git commit -am "$date: $(echo -n $(cat /etc/hostname)) rsync'ed Kanzler-PC: IM, IncrediMail, Outlook, Outlook-Dateien, StarMoney 8.0 and StarMoney 9.0"
