#!/usr/bin/bash

cd /data/openpilot/
./selfdrive/golden/kill_all.sh

cd /
rm -rf /runonce/
./comma.sh

