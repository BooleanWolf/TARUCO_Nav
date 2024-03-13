#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

ROTATING_SPEED = 200


class Tnav:
    def __init__(self) -> None:
        rospy.init_node("TNAV_HQ", anonymous=True)
        self.pub = rospy.Publisher('/cmd_vel',Twist,queue_size=10)
    
    def finding(self):
        data = Twist()
        data.angular.z = ROTATING_SPEED
        self.pub.publish(data) 
    
    
        
    

