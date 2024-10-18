#include <iostream>
#include "ros/ros.h"
#include <moveit/move_group_interface/move_group_interface.h>

using namespace std;

int main(int argc, char **argv) {

    ros::init(argc, argv, "dofbot_random_move_cpp");

    ros::NodeHandle n;

    ros::AsyncSpinner spinner(1);

    spinner.start();

    moveit::planning_interface::MoveGroupInterface dofbot("dofbot");

    dofbot.setMaxVelocityScalingFactor(1.0);

    dofbot.setMaxAccelerationScalingFactor(1.0);

//    dofbot.setNamedTarget("down");

//    dofbot.move();
//    sleep(0.1);
    while (true) {

        dofbot.setRandomTarget();

        dofbot.move();
        sleep(0.5);
    }
    return 0;
}

