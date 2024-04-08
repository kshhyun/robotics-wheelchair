#!/usr/bin/env python
# -*- coding: utf-8 -*-

#테스트 성공
#터틀봇에서 A 문자열 토픽 발행 테스트 파일

import rospy
from std_msgs.msg import String
import time

# 노드 초기화
rospy.init_node('test_publisher', anonymous=True)

 # 'test' 토픽으로 메시지를 발행할 Publisher 생성
pub = rospy.Publisher('test', String, queue_size=1)
rate = rospy.Rate(1) 
msg = String()


if __name__ == '__main__':
  msg = 'test'
  
  while not rospy.is_shutdown():
    pub.publish(msg)
    print(msg+"를 보내고 있습니다") #publisher 발행 확인 메시지 출력
    rate.sleep()