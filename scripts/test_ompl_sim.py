#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from math import pi, sin, cos
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list
from geometry_msgs.msg import Pose

# Setup
moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('test_ompl_commander', anonymous=True)
robot = moveit_commander.RobotCommander(ns="panda")
scene= moveit_commander.PlanningSceneInterface()
group_name="panda_arm"
move_group=moveit_commander.MoveGroupCommander(group_name)

# Set planning pipeline name
#move_group.set_planner_id("PTP")
move_group.set_planner_id("ompl")

joint_goal = move_group.get_current_joint_values()
joint_goal[0] = 0
joint_goal[1] = -pi/4
joint_goal[2] = 0
joint_goal[3] = -pi/2
joint_goal[4] = 0
joint_goal[5] = pi/3
joint_goal[6] = 0

move_group.go(joint_goal, wait=True)

center = [0.6, 0.0, 0.2]
radius = 0.1
step = pi/8
angle = 0

pose_target = Pose()
pose_target.orientation.x = 1.0
pose_target.orientation.y = 0.0
pose_target.orientation.z = 0.0
pose_target.orientation.w = 0.0

while not rospy.is_shutdown():
	pose_target.position.x = center[0] - cos(angle) * radius
	pose_target.position.y = center[1] + sin(angle) * radius
	pose_target.position.z = center[2]
	move_group.set_pose_target(pose_target)
	move_group.go(wait=True)
	move_group.stop()
	move_group.clear_pose_targets()
	angle += step
