#!/usr/bin/env python
from geometry_msgs.msg import Twist
import rospy

def callback(vel_message):
    print(vel_message)
    if vel_message.linear.x > 0:
	print('Up button is pressed!')
    elif vel_message.linear.x < 0:
	print('Down button is pressed!')
    elif vel_message.angular.z > 0:
	print('Left button is pressed!')
    elif vel_message.angular.z < 0:
	print('Right button is pressed!')

def listener():
    rospy.init_node('listener', anonymous=True)    
    rospy.Subscriber('/turtle1/cmd_vel', Twist, callback)
    rospy.spin() 
if __name__ == '__main__':
    listener()
