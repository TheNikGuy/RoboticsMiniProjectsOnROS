#!/usr/bin/env python

import rospy
import random
from cr_week8_test.msg import *

def interaction_generator():
	#creating a node 'interaction_generator'
	rospy.init_node('interaction_generator', anonymous=True)

	#creating a Publisher which returns values on topic 'object_info'
	oipub = rospy.Publisher('object_info', object_info, queue_size=10)
	#creating a Publisher which returns values on topic 'human_info'
	hipub = rospy.Publisher('human_info', human_info, queue_size=10)

	oi = object_info()		#taking the variables from message 'object_info'
	hi = human_info()		#taking the variables from message 'human_info'
	oi.id = 1
	rate = rospy.Rate(0.1) 	# to generate values after every 10 secs
	while not rospy.is_shutdown():
		oi.object_size = random.randint(1, 2) 	#generating a random integer 1 or 2 for object size
		hi.id = oi.id
		hi.human_action = random.randint(1, 3)	#generating a random integer between 1 and 3 for human action
		hi.human_expression = random.randint(1, 3)	#generating a random integer between 1 and 3 for human expression
		
		oipub.publish(oi)	#publishing object variables on object_info message
		hipub.publish(hi)	#publishing human variables on human_info message
		
		rate.sleep()
		
		oi.id += 1		#incrementing the ID after 10 secs

if __name__ == '__main__':
	try:
		interaction_generator()		#making a call to the function 'interaction_generator'
	except rospy.ROSInterruptException:
		pass
