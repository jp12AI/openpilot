#!/bin/bash

source ./selfdrive/golden/guess_op_ip.sh

echo $OP_IP

PORT=8022
RSA_FILE=~/.ssh/op.rsa

set -x
scp -r -P $PORT -i $RSA_FILE $1 root@$OP_IP:/data/openpilot/$2