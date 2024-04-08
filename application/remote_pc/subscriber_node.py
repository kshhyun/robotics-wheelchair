#! /usr/bin/env python
import rospy
from std_msgs.msg import String
import os


def msg_callback(msg):
    cmd = "python3 ~/app/manualDriving_to_openCR.py " + str(msg.data)
    os.system(cmd)


rospy.init_node('manualDriving_subscriber', anonymous=True)
rate = rospy.Rate(1)

if __name__ == '__main__':
    while not rospy.is_shutdown():
        sub = rospy.Subscriber('/direction', String, msg_callback, queue_size=1)
        rate.sleep()
    
