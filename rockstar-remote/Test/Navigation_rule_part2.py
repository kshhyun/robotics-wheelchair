#!/usr/bin/env python
# -*- coding: utf-8 -*-

#로봇의 현재위치를 파악하고, 목적지까지 올바른 경로로 이동 test
#맵의 자율주행 부분(파트2)의 룰을 작성함

import rospy
import tf
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from std_msgs.msg import String
from geometry_msgs.msg import Pose

# 노드 초기화
rospy.init_node('control_test', anonymous=False)
ac = actionlib.SimpleActionClient("move_base", MoveBaseAction)


#변수 초기화
goal = MoveBaseGoal()
goalpos = '' #목적지 이름 문자열
position = '' #현재 로봇 위치

#현재위치 관련
tf_listener = tf.TransformListener() 
tf_blistener = tf.TransformListener(tf_listener) 

#다음 목적지 설정
def pt1():
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
         print("goal: pt1")
def pt2():
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
         print("goal: pt2")
def pt3():
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
         print("goal: pt3")    
def pt4():
     #goal=pt2 설정
         goal.target_pose.header.frame_id = "map"
         goal.target_pose.header.stamp = rospy.Time.now()

         goal.target_pose.pose.orientation.x = 0
         goal.target_pose.pose.orientation.y = 0
         goal.target_pose.pose.orientation.z = 0
         goal.target_pose.pose.orientation.w = 1.0

         goal.target_pose.pose.position.x = 1.2401
         goal.target_pose.pose.position.y = -1.208
         goal.target_pose.pose.position.z = 0
         print("goal: pt4")
def pt5():
     #goal=pt5 설정
         goal.target_pose.header.frame_id = "map"
         goal.target_pose.header.stamp = rospy.Time.now()

         goal.target_pose.pose.orientation.x = 0
         goal.target_pose.pose.orientation.y = 0
         goal.target_pose.pose.orientation.z = 0
         goal.target_pose.pose.orientation.w = 1.0

         goal.target_pose.pose.position.x = 1.279
         goal.target_pose.pose.position.y = 0.117
         goal.target_pose.pose.position.z = 0
         print("goal: pt5")
def pt6():
     #goal=pt6 설정
         goal.target_pose.header.frame_id = "map"
         goal.target_pose.header.stamp = rospy.Time.now()

         goal.target_pose.pose.orientation.x = 0
         goal.target_pose.pose.orientation.y = 0
         goal.target_pose.pose.orientation.z = 0
         goal.target_pose.pose.orientation.w = 1.0

         goal.target_pose.pose.position.x = 0.5417
         goal.target_pose.pose.position.y = 0.3574
         goal.target_pose.pose.position.z = 0
         print("goal: pt6")
def desk():
     #goal=desk 설정
         goal.target_pose.header.frame_id = "map"
         goal.target_pose.header.stamp = rospy.Time.now()

         goal.target_pose.pose.orientation.x = 0
         goal.target_pose.pose.orientation.y = 0
         goal.target_pose.pose.orientation.z = 0
         goal.target_pose.pose.orientation.w = 1.0

         goal.target_pose.pose.position.x = 0.0
         goal.target_pose.pose.position.y = 0.0
         goal.target_pose.pose.position.z = 0
         print("goal: desk")
def center():
      #goal=응급의료센터 설정
         goal.target_pose.header.frame_id = "map"
         goal.target_pose.header.stamp = rospy.Time.now()

         goal.target_pose.pose.orientation.x = 0
         goal.target_pose.pose.orientation.y = 0
         goal.target_pose.pose.orientation.z = 0
         goal.target_pose.pose.orientation.w = 1.0

         goal.target_pose.pose.position.x = 1.1809
         goal.target_pose.pose.position.y = -1.677
         goal.target_pose.pose.position.z = 0
         print("goal: center")
def CT():
      #goal=CT 설정
         goal.target_pose.header.frame_id = "map"
         goal.target_pose.header.stamp = rospy.Time.now()

         goal.target_pose.pose.orientation.x = 0
         goal.target_pose.pose.orientation.y = 0
         goal.target_pose.pose.orientation.z = 0
         goal.target_pose.pose.orientation.w = 1.0

         goal.target_pose.pose.position.x = 1.3202
         goal.target_pose.pose.position.y = -0.461
         goal.target_pose.pose.position.z = 0
         print("goal: CT")

#수동주행->자율주행 스팟
def Out_spot():
      #goal=Out 설정
         goal.target_pose.header.frame_id = "map"
         goal.target_pose.header.stamp = rospy.Time.now()

         goal.target_pose.pose.orientation.x = 0
         goal.target_pose.pose.orientation.y = 0
         goal.target_pose.pose.orientation.z = 0
         goal.target_pose.pose.orientation.w = 1.0

         goal.target_pose.pose.position.x = 0.1943
         goal.target_pose.pose.position.y = -1.1960
         goal.target_pose.pose.position.z = 0
         print("goal: Out")

