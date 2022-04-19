#! /usr/bin/env python

import rospy
from services_quiz.srv import BB8CustomServiceMessage, BB8CustomServiceMessageRequest

rospy.init_node('client')
rospy.wait_for_service('/move_bb8_in_square_custom')

# print("Send request to service server")
square_service = rospy.ServiceProxy(
    '/move_bb8_in_square_custom', BB8CustomServiceMessage)
square_request = BB8CustomServiceMessageRequest()

square_request.side = 1
square_request.repetitions = 2
result = square_service(square_request)

square_request.side = 2
square_request.repetitions = 1
result = square_service(square_request)
