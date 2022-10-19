#!/usr/bin/env python

import rospy

def param():
	rospy.init_node('param', anonymous=True)
	rate = rospy.Rate(1)
	while not rospy.is_shutdown():
	value = rospy.get_param('/mode', 'not_found')
	rospy.loginfo(value)
	rate.sleep()

if __name__=="__main__":
	try:
		param()
	except rospy.ROSInterruptException:
		pass
