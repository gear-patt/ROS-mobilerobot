#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

def turtle_triangular_move():
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rospy.init_node('triangle_move', anonymous=True)
    rate = rospy.Rate(10)
    tw = Twist()
    x_count = 0
    while not rospy.is_shutdown():
	if x_count < 10:
		tw.linear.x = 3
		tw.linear.y = 0
		tw.linear.z = 0
		tw.angular.x = 0
		tw.angular.y = 0
		tw.angular.z = 0
		pub.publish(tw)
		x_count+=1
		rate.sleep()
	elif x_count >= 10 and x_count < 15:
		tw.linear.x = -3
		tw.linear.y = 3
		tw.linear.z = 0
                tw.angular.x = 0
                tw.angular.y = 0
                tw.angular.z = 0
		pub.publish(tw)
                x_count+=1
		rate.sleep()
	elif x_count >= 15 and x_count < 20:
		tw.linear.x = -3
                tw.linear.y = -3
                tw.linear.z = 0
                tw.angular.x = 0
                tw.angular.y = 0
                tw.angular.z = 0
                pub.publish(tw)
		x_count+=1
		rate.sleep()
	elif x_count >= 20 and x_count<25:
		tw.linear.x = 3
                tw.linear.y = 0
                tw.linear.z = 0
                tw.angular.x = 0
                tw.angular.y = 0
                tw.angular.z = 0
                pub.publish(tw)
		x_count+=1
		rate.sleep()
		
	elif x_count==25:
		tw.linear.x = 0
                tw.linear.y = 0
                tw.linear.z = 0
                tw.angular.x = 0
                tw.angular.y = 0
                tw.angular.z = 0
                pub.publish(tw)
                rate.sleep()
		break
if __name__ == '__main__':
    try:
        turtle_triangular_move()
    except rospy.ROSInterruptException:
        pass
