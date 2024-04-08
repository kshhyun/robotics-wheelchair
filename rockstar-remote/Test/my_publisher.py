#!/usr/bin/env python
import rospy
from std_msgs.msg import String

rospy.init_node('my_publisher', anonymous=True)
pub = rospy.Publisher('my_topic', String, queue_size=10)
rate = rospy.Rate(1)  # 1 Hz

while not rospy.is_shutdown():
    message = "0911_test"
    rospy.loginfo(message)
    pub.publish(message)
    rate.sleep()