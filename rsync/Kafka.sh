#!/bin/bash
#
# Kafka
#

# start time
date=$(echo -n $(date))
cd /home/Backups/Kafka/git/

#
# dovecot
#

rsync -ar --delete -i /home/dovecot . > rsync.log

#
# etc
#

rsync -ar --delete -i /etc . >> rsync.log

#
# mysql
#

rsync -ar --delete -i /home/mysql . >> rsync.log

#
# intern (Wiki)
#

rsync -ar --delete -i /home/www/intern . >> rsync.log

git add .
git commit -am "$date: $(echo -n $(cat /etc/hostname)) rsync'ed dovecot, etc, mysql and intern"
