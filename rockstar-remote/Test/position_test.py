#!/usr/bin/env python
# -*- coding: utf-8 -*-

#현재위치 파악 테스트 -> 테스트 완료 

import rospy
import tf
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from std_msgs.msg import String
from geometry_msgs.msg import Pose

#노드 초기화
rospy.init_node('postion_test', anonymous=False)

#변수 초기화
position = '' #현재 로봇 위치

#현재위치 관련 변수 설정
tf_listener = tf.TransformListener() 
tf_blistener = tf.TransformListener(tf_listener) 


#목적지 설정 버튼 클릭 시 실행되는 함수
#현재 로봇 위치 파악 함수
def msg_callback(msg):
    print("check_robot_position 함수 호출 시작")
    global position 

    try:
        (trans, rot) = tf_listener.lookupTransform('/map', '/base_footprint', rospy.Time(0)) #현재 시간에 대한 로봇 위치 가져옴
       
        # x,y 좌표 확인
        x = trans[0]
        y = trans[1]

        #x,y 좌표에 따른 position 변수에 문자열 저장
        if (-1<= x <=0.34) and (-0.811<= y <= 0.034):
            position = 'desk' #접수처
            print("현재위치:", position)

        elif (0.34<= x <=0.6496) and (-0.811<= y <= 0.034):
            position = 'pt1' 
            print("현재위치:", position)
        
        elif (0.34 <= x <= 0.6496) and (-1.707 <= y <= -0.811):
            position = 'pt2' 
            print("현재위치:", position)
	
        elif (0.649 <= x <= 1.007) and (-1.707<= y <= -0.811):
            position = 'pt3'
            print("현재위치:", position)
        elif (1.007 <= x <= 5 ) and (-1.487 <= y <= -0.731):
            position = 'pt4'
            print("현재위치:", position)
        elif (0.6494 <= x <= 5 ) and (-0.730 <= y <= -0.271):
            position = 'CT'
            print("현재위치:", position)
        elif (0.6494 <= x <= 5 ) and (-0.270 <= y <= 5):
            position = 'pt5'
            print("현재위치:", position)
        elif (0.34 <= x <= 0.6493 ) and (-0.034 <= y <= 5):
            position = 'pt6'
            print("현재위치:", position)
        
    except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
        rospy.logerr("예외발생")

if __name__ == '__main__':
    try:
        # 목적지 설정 시 토픽 발송 노드
        rospy.Subscriber('/rockstar', String, msg_callback, queue_size=1)

        # 노드가 종료될 때까지 실행
        rospy.spin()

    except rospy.ROSInterruptException:
        pass
