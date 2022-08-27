#!/usr/bin/env python

import rospy
import random
from ar_week5_test.msg import cubic_traj_params

def points_generator():
    pub = rospy.Publisher('points_generator', cubic_traj_params, queue_size=10)
    rospy.init_node('points_generator', anonymous=True)
    param = cubic_traj_params()
    rate = rospy.Rate(0.05) # 20sec
    while not rospy.is_shutdown():
        param.p0 = random.uniform(-10, 10)
	param.pf = random.uniform(-10, 10)
	param.v0 = random.uniform(-10, 10)
	param.vf = random.uniform(-10, 10)
	param.t0 = 0
	dt = round(random.uniform(5, 10), 0)
	param.tf = param.t0 + dt
        rospy.loginfo(param)
        pub.publish(param)
        rate.sleep()

if __name__ == '__main__':
    try:
        points_generator()
    except rospy.ROSInterruptException:
        pass
