#! /usr/bin/env python

import rospy
from nav_msgs.msg import Odometry


def callback(msg):
    print("-----flex---------------")
    print(msg.header)


rospy.init_node('odom_sub_node')
sub = rospy.Subscriber('/odom', Odometry, callback)
rospy.spin()
 