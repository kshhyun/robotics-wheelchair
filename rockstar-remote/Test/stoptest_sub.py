#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from geometry_msgs.msg import Twist

# 콜백 함수
def cmd_vel_callback(msg):
    # 받은 Twist 메시지를 출력하거나 다른 작업을 수행할 수 있습니다.
    print("Received Twist message: linear.x={}, angular.z={}".format(msg.linear.x, msg.angular.z))

if __name__ == '__main__':
    rospy.init_node("cmd_vel_subscriber")  # 노드 초기화

    # "/cmd_vel" 토픽을 구독하고 메시지를 받을 때마다 cmd_vel_callback 함수 호출
    rospy.Subscriber("/cmd_vel", Twist, cmd_vel_callback)

    # 노드를 종료할 때까지 대기
    rospy.spin()
