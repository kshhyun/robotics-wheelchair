#!/usr/bin/env python
# -*- coding: utf-8 -*-

#selDestination.py의 /rockstar, /start publisher를 sub 하고 목적지로 이동하는 test

import rospy
import tf
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from std_msgs.msg import String
from geometry_msgs.msg import Pose

# 노드 초기화
rospy.init_node('control_test', anonymous=False)
ac = actionlib.SimpleActionClient("move_base", MoveBaseAction)
goal = MoveBaseGoal()
goalpos = ''
position='' #현재 로봇 위치 
tf_listener = tf.TransformListener()

#현재 로봇 위치 확인 함수
def check_robot_position():
    print("check_robot_position 함수 호출 시작")
    global position
    try:
        (trans, rot) = tf_listener.lookupTransform('/map', '/base_footprint', rospy.Time(0)) #현재 시간에 대한 로봇 위치 가져옴
       
        # x,y 좌표 확인
        x = trans[0]
        y = trans[1]

        #x,y 좌표에 따른 position 변수에 문자열 저장
        if (-0.0 <= x <=0.1) and (-0.1<= y <= 0.1):
            position = 'desk' #접수처
            print(position)
        elif x==1.385 and y==-1.664:
            position = 'urology' #비뇨기과
            print(position)
    except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
        rospy.logerr("예외발생")
        

#목적지 설정 버튼 클릭 시 실행
def msg_callback(msg):
    print("msg_callback 호출")

    global goal
    global goalpos
    check_robot_position()

    #접수처->비뇨기과 or 접수처 -> CT촬영실
    if (position=='접수처' and msg.data=='1') or (position=='접수처' and msg.data=='2'):

         goalpos = msg.data
         
         #pt1 좌표 설정
         goal.target_pose.header.frame_id = "map"
         goal.target_pose.header.stamp = rospy.Time.now()

         goal.target_pose.pose.orientation.x = 0
         goal.target_pose.pose.orientation.y = 0
         goal.target_pose.pose.orientation.z = 0.0
         goal.target_pose.pose.orientation.w = 1.0

         goal.target_pose.pose.position.x = 0.536
         goal.target_pose.pose.position.y = 0.0
         goal.target_pose.pose.position.z = 0
         print(goal, "goal 값 설정 완료")
            

#주행시작 버튼 클릭 시 실행 
def goal_move(msg):
    print("goal_move 함수 호출 시작")
    global goal
    global goalpos

    #pt1으로 이동
    print(goal, "goal 목적지로 이동 시작")
    ac.send_goal(goal)
    ac.wait_for_result()
    
    if goalpos==1 or goalpos==2:
         
         #goal=pt2 설정
         goal.target_pose.header.frame_id = "map"
         goal.target_pose.header.stamp = rospy.Time.now()

         goal.target_pose.pose.orientation.x = 0
         goal.target_pose.pose.orientation.y = 0
         goal.target_pose.pose.orientation.z = 0.0
         goal.target_pose.pose.orientation.w = 1.0

         goal.target_pose.pose.position.x = 0.536
         goal.target_pose.pose.position.y = -1.151
         goal.target_pose.pose.position.z = 0
         print(goal, "goal 값 설정 완료")
        
        #goal=pt2 이동
         ac.send_goal(goal)
         ac.wait_for_result()

         #goal=pt3 설정
         goal.target_pose.header.frame_id = "map"
         goal.target_pose.header.stamp = rospy.Time.now()

         goal.target_pose.pose.orientation.x = 0
         goal.target_pose.pose.orientation.y = 0
         goal.target_pose.pose.orientation.z = 0.0
         goal.target_pose.pose.orientation.w = 1.0

         goal.target_pose.pose.position.x = 1.385
         goal.target_pose.pose.position.y = -1.151
         goal.target_pose.pose.position.z = 0
         print(goal, "goal 값 설정 완료")
        
        #goal=pt3 이동
         ac.send_goal(goal)
         ac.wait_for_result()

         if goalpos==1:
             #goal=비뇨기과 설정
            goal.target_pose.header.frame_id = "map"
            goal.target_pose.header.stamp = rospy.Time.now()

            goal.target_pose.pose.orientation.x = 0
            goal.target_pose.pose.orientation.y = 0
            goal.target_pose.pose.orientation.z = 0.0
            goal.target_pose.pose.orientation.w = 1.0

            goal.target_pose.pose.position.x = 1.385
            goal.target_pose.pose.position.y = -1.664
            goal.target_pose.pose.position.z = 0
            print(goal, "goal 값 설정 완료")

            #goal=비뇨기과 이동
            ac.send_goal(goal)
            ac.wait_for_result()

         elif goalpos==2:
             #goal=CT촬영실 설정
             goal.target_pose.header.frame_id = "map"
             goal.target_pose.header.stamp = rospy.Time.now()

             goal.target_pose.pose.orientation.x = 0
             goal.target_pose.pose.orientation.y = 0
             goal.target_pose.pose.orientation.z = 0.0
             goal.target_pose.pose.orientation.w = 1.0

             goal.target_pose.pose.position.x = 1.385
             goal.target_pose.pose.position.y = -0.509
             goal.target_pose.pose.position.z = 0
             print(goal, "goal 값 설정 완료")

             #goal=CT촬영실 이동
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
