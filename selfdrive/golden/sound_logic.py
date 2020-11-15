#!/usr/bin/env python3

from cereal import car
from common.params import Params
import cereal.messaging as messaging
import os
import cereal.messaging.messaging_pyx as messaging_pyx
import time
from cereal import log
from opendbc.can.parser import CANParser
import json
from common.realtime import Ratekeeper
import platform
from common.op_params import opParams

BASE_PATH='/data/openpilot/selfdrive/'
SOUND_PATH=BASE_PATH + 'golden/sounds/'
OP_SOUND_PATH=BASE_PATH + 'assets/sounds/'
SOUND_PLAYER=BASE_PATH + 'golden/sound_player/sound_player '

is_osx = platform.system() == 'Darwin'
if is_osx:
  SOUND_PATH='/Users/lixin/Project/op_sync/golden/sounds/'
  OP_SOUND_PATH='/Users/lixin/Project/openpilot/selfdrive/assets/sounds/'
  SOUND_PLAYER='afplay '

def play_sound(snd_file, play_time, time_gap):
    t_now = time.time()
    if (t_now - play_time) < time_gap:
      return play_time
    cmd = SOUND_PLAYER + snd_file
    print(cmd)
    os.system(cmd)
    return t_now

def sound_logic_thread():

    sm = messaging.SubMaster(['carState'])
    rk = Ratekeeper(1.0, print_delay_threshold=None)
    play_time = 0
    last_lane_offset = 0.0
    op_params = opParams()

    play_sound('init_alert.wav', 0, 0)

    while True:
      try:
          sm.update()

      except messaging_pyx.MessagingError:
          print('MessagingError error happens')

      cur_lane_offset = op_params.get('lane_offset')
      if cur_lane_offset != last_lane_offset:
        play_time = play_sound('lane_offset_changed.wav', play_time, 3)
        last_lane_offset = cur_lane_offset

      rk.keep_time()

def main():
  sound_logic_thread()

if __name__ == "__main__":
  main()
