#! /usr/bin/env python3
import rospy

from visualization_msgs.msg import Marker, MarkerArray
from geometry_msgs.msg import Point, Quaternion
from sensor_msgs.msg import JointState
from tf.transformations import quaternion_about_axis, quaternion_multiply
import Arm_Lib
from math import pi
import numpy as np

publisher = rospy.Publisher("/line_new", Marker, queue_size = 10)
theta1 = 0.0
theta2 = 0.0

def line_callback(msg):
# slopeXY = float(joint_state_msg.position
	
	# line.points = np.array(middlePoint_X, middlePoint_Y, middlePoint_Z)
	line = Marker()
	line.action = Marker.ADD
	line.header.frame_id = "draw_line_new"
	line.pose.orientation.w = 1.0
	line.type = Marker().LINE_STRIP
	line.scale.x = 0.05
	line.color.b = 1.0
	line.color.g = 1.0
	line.color.a = 1.0
	line.lifetime.secs = 1
	
	joints = [0.0, 0.0]
	joints[0] = msg.position[0]
	joints[1] = msg.position[1]

	line.points.append(Point(0, 0, 0))
	line.points.append(Point(0, 0, 1000))
	
	conbined_quaternion = (1.0, 0.0, 0.0, 0.0)
	
	print("> Joint 1: {0} Radian".format(joints[0]))
	print("> Joint 2: {0} Radian".format(joints[1]))
	
	# first: servo2(x, z)
	rotation_quaternion_y = quaternion_about_axis(int(-1) * (joints[1] + (pi / 2)), (0, 1, 0))
	conbined_quaternion = quaternion_multiply(conbined_quaternion, rotation_quaternion_y)
	
	# second: servo1(x, y)
	rotation_quaternion_z = quaternion_about_axis((joints[0] + (pi)), (0, 0, 1))
	conbined_quaternion = quaternion_multiply(conbined_quaternion, rotation_quaternion_z)
	
	line.pose.orientation = Quaternion(*conbined_quaternion)
	
	publisher.publish(line)
	
if __name__ == '__main__':
	rospy.init_node("draw_line_new")
	subscriber = rospy.Subscriber("/joint_states", JointState, line_callback)
	rospy.spin()
