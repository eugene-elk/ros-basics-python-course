#! /usr/bin/env python

import time
import rospy
import actionlib
from ardrone_as.msg import ArdroneAction, ArdroneGoal, ArdroneResult, ArdroneFeedback
from geometry_msgs.msg import Twist
from std_msgs.msg import Empty

PENDING = 0
ACTIVE = 1
DONE = 2
WARN = 3
ERROR = 4

nImage = 1


def feedback_callback(feedback):
    global nImage
    print('[Feedback] image n.%d received' % nImage)
    nImage += 1


rospy.init_node('drone_action_client')
client = actionlib.SimpleActionClient('/ardrone_action_server', ArdroneAction)

pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
move = Twist()
takeoff = rospy.Publisher('/drone/takeoff', Empty, queue_size=1)
landing = rospy.Publisher('/drone/land', Empty, queue_size=1)
empty_msg = Empty()

rospy.loginfo('Waiting for Action Server')
client.wait_for_server()
rospy.loginfo('Action Server Found')

goal = ArdroneGoal()
goal.nseconds = 10

rate = rospy.Rate(1)

while takeoff.get_num_connections() < 1:
    rospy.loginfo("Waiting for connection for Takeoff")
    time.sleep(1)

takeoff.publish(empty_msg)
rospy.loginfo("Taking off")
time.sleep(1)

client.send_goal(goal, feedback_cb=feedback_callback)
state_result = client.get_state()

while state_result < DONE:
    rospy.loginfo("Flying in circle")
    move.linear.x = 0.5
    move.angular.z = 0.5
    pub.publish(move)
    rate.sleep()
    state_result = client.get_state()
    rospy.loginfo("state_result: "+str(state_result))

move.linear.x = 0.0
move.angular.z = 0.0
pub.publish(move)

rospy.loginfo("[Result] State: "+str(state_result))
if state_result == ERROR:
    rospy.logerr("Something went wrong in the Server Side")
if state_result == WARN:
    rospy.logwarn("There is a warning in the Server Side")

while landing.get_num_connections() < 1:
    rospy.loginfo("Waiting for connection for Landing")
    time.sleep(1)

landing.publish(empty_msg)
rospy.loginfo("Landing")
time.sleep(1)

#rospy.loginfo("[Result] State: "+str(client.get_result()))
