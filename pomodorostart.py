#!/usr/bin/python3
import time
referencefile = open('./referencetime.py','w')
referencefile.write('startTime=' + str(int(time.time())) + '\n')
referencefile.write('breakCounter=0')
