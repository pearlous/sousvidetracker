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

# Get SetTemp, CurrentTemp, and add Time Stamp

#Variables
#Username            
SVuser = 'Johnny'

#Cook Name          
SVcookName = 'Kroger Chicken Breast Bone In'

#Target Temp
SVtargetTemp = '93'

#Current Temp      
SVcurrentTemp = pa.get_current_temperature()

#Cook Time           
SVcookTime = '15'

#Temp Unit (C/F)  
SVtempUnit ='f'


#Heat up before starting the timer (unlike the app, that starts the timer right away)
pa.set_temperature(float(SVtargetTemp))
pa.start_anova()
pa.set_timer(int(SVcookTime))

import time
from datetime import datetime

SVnow = datetime.now()
SVformattedDate = SVnow.strftime('%c')
SVtimerStatus = pa.get_timer()
SVstatus =pa.get_status()
SVtimerNow = SVtimerStatus.rsplit(' ',1)[0]
SVtimerState = SVtimerStatus.rsplit(' ',1)[1]

import csv

with open(SVnow.strftime("%m-%d-%Y-%H-%M") + '.csv', 'w') as f:
  fieldnames = ['Date', 'User', 'Cook Name', 'Target Temp', 'Current Temp', 'Timer Start', 'Current Timer', 'Timer Status', 'Unit', 'Status']
  thewriter = csv.DictWriter(f, fieldnames=fieldnames)
  thewriter.writeheader()
  while float(SVcurrentTemp) < float(SVtargetTemp) :
    print('Not up to temp yet...')
    SVcurrentTemp = pa.get_current_temperature()
    SVnow = datetime.now()
    SVformattedDate = SVnow.strftime('%c')
    # Print to CSV
    print(SVformattedDate, SVuser, SVcookName, SVtargetTemp, SVcurrentTemp, SVcookTime, SVtimerNow, SVtimerState, SVtempUnit, SVstatus)
    thewriter.writerow({'Date': SVformattedDate, 'User' : SVuser, 'Cook Name' : SVcookName, 'Target Temp' : SVtargetTemp, 'Current Temp' : SVcurrentTemp, 'Timer Start' : SVcookTime, 'Current Timer' : SVtimerNow, 'Timer Status' : SVtimerState, 'Unit' : SVtempUnit, 'Status' : SVstatus})   
    print('Temp is: ' + SVcurrentTemp)
    time.sleep(30)
  pa.start_timer()
  while SVtimerStatus.rsplit(' ',1)[1] != u'stopped' :
    # Get Timestamp
    SVnow = datetime.now()
    SVformattedDate = SVnow.strftime('%c')
    SVtimerStatus = pa.get_timer()
    SVtimerNow = SVtimerStatus.rsplit(' ',1)[0]
    SVtimerState = SVtimerStatus.rsplit(' ',1)[1]
    SVcurrentTemp = pa.get_current_temperature()
    print(SVformattedDate, SVuser, SVcookName, SVtargetTemp, SVcurrentTemp, SVcookTime, SVtimerNow, SVtimerState, SVtempUnit, SVstatus)
    thewriter.writerow({'Date': SVformattedDate, 'User' : SVuser, 'Cook Name' : SVcookName, 'Target Temp' : SVtargetTemp, 'Current Temp' : SVcurrentTemp, 'Timer Start' : SVcookTime, 'Current Timer' : SVtimerNow, 'Timer Status' : SVtimerState, 'Unit' : SVtempUnit, 'Status' : SVstatus})   
    time.sleep(30)

print("Completed: " + SVformattedDate)
# Don't stop the Anova, you might not be home!
