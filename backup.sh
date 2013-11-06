#!/bin/bash
clear
echo 'Starting, this might take some time.'
#Making simple tar.gz backup from /home/sites/ folder(s)
tar -czPf backup.tar.gz /home/sites/
echo 'Backup done!'

echo 'Starting upload to ftp server'
#Todo, add some upload functions
ftp -n backup.resac.eu <<END_SCRIPT
quote USER backup
quote PASS xxxXXxx
put backup.tar.gz
quit
END_SCRIPT

