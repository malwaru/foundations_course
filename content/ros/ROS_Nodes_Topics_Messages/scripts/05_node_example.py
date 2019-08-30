#!/usr/bin/env python

import rospy
from utils import Turtle


rospy.init_node('move_turtle')
rate = rospy.Rate(20)

# an instance of Turtle class (or a variable/object of type Turtle)
turtle1 = Turtle(1)

while not rospy.is_shutdown():
    print "\n---------\n", turtle1.get_pose()
    rate.sleep()
