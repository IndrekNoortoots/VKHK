#!/bin/bash
clear
echo 'Starting, this might take some time.'
#Making simple tar.gz backup from /home/sites/ folder(s)
tar -czPf backup.tgz /home/sites/
echo 'Backup done!'

#Todo, add some upload functions
