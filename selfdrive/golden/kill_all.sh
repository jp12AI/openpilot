#!/usr/bin/bash

ps -ef | grep 'thermald' | grep -v grep | awk '{print $1}' | xargs -r kill -9
ps -ef | grep 'manager.py' | grep -v grep | awk '{print $1}' | xargs -r kill -9
ps -ef | grep 'phone_control' | grep -v grep | awk '{print $1}' | xargs -r kill -9

ps -ef | grep 'thermald' 
ps -ef | grep 'manager.py'
ps -ef | grep 'phone_control'

