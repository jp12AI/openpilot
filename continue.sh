#!/usr/bin/bash

touch /data/no_ota_updates

cd /data/openpilot
#git pull --rebase

rm /tmp/ip.tmp
rm /tmp/op_simulation
#rm /tmp/lane_offset
rm /tmp/op_date
rm /tmp/git_hash
#rm /tmp/op_git_updated

#NOW=$(date +"%m_%d_%Y")
#LOG_FILE=/data/openpilot/op_$NOW.log
#exec ./launch_openpilot.sh > $LOG_FILE
exec ./launch_openpilot.sh

