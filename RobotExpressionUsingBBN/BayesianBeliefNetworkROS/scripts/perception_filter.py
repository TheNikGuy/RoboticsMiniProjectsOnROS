#!/usr/bin/env python

import rospy
import random
from message_filters import ApproximateTimeSynchronizer, Subscriber
from cr_week8_test.msg import *

#ApproximateTimeSynchronizer callback
def robotperception(object, human):
	#generating a random integer between 1 and 3 for perception of robot i.e. if one of the sensor fails
	perception = random.randint(1, 8)
	#creating a Publisher which returns values on topic 'perceived_info'
	rppub = rospy.Publisher('perceived_info', perceived_info, queue_size=10)
	
	#selecting which value to be unrecognized based on the conditions stated in Assignment Statement
	if perception == 1:
		object.object_size = 0
	if perception == 2:
		human.human_action = 0
	if perception == 3:
		human.human_expression = 0
	if perception == 4:
		object.object_size = 0
		human.human_action = 0
	if perception == 5:
		object.object_size = 0
		human.human_expression = 0
	if perception == 6:
		human.human_action = 0
		human.human_expression = 0
	if perception == 7:
		object.object_size = 0
		human.human_action = 0
		human.human_expression = 0
	if perception == 8:
		None

	#publishing perceived variables on perceived_info message
	rppub.publish(object.id, object.object_size, human.human_action, human.human_expression)

def perception_filter():	
	rospy.init_node('perception_filter', anonymous=True)
	
	#subscribing to 'object_info' with message_filters::Subscriber
	object_sub = Subscriber('object_info', object_info)
	#subscribing to 'human_info' with message_filters::Subscriber
	human_sub = Subscriber('human_info', human_info)
	
	#using ApproximateTimeSynchronizer for making simultaneous calls to 2 subscriber
	ats = ApproximateTimeSynchronizer([object_sub, human_sub], queue_size=10, slop=0.1, allow_headerless=True)
	#implementing callback	
	ats.registerCallback(robotperception)
	
	rospy.spin()

if __name__ == '__main__':
	try:
		perception_filter()
	except rospy.ROSInterruptException:
		pass
