#!/usr/bin/env python3
#coding=utf-8
import time
import math
import rospy
import random as rd
from Arm_Lib import Arm_Device
from sensor_msgs.msg import JointState

Arm = Arm_Device()
time.sleep(.1)
# Length of servo 2 : 4cm
# standard(base) : a pair of boards between servo 1 and servo 2
#   servo 2
#    |   |
#   ------- standard
#   -------  (base)
#   servo 1

def main():
    
    print("***Coord of object***")
    x = int(input("X coord >> "))
    y = int(input("Y coord >> "))
    z = int(input("Z coord >> "))
    
    while True:

        slopeXY = float(y / x)
        slopeXZ = float(z / x)
        
        print("slopeXY: ", slopeXY)
        print("slopeXZ: ", slopeXZ)

        theta1 = math.degrees(math.atan(slopeXY))
        theta2 = math.degrees(math.atan(slopeXZ))

        print("theta1: ", theta1)
        print("theta2: ", theta2)

        Arm.Arm_serial_servo_write(1, theta1, 1000)
        Arm.Arm_serial_servo_write(2, theta2, 1000)
        time.sleep(1)
        
        x += int(rd.uniform(-10.0, 10.0))
        y += int(rd.uniform(-10.0, 10.0))
        z += int(rd.uniform(-10.0, 10.0))
        
        if x == 0:
            x += 1
            
        if z < 0:
            z *= -1
        
        print("")
        print("----------")
        print("")
        print("X: ", x)
        print("Y: ", y)
        print("Z: ", z)
        
def reset_arm():
    Arm.Arm_serial_servo_write(1, 0, 5000)
    time.sleep(1)
    Arm.Arm_serial_servo_write(2, 90, 5000)
    time.sleep(1)
    
    
try :
    reset_arm()
    main()
except KeyboardInterrupt:
    reset_arm()
    print(" Program closed! ")
    pass
