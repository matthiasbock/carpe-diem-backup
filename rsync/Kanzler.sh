#!/bin/bash
#
# Kanzler-PC
#

# start time
date=$(echo -n $(date))
cd /home/Backups/Kanzler/git/

# mount Samba share
umount -fl /media/Kanzler/CaDi_Verwaltung
sleep 3
mount /media/Kanzler/CaDi_Verwaltung
sleep 2

rsync -ar --delete -i "/media/Kanzler/CaDi_Verwaltung" . > rsync.log

umount -fl /media/Kanzler/CaDi_Verwaltung

git add .
git commit -am "$date: $(echo -n $(cat /etc/hostname)) rsync'ed Kanzler-PC: CaDi-Verwaltung"



# mount Samba share
#umount -fl /media/Kanzler/C
#sleep 5
#mount /media/Kanzler/C
#sleep 2

#rsync -ar --delete -i "/media/Kanzler/C/Users/Kanzler/AppData/Local/IM" . > rsync.log

#rsync -ar --delete -i "/media/Kanzler/C/ProgramData/IncrediMail" . >> rsync.log

#rsync -ar --delete -i "/media/Kanzler/C/Users/Kanzler/AppData/Local/Microsoft/Outlook" . >> rsync.log

#rsync -ar --delete -i "/media/Kanzler/C/Users/Kanzler/Documents/Outlook-Dateien" . >> rsync.log

#rsync -ar --delete -i "/media/Kanzler/C/ProgramData/StarMoney 8.0" . >> rsync.log

#rsync -ar --delete -i "/media/Kanzler/C/ProgramData/StarMoney 9.0" . >> rsync.log

#umount -fl /media/Kanzler/C
