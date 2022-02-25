#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float64
from sor_ros101_ramirez.msg import Cylinder

density = 0
density_found = False
volume = 0
volume_found = False

def density_callback(data):
	global density
	global density_found
	density = data.data
	density_found = True

def volume_callback(data):
	global volume
	global volume_found
	volume=data.volume
	volume_found = True
	
def calculate_weight():
	if volume_found and density_found:
		weight=volume * density
		pub.publish(weight)

rospy.init_node("weight_calc")
rospy.Subscriber("/density", Float64, density_callback)
rospy.Subscriber("/cylinder", Cylinder, volume_callback)
pub = rospy.Publisher("/weight", Float64, queue_size=10)

while not rospy.is_shutdown():
	calculate_weight()
	rospy.sleep(0.1)

