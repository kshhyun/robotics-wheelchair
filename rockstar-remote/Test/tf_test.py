#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import tf
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from std_msgs.msg import String
from geometry_msgs.msg import Pose

# 노드 초기화
rospy.init_node('ts_test', anonymous=False)
ac = actionlib.SimpleActionClient("move_base", MoveBaseAction)
goal = MoveBaseGoal()
goalpos = '' #목적지 이름 문자열
position = '' #현재 로봇 위치
tf_listener = tf.TransformListener() 
tf_blistener = tf.TransformListener(tf_listener) 

#현재 로봇 위치 파악 함수 -> 현재 좌표를 확인해 position 변수에 현재 위치명 저장
def check_robot_position():
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
        

 
#목적지 설정(디스플레이) 시 실행되는 함수
def msg_callback(msg):
    print("msg_callback 함수 실행")
    global position, goalpos, goal


    goalpos = msg.data #pub으로부터 전달받은 목적지 문자열 저장

    check_robot_position() #현재위치 파악 
    
    if position =='desk': #현재 위치가 접수처면 pt1으로 이동
         #goal=pt1 설정
         goal.target_pose.header.frame_id = "map"
         goal.target_pose.header.stamp = rospy.Time.now()

         goal.target_pose.pose.orientation.x = 0
         goal.target_pose.pose.orientation.y = 0
         goal.target_pose.pose.orientation.z = 0
         goal.target_pose.pose.orientation.w = 1.0

         goal.target_pose.pose.position.x = 0.485
         goal.target_pose.pose.position.y = -0.0709
         goal.target_pose.pose.position.z = 0
         print("pt1 goal 값 설정 완료")
    elif position =='pt1': #현재 위치가 pt1이면 pt2로 이동
         #goal=pt2 설정
         goal.target_pose.header.frame_id = "map"
         goal.target_pose.header.stamp = rospy.Time.now()

         goal.target_pose.pose.orientation.x = 0
         goal.target_pose.pose.orientation.y = 0
         goal.target_pose.pose.orientation.z = 0
         goal.target_pose.pose.orientation.w = 1.0

         goal.target_pose.pose.position.x = 0.485
         goal.target_pose.pose.position.y = -0.9833
         goal.target_pose.pose.position.z = 0
         print("pt2 goal 값 설정 완료")
    elif position =='pt2': #현재 위치가 pt2면 pt3으로 이동
         #goal=pt3 설정
         goal.target_pose.header.frame_id = "map"
         goal.target_pose.header.stamp = rospy.Time.now()

         goal.target_pose.pose.orientation.x = 0
         goal.target_pose.pose.orientation.y = 0
         goal.target_pose.pose.orientation.z = 0
         goal.target_pose.pose.orientation.w = 1.0

         goal.target_pose.pose.position.x = 0.884
         goal.target_pose.pose.position.y = -1.208
         goal.target_pose.pose.position.z = 0
         print("pt3 goal 값 설정 완료")
    elif position =='pt3': #현재 위치가 pt3면 pt4로 이동
         #goal=pt4
         goal.target_pose.header.frame_id = "map"
         goal.target_pose.header.stamp = rospy.Time.now()

         goal.target_pose.pose.orientation.x = 0
         goal.target_pose.pose.orientation.y = 0
         goal.target_pose.pose.orientation.z = 0
         goal.target_pose.pose.orientation.w = 1.0

         goal.target_pose.pose.position.x = 1.2401
         goal.target_pose.pose.position.y = -1.208
         goal.target_pose.pose.position.z = 0
         print("pt4 goal 값 설정 완료")
    
    
#주행시작 버튼 클릭 시 실행 
def goal_move(msg):
    print("goal_move 함수 호출 시작")
    global goal
    global goalpos

    #pt1으로 이동
    print("goal 목적지로 이동 시작")
    ac.send_goal(goal)
    ac.wait_for_result()
  


if __name__ == '__main__':
    try:
        # MoveBaseAction 서버가 준비될 때까지 대기
        ac.wait_for_server(rospy.Duration(5))

        # 목적지 설정 시 토픽 발송 노드
        rospy.Subscriber('/rockstar', String, msg_callback, queue_size=1)

        # 주행 시작 시 토픽 발송 노드 구독
        rospy.Subscriber('/start', String, goal_move, queue_size=1)


        # 노드가 종료될 때까지 실행
        rospy.spin()

    except rospy.ROSInterruptException:
        pass