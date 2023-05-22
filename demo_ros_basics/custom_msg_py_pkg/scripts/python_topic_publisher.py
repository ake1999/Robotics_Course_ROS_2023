#!/usr/bin python3

import rospy
from custom_msg_cpp_pkg.msg import JointAngle

def talker():
    pub = rospy.Publisher('/joint_angle', JointAngle, queue_size=10)
    rospy.init_node('py_topic_publisher', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    number_count = 1
    while not rospy.is_shutdown():
        msg = JointAngle()
        msg.joint_name = "joint_2"
        msg.angle = number_count
        rospy.loginfo("Send the angle of %s [%d]", msg.joint_name, msg.angle)
        pub.publish(msg)
        rate.sleep()
        number_count += 1

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
