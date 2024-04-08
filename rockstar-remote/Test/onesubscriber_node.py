#!/usr/bin/env python
# -*- coding: utf-8 -*-

#onepublisher_node 수신 확인 테스트 파일

import rospy
from std_msgs.msg import String

def msg_callback(msg):
  print(msg)
  
if __name__ == '__main__':
  rospy.init_node('one_subscriber')
  sub = rospy.Subscriber('/onetest', String, msg_callback, queue_size=1)
  
  rospy.spin()
  
