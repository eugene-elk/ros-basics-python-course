#! /usr/bin/env python

import rospy
from services_quiz.srv import BB8CustomServiceMessage, BB8CustomServiceMessageResponse
from geometry_msgs.msg import Twist

move = Twist()


def callback(request):
    # print("Service has been called")

    count_of_squares = request.repetitions

    for i in range(count_of_squares * 4):

        # print("Move number: ", i)

        move.angular.z = 0
        move.linear.x = 0.5
        my_pub.publish(move)
        rospy.sleep(request.side * 2.4)

        move.angular.z = 0
        move.linear.x = 0
        my_pub.publish(move)
        rospy.sleep(1)

        move.angular.z = 0.53
        move.linear.x = 0
        my_pub.publish(move)
        rospy.sleep(3)

        move.angular.z = 0
        move.linear.x = 0
        my_pub.publish(move)
        rospy.sleep(1)

    result = BB8CustomServiceMessageResponse()
    result.success = True

    # print("Finished service")
    return result


rospy.init_node('server')
my_service = rospy.Service(
    '/move_bb8_in_square_custom', BB8CustomServiceMessage, callback)
my_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)

rospy.spin()
