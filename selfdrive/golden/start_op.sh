#!/usr/bin/bash

cd /data/openpilot/
./selfdrive/golden/kill_all.sh

rm /tmp/op_git_updated

cd /
rm -rf /runonce/

export SIMULATION=1
export NOSENSOR=1

./comma.sh

