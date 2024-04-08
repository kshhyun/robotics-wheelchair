#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy #파이썬에서 ros에 접근하기 위함
from geometry_msgs.msg import Point, Twist #cmd_vel 토픽이 geometry 메시지의 Twist 형 지정

speed = Twist() #임포트한 Twist를 speed 변수에 저장
rospy.init_node("stop") #test_cmd_vel 이름으로 노드를 생성해 초기화
rate = rospy.Rate(100) #코드의 주기 지정
pub = rospy.Publisher("/cmd_vel", Twist, queue_size=1) #cmd_vel 토픽을 사용할 것, (cmd_vel 토픽은 Twist형) 타입을 지정해 pub에 저장

#문자열 전달 -> 터틀봇-리모트PC 연결에서 활용할 예정
destination = {
    'x':'stop'
    }

#목적지 이동 좌표 전달
def destination_pub(destination):
    stop(destination['x']) #매개변수로 받은 desination의값을 stop 함수에 전달함

#정지 함수
def stop(x):
    if x == 'stop':
        speed.linear.x=0.0
        speed.linear.y=0.0
        speed.linear.z=0.0
        speed.angular.x=0.0
        speed.angular.y=0.0
        speed.angular.z=0.0
        rospy.signal_shutdown("정지 후 노드 종료")  # 노드 종료 신호 발생
    else:
        print("stop이 아님")

while not rospy.is_shutdown(): #계속 진행
		pub.publish(speed)
		rate.sleep() 
