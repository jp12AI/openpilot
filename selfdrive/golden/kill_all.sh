#!/usr/bin/bash

ps -ef | grep 'thermald' | grep -v grep | awk '{print $1}' | xargs -r kill -9
ps -ef | grep 'manager.py' | grep -v grep | awk '{print $1}' | xargs -r kill -9
ps -ef | grep 'phone_control' | grep -v grep | awk '{print $1}' | xargs -r kill -9
ps -ef | grep 'manage_athenad' | grep -v grep | awk '{print $1}' | xargs -r kill -9
ps -ef | grep 'launch_chffrplus' | grep -v grep | awk '{print $1}' | xargs -r kill -9
ps -ef | grep 'athenad' | grep -v grep | awk '{print $1}' | xargs -r kill -9
ps -ef | grep 'can_bridge' | grep -v grep | awk '{print $1}' | xargs -r kill -9
#ps -ef | grep 'start_op' | grep -v grep | awk '{print $1}' | xargs -r kill -9

ps -ef | grep 'thermald'
ps -ef | grep 'manager.py'
ps -ef | grep 'phone_control'

