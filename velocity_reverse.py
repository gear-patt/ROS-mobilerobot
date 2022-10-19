#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

pub = rospy.Publisher('turtle1/cmd_vel_reversed', Twist, queue_size=10)

def callback(data):
	data_out = Twist()
	data_out.linear.x = -data.linear.x
	data_out.angular.z = -data.angular.z
	pub.publish(data_out)

def listener():
	rospy.init_node('velocity_reverse')
	rospy.Subscriber('turtle1/cmd_vel', Twist, callback)
	rospy.spin()

if __name__ == '__main__':
	listener()
