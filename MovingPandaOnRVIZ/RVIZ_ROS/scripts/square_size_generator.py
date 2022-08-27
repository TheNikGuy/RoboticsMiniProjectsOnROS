#!/usr/bin/env python

import rospy
import random
from ar_week10_test.msg import *

def square_size_generator():
	#creating a node 'square_size_generator'
	rospy.init_node('square_size_generator', anonymous=True)

	#creating a Publisher which returns values on topic 'square_size_info'
	sidepub = rospy.Publisher('square_size_info', square_size_info, queue_size=10)

	ss = square_size_info()		#taking the variables from message 'square_size_info'

	rate = rospy.Rate(0.05) 	# to generate values after every 20 secs
	while not rospy.is_shutdown():
		ss.side = random.uniform(0.05, 0.20) 	#generating a random float between 0.05 and 0.20 for square side
		
		sidepub.publish(ss)	#publishing object variables on square_size_info message
		rospy.loginfo(ss)

		rate.sleep()

if __name__ == '__main__':
	try:
		square_size_generator()		#making a call to the function 'square_size_generator'
	except rospy.ROSInterruptException:
		pass
