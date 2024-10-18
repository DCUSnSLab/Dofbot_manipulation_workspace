#! /usr/bin/env python3

import rospy
import numpy as np
import math
from visualization_msgs.msg import Marker
from geometry_msgs.msg import Point
from sensor_msgs.msg import JointState
from std_msgs.msg import ColorRGBA

DE2RA = math.pi / 180.00

def draw_callback(msg):
	rate = rospy.Rate(10)
	
	start_point = Point()
	start_point.x = 0.0
	start_point.y = 0.0
	start_point.z = 0.11
	line_length = 2.0
	
	## XY Marker
	markerXY = Marker()
	markerXY.header.frame_id = "base_link"
	markerXY.header.stamp = rospy.Time.now()
	markerXY.ns = 'robot_arm_direction_xy'
	markerXY.id = 0
	markerXY.type = Marker.ARROW
	markerXY.action = Marker.ADD
	markerXY.scale.x = 0.05
	markerXY.scale.y = 0.1
	markerXY.scale.z = 0.1
	markerXY.color = ColorRGBA(0.0, 1.0, 0.0, 0.5)
	
	print(f'> msg.position = [{msg.position[0]}, {msg.position[1]}]')

	## Calculate Joint1
	k1 = 111.111
	XYend_point = Point()
	if msg.position[0] >= 1.565:
		XYend_point.x = -1.0 * line_length
		XYend_point.y = 0.0
	elif msg.position[0] > 0 and msg.position[0] < 1.565:
		k1 = math.tan(msg.position[0])
		y1 = line_length / (((k1*k1) + 1) ** 0.5)
		x1 = (((line_length**2) - (y1**2)) ** 0.5) * -1.0
		XYend_point.x = x1
		XYend_point.y = y1
	elif msg.position[0] == 0:
		XYend_point.x = 0.0
		XYend_point.y = line_length
	elif msg.position[0] >= -1.565  and msg.position[0] < 0:
		k1 = math.tan(msg.position[0])
		y1 = line_length / (((k1*k1) + 1) ** 0.5)
		x1 = ((line_length**2) - (y1**2)) ** 0.5
		XYend_point.x = x1
		XYend_point.y = y1
	else:
		XYend_point.x = line_length
		XYend_point.y = 0.0
	print(f'> k1 = {k1}')
	XYend_point.z = 0.11
	markerXY.points.append(start_point)
	markerXY.points.append(XYend_point)
	print(f'> XYend_point = ({XYend_point.x}, {XYend_point.y}, {XYend_point.z})')
	print(f'> x^2 + y^2 = r^2')
	print('> {0:.2f} + {1:.2f} = {2:.2f}\n'.format(XYend_point.x**2, XYend_point.y**2, (XYend_point.x**2) + (XYend_point.y**2)))
	XY_pub = rospy.Publisher('vis_xy', Marker, queue_size=10)
	markerXY.header.stamp = rospy.Time.now()
	XY_pub.publish(markerXY)
	
	## YZ Marker
	markerYZ = Marker()
	markerYZ.header.frame_id = "base_link"
	markerYZ.header.stamp = rospy.Time.now()
	markerYZ.ns = 'robot_arm_direction_yz'
	markerYZ.id = 0
	markerYZ.type = Marker.ARROW
	markerYZ.action = Marker.ADD
	markerYZ.scale.x = 0.05
	markerYZ.scale.y = 0.1
	markerYZ.scale.z = 0.1
	markerYZ.color = ColorRGBA(0.0, 0.0, 1.0, 0.5)

	## Calculate Joint2
	k2 = 222.222
	YZend_point = Point()
	if msg.position[1] >= 1.565:
		YZend_point.y = -1.0 * line_length
		YZend_point.z = 0.0
	elif msg.position[1] > 0 and msg.position[1] < 1.565:
		k2 = math.tan(msg.position[1])
		z2 = line_length / (((k2*k2) + 1) ** 0.5)
		y2 = (((line_length**2) - (z2**2)) ** 0.5)
		YZend_point.y = -1.0 * y2
		YZend_point.z = z2
	elif msg.position[1] == 0:
		YZend_point.y = 0.0
		YZend_point.z = line_length
	elif msg.position[1] >= -1.565  and msg.position[1] < 0:
		k2 = math.tan(msg.position[1])
		z2 = line_length / (((k2*k2) + 1) ** 0.5)
		y2 = (((line_length**2) - (z2**2)) ** 0.5) * -1.0
		YZend_point.y = -1.0 * y2
		YZend_point.z = z2
	else:
		YZend_point.y = line_length
		YZend_point.z = 0.0
	
	print(f'> k2 = {k2}')
	YZend_point.x = 0.0
	YZend_point.z += 0.11
	markerYZ.points.append(start_point)
	markerYZ.points.append(YZend_point)
	print(f'> YZend_point = ({YZend_point.x}, {YZend_point.y}, {YZend_point.z})')
	print(f'> y^2 + z^2 = r^2')
	print('> {0:.2f} + {1:.2f} = {2:.2f}\n'.format(YZend_point.y**2, YZend_point.z**2, (YZend_point.y**2) + (YZend_point.z**2)))
	YZ_pub = rospy.Publisher('vis_yz', Marker, queue_size=10)
	markerYZ.header.stamp = rospy.Time.now()
	YZ_pub.publish(markerYZ)
	
		
	## Direction Marker(xyz)
	marker = Marker()
	marker.header.frame_id = "base_link"
	marker.header.stamp = rospy.Time.now()
	marker.ns = 'robot_arm_direction'
	marker.id = 0
	marker.type = Marker.ARROW
	marker.action = Marker.ADD
	marker.scale.x = 0.05
	marker.scale.y = 0.1
	marker.scale.z = 0.1
	marker.color = ColorRGBA(1.0, 0.0, 0.0, 0.5)
	
	theta_1 = 0.5
	theta_2 = 0.5
	#theta_1 = math.atan(XYend_point.y / XYend_point.x)
	#theta_2 = math.atan(YZend_point.z / YZend_point.y)
	print(f'> theta_1 = {theta_1}, theta_2 = {theta_2}')
	
	L1 = 1.0
	L2 = 2.0
	R_z = np.array([[np.cos(theta_1), -np.sin(theta_1), 0],
			 [np.sin(theta_1),  np.cos(theta_1), 0],
			 [0,               0,               1]])
	R_x = np.array([[1,               0,               0],
			 [0,  np.cos(theta_2), -np.sin(theta_2)],
			 [0,  np.sin(theta_2),  np.cos(theta_2)]])
	print('> R')
	print(R_z)
	print(R_x)
	print()
	
	P1 = np.array([L1, 0, 0])
	P2 = np.array([0, 0, L2])
	print('> P')
	print(P1)
	print(P2)
	print()
	
	P1_rotated = R_z @ P1
	P2_rotated = R_x @ P2
	print('> P_rotated')
	print(P1_rotated)
	print(P2_rotated)
	print()
	
	final_position = P1_rotated + P2_rotated
	
	## Calculate Direction
	end_point = Point()
	end_point.x = final_position[0]
	end_point.y = final_position[1]
	end_point.z = final_position[2]
	print('> final_position')
	print(end_point)
	print()
	
	marker.points.append(start_point)
	marker.points.append(end_point)
	marker_pub = rospy.Publisher('visulize_direction', Marker, queue_size=10)
	marker.header.stamp = rospy.Time.now()
	marker_pub.publish(marker)
	rate.sleep()
	
if __name__ == '__main__':
	rospy.init_node('direction_vis')
	subscriber = rospy.Subscriber('/joint_states', JointState, draw_callback)
	rospy.spin()
