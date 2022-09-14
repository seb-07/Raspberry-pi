import time

import pigpio

SERVO = 27

pi = pigpio.pi() # Connect to local Pi.
time.sleep(3)
pi.set_servo_pulsewidth(SERVO, 1000) # Minimum throttle.

time.sleep(1)

pi.set_servo_pulsewidth(SERVO, 1200) # Maximum throttle.

time.sleep(7)

pi.set_servo_pulsewidth(SERVO, 1100) # Slightly open throttle.

time.sleep(1)

pi.set_servo_pulsewidth(SERVO, 0) # Stop servo pulses.

pi.stop() # Disconnect from local Raspberry Pi.
















