#! /usr/bin/env python

import time
import rospy
import random

# Options: DEBUG, INFO, WARN, ERROR, FATAL
rospy.init_node('log_demo', log_level=rospy.INFO)
rate = rospy.Rate(0.5)

while not rospy.is_shutdown():
    rospy.logdebug("Debug message")
    rospy.loginfo("Info message")
    rospy.logwarn("Warning time: " + str(time.time()))
    port_number = random.randint(1, 100)
    rospy.logerr("Random error: " + str(port_number))
    rospy.logfatal("Fatal_error")
    rate.sleep()
