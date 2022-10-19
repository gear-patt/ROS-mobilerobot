#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
import sys

def turtle_circular_move(radius):
    pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)
    rospy.init_node('circularmove')
    rate = rospy.Rate(10) # 10hz
    tw = Twist()
    while not rospy.is_shutdown():
	tw.linear.x = radius
	tw.linear.y = 0
	tw.linear.z = 0
	tw.angular.x = 0
	tw.angular.y = 0
	tw.angular.z = 1
	rospy.loginfo("Radius = %f", radius)
	pub.publish(tw)
	rate.sleep()
if __name__ == '__main__':
    try:
        turtle_circular_move(float(2))
    except rospy.ROSInterruptException:
        pass
