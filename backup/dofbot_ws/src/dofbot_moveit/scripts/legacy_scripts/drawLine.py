#! /usr/bin/env python3
import rospy
from visualization_msgs.msg import Marker, MarkerArray
from geometry_msgs.msg import Point
import numpy as np

publisher = rospy.Publisher("/line", Marker, queue_size = 10)

def marker_array_callback(msg):
	bboxPoints = [0.0, 0.0]
	bboxPoints[0] = msg.markers[0].points[0]
	bboxPoints[1] = msg.markers[0].points[1]
	middlePoint_X = float((bboxPoints[0].x + bboxPoints[1].x) / 2)
	middlePoint_Y = float((bboxPoints[0].y + bboxPoints[1].y) / 2)
	middlePoint_Z = float((bboxPoints[0].z + bboxPoints[1].z) / 2)
	
	# line.points = np.array(middlePoint_X, middlePoint_Y, middlePoint_Z)
	line = Marker()
	line.action = Marker.ADD
	line.header.frame_id = "draw_line"
	line.pose.orientation.w = 1.0
	line.type = Marker().LINE_STRIP
	line.scale.x = 0.05
	line.color.b = 1.0
	line.color.g = 1.0
	line.color.a = 1.0
	line.lifetime.secs = 1
	
	p = Point()
	d = Point()
	p.x = 0
	p.y = 0
	p.z = 0
	d.x = middlePoint_X
	d.y = middlePoint_Y
	d.z = middlePoint_Z
	line.points.append(p)
	line.points.append(d)
	
	publisher.publish(line)
	
if __name__ == '__main__':
	rospy.init_node("draw_line")
	subscriber = rospy.Subscriber("/bounding_boxes", MarkerArray, marker_array_callback)
	rospy.spin()
