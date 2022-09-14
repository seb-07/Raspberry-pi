
import sys
sys.path.append('../../')
import time
from DFRobot_BMX160 import BMX160

bmx = BMX160(1)

#begin return True if succeed, otherwise return False
while not bmx.begin():
    time.sleep(2)


def main():
    while True:
        data= bmx.get_all_data()
        time.sleep(1)
        print("magn: x: {0:.2f} uT, y: {1:.2f} uT, z: {2:.2f} uT".format(data[0],data[1],data[2]))
        print(" ")

if __name__ == "__main__":
    main()


