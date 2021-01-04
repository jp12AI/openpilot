#!/usr/bin/bash

cd /data/openpilot/
./selfdrive/golden/killall.sh

cd /
rm -rf /runonce/
./comma.sh

