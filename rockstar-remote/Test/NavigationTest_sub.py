#!/usr/bin/env python
# -*- coding: utf-8 -*-

#테스트 성공
#publisher_node.py 에서 A 토픽을 받아 목적지로 이동

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from std_msgs.msg import String
from geometry_msgs.msg import Pose

# 노드 초기화
rospy.init_node('navigation_control', anonymous=False)
ac = actionlib.SimpleActionClient("move_base", MoveBaseAction)

# 목적지 이동 함수
def move_to(x, y, z, w):
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()

    goal.target_pose.pose.orientation.x = 0
    goal.target_pose.pose.orientation.y = 0
    goal.target_pose.pose.orientation.z = z
    goal.target_pose.pose.orientation.w = w

    goal.target_pose.pose.position.x = x
    goal.target_pose.pose.position.y = y
    goal.target_pose.pose.position.z = 0

    ac.send_goal(goal)
    ac.wait_for_result()

# 'test' 토픽을 구독하고 메시지를 받았을 때 이동 명령 실행
def msg_callback(msg):
    if msg.data == 'test':
        rospy.loginfo("Received 'A' from the topic.")
        destination = {
            'x': 1.4,
            'y': -0.5,
            'z': 0.0,
            'w': 1.0
        }
        move_to(destination['x'], destination['y'], destination['z'], destination['w'])

if __name__ == '__main__':
    try:
        # MoveBaseAction 서버가 준비될 때까지 대기
        ac.wait_for_server(rospy.Duration(5))

        # '/test' 토픽에서 메시지를 구독하고, 메시지가 수신되면 msg_callback 함수 호출
        rospy.Subscriber('/test', String, msg_callback, queue_size=1)

        # 노드가 종료될 때까지 실행
        rospy.spin()

    except rospy.ROSInterruptException:
        pass
