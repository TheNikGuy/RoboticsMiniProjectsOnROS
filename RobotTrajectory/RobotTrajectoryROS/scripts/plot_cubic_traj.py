#!/usr/bin/env python
import rospy
from ar_week5_test.msg import cubic_traj_coeffs
from std_msgs.msg import Float32
from datetime import datetime

def callback(data):
	pub1 = rospy.Publisher('position', Float32, queue_size = 1)
	pub2 = rospy.Publisher('velocity', Float32, queue_size = 1)
	pub3 = rospy.Publisher('acceleration', Float32, queue_size = 1)

	t = 0
	start = datetime.now()
	r = rospy.Rate(10)
	
	while (data.tf>t):
		t = (datetime.now()-start).total_seconds()
		pos = data.a0 + (data.a1*t) + (data.a2*(t**2)) + (data.a3*(t**3))
		vel = data.a1 + (2*data.a2*t) + (3*data.a3*(t**2))
		acc = (2*data.a2) + (6*data.a3*t)
		pub1.publish(pos)
		pub2.publish(vel)
		pub3.publish(acc)
		r.sleep()

	#print("Publishing all 3 trajectories")

def plot_cubic_traj():
	rospy.init_node('plot_cubic_traj', anonymous=True)

	rospy.Subscriber('coeffs', cubic_traj_coeffs, callback)

	rospy.spin()

if __name__ == '__main__':
    try:
        plot_cubic_traj()
    except rospy.ROSInterruptException:
        pass
