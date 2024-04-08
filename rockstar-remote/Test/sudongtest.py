#!/usr/bin/env python
# -*- coding: utf-8 -*-

#로봇의 현재위치를 파악하고, 목적지까지 올바른 경로로 이동 test
import rospy
import tf
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from geometry_msgs.msg import Twist
from std_msgs.msg import String
from geometry_msgs.msg import Pose
from std_msgs.msg import Empty

# 노드 초기화
rospy.init_node('control_test', anonymous=False)
ac = actionlib.SimpleActionClient("move_base", MoveBaseAction)
#변수 초기화
goal = MoveBaseGoal()

#목적지 설정 함수 (함수 이름의 spot으로 goal 설정)
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

#목적지로 이동하는 함수
def robot_move():
    print("robot_move 함수 호출 시작")

    global goal
    global goalpos

    ac.send_goal(goal)
    ac.wait_for_result()
      
#목적지 설정(디스플레이) 시 실행되는 함수
#현재 위치 확인 후 초기 목적지 설정
# !!!현재 왼쪽부분 목적지만 도착한다고 가정
def msg_callback(msg):
    pt1()
    robot_move()

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