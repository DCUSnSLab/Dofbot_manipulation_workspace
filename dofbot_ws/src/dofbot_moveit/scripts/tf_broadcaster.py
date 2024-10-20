#!/usr/bin/env python3
#-*-coding:utf-8 -*-
from sensor_msgs.msg import JointState
from sensor_msgs.msg import PointCloud2
from visualization_msgs.msg import MarkerArray
from geometry_msgs.msg import TransformStamped
import math
import rospy
import tf

if __name__ == '__main__':
    # ROS 노드를 초기화합니다.
    rospy.init_node('tf_broadcaster_node')

    # tf broadcaster를 생성합니다.
    broadcaster = tf.TransformBroadcaster()

    rate = rospy.Rate(15)  # 변환 정보를 15Hz로 브로드캐스트합니다.
    
    angle = math.pi / 2
    qx = 0
    qy = math.sin(angle / 2)
    qz = 0
    qw = math.cos(angle / 2)

    while not rospy.is_shutdown():
	# 변환 정보를 브로드캐스트합니다.
        broadcaster.sendTransformMessage(transform_msg)
        
        transform_msg = TransformStamped()  # 새로운 TransformStamped 메시지를 생성합니다.
        transform_msg.header.stamp = rospy.Time.now()  # 현재 시간으로 타임스탬프를 업데이트합니다.
        transform_msg.header.frame_id = 'base_link'
        transform_msg.child_frame_id = 'draw_line_new'
        transform_msg.transform.translation.x = 0.0
        transform_msg.transform.translation.y = 0.0
        transform_msg.transform.translation.z = 0.0
        transform_msg.transform.rotation.x = 0.0
        transform_msg.transform.rotation.y = 0.0
        transform_msg.transform.rotation.z = 0.0
        transform_msg.transform.rotation.w = 1.0

        # 변환 정보를 브로드캐스트합니다.
        broadcaster.sendTransformMessage(transform_msg)

        rate.sleep()
