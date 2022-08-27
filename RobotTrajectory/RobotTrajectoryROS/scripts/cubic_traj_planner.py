#!/usr/bin/env python
import rospy
from ar_week5_test.srv import *
from ar_week5_test.msg import cubic_traj_params
from ar_week5_test.msg import cubic_traj_coeffs

def callback(data):
	pub = rospy.Publisher('coeffs', cubic_traj_coeffs, queue_size=10)
    
	try:
		compute = rospy.ServiceProxy('handle_computation_service', compute_cubic_traj)
		resp = compute(data)

		coeffs = cubic_traj_coeffs()

		coeffs.a0 = resp.a0
		coeffs.a1 = resp.a1
		coeffs.a2 = resp.a2
		coeffs.a3 = resp.a3
		coeffs.t0 = data.t0
		coeffs.tf = data.tf

		print coeffs
		pub.publish(coeffs)

	except rospy.ServiceException as e:
		print "Service call failed: %s" %e


def cubic_traj_planner():
    rospy.init_node('cubic_traj_planner', anonymous=True)
    rospy.wait_for_service('handle_computation_service')
    rospy.Subscriber("points_generator", cubic_traj_params, callback)
    rospy.spin()
	
if __name__ == '__main__':
    cubic_traj_planner()
