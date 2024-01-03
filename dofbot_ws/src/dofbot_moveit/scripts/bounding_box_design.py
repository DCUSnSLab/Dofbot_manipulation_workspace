#!/usr/bin/env python3
# pubsubcp.py 코드를 경량화한 스크립트입니다.

import rospy
import random as rd
from visualization_msgs.msg import Marker, MarkerArray
from zed_interfaces.msg import ObjectsStamped
from std_msgs import *

DO_YOU_WANNA_DEBUG = True

class BoundingBoxesDesign:
    def __init__(self):
        self.marker_array_publisher = rospy.Publisher('/bounding_boxes', MarkerArray, queue_size=10)
        self.objects_subscriber = rospy.Subscriber('/zed2/zed_node/obj_det/objects', ObjectsStamped, self.objects_callback)

    def objects_callback(self, msg: ObjectsStamped):
        bounding_boxes = MarkerArray()
        obj_index = 0
        for obj in msg.objects:
            self.print_bounding_box_coord_info(DO_YOU_WANNA_DEBUG, obj, obj_index)
            bounding_boxes.markers.append(self.make_bounding_box(obj, obj_index))
            obj_index += 1
        self.marker_array_publisher.publish(bounding_boxes)

    def make_bounding_box(self, obj: list, obj_index: int) -> MarkerArray:
        bounding_box = Marker()
        # 직육면체의 변의 길이를 계산합니다.
        width = float(obj.bounding_box_3d.corners[0].x - obj.bounding_box_3d.corners[1].x)
        height = float(obj.bounding_box_3d.corners[2].y - obj.bounding_box_3d.corners[1].y)
        verticality = float(obj.bounding_box_3d.corners[1].z - obj.bounding_box_3d.corners[5].z)

        # 직육면체의 중점 좌표를 계산합니다.
        x = float((obj.bounding_box_3d.corners[0].x + obj.bounding_box_3d.corners[1].x) / 2)
        y = float((obj.bounding_box_3d.corners[1].y + obj.bounding_box_3d.corners[2].y) / 2)
        z = float((obj.bounding_box_3d.corners[5].z + obj.bounding_box_3d.corners[1].z) / 2)

        # CUBE 타입의 마커를 생성합니다.
        bounding_box.header.stamp = rospy.Time.now()
        bounding_box.header.frame_id = 'zed2_left_camera_frame'
        bounding_box.id = obj.label_id
        bounding_box.ns = "BOX_" + str(obj_index)
        bounding_box.action = Marker.ADD
        bounding_box.type = Marker.CUBE
        # 마커의 중점을 설정합니다.
        bounding_box.pose.position.x = x
        bounding_box.pose.position.y = y
        bounding_box.pose.position.z = z
        # 마커의 크기를 설정합니다.
        bounding_box.scale.x = width
        bounding_box.scale.y = height
        bounding_box.scale.z = verticality
        bounding_box.color.r = rd.randint(1, 255)
        bounding_box.color.g = rd.randint(1, 255)
        bounding_box.color.b = rd.randint(1, 255)
        bounding_box.color.a = 0.3  # 마커의 불투명도를 설정합니다.
        bounding_box.lifetime.secs = 1

        return bounding_box

    def print_bounding_box_coord_info(self, turn_on: bool, obj: list, obj_index: int):
        if obj_index == 0: print("*---*---*---*---*---*---*---*---*---*---*---*---*---*---")
        print("{0}번째 객체의 바운딩 박스 정보".format(obj_index))
        print("*      1 ------- 2 ({0:.1f}, {1:.1f}, {2:.1f})".format(obj.bounding_box_3d.corners[2].x, obj.bounding_box_3d.corners[2].y, obj.bounding_box_3d.corners[2].z))
        print("*     /.        /|")
        print("*    0 ------- 3 | ({0:.1f}, {1:.1f}, {2:.1f})".format(obj.bounding_box_3d.corners[3].x, obj.bounding_box_3d.corners[3].y, obj.bounding_box_3d.corners[3].z))
        print("*    | .       | |")
        print("*    | 5.......| 6 ({0:.1f}, {1:.1f}, {2:.1f})".format(obj.bounding_box_3d.corners[6].x, obj.bounding_box_3d.corners[6].y, obj.bounding_box_3d.corners[6].z))
        print("*    |.        |/")
        print("*    4 ------- 7")
        print("*    ({0:.1f}, {1:.1f}, {2:.1f})".format(obj.bounding_box_3d.corners[4].x, obj.bounding_box_3d.corners[4].y, obj.bounding_box_3d.corners[4].z))

        width = float(obj.bounding_box_3d.corners[0].x - obj.bounding_box_3d.corners[1].x)
        height = float(obj.bounding_box_3d.corners[2].y - obj.bounding_box_3d.corners[1].y)
        verticality = float(obj.bounding_box_3d.corners[1].z - obj.bounding_box_3d.corners[5].z)
        print("> [ 크기 ]")
        print("> x 세로 (0-1) : {0:.2f}".format(width))
        print("> y 가로 (2-1) : {0:.2f}".format(height))
        print("> z 높이 (1-5) : {0:.2f}".format(verticality))

        x = float((obj.bounding_box_3d.corners[0].x + obj.bounding_box_3d.corners[1].x) / 2)
        y = float((obj.bounding_box_3d.corners[1].y + obj.bounding_box_3d.corners[2].y) / 2)
        z = float((obj.bounding_box_3d.corners[5].z + obj.bounding_box_3d.corners[1].z) / 2)
        print("> [ 중점 ]")
        print("> ({0:.1f}, {1:.1f}, {2:.1f})".format(x, y, z))
        print("*---*---*---*---*---*---*---*---*---*---*---*---*---*---")

if __name__ == '__main__':
    while not rospy.is_shutdown():
        BoundingBoxesDesign()
        rospy.init_node('bbox_publisher')
        rospy.spin()