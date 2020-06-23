#!/usr/bin/env python



# Connect to the device
# You may need to start and stop the Anova with the app to get bluetooth to be listening

from pyanova import pyanova
import re

pa = pyanova.PyAnova(auto_connect=False)

devices = pa.discover(list_all=False, dev_mac_pattern=re.compile('^F4:5E:AB'), timeout=3)

print devices

try:
  pa.connect_device(devices[0])
except Exception:
  pass

pa.stop_anova()

