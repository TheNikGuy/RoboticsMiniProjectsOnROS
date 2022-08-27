#!/usr/bin/env python

import rospy
import random
from cr_week8_test.msg import *
from cr_week8_test.srv import *
from bayesian.bbn import *
from bayesian.utils import make_key
from bayesian.exceptions import *

#Function which creates a node which returns Object Size Probability for BBN
def f_O(O):
	return 1.0/2.0

#Function which creates a node which returns Human Action Probability for BBN
def f_HA(HA):
	return 1.0/3.0

#Function which creates a node which returns Human Expression Probability for BBN
def f_HE(HE):
	return 1.0/3.0

#Function which creates a node which returns Robot Expression Probability for BBN
#Values are derived from the Conditional Probability Table (CPT) given in Assignment Statement
def f_RE(O, HA, HE, RE):
	if RE == '1':
		if HE == '1' and HA == '1':
			if O == '1':
				return 0.8
			elif O == '2':
				return 1
		if HE == '1' and HA == '2':
			if O == '1':
				return 0.8
			elif O == '2':
				return 1
		if HE == '1' and HA == '3':
			if O == '1':
				return 0.6
			elif O == '2':
				return 0.8
		
		if HE == '2' and HA == '1':
			if O == '1':
				return 0.0
			elif O == '2':
				return 0
		if HE == '2' and HA == '2':
			if O == '1':
				return 0.0
			elif O == '2':
				return 0.1
		if HE == '2' and HA == '3':
			if O == '1':
				return 0.0
			elif O == '2':
				return 0.2

		if HE == '3' and HA == '1':
			if O == '1':
				return 0.7
			elif O == '2':
				return 0.8
		if HE == '3' and HA == '2':
			if O == '1':
				return 0.8
			elif O == '2':
				return 0.9
		if HE == '3' and HA == '3':
			if O == '1':
				return 0.6
			elif O == '2':
				return 0.7
	
	if RE == '2':
		if HE == '1' and HA == '1':
			if O == '1':
				return 0.2
			elif O == '2':
				return 0.0
		if HE == '1' and HA == '2':
			if O == '1':
				return 0.2
			elif O == '2':
				return 0.0
		if HE == '1' and HA == '3':
			if O == '1':
				return 0.2
			elif O == '2':
				return 0.2
		
		if HE == '2' and HA == '1':
			if O == '1':
				return 0.0
			elif O == '2':
				return 0.0
		if HE == '2' and HA == '2':
			if O == '1':
				return 0.1
			elif O == '2':
				return 0.1
		if HE == '2' and HA == '3':
			if O == '1':
				return 0.2
			elif O == '2':
				return 0.2

		if HE == '3' and HA == '1':
			if O == '1':
				return 0.3
			elif O == '2':
				return 0.2
		if HE == '3' and HA == '2':
			if O == '1':
				return 0.2
			elif O == '2':
				return 0.1
		if HE == '3' and HA == '3':
			if O == '1':
				return 0.2
			elif O == '2':
				return 0.2
	if RE == '3':
		if HE == '1' and HA == '1':
			if O == '1':
				return 0.0
			elif O == '2':
				return 0.0
		if HE == '1' and HA == '2':
			if O == '1':
				return 0.0
			elif O == '2':
				return 0.0
		if HE == '1' and HA == '3':
			if O == '1':
				return 0.2
			elif O == '2':
				return 0.0
		
		if HE == '2' and HA == '1':
			if O == '1':
				return 1.0
			elif O == '2':
				return 1.0
		if HE == '2' and HA == '2':
			if O == '1':
				return 0.9
			elif O == '2':
				return 0.8
		if HE == '2' and HA == '3':
			if O == '1':
				return 0.8
			elif O == '2':
				return 0.6

		if HE == '3' and HA == '1':
			if O == '1':
				return 0.0
			elif O == '2':
				return 0.0
		if HE == '3' and HA == '2':
			if O == '1':
				return 0.0
			elif O == '2':
				return 0.0
		if HE == '3' and HA == '3':
			if O == '1':
				return 0.2
			elif O == '2':
				return 0.1

"""
Callback function for the service 'predict_robot_expression' which implements the BBN and makes the Robot Expression probabilities to be available when the service is called.
"""
def implement(data):
	p = data.info			#info contains the input to 'predict_robot_expression' which is all the values from 'perceived_info' message
	
	O = str(p.object_size)
	HA = str(p.human_action)
	HE = str(p.human_expression)	#as 'build_bbn' input i.e. node and value is accepted in string

	"""
	Building a Bayesian Belief Network which takes all the functions representing nodes and a domain dictionary as parameters 
	"""
	robot_bbn = build_bbn(
		f_O,
		f_HA,
		f_HE,
		f_RE,
		domains=dict(
			O = ['1', '2'],		
			HA = ['1', '2', '3'],
			HE = ['1', '2', '3'],
			RE = ['1', '2', '3']))	
	
	"""
	Filtering 'query()' call based on the values received from 'perceived_info' message
	"""
	if O =='0' and HA == '0' and HE == '0':
		robot = robot_bbn.query()
	elif O == '0' and HA == '0':
		robot = robot_bbn.query(HE=HE)
	elif O == '0' and HE == '0':
		robot = robot_bbn.query(HA=HA)
	elif HA == '0' and HE == '0':
		robot = robot_bbn.query(O=O)
	elif HE == '0':
		robot = robot_bbn.query(O=O, HA=HA)
	elif HA == '0':
		robot = robot_bbn.query(O=O, HE=HE)
	elif O == '0':
		robot = robot_bbn.query(HA=HE, HE=HE)

	perc = {n[1]:v for n,v in robot.items() if n[0]=='RE'}		#retrieving the Robot Expression as Value:Marginal
	
	"""
	Returning the Marginals i.e. Robot Expression Probabilities and ID as the response from service 'predict_robot_expression'
	"""
	return predict_robot_expressionResponse(p.id, perc['1'], perc['2'], perc['3'])


def robot_expression_prediction():	
	rospy.init_node('robot_expression_prediction', anonymous=True)		#creating a node 'robot_expression_prediction'
	
	#creating a ROS Service 'predict_robot_expression'
	s = rospy.Service('predict_robot_expression', predict_robot_expression, implement)
	
	rospy.spin()

if __name__ == '__main__':
	try:
		robot_expression_prediction()			#making a call to the function 'robot_expression_prediction'
	except rospy.ROSInterruptException:
		pass
