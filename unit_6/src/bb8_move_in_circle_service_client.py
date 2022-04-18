#! /usr/bin/env python

import rospy
from std_srvs.srv import Empty, EmptyRequest


rospy.init_node('circle_client')
print("Waiting for service server")
rospy.wait_for_service('/move_bb8_in_circle')

print("Send request to service server")
circle_service = rospy.ServiceProxy('/move_bb8_in_circle', Empty)
circle_request = EmptyRequest()
result = circle_service(circle_request)
print(result)
