#!/usr/bin/env python3

import rospy
from math import pi
import math
import Arm_Lib
from visualization_msgs.msg import MarkerArray, Marker

RA2DE = 180 / pi

def marker_array_callback(msg):
	marker = msg.markers[0]
	
	bboxPoints = [0.0, 0.0]
	bboxPoints[0] = marker.points[0]
	bboxPoints[1] = marker.points[1]
	middlePoint_X = float((bboxPoints[0].x + bboxPoints[1].x) / 2)
	middlePoint_Y = float((bboxPoints[0].y + bboxPoints[1].y) / 2)
	middlePoint_Z = float((bboxPoints[0].z + bboxPoints[1].z) / 2)
	
	slopeXY = float(middlePoint_Y / middlePoint_X)
	slopeXZ = float(middlePoint_Z / middlePoint_X)
        
	print("slopeXY: ", slopeXY)
	print("slopeXZ: ", slopeXZ)
        
	theta1 = math.degrees(math.atan(slopeXY))
	theta2 = math.degrees(math.atan(slopeXZ))

	print("theta1: ", theta1)
	print("theta2: ", theta2)

	Arm.Arm_serial_servo_write(1, theta1, 100)
	Arm.Arm_serial_servo_write(2, theta2, 100)
	# time.sleep(0.1)
        
if __name__ == '__main__':
	Arm = Arm_Lib.Arm_Device()
	rospy.init_node("bbox_subscriber")
	subscriber = rospy.Subscriber("/bounding_boxes", MarkerArray, marker_array_callback)
	rospy.spin()
        
