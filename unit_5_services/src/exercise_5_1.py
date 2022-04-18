#! /usr/bin/env python

import rospy
# Import the service message used by the service /trajectory_by_name
from iri_wam_reproduce_trajectory.srv import ExecTraj, ExecTrajRequest
import rospkg

rospy.init_node('service_execute_trajectory_client')

rospack = rospkg.RosPack()
traj_filepath = rospack.get_path(
    'iri_wam_reproduce_trajectory') + "/config/get_food.txt"

rospy.wait_for_service('/execute_trajectory')

exec_traj_service = rospy.ServiceProxy('/execute_trajectory', ExecTraj)
# Create an object of type TrajByNameRequest
exec_traj_object = ExecTrajRequest()
# Fill the variable traj_name of this object with the desired value
exec_traj_object.file = traj_filepath
# Send through the connection the name of the trajectory to be executed by the robot
result = exec_traj_service(exec_traj_object)
# Print the result given by the service called
print(result)
