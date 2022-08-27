#!/usr/bin/env python
import rospy
import numpy as np
from numpy.linalg import inv
from ar_week5_test.srv import *

def handle_computation(req):
	
	param = req.params
	
	expres = np.array([[1, param.t0, param.t0**2, param.t0**3], [0, 1, 2*param.t0, 3*(param.t0**2)], [1, param.tf, param.tf**2, param.tf**3], [0, 1, 2*param.tf, 3*(param.tf**2)]], ndmin=2)
	
	qvmat = np.array([param.p0, param.v0, param.pf, param.vf], ndmin=1).T
	
	print(qvmat)
	
	result = np.dot(inv(expres), qvmat)

	coeffmat = list(result)	

	print(coeffmat)

	return compute_cubic_trajResponse(coeffmat[0], coeffmat[1], coeffmat[2], coeffmat[3])
  
def compute_cubic_coeffs():
    	rospy.init_node('compute_cubic_coeffs', anonymous=True)
	
	s = rospy.Service('handle_computation_service', compute_cubic_traj, handle_computation)

	rospy.spin()

if __name__ == '__main__':
    compute_cubic_coeffs()
