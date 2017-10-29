#!/usr/bin/python3
import os
import time
import referencetime
import config
elapsedtime = int(time.time()) - referencetime.startTime
minutes = int(elapsedtime/60)
seconds = elapsedtime % 60

remainingminutes = config.pomolength - minutes
remainingseconds = 60 - seconds

if (remainingminutes <= 0):
    os.system('/home/connor/Documents/bash/pomo/pomodorostart.py')
    os.system('i3lock -i /home/connor/Pictures/lockbackround.png')

print(str(remainingminutes) + ':' + str(remainingseconds))
