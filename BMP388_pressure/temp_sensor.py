
import bmp388
import time
# Create a bmp388 object to communicate with I2C.
bmp388 = bmp388.DFRobot_BMP388_I2C()

# Read temperature and print it
while 1:
  temp = bmp388.readTemperature()
  print("Temperature : %s C" %temp)
  time.sleep(0.5)




