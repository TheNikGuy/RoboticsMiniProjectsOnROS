#!/usr/bin/env python

import rospy
import sys
import copy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from math import pi
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list
from ar_week10_test.msg import *

"""
Fucntion to move the Panda robot to a starting configuration, defined in joints space as follows:
start_conf = [0, -pi/4, 0, -pi/2, 0, pi/3, 0]
"""
def go_to_joint_state():
	## First initialize 'moveit_commander' and a 'rospy' node
	moveit_commander.roscpp_initialize(sys.argv)
	move_group = moveit_commander.MoveGroupCommander("panda_arm")
	
	joint_goal = move_group.get_current_joint_values()
	joint_goal[0] = 0
	joint_goal[1] = -pi/4
	joint_goal[2] = 0
	joint_goal[3] = -pi/2
	joint_goal[4] = 0
	joint_goal[5] = pi/3
	joint_goal[6] = 0

	# the go command can be called with joint values
	move_group.go(joint_goal, wait=True)

	return move_group

"""
Fucntion to plan a Cartesian path that will realize the desired motion of the robot end-effector
(i.e. a square of the desired size on the x-y Cartesian plane)
"""
def plan_cartesian_path(move_group, side, scale=1):

	# planning a Cartesian path by specifying a list of waypoints for the end-effector to go through.
	waypoints = []

	wpose = move_group.get_current_pose().pose

	wpose.position.x += scale * side	# Move forward in (x)
	waypoints.append(copy.deepcopy(wpose))

	wpose.position.y += scale * side	# Move sideways(left) in (y)
	waypoints.append(copy.deepcopy(wpose))

	wpose.position.x -= scale * side	# Move backwards in (x)
	waypoints.append(copy.deepcopy(wpose))

	wpose.position.y -= scale * side	# Move sideways(right) in (y)
	waypoints.append(copy.deepcopy(wpose))
	# back to initial

	
	# the compute command can be called with pose values, this is just planning
	(plan, fraction) = move_group.compute_cartesian_path(waypoints, 0.01, 0.0)
	return plan, fraction

"""
Function to display the planned trajectory on rViz
"""
def display_trajectory(plan, trajpub):
	robot = moveit_commander.RobotCommander()

	display_trajectory = moveit_msgs.msg.DisplayTrajectory()
	display_trajectory.trajectory_start = robot.get_current_state()
	display_trajectory.trajectory.append(plan)
	trajpub.publish(display_trajectory)

"""
Function to execute the planned trajectory on rViz
"""
def execute_plan(move_group, plan):
	move_group.execute(plan, wait=True)

def movepandarobot(data):
	print('---------------------------------------------------------------------')
	print('Move Panda - Waiting for the Desired size of Square Trajectory')
	print('---------------------------------------------------------------------')
	side = data.side
	print('Move Panda - Received Square Size - {side}'.format(side=side))
	print('---------------------------------------------------------------------')
	
	print('Move Panda - Going to Start Configuration')
	print('---------------------------------------------------------------------')
	move_group = go_to_joint_state()
	print('---------------------------------------------------------------------')
	print('Move Panda - Planning Motion Trajectory')
	print('---------------------------------------------------------------------')
	cartesian_plan, fraction = plan_cartesian_path(move_group, side)

	#rospy.sleep(0.1)
	print('---------------------------------------------------------------------')
	print('Move Panda - Showing Planned Trajectory')
	print('---------------------------------------------------------------------')
	
	# creating a 'trajpub' ROS publisher which is used to display
	trajpub = rospy.Publisher('/move_group/display_planned_path', moveit_msgs.msg.DisplayTrajectory, queue_size=10)
	display_trajectory(cartesian_plan, trajpub)

	rospy.sleep(10)
	print('---------------------------------------------------------------------')
	print('Move Panda - Executing Planned Trajectory')
	print('---------------------------------------------------------------------')
	execute_plan(move_group, cartesian_plan)


def move_panda_sqaure():
	#creating a node 'move_panda_sqaure'
	rospy.init_node('move_panda_sqaure', anonymous=True)

	#subscribing to the message 'square_size_info'
	rospy.Subscriber('square_size_info', square_size_info, movepandarobot)

	rospy.spin()

if __name__ == '__main__':
	try:
		move_panda_sqaure()		#making a call to the function 'move_panda_sqaure'
	except rospy.ROSInterruptException:
		pass
