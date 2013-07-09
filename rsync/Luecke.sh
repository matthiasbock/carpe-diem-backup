#!/bin/bash
#
# Luecke-PC
#

# start time
date=$(echo -n $(date))
cd /home/Backups/Luecke/git/

# mount //Luecke-PC/C
umount -fl /media/Luecke/C
sleep 5
mount /media/Luecke/C
sleep 2

rsync -ar --delete -i "/media/Luecke/C/Users/Lücke/AppData/Local/IM" . > rsync.log

rsync -ar --delete -i "/media/Luecke/C/ProgramData/IncrediMail" . >> rsync.log

rsync -ar --delete -i "/media/Luecke/C/Users/Lücke/AppData/Local/Microsoft/Outlook" . >> rsync.log

rsync -ar --delete -i "/media/Luecke/C/Users/Lücke/Documents/Outlook-Dateien" . >> rsync.log

rsync -ar --delete -i "/media/Luecke/C/ProgramData/StarMoney 8.0" . >> rsync.log

rsync -ar --delete -i "/media/Luecke/C/ProgramData/StarMoney 9.0" . >> rsync.log

umount -fl /media/Luecke/C

git add .
git commit -am "$date: $(echo -n $(cat /etc/hostname)) rsync'ed Luecke-PC: IM, IncrediMail, Outlook, Outlook-Dateien, StarMoney 8.0 and StarMoney 9.0"
