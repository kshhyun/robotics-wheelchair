#!/usr/bin/env python
# -*- coding: utf-8 -*-

#문자열을 한번만 보내고 종료 

import rospy
from std_msgs.msg import String

# 노드 초기화
rospy.init_node('One_publisher', anonymous=True)

# 'onetest' 토픽으로 메시지를 발행할 Publisher 생성
pub = rospy.Publisher('onetest', String, queue_size=1)

if __name__ == '__main__':
     msg = 'one'
     pub.publish(msg)  # 'A' 문자열 발행
     print(msg+"전달 함")
     rospy.sleep(1)  # 1초 동안 대기 후 종료