#수동주행<-자율주행 스팟
def In_spot():
      #goal=In 설정
         goal.target_pose.header.frame_id = "map"
         goal.target_pose.header.stamp = rospy.Time.now()

         goal.target_pose.pose.orientation.x = 0
         goal.target_pose.pose.orientation.y = 0
         goal.target_pose.pose.orientation.z = 0
         goal.target_pose.pose.orientation.w = 1.0

         goal.target_pose.pose.position.x = 0.8685
         goal.target_pose.pose.position.y = -1.8902
         goal.target_pose.pose.position.z = 0
         print("goal: In")

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
        elif (0.6494 <= x <= 5 ) and (-0.730 <= y <= -0.271):
            position = 'CT' #CT촬영실
            print("현재위치:", position)
        elif (1.007 <= x <= 5 ) and (-2 <= y <= -1.4874): #y좌표 수정 필요
            position = 'center' #응급의료 센터
            print("현재위치:", position)

        #수동주행 파트
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
        elif (0.6494 <= x <= 5 ) and (-0.270 <= y <= 5):
            position = 'pt5'
            print("현재위치:", position)
        elif (0.34 <= x <= 0.6493 ) and (-0.034 <= y <= 5):
            position = 'pt6'
            print("현재위치:", position)

        #자율주행
        elif ( -5 <= x <= 0.1943 ) and ( -10 <= y <= 0.811 ):
            position = 'A'
            print("현재위치:", position)
        elif ( 0.1944 <= x <= 5 ) and ( -10 <= y <= -1.8902):
            position = 'B'
            print("현재위치:", position)

    except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
        rospy.logerr("예외발생")


 
#목적지 설정(디스플레이) 시 실행되는 함수
#현재 위치 확인 후 목적지 설정

# !!!현재 왼쪽부분 목적지만 도착한다고 가정
def msg_callback(msg):

    print("msg_callback 함수 실행")
    global position, goalpos, goal

    goalpos = msg.data #pub으로부터 전달받은 목적지를 문자열로 position  저장

    check_robot_position() #현재위치 파악 

    if position == 'A':
        if goalpos == '2': #goalpos == '2'는 CT
            In_spot() #out 스팟으로 goal 값 설정
            print('out spot값 설정 완료')
            goal_move(None)


    '''
    elif position =='center': #현재 위치가 응급의료센터면 CT, 접수처를 가기위해 pt3을 지나야함
        #goal=pt3 설정
         goal.target_pose.header.frame_id = "map"
         goal.target_pose.header.stamp = rospy.Time.now()

         goal.target_pose.pose.orientation.x = 0
         goal.target_pose.pose.orientation.y = 0
         goal.target_pose.pose.orientation.z = 0.0
         goal.target_pose.pose.orientation.w = 1.0

         goal.target_pose.pose.position.x = 0.8
         goal.target_pose.pose.position.y = -1.18
         goal.target_pose.pose.position.z = 0
         print(goal, "goal 값 설정 완료")

    elif position =='CT': #현재 위치가 CT촬영실이면, 어딜가든 pt4 -> pt5  해야함
        #goal=pt4 설정
         goal.target_pose.header.frame_id = "map"
         goal.target_pose.header.stamp = rospy.Time.now()

         goal.target_pose.pose.orientation.x = 0
         goal.target_pose.pose.orientation.y = 0
         goal.target_pose.pose.orientation.z = 0
         goal.target_pose.pose.orientation.w = 1

         goal.target_pose.pose.position.x = 1.236
         goal.target_pose.pose.position.y = -0.2
         goal.target_pose.pose.position.z = 0
         print(goal, "goal 값 설정 완료")
'''
        


