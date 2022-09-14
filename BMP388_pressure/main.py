import bmp388
import time

# Create a bmp388 object to communicate with I2C.
bmp388 = bmp388.DFRobot_BMP388_I2C()

# Read pressure and print it.
while 1:
  pres = bmp388.readPressure()
  print("Pressure : %s Pa" %pres)
  time.sleep(0.5)




