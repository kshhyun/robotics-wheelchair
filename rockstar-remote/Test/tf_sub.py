#!/usr/bin/env python
# -*- coding: utf-8 -*-

#접수처부분 테스트 성공
#selDestination.py의 /rockstar, /start publisher를 sub 하고 이동하는 test

import rospy
import os
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from std_msgs.msg import String
from geometry_msgs.msg import Pose

# 노드 초기화
rospy.init_node('control_test', anonymous=False)
ac = actionlib.SimpleActionClient("move_base", MoveBaseAction)
goal = MoveBaseGoal()
xpoint=''
ypoint=''


#현재 로봇 위치 확인 함수
def check_robot_position():
    global xpoint
    global ypoint
    print("로봇 위치 확인 함수 실행")

    # 터미널 명령 실행
    result = os.system("rosrun tf tf_echo map base_footprint")

    # 출력에서 Translation 값을 파싱
    translation_str = result.decode().split("\n")[1]  # Translation 줄을 선택
    translation_str = translation_str.split(":")[1].strip()  # ":" 뒤의 값만 선택하고 공백 제거
    translation = [float(val) for val in translation_str[1:-1].split(",")]  # "[0.1, -1.0, 0.0]" 형태를 파싱하여 리스트로 변환

    xpoint=str(translation[0])
    ypoint=str(translation[1])



#목적지 설정버튼을 눌렀을 때 -> 목적지 좌표 전달 함수
def msg_callback(msg):
    print("msg_callback 함수 호출됨")
    global xpoint
    global ypoint

    check_robot_position()

    # 1 데이터를 받았을때 비뇨기과 좌표 전달
    if msg.data == '1' and (-0.2 <= xpoint <=0.3) and (-0.1<= ypoint <= 1.0) :
        #print("토픽 문자열 1 수신 완료")
        #print(msg)
        #rospy.loginfo("Received 'A' from the topic.")
        destination = {
            'x': 0.536,
            'y': -1.0,
            'z': 0.0,
            'w': 1.0
        }
        move_to(destination['x'], destination['y'], destination['z'], destination['w'])
        #print("move_to 함수 호출 완료")
    
    # 2 데이터를 받았을때 화장실 좌표 전달
    elif msg.data == '2' and (0.2<= xpoint <= 1.2) and (-3.0<= ypoint <= 0.0):
        #rospy.loginfo("Received 'B' from the 'btest' topic.")
        destination = {
            'x': 0.536,
            'y': -1.151,
            'z': 0.0,
            'w': 1.0
        }
        move_to(destination['x'], destination['y'], destination['z'], destination['w'])

    # 3 데이터를 받았을 때 탈의실 좌표 전달
    elif msg.data == '3':
         #rospy.loginfo("Received 'one' from the 'bonetest' topic.")
         destination = {
            'x': 0.3,
            'y': -0.7,
            'z': 0.0,
            'w': 1.0
        }
         move_to(destination['x'], destination['y'], destination['z'], destination['w'])

    # 4 데이터를 받았을 때 CT 촬영실 좌표 전달
    elif msg.data == '4':
         #rospy.loginfo("Received 'one' from the 'bonetest' topic.")
         destination = {
            'x': 0.0,
            'y': -2.0,
            'z': 0.0,
            'w': 1.0
        }
         move_to(destination['x'], destination['y'], destination['z'], destination['w'])



# 목적지 goal 지정함수
def move_to(x, y, z, w):
    global goal
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()

    goal.target_pose.pose.orientation.x = 0
    goal.target_pose.pose.orientation.y = 0
    goal.target_pose.pose.orientation.z = z
    goal.target_pose.pose.orientation.w = w

    goal.target_pose.pose.position.x = x
    goal.target_pose.pose.position.y = y
    goal.target_pose.pose.position.z = 0
    #print(goal, "goal 값 설정 완료")



#주행 시작 함수
def goal_move(msg):
    #print("start 문자열 수신 완료")
    global goal
    if msg.data == 'start':
        #print(goal, "goal 목적지로 이동 시작")
        ac.send_goal(goal)
        ac.wait_for_result()



if __name__ == '__main__':
    try:
        # MoveBaseAction 서버가 준비될 때까지 대기
        ac.wait_for_server(rospy.Duration(5))

        # 목적지 설정 시 토픽 발송 노드 구독
        rospy.Subscriber('/rockstar', String, msg_callback, queue_size=1)

        # 주행 시작 시 토픽 발송 노드 구독
        rospy.Subscriber('/start', String, goal_move, queue_size=1)


        # 노드가 종료될 때까지 실행
        rospy.spin()

    except rospy.ROSInterruptException:
        pass
