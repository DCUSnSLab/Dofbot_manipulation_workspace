#!/usr/bin/env python
# coding: utf-8
import Arm_Lib
from time import sleep


class garbage_grap_move:
    def __init__(self):

        self.move_status = True

        self.arm = Arm_Lib.Arm_Device()

        self.grap_joint = 135

    def move(self, joints, joints_down):

        joints_uu = [90, 80, 50, 50, 265, self.grap_joint]

        joints_up = [joints_down[0], 80, 50, 50, 265, 30]

        self.arm.Arm_serial_servo_write6_array(joints_uu, 1000)
        sleep(1)
        for i in range(5):
            self.arm.Arm_serial_servo_write(6, 180, 100)
            sleep(0.08)
            self.arm.Arm_serial_servo_write(6, 30, 100)
            sleep(0.08)

        # self.arm.Arm_serial_servo_write(6, 30, 500)
        # sleep(0.5)

        self.arm.Arm_serial_servo_write6_array(joints, 500)
        sleep(0.5)

        self.arm.Arm_serial_servo_write(6, self.grap_joint, 500)
        sleep(0.5)

        self.arm.Arm_serial_servo_write6_array(joints_uu, 1000)
        sleep(1)

        self.arm.Arm_serial_servo_write(1, joints_down[0], 500)
        sleep(0.5)

        self.arm.Arm_serial_servo_write6_array(joints_down, 1000)
        sleep(1)

        self.arm.Arm_serial_servo_write(6, 30, 500)
        sleep(0.5)

        self.arm.Arm_serial_servo_write6_array(joints_up, 1000)
        sleep(1)

    def arm_run(self, name, joints):

        # Hazardous waste-- Red
        if name == "Syringe" or name == "Used_batteries" or name == "Expired_cosmetics" or name == "Expired_tablets" and self.move_status == True:

            self.move_status = False
            # print("Hazardous waste")
            # print(joints[0], joints[1], joints[2], joints[3], joints[4])

            joints = [joints[0], joints[1], joints[2], joints[3], 265, 30]

            joints_down = [45, 80, 35, 40, 265, self.grap_joint]

            # joints_down = [45, 50, 20, 60, 265, self.grap_joint]

            self.move(joints, joints_down)

            self.move_status = True
        # Recyclable waste--Blue
        if name == "Zip_top_can" or name == "Newspaper" or name == "Old_school_bag" or name == "Book" and self.move_status == True:
            self.move_status = False
            # print("Recyclable waste")
            # print(joints[0], joints[1], joints[2], joints[3], joints[4])
            joints = [joints[0], joints[1], joints[2], joints[3], 265, 30]
            joints_down = [27, 110, 0, 40, 265, self.grap_joint]
            # joints_down = [27, 75, 0, 50, 265, self.grap_joint]
            self.move(joints, joints_down)
            self.move_status = True
        # Kitchen waste-- Green
        if name == "Fish_bone" or name == "Watermelon_rind" or name == "Apple_core" or name == "Egg_shell" and self.move_status == True:
            self.move_status = False
            # print("Kitchen waste")
            # print(joints[0], joints[1], joints[2], joints[3], joints[4])
            joints = [joints[0], joints[1], joints[2], joints[3], 265, 30]
            joints_down = [152, 110, 0, 40, 265, self.grap_joint]
            # joints_down = [147, 75, 0, 50, 265, self.grap_joint]
            self.move(joints, joints_down)
            self.move_status = True

        # Others waste--gray
        if name == "Cigarette_butts" or name == "Toilet_paper" or name == "Peach_pit" or name == "Disposable_chopsticks" and self.move_status == True:
            self.move_status = False
            # print("Others waste")
            # print(joints[0], joints[1], joints[2], joints[3], joints[4])
            joints = [joints[0], joints[1], joints[2], joints[3], 265, 30]
            joints_down = [137, 80, 35, 40, 265, self.grap_joint]
            # joints_down = [133, 50, 20, 60, 265, self.grap_joint]
            self.move(joints, joints_down)
            self.move_status = True
