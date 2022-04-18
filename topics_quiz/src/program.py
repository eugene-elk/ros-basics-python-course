#! /usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist


def callback(msg):
    left, front, right = msg.ranges[719], msg.ranges[360], msg.ranges[0]
    print(left, front, right)

    move.linear.x = 0
    move.angular.z = 0

    if front > 1:
        move.linear.x = 0.3
    else:
        move.linear.x = 0.2
        move.angular.z = 0.3

    if right < 1:
        move.angular.z = 0.3
    if left < 1:
        move.angular.z = -0.3

    # if front < 1:
    #     move.linear.x = 0.2
    #     move.angular.z = 0.3
    # elif right < 1:
    #     move.linear.x = 0
    #     move.angular.z = 0.3
    # elif left < 1:
    #     move.linear.x = 0
    #     move.angular.z = -0.3
    # else:
    #     move.linear.x = 0.2
    #     move.angular.z = 0

    pub.publish(move)


rospy.init_node('topics_quiz_node')
rate = rospy.Rate(2)
sub = rospy.Subscriber('/kobuki/laser/scan', LaserScan, callback)
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)

move = Twist()
move.linear.x = 0
move.angular.z = 0

rospy.spin()
