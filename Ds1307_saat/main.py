
import sys
import time
import datetime

import SDL_DS1307

# Main Program


filename = time.strftime(("%Y / %m / %d% , H/%M / %SRTCTest") + ".txt")
starttime = datetime.datetime.utcnow()

ds1307 = SDL_DS1307.SDL_DS1307(1, 0x68)
ds1307.write_now()

# Main Loop - sleeps 10 minutes, then reads and prints values of all clocks


while True:

        currenttime = datetime.datetime.utcnow()

        deltatime = currenttime - starttime

        print ("%s" % ds1307.read_datetime())










