#!/usr/bin/python3
import referencetime
import config
import time
elapsedtime = int(time.time()) - referencetime.startTime
minutes = int(elapsedtime/60)
seconds = elapsedtime % 60

remainingminutes = config.pomolength - minutes
remainingseconds = 60 - seconds

print(str(remainingminutes) + ':' + str(remainingseconds))
