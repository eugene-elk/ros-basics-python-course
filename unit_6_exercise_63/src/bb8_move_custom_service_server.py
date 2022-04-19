#! /usr/bin/env python

import rospy
from my_custom_srv_msg_pkg.srv import MyCustomServiceMessage, MyCustomServiceMessageResponse
from geometry_msgs.msg import Twist

move = Twist()


def callback(request):
    print("The Service move_bb8_in_circle_custom has been called")

    move.angular.z = 0.2
    move.linear.x = 0.2
    my_pub.publish(move)

    print('Start sleep')
    rospy.sleep(request.duration)
    print('Finish sleep')

    move.angular.z = 0
    move.linear.x = 0
    my_pub.publish(move)

    result = MyCustomServiceMessageResponse()
    result.success = True

    print("Finished service move_bb8_in_circle_custom")
    return result


rospy.init_node('circle_custom_server')
my_service = rospy.Service(
    '/move_bb8_in_circle_custom', MyCustomServiceMessage, callback)
my_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)

rospy.spin()
