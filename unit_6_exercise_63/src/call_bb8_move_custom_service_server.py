#! /usr/bin/env python

import rospy
from my_custom_srv_msg_pkg.srv import MyCustomServiceMessage, MyCustomServiceMessageRequest

rospy.init_node('circle_custom_client')
print("Waiting for service server")
rospy.wait_for_service('/move_bb8_in_circle_custom')

print("Send request to service server")
circle_service = rospy.ServiceProxy(
    '/move_bb8_in_circle_custom', MyCustomServiceMessage)
circle_request = MyCustomServiceMessageRequest()
circle_request.duration = 7
result = circle_service(circle_request)
print(result)
