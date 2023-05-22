#!/usr/bin python3

import rospy
from my_robot_control_pkg.srv import DesiredPosition, DesiredPositionResponse

def handle_desired_position(request):
    rospy.loginfo("Received desired position: x=%.2f, y=%.2f, z=%.2f", request.x, request.y, request.z)
    # Perform the necessary operations with the desired position
    # ...
    success = True  # Set the success flag based on the operation's outcome

    return DesiredPositionResponse(success)

def position_server():
    rospy.init_node('position_server')
    rospy.Service('desired_position', DesiredPosition, handle_desired_position)
    rospy.loginfo("Ready to receive desired position requests.")
    rospy.spin()

if __name__ == '__main__':
    position_server()
