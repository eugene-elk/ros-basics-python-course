#! /usr/bin/env python

import rospy
from std_msgs.msg import Int32

rospy.init_node('publish_node')
rate = rospy.Rate(1)
pub = rospy.Publisher('/topic_test', Int32, queue_size=1)

value_to_publish = 0

while not rospy.is_shutdown():
    rospy.loginfo("Publisher writes: " + str(value_to_publish))
    pub.publish(value_to_publish)
    value_to_publish += 1
    rate.sleep()
