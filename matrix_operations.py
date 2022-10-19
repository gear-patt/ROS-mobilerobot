#!/usr/bin/env python

from __future__ import print_function

from beginner_tutorials.srv import MatrixOperations,MatrixOperationsResponse
import rospy
    
def mat_op(req):
    value = rospy.get_param('/mode', 'sum') #sum is the default
    if value == 'sum':
	print('Returning the sum of all elements: ' + str(req.a11+req.a12+req.a21+req.a22))
	return MatrixOperationsResponse(req.a11+req.a12+req.a21+req.a22)
    elif value == 'max':
	print('Returning the max of all elements: ' + str(max([req.a11,req.a12,req.a21,req.a22])))
	return MatrixOperationsResponse(max([req.a11,req.a12,req.a21,req.a22]))
    elif value == 'min':
        print('Returning the min of all elements: ' + str(min([req.a11,req.a12,req.a21,req.a22])))
	return MatrixOperationsResponse(min([req.a11,req.a12,req.a21,req.a22]))
    elif value == 'det':
	print('Returning the det of the matrix: ' + str(req.a11*req.a22-req.a12*req.a21))
	return MatrixOperationsResponse(req.a11*req.a22-req.a12*req.a21)

def matrix_operations_server():
    rospy.init_node('matrix_operations', anonymous=True)
    rate = rospy.Rate(1)
    s = rospy.Service('matrix_operations', MatrixOperations, mat_op)
    print("Ready to define the matrix")
    rospy.spin()

if __name__ == "__main__":
    matrix_operations_server()
