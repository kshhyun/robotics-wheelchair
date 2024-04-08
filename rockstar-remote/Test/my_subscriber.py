#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo("Received: %s", data.data)

def listener():
    rospy.init_node('my_subscriber', anonymous=True)
    rospy.Subscriber('my_topic', String, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()