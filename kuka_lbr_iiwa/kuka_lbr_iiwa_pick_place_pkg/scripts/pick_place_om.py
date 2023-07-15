import sys
import rospy
import moveit_commander
import geometry_msgs.msg
import tf2_ros
import time

# Initialize MoveIt Commander and ROS node
moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('pick_and_place', anonymous=True)

# Create MoveGroupCommander objects for the arm and gripper groups
arm_group = moveit_commander.MoveGroupCommander('arm')
gripper_group = moveit_commander.MoveGroupCommander('gripper')

# Set planning time and other parameters
arm_group.set_planning_time(10)
arm_group.set_goal_tolerance(0.01)
gripper_group.set_goal_tolerance(0.002)

# Set velocity scaling factor (0.0 - 1.0)
arm_group.set_max_velocity_scaling_factor(0.6)  # Example: Set to 0.5 for 50% of maximum velocity

# Define pick and place poses as geometry_msgs.msg.Pose objects
#pick_pose = geometry_msgs.msg.Pose()
# Set the pick pose coordinates (position and orientation)
#pick_pose.position.x = 0.0
#pick_pose.position.y = 0.2
#pick_pose.position.z = 0.05
#pick_pose.orientation.x = 0.0
#pick_pose.orientation.y = 0.707
#pick_pose.orientation.z = 0.0
#pick_pose.orientation.w = 0.707

#place_pose = geometry_msgs.msg.Pose()
# Set the place pose coordinates (position and orientation)
#place_pose.position.x = 0.01
#place_pose.position.y = 0.0
#place_pose.position.z = 0.01
#place_pose.orientation.x = 0.0
#place_pose.orientation.y = 0.707
#place_pose.orientation.z = 0.0
#place_pose.orientation.w = 0.707

# Open the gripper and deactivate it
gripper_group.go([-0.01, -0.01], wait=True)  # Deactivate gripper
gripper_group.stop()

# Plan and execute the pick motion
#arm_group.set_pose_target(pick_pose)
arm_group.go([0,0.3632,-0.9425,1.5184],wait=True)
arm_group.stop()
#arm_group.clear_pose_targets()
#time.sleep(1)

#pick_pose.position.z = 0.01
#arm_group.set_pose_target(pick_pose)
arm_group.go([0,0.6632,-0.9425,1.5184],wait=True)
arm_group.stop()
#arm_group.clear_pose_targets()

# Activate the gripper and close it
gripper_group.go([0.0027,0.0027], wait=True)  # Activate gripper
gripper_group.stop()

#pick_pose.position.z = 0.05
#arm_group.set_pose_target(pick_pose)
arm_group.go([0,0.3,-0.9425,1.5184],wait=True)
arm_group.stop()
#arm_group.clear_pose_targets()

# Plan and execute the place motion
#arm_group.set_pose_target(place_pose)
arm_group.go([1.57,0.6632,-0.9425,1.5184],wait=True)
arm_group.stop()
#arm_group.clear_pose_targets()


# Open the gripper and deactivate it
gripper_group.go([-0.01, -0.01], wait=True)  # Deactivate gripper
gripper_group.stop()

#place_pose.position.z = 0.05
#arm_group.set_pose_target(place_pose)
arm_group.go([1.57,0.3,-0.9425,1.5184],wait=True)
arm_group.stop()
#arm_group.clear_pose_targets()

# Shutdown MoveIt Commander and ROS node
moveit_commander.roscpp_shutdown()
moveit_commander.os._exit(0)
