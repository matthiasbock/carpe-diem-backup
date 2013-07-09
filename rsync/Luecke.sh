#!/bin/bash

#
# Luecke-PC
#

date=$(echo -n $(date))

umount -fl /media/Luecke/C
sleep 5
mount /media/Luecke/C

cd /home/Backups/Luecke/git/
rsync -ar --delete -i /media/Luecke/C/Users/Lücke/AppData/Local/IM/* /home/Backups/Luecke/git/IM/ &> /home/Backups/Luecke/IM.log
git add .
git commit -am "$date: $(echo -n $(cat /etc/hostname)) rsync'ed C:/Users/Luecke/AppData/Local/IM/ on LUECKE-PC (192.168.3.114) with IM/"
