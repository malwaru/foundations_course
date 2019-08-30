#!/usr/bin/env python

import rospy

# importing needed msg classes
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from turtlesim.msg import Color
# importing numpy
import numpy as np


# define a class named turtle
class Turtle:
    # constructor
    def __init__(self, turtle_number=1):
        # define a private variable of type Publisher (an instance of Publisher)
        self.__pub = rospy.Publisher('/turtle'+str(turtle_number)+'/cmd_vel',
                                     Twist, queue_size=10)
        # define subscribers for pose and color topics, and assign callbacks
        rospy.Subscriber('/turtle'+str(turtle_number)+'/pose', Pose,
                         callback=self.__pose_cb)

        rospy.Subscriber('/turtle'+str(turtle_number)+'/color_sensor', Color,
                         callback=self.__color_cb)

        # private attribute to hold the turtle pose
        self.__pose = np.array([[0.0],
                               [0.0],
                               [0.0]])
        # private attribute to hold the turtle velocity
        self.__velocity = np.array([[0.0],
                               [0.0],
                               [0.0]])
        # private attribute to hold the color sensor of the turtle
        self.__color = [0,0,0]

    # define a private method to be used as the callback function for the pose msg
    def __pose_cb(self, msg):
        self.__pose = np.array([[msg.x],
                               [msg.y],
                               [msg.theta]])

        self.__velocity = np.array([[msg.linear_velocity],
                                   [0.0],
                                   [msg.angular_velocity]])

    # define a private method to be used as the callback function for the color msg
    def __color_cb(self, msg):
        self.__color = [msg.r, msg.g, msg.b]

    # a public method to be used by the user to get pose
    def get_pose(self):
        return self.__pose

    # a public method to be used by the user to get velocity
    def get_velocity(self):
        return self.__velocity

    # a public method to be used by the user to get color reading
    def sense_color(self):
        return self.__color
