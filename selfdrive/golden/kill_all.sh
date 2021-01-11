#!/usr/bin/bash

function kill_process()
{
    proc_name=$1
    echo 'killing '$proc_name
    find_result=$(ps -ef | grep $proc_name | awk '{print $2}')
    if [[ ${find_result} != 0 ]];then
        kill -2 ${find_result} # kill with ctrl^c
        kill -9 ${find_result} # force kill
    fi
}

function check_process()
{
    proc_name=$1
    ps -ef | grep $proc_name
}

kill_process thermald
kill_process manager.py
kill_process phone_control
kill_process manage_athenad
kill_process launch_chffrplus
kill_process athenad
kill_process can_bridge
#kill_process start_op

check_process thermald
check_process manager.py
check_process phone_control