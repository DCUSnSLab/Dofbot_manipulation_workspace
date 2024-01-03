#!/usr/bin/env python3
# ROBOT COM 전용 스크립트입니다.
import rospy
import math
import Arm_Lib
from visualization_msgs.msg import MarkerArray, Marker
from sensor_msgs.msg import JointState

## 단위 변환 및 디버깅과 관련된 상수를 정의합니다.
RA2DE = float(180.00 / math.pi)
DE2RA = float(math.pi / 180.00)
DO_YOU_WANNA_DEBUG = True

class RobotManipulation:
    def __init__(self):
        self.sbus = Arm_Lib.Arm_Device()
        self.marker_array_subscriber = rospy.Subscriber('/bounding_boxes', MarkerArray, self.marker_array_callback)
        self.joint_state_publisher = rospy.Publisher('/joint_states', JointState, queue_size=10)
    def marker_array_callback(self, msg: MarkerArray):
        # 디버깅 메소드를 사용해 메시지의 내용물을 확인합니다.
        self.print_each_marker_info(DO_YOU_WANNA_DEBUG, msg)

        # 0번째 객체를 트래킹만을 고려합니다.
        ## 3차원 좌표를 2차원 좌표로 각각 분할합니다.
        xy_obj = [msg.markers[0].pose.position.x, msg.markers[0].pose.position.y]
        xz_obj = [msg.markers[0].pose.orientation.x, msg.markers[0].pose.position.z]
        ## 각 2차원 좌표와 원점을 잇는 직선의 기울기를 각각 계산합니다.
        slope_of_line = [float(xy_obj[1] / xy_obj[0]), float(xz_obj[1] / xz_obj[0])]
        ## 각 기울기에 대응하는 서보모터가 돌아야 할 각도를 각각 계산합니다.
        radian_of_servo = [math.atan(slope_of_line[0]), math.atan(slope_of_line[1])]
        degree_of_servo = [radian_of_servo[0] * RA2DE, radian_of_servo[1] * RA2DE]  # 호도법으로 계산된 각도는 실물 서보모터를 회전시키는 데 사용됩니다.

        # 서보모터 컨트롤 전, 예외 상황을 처리합니다.
        if msg.markers[0].pose.position.z < 0:  # 객체의 중점이 지하에 위치한 경우
            self.sbus.Arm_serial_servo_write(1, 0, 100)
            self.sbus.Arm_serial_servo_write(2, 90, 100)
            print("Object is under the ground ! !")

        # 실물 서보모터를 각각 회전시킵니다.
        self.sbus.Arm_serial_servo_write(1, degree_of_servo[0] + 90, 100)
        self.sbus.Arm_serial_servo_write(2, degree_of_servo[1], 100)

        # 발행을 준비합니다.
        joint_state_msg = JointState()
        joint_state_msg.name = ["servo1", "servo2"]
        # Dofbot는 오직 Degree만을 사용하므로, Radian 단위를 사용하는 JointState 메시지에 넣을 때 꼭 단위 변환을 해주어야 합니다.
        joint_state_msg.position = [self.sbus.Arm_serial_servo_read(1) * DE2RA, self.sbus.Arm_serial_servo_read(2) * DE2RA]
        joint_state_msg.header.stamp = rospy.Time.now()
        self.joint_state_publisher(joint_state_msg)

    def print_slope_and_angle_info(self, turn_on: bool):
        if turn_on:
            print()

    def print_each_marker_info(self, turn_on: bool, marker_ary: MarkerArray):
        if turn_on:
            for marker in marker_ary:
                # 마커의 정보를 출력합니다.
                print("Header : {0}".format(marker.header))
                print("ID : {0}".format(marker.id))
                print("Type : {0}".format(marker.type))
                # 바운딩 박스의 중점을 출력합니다.
                print("Middle Point Coord : ")
                for i in range(8):
                    print("\t> ({1:.2f}, {2:.2f}, {3:.2f})".format(i, marker.pose.position.x, marker.pose.position.y, marker.pose.position.z))
                print()

if __name__ == '__main__':
    while not rospy.is_shutdown():
        RobotManipulation()
        rospy.init_node('manipulator_state_publisher')
        rospy.spin()