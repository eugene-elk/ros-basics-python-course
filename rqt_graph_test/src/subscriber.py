#! /usr/bin/env python

import rospy
from std_msgs.msg import Int32


def callback(msg):
    rospy.loginfo("Subscriber reads: " + str(msg))


rospy.init_node('subscribe_node')
sub = rospy.Subscriber('/topic_test', Int32, callback)
rate = rospy.Rate(1)
rospy.spin()
