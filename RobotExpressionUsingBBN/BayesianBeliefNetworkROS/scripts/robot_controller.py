#!/usr/bin/env python

import rospy
from cr_week8_test.msg import *
from cr_week8_test.srv import *
from bayesian.bbn import *

"""
Callback function for 'perceived_info' which calls the service 'predict_robot_expression' and publishes Robot Expression probabilities on 'robot_info' topic
"""
def performperception(data):
	#creating a Publisher which returns values on topic 'robot_info'
	repub = rospy.Publisher('robot_info', robot_info, queue_size=10)
	#calling 'predict_robot_expression' service and storing response in 'compute'
	compute = rospy.ServiceProxy('predict_robot_expression', predict_robot_expression)
	
	re = robot_info()
	r = compute(data)
	
	#Assigning the 'robot_info' message variables with response from 'predict_robot_expression' service
	re.id = data.id
	re.p_happy = r.p_happy
	re.p_sad = r.p_sad
	re.p_neutral = r.p_neutral

	repub.publish(re)	#publishing robot expression probabilities on 'robot_info' message
	

def robot_controller():
	#creating a node 'robot_controller'
	rospy.init_node('robot_controller', anonymous=True)
	#waiting for the response from service 'predict_robot_expression'
	rospy.wait_for_service('predict_robot_expression')
	
	#subscribing to 'perceived_info'
	rospy.Subscriber('perceived_info', perceived_info, performperception)
	
	rospy.spin()

if __name__ == '__main__':
	try:
		robot_controller()		#making a call to the function 'interaction_generator'
	except rospy.ROSInterruptException:
		pass
