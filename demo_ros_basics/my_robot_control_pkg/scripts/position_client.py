#!/usr/bin python3

import rospy
from my_robot_control_pkg.srv import DesiredPosition, DesiredPositionRequest

def position_client():
    rospy.wait_for_service('desired_position')
    try:
        desired_position = rospy.ServiceProxy('desired_position', DesiredPosition)
        request = DesiredPositionRequest()
        request.x = 1.0  # Set the desired position coordinates
        request.y = 2.0
        request.z = 3.0
        response = desired_position(request)
        rospy.loginfo("Received response: %s", response.success)
    except rospy.ServiceException as e:
        rospy.logerr("Service call failed: %s", e)

if __name__ == '__main__':
    rospy.init_node('position_client')
    position_client()
