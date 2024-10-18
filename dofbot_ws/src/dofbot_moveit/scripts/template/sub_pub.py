#! /usr/bin/env python3
## 하나의 토픽을 구독하여 값을 받은 후, 가공하여 발행하는 스크립트 템플릿

import rospy
from std_msgs.msg import PubMsg, SubMsg

def submsg_callback(msg):
	## Set ROS Configuration and Publisher
	rate = rospy.Rate(10)	
	pub = rospy.Publisher('topic_name_for_publishing', PubMsg, queue_size=10)	
	
	## Init Message for Publishing
	pub_msg = PubMsg()
	
	## Define Contents of Message with Subscriber's Message
	
	## Publish Message
	pub.publish(pub_msg)
	rate.sleep()
	
if __name__ == '__main__':
	## Init Node
	rospy.init_node('node_name')
	## Init Subscriber
	subscriber = rospy.Subscriber('topic_name_for_subscribing', SubMsg, submsg_callback)
	rospy.spin()
