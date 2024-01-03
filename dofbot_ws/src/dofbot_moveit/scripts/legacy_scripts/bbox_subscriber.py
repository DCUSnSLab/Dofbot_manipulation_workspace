#!/usr/bin/env python3
import rospy
import time
import math
import Arm_Lib
from visualization_msgs.msg import MarkerArray
from visualization_msgs.msg import Marker
from sensor_msgs.msg import JointState
from geometry_msgs.msg import Point

RA2DE = float(180 / math.pi)
DE2RA = float(math.pi / 180)
joint_state_msg = JointState()
theta1 = 0.0 # Radian
theta2 = 0.0 # Radian
RvizRobotAngle = [0.0, 0.0] # Radian

publisher = rospy.Publisher('/joint_states', JointState, queue_size=10)
def marker_array_callback(msg):
        # Choose object[0]
        bboxPoints = msg.markers[0].points
        print("bboxPoints Length: {0}".format(len(bboxPoints)))
        for i in range(2):
            print("bboxPoints[{0}]: {1}".format(i, bboxPoints[i]))
        print()

        rate = rospy.Rate(10)

        # Calculate middlePoint coord
        middlePoint_X = float((bboxPoints[0].x + bboxPoints[1].x) / 2.00)
        middlePoint_Y = float((bboxPoints[0].y + bboxPoints[1].y) / 2.00)
        middlePoint_Z = float((bboxPoints[0].z + bboxPoints[1].z) / 2.00)

        # slope of line
        slopeXY = float(middlePoint_Y / middlePoint_X)
        slopeXZ = float(middlePoint_Z / middlePoint_X)

        print("slopeXY: ", slopeXY)
        print("slopeXZ: ", slopeXZ)

        # radian
        theta1 = math.atan(slopeXY)
        theta2 = math.atan(slopeXZ)

        if middlePoint_Y > 0:
            theta2 = math.pi - theta2
        if middlePoint_Z < 0:
            sbus.Arm_serial_servo_write(1, 0, 100)
            sbus.Arm_serial_servo_write(2, 90, 100)
            print("Object is under the ground ! !")
            exit()

        print("theta1(RA): {0}\t(DE): {1}".format(theta1, theta1 * RA2DE))
        print("theta2(RA): {0}\t(DE): {1}".format(theta2, theta2 * RA2DE))

        sbus.Arm_serial_servo_write(1, theta1 * RA2DE + 90, 100)
        sbus.Arm_serial_servo_write(2, theta2 * RA2DE, 100)

        joint_state_msg.name = ['joint1', 'joint2']
        for i in range(2):
            RvizRobotAngle[i] = sbus.Arm_serial_servo_read(i + 1) * DE2RA
            print(RvizRobotAngle[i])
        joint_state_msg.position = RvizRobotAngle
        joint_state_msg.header.stamp = rospy.Time.now()
        publisher.publish(joint_state_msg)
        rate.sleep()

if __name__ == '__main__':
        sbus = Arm_Lib.Arm_Device()
        rospy.init_node("bbox_subscriber")
        subscriber = rospy.Subscriber("/bounding_boxes", MarkerArray, marker_array_callback)

        rospy.spin()