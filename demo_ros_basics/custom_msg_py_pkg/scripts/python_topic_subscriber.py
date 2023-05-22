#!/usr/bin python3
import rospy
from custom_msg_cpp_pkg.msg import JointAngle

def callback(msg):
    rospy.loginfo("Received the angle of %s [%d]", msg.joint_name, msg.angle)
    
def listener():
    rospy.init_node('py_topic_subscriber', anonymous=True)
    rospy.Subscriber("/joint_angle", JointAngle, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
