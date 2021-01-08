#!/usr/bin/env python3
import os
import time
import math
import atexit
import numpy as np
import threading
import random
import cereal.messaging as messaging
import argparse
from common.params import Params
from common.realtime import Ratekeeper
from selfdrive.golden.can import can_function, sendcan_function
from selfdrive.car.honda.values import CruiseButtons
import queue
import subprocess

import sys
import signal

params = Params()

def main():

  global params
  params.delete("Offroad_ConnectivityNeeded")
  params.delete("CalibrationParams")
  params.put("CalibrationParams", '{"calib_radians": [0,0,0], "valid_blocks": 20}')

  os.system('echo 1 > /tmp/op_simulation')
  os.system('echo 1 > /tmp/force_calibration')
  os.system('service call audio 3 i32 3 i32 0 i32 1')

  rom multiprocessing import Process, Queue
  q = Queue()
  from selfdrive.golden.keyboard_ctrl import keyboard_poll_thread
    keyboard_poll_thread(q)

  global pm

  pm = messaging.PubMaster(['can', 'health'])

  # can loop
  sendcan = messaging.sub_sock('sendcan')
  rk = Ratekeeper(100, print_delay_threshold=None)
  steer_angle = 0.0
  speed = 50.0 / 3.6
  engage = False
  cruise_button = 0

  while 1:

    # check keyboard input
    if not q.empty():
      message = q.get()
      m = message.split('_')
      if m[0] == "cruise":
        if m[1] == "down":
          cruise_button = CruiseButtons.DECEL_SET
          engage = True
        if m[1] == "up":
          cruise_button = CruiseButtons.RES_ACCEL
          engage = True
        if m[1] == "cancel":
          cruise_button = CruiseButtons.CANCEL
          engage = False

    can_function(pm, speed * 3.6, steer_angle, rk.frame, cruise_button=cruise_button, is_engaged=engage)
    #if rk.frame%5 == 0:
    #  throttle, brake, steer = sendcan_function(sendcan)
    #  steer_angle += steer/10000.0 # torque
    #  # print(speed * 3.6, steer, throttle, brake)

    dat = messaging.new_message('health')
    dat.valid = True
    dat.health = {
      'ignitionLine': True,
      'hwType': "uno",
      'controlsAllowed': True,
      'safetyModel': "hondaNidec"
    }
    pm.send('health', dat)

    rk.keep_time()

def signal_handler(sig, frame):
    print('You pressed Ctrl+C!')

    global pm

    dat = messaging.new_message('health')
    dat.valid = True
    dat.health = {
      'ignitionLine': False,
      'hwType': "uno",
      'controlsAllowed': True,
      'safetyModel': "hondaNidec"
    }

    for seq in range(10):
      pm.send('health', dat)
      time.sleep(0.1)

    global params
    params.delete("CalibrationParams")

    print ("exiting")
    sys.exit(0)

if __name__ == "__main__":
  signal.signal(signal.SIGINT, signal_handler)

  print ("input 1 to curse set/-")
  print ("input 2 to curse resume/+")
  print ("input 3 to curse cancel")
  print ("input q to quit")

  main()

