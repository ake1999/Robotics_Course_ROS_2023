#include "ros/ros.h"
#include "custom_msg_cpp_pkg/JointAngle.h"
#include <iostream>

void joint_angle_callback(const custom_msg_cpp_pkg::JointAngle::ConstPtr& msg) {
    ROS_INFO("Received the angle of %s [%d]", msg->joint_name.c_str(), msg->angle);
}

int main(int argc, char **argv) {  
    ros::init(argc, argv,"cpp_topic_subscriber");
    ros::NodeHandle node_obj;
    ros::Subscriber subscriber = node_obj.subscribe("/joint_angle",10,joint_angle_callback);
    ros::spin();
    return 0;
}
