#! /usr/bin/env python

import rospy
from example42.msg import Age

rospy.init_node('publish_age_node')
rate = rospy.Rate(1)
pubAge = rospy.Publisher('/robot_age', Age, queue_size=1)
age = Age()
age.years = 1
age.months = 3
age.days = 2

while not rospy.is_shutdown():
    pubAge.publish(age)
    rate.sleep()
 