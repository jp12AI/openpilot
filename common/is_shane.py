import importlib

try:
  Params = importlib.import_module('common.params').Params
  is_shane = Params().get("DongleId").decode('utf8') in ['14431dbeedbf3558', 'e010b634f3d65cdb']  # returns if fork owner is current user
  is_golden = Params().get("DongleId").decode('utf8') in ['927e1bceaf39b7c1', 'c369e78c7e6f747c']  # returns if fork owner is current user
except:  # in case params isn't built
  is_shane = False
  is_golden = False