#주행 시작 버튼 클릭 시 실행
#정해진 목적지로 이동 
def goal_move(msg):
    print("goal_move 함수 호출 시작")

    global goal
    global goalpos

    #msg_callback 에서 지정한 첫번째 point로 이동
    print("첫번째 포인트로 이동 시작")

    ac.send_goal(goal)
    ac.wait_for_result()
    '''
    #현재 위치가 접수처이면 어딜가든 무조건 pt1을 지남
    if position == 'desk':
         pt1()
        
        #goal=pt3 이동
         ac.send_goal(goal)
         ac.wait_for_result()

         if goalpos == '1': #목적지가 응급의료센터이면
             #goal=응급의료센터 설정
             goal.target_pose.header.frame_id = "map"
             goal.target_pose.header.stamp = rospy.Time.now()

             goal.target_pose.pose.orientation.x = 0
             goal.target_pose.pose.orientation.y = 0
             goal.target_pose.pose.orientation.z = 0.0
             goal.target_pose.pose.orientation.w = 1.0

             goal.target_pose.pose.position.x = 1.247
             goal.target_pose.pose.position.y = -1.666
             goal.target_pose.pose.position.z = 0
             print(" 응급의료센터 설정 완료")

         elif goalpos == '2':
             #goal=CT 촬영실 설정
            goal.target_pose.header.frame_id = "map"
            goal.target_pose.header.stamp = rospy.Time.now()

            goal.target_pose.pose.orientation.x = 0
            goal.target_pose.pose.orientation.y = 0
            goal.target_pose.pose.orientation.z = 0
            goal.target_pose.pose.orientation.w = 1

            goal.target_pose.pose.position.x = 1.236
            goal.target_pose.pose.position.y = -0.2
            goal.target_pose.pose.position.z = 0
            print(goal, "goal 값 설정 완료")

         #정해진 목적지로 이동
         ac.send_goal(goal)
         ac.wait_for_result()
        
    elif position == 'center' and (goalpos == '2' or goalpos == '0'): #ct촬영실 -> pt4 -> pt5
             #goal=CT 촬영실 설정
             goal.target_pose.header.frame_id = "map"
             goal.target_pose.header.stamp = rospy.Time.now()

             goal.target_pose.pose.orientation.x = 0
             goal.target_pose.pose.orientation.y = 0
             goal.target_pose.pose.orientation.z = 0
             goal.target_pose.pose.orientation.w = 1

             goal.target_pose.pose.position.x = 1.247
             goal.target_pose.pose.position.y = -0.4563
             goal.target_pose.pose.position.z = 0
             print(goal, "goal 값 설정 완료")

             #goal=CT촬영실 이동
             ac.send_goal(goal)
             ac.wait_for_result()

             if goalpos =='0':
                 #goal=pt4 설정
                goal.target_pose.header.frame_id = "map"
                goal.target_pose.header.stamp = rospy.Time.now()

                goal.target_pose.pose.orientation.x = 0
                goal.target_pose.pose.orientation.y = 0
                goal.target_pose.pose.orientation.z = 0
                goal.target_pose.pose.orientation.w = 1

                goal.target_pose.pose.position.x = 1.247
                goal.target_pose.pose.position.y = -0.2
                goal.target_pose.pose.position.z = 0
                print(goal, "goal 값 설정 완료")

                ac.send_goal(goal)
                ac.wait_for_result()

                 #goal=pt5 설정
                goal.target_pose.header.frame_id = "map"
                goal.target_pose.header.stamp = rospy.Time.now()

                goal.target_pose.pose.orientation.x = 0
                goal.target_pose.pose.orientation.y = 0
                goal.target_pose.pose.orientation.z = 0
                goal.target_pose.pose.orientation.w = 1

                goal.target_pose.pose.position.x = 0.07
                goal.target_pose.pose.position.y = -0.2
                goal.target_pose.pose.position.z = 0
                print(goal, "goal 값 설정 완료")

                ac.send_goal(goal)
                ac.wait_for_result()

                #goal=접수처 설정
                goal.target_pose.header.frame_id = "map"
                goal.target_pose.header.stamp = rospy.Time.now()

                goal.target_pose.pose.orientation.x = 0
                goal.target_pose.pose.orientation.y = 0
                goal.target_pose.pose.orientation.z = 0
                goal.target_pose.pose.orientation.w = 1

                goal.target_pose.pose.position.x = -0.021
                goal.target_pose.pose.position.y = -0.047
                goal.target_pose.pose.position.z = 0
                print(goal, "goal 값 설정 완료")

                ac.send_goal(goal)
                ac.wait_for_result()

    elif position == 'CT' and (goalpos == '0' or goalpos == '1'): #ct촬영실 -> pt4 -> pt5     
             #goal=pt5 설정
             goal.target_pose.header.frame_id = "map"
             goal.target_pose.header.stamp = rospy.Time.now()

             goal.target_pose.pose.orientation.x = 0
             goal.target_pose.pose.orientation.y = 0
             goal.target_pose.pose.orientation.z = 0
             goal.target_pose.pose.orientation.w = 1

             goal.target_pose.pose.position.x = 0.07
             goal.target_pose.pose.position.y = -0.2
             goal.target_pose.pose.position.z = 0
             print(goal, "goal 값 설정 완료")

             ac.send_goal(goal)
             ac.wait_for_result()
             
             if goalpos=='0':
                  #goal=접수처 설정
                goal.target_pose.header.frame_id = "map"
                goal.target_pose.header.stamp = rospy.Time.now()

                goal.target_pose.pose.orientation.x = 0
                goal.target_pose.pose.orientation.y = 0
                goal.target_pose.pose.orientation.z = 0
                goal.target_pose.pose.orientation.w = 1

                goal.target_pose.pose.position.x = 0.07
                goal.target_pose.pose.position.y = -0.2
                goal.target_pose.pose.position.z = 0
                print(goal, "goal 값 설정 완료")

                ac.send_goal(goal)
                ac.wait_for_result()
             elif goalpos=='1':
                  #goal=응급센터 설정
                goal.target_pose.header.frame_id = "map"
                goal.target_pose.header.stamp = rospy.Time.now()

                goal.target_pose.pose.orientation.x = 0
                goal.target_pose.pose.orientation.y = 0
                goal.target_pose.pose.orientation.z = 0.0
                goal.target_pose.pose.orientation.w = 1.0

                goal.target_pose.pose.position.x = 1.247
                goal.target_pose.pose.position.y = -1.666
                goal.target_pose.pose.position.z = 0
                print(goal, "goal 값 설정 완료")

                ac.send_goal(goal)
                ac.wait_for_result()
'''


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