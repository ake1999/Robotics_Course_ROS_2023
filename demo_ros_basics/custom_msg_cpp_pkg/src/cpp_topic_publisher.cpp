#include "ros/ros.h"
#include "custom_msg_cpp_pkg/JointAngle.h"
#include <iostream>

int main(int argc, char **argv) {
    ros::init(argc, argv,"cpp_topic_publisher");
    ros::NodeHandle node_obj;
    ros::Publisher publisher = node_obj.advertise<custom_msg_cpp_pkg::JointAngle>("/joint_angle", 10);
    ros::Rate loop_rate(10);
    int number_count = 0;

    while ( ros::ok() ) {
        custom_msg_cpp_pkg::JointAngle msg;
        msg.joint_name = "joint_1";
        msg.angle = number_count;
        ROS_INFO("send the angle of %s [%d]", msg.joint_name.c_str(), msg.angle);
        publisher.publish(msg);
        loop_rate.sleep();
        ++number_count;
    }

    return 0;
}
