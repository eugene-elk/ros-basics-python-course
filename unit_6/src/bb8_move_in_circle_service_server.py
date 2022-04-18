#! /usr/bin/env python

import rospy
from std_srvs.srv import Empty, EmptyResponse
from geometry_msgs.msg import Twist

move = Twist()


def my_callback(request):
    print("The Service move_bb8_in_circle has been called")
    rospy.loginfo("The Service move_bb8_in_circle has been called")
    move.angular.z = 0.2
    move.linear.x = 0.2
    my_pub.publish(move)
    print("Finished service move_bb8_in_circle")
    rospy.loginfo("Finished service move_bb8_in_circle")
    return EmptyResponse()


rospy.init_node('circle_server')
my_service = rospy.Service('/move_bb8_in_circle', Empty, my_callback)
my_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)

rospy.spin()
