#!/usr/bin/bash

cd /data/openpilot/
./selfdrive/golden/kill_all.sh

rm /tmp/op_git_updated

cd /
rm -rf /runonce/
./comma.sh

