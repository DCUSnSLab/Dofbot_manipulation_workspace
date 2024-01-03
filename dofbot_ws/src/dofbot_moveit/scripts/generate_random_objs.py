#!/usr/bin/env python3
# 작업 완료

import random as rd
import rospy
from visualization_msgs.msg import Marker, MarkerArray
from std_msgs import *

DO_YOU_WANNA_DEBUG = True

class GenerateRandomObjects:
    def __init__(self):
        self.obj_list = [Marker(), Marker(), Marker()]
        self.init_objs()
    def init_objs(self):
        for i in range(3):
            self.obj_list[i].header.stamp = rospy.Time.now()
            self.obj_list[i].header.frame_id = "random_objs_frame"
            self.obj_list[i].id = i
            self.obj_list[i].ns = "OBJ_" + str(i)
            self.obj_list[i].action = Marker.ADD
            self.obj_list[i].type = Marker.CUBE

            tmp_coord = self.generate_random_coord()
            self.obj_list[i].pose.position.x = tmp_coord[0]
            self.obj_list[i].pose.position.y = tmp_coord[1]
            self.obj_list[i].pose.position.z = tmp_coord[2]

            tmp_size = self.generate_random_size()
            self.obj_list[i].scale.x = tmp_size[0]
            self.obj_list[i].scale.y = tmp_size[1]
            self.obj_list[i].scale.z = tmp_size[2]

            self.obj_list[i].color.r = rd.randint(1, 255)
            self.obj_list[i].color.g = rd.randint(1, 255)
            self.obj_list[i].color.b = rd.randint(1, 255)
            self.obj_list[i].color.a = 1.0
            self.obj_list[i].lifetime.secs = 1
    def generate_random_coord(self):
        coord = [0, 0, 0]
        for i in range(3):
            if i == 2:
                coord[i] = rd.randint(0, 20)
            else:
                coord[i] = rd.randint(-20, 20)
        return coord
    def generate_random_size(self):
        size = [0, 0, 0]
        for i in range(3):
            size[i] = rd.randint(1, 10)
        return size
    def move_objs(self):
        distance = [-2, -1, 0, 1, 2]
        for i in range(3):
            self.obj_list[i].pose.position.x += distance[rd.randint(0, 4)]
            self.obj_list[i].pose.position.y += distance[rd.randint(0, 4)]
            self.obj_list[i].pose.position.z += distance[rd.randint(0, 4)]
    def return_objs(self):
        return self.obj_list

if __name__ == '__main__':
    objs = GenerateRandomObjects()
    rospy.init_node('generated_objs_publisher')
    publisher = rospy.Publisher('/generated_objects', MarkerArray, queue_size=10)
    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        objs.move_objs()
        current_objs = objs.return_objs()
        msg = MarkerArray()
        for i in range(3):
            msg.markers.append(current_objs[i])
        rospy.loginfo(msg)
        publisher.publish(msg)
        rate.sleep()