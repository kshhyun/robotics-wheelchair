#!/usr/bin/env python
# -*- coding: utf-8 -*-

#테스트 성공
#리모트PC에서 터틀봇 /test (A 문자열 발행) 토픽 수신 테스트 파일

import rospy
from std_msgs.msg import String

def msg_callback(msg):
  print(msg)
  
if __name__ == '__main__':
  rospy.init_node('test_subscriber')
  sub = rospy.Subscriber('/test', String, msg_callback, queue_size=1)
  
  rospy.spin()
  
