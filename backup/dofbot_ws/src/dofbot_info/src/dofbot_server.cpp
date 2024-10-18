#include <iostream>
#include "ros/ros.h"
#include <dofbot_info/kinemarics.h>
#include "dofbot_kinemarics.h"

using namespace KDL;
using namespace std;
Dofbot dofbot = Dofbot();

const float RA2DE = 180.0f / M_PI;

const float DE2RA = M_PI / 180.0f;
const char *urdf_file = "/home/dofbot/dofbot_ws/src/dofbot_info/urdf/dofbot.urdf";
int a = 0;


bool srvicecallback(dofbot_info::kinemaricsRequest &request, dofbot_info::kinemaricsResponse &response) {
    if (request.kin_name == "fk") {
        double joints[]{request.cur_joint1, request.cur_joint2, request.cur_joint3, request.cur_joint4,
                        request.cur_joint5};

        vector<double> initjoints;

        vector<double> initpos;

        for (int i = 0; i < 5; ++i) initjoints.push_back((joints[i] - 90) * DE2RA);

        dofbot.dofbot_getFK(urdf_file, initjoints, initpos);
        cout << "--------- Fk ---------" << a << "--------- Fk ---------" << endl;
        cout << "XYZcoordinate: " << initpos.at(0) << " ," << initpos.at(1) << " ," << initpos.at(2) << endl;
        cout << "Roll,Pitch,Yaw： " << initpos.at(3) << " ," << initpos.at(4) << " ," << initpos.at(5) << endl;
        response.x = initpos.at(0);
        response.y = initpos.at(1);
        response.z = initpos.at(2);
        response.Roll = initpos.at(3);
        response.Pitch = initpos.at(4);
        response.Yaw = initpos.at(5);
    }
    if (request.kin_name == "ik") {

//         double tool_param = 0.12;

        double Roll = 2.5 * request.tar_y * 100 - 207.5;
        double Pitch = 0;
        double Yaw = 0;

//         double init_angle = atan2(double(request.tar_x), double(request.tar_y));

//         double dist = tool_param * sin((180 + Roll) * DE2RA);

//         double distance = hypot(request.tar_x, request.tar_y) - dist;

//         double x = distance * sin(init_angle);
//         double y = distance * cos(init_angle);
//         double z = tool_param * cos((180 + Roll) * DE2RA);
        double x = request.tar_x;
        double y = request.tar_y;
        double z = 0.01;
        ///////////////////////////
        if (request.tar_z >= 0.2) {
            x=request.tar_x;
            y=request.tar_y;
            z=request.tar_z;
            Roll= -90;
        }

        double xyz[]{x, y, z};

        double rpy[]{Roll * DE2RA, Pitch * DE2RA, Yaw * DE2RA};
        cout << xyz[0] << " , " << xyz[1] << " , " << xyz[2] << "\t"
        << rpy[0] << " , " << rpy[1] << " , " << rpy[2] << endl;

        vector<double> outjoints;

        vector<double> targetXYZ;

        vector<double> targetRPY;
        for (int k = 0; k < 3; ++k) targetXYZ.push_back(xyz[k]);
        for (int l = 0; l < 3; ++l) targetRPY.push_back(rpy[l]);

        dofbot.dofbot_getIK(urdf_file, targetXYZ, targetRPY, outjoints);

        cout << "--------- Ik ---------" << a << "--------- Ik ---------" << endl;
        for (int i = 0; i < 5; i++) cout << (outjoints.at(i) * RA2DE) + 90 << ",";
        cout << endl;
        a++;
        response.joint1 = (outjoints.at(0) * RA2DE) + 90;
        response.joint2 = (outjoints.at(1) * RA2DE) + 90;
        response.joint3 = (outjoints.at(2) * RA2DE) + 90;
        response.joint4 = (outjoints.at(3) * RA2DE) + 90;
        response.joint5 = (outjoints.at(4) * RA2DE) + 90;
    }
    return true;
}

int main(int argc, char **argv) {
    cout << "Waiting to receive******" << endl;

    ros::init(argc, argv, "dofbot_server");

    ros::NodeHandle n;

    ros::ServiceServer server = n.advertiseService("dofbot_kinemarics", srvicecallback);

    ros::spin();
    return 0;
}
