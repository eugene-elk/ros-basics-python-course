#! /usr/bin/env python

import time
import rospy
import actionlib
from geometry_msgs.msg import Twist
from std_msgs.msg import Empty  # for takeoff and landing
from actionlib.msg import TestFeedback, TestResult, TestAction


class MoveDroneSquareClass():

    _feedback = TestFeedback()
    _result = TestResult()

    def __init__(self):
        self._as = actionlib.SimpleActionServer(
            "square_as", TestAction, self.goal_callback, False)
        self._as.start()

    def move_fwd(self):
        rospy.loginfo("Move Forward")
        self.move.linear.x = 1.0
        self.move.linear.y = 0.0
        self.move.angular.z = 0.0
        while self.pub.get_num_connections() < 1:
            rospy.logwarn("Waiting for connection for moving forward")
            time.sleep(0.1)
            self.seconds += 0.1
        self.pub.publish(self.move)

    def move_bwd(self):
        rospy.loginfo("Move Backward")
        self.move.linear.x = -1.0
        self.move.linear.y = 0.0
        self.move.angular.z = 0.0
        while self.pub.get_num_connections() < 1:
            rospy.logwarn("Waiting for connection for moving backward")
            time.sleep(0.1)
            self.seconds += 0.1
        self.pub.publish(self.move)

    def move_right(self):
        rospy.loginfo("Move Right")
        self.move.linear.x = 0.0
        self.move.linear.y = 1.0
        self.move.angular.z = 0.0
        while self.pub.get_num_connections() < 1:
            rospy.logwarn("Waiting for connection for moving right")
            time.sleep(0.1)
            self.seconds += 0.1
        self.pub.publish(self.move)

    def move_left(self):
        rospy.loginfo("Move Left")
        self.move.linear.x = 0.0
        self.move.linear.y = -1.0
        self.move.angular.z = 0.0
        while self.pub.get_num_connections() < 1:
            rospy.logwarn("Waiting for connection for moving right")
            time.sleep(0.1)
            self.seconds += 0.1
        self.pub.publish(self.move)

    def stop(self):
        rospy.loginfo("Stop Drone")
        self.move.linear.x = 0.0
        self.move.linear.y = 0.0
        self.move.angular.z = 0.0
        while self.pub.get_num_connections() < 1:
            rospy.logwarn("Waiting for connection to stop")
            time.sleep(0.1)
            self.seconds += 0.1
        self.pub.publish(self.move)

    def goal_callback(self, goal):

        r = rospy.Rate(1)
        success = True

        self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        self.move = Twist()
        self.takeoff = rospy.Publisher('/drone/takeoff', Empty, queue_size=1)
        self.landing = rospy.Publisher('/drone/land', Empty, queue_size=1)
        self.empty_msg = Empty()

        self.square_side_seconds = goal.goal
        self.sleep_in_corner_seconds = 2.0
        self.seconds = 0.0

        while self.takeoff.get_num_connections() < 1:
            rospy.loginfo("Waiting for connection for Takeoff")
            time.sleep(1)
        self.takeoff.publish(self.empty_msg)

        for i in range(0, 4):

            if self._as.is_preempt_requested():
                rospy.loginfo('The goal has been cancelled/preempted')
                self._as.set_preempted()
                success = False
                break

            if i == 0:
                self.move_fwd()
                time.sleep(self.square_side_seconds)
                self.seconds += self.square_side_seconds
                self.stop()
                time.sleep(self.sleep_in_corner_seconds)
                self.seconds += self.sleep_in_corner_seconds

            elif i == 1:
                self.move_right()
                time.sleep(self.square_side_seconds)
                self.seconds += self.square_side_seconds
                self.stop()
                time.sleep(self.sleep_in_corner_seconds)
                self.seconds += self.sleep_in_corner_seconds

            elif i == 2:
                self.move_bwd()
                time.sleep(self.square_side_seconds)
                self.seconds += self.square_side_seconds
                self.stop()
                time.sleep(self.sleep_in_corner_seconds)
                self.seconds += self.sleep_in_corner_seconds

            elif i == 3:
                self.move_left()
                time.sleep(self.square_side_seconds)
                self.seconds += self.square_side_seconds
                self.stop()
                time.sleep(self.sleep_in_corner_seconds)
                self.seconds += self.sleep_in_corner_seconds

            self._feedback.feedback = i
            self._as.publish_feedback(self._feedback)
            r.sleep()

        while self.landing.get_num_connections() < 1:
            rospy.loginfo("Waiting for connection for Landing")
            time.sleep(1)
        self.landing.publish(self.empty_msg)

        if success:
            self._result.result = int(self.seconds)
            rospy.loginfo('Square finished successfull')
            self._as.set_succeeded(self._result)


if __name__ == '__main__':
    rospy.init_node('drone_action_client')
    MoveDroneSquareClass()
    rospy.spin()
