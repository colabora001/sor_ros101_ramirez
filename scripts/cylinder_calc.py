#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float64
from ros_tutorial.msg import Cylinder

from math import pi

radius=0
radius_squared = 0
height = 0

radius_found = false
radius_squared_found = false
height_found = false

def radius_callback(data):
	global radius
	global radius_found
	radius = data.data
	radius_found = true
def radius_squared_callback(data):
	global radius_squared
	global radius_squared_found
	radius_squared = data.data
	radius_squared_found = true
def height_callback(data):
	global height
	global height_found
	height = data.data
	height_found = true

def calculate():
	if radius_found and radius_squared_found and height_found:
		msg = Cylinder()
		msg.volume = pi * radius_Square * height
		msg.surface_area = 2 * pi * (radius * height + radius_squared)
		pub.publish(msg)

rospy.ini_node("cylinder_calc")
rospy.Subscriber("/radius", Float64, radius_callback)
rospy.Subscriber("/radius_squared", Float64, radius_squared_callback)
rospy.Subscriber("/height", Float64, height_callback)
pub = rospy.Publisher("/cylinder", Cylinder, queue_size=10)


while not rospy.is_shutdown():
	calculate()
	rospy.sleep(0.1)
	
