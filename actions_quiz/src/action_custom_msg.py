#! /usr/bin/env python

import time
import rospy
import actionlib
# from geometry_msgs.msg import Twist
from std_msgs.msg import Empty
from actions_quiz.msg import CustomActionMsgFeedback, CustomActionMsgResult, CustomActionMsgAction


class ActionCustomMsg():

    _feedback = CustomActionMsgFeedback()
    _result = CustomActionMsgResult()

    def __init__(self):
        self._as = actionlib.SimpleActionServer(
            "action_custom_msg_as", CustomActionMsgAction, self.goal_callback, False)
        self._as.start()

    def goal_callback(self, goal):

        r = rospy.Rate(1)
        success = True

        self.takeoff = rospy.Publisher('/drone/takeoff', Empty, queue_size=1)
        self.landing = rospy.Publisher('/drone/land', Empty, queue_size=1)
        self.empty_msg = Empty()

        if goal.goal == "TAKEOFF":
            while self.takeoff.get_num_connections() < 1:
                rospy.loginfo("Waiting for connection for Takeoff")
                time.sleep(0.1)
            self.takeoff.publish(self.empty_msg)

            self._feedback.feedback = 'TAKEOFF'
            for i in range(3):
                self._as.publish_feedback(self._feedback)
                r.sleep()

        elif goal.goal == "LAND":
            while self.landing.get_num_connections() < 1:
                rospy.loginfo("Waiting for connection for Landing")
                time.sleep(0.1)
            self.landing.publish(self.empty_msg)

            self._feedback.feedback = 'LAND'
            for i in range(3):
                self._as.publish_feedback(self._feedback)
                r.sleep()

        else:
            rospy.logwarn("Allowed commands: TAKEOFF, LAND")

        if success:
            self._result = Empty()
            self._as.set_succeeded(self._result)


if __name__ == '__main__':
    rospy.init_node('action_custom_msg_node')
    ActionCustomMsg()
    rospy.spin()
