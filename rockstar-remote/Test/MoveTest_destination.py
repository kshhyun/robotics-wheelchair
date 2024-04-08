#!/usr/bin/env python

#테스트 성공
#파이썬 파일을 실행시키면 destination에 지정된 목적지(현재 접수처)로 이동하는 내용

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from geometry_msgs.msg import Pose

# 노드 초기화
rospy.init_node('map_navigation', anonymous=False)
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

# 목적지 좌표를 딕셔너리에 저장
destination = {
    'x': 1.4,
    'y': -0.5,
    'z': 0.0,
    'w': 1.0
}

if __name__ == "__main__":
    try:
        ac.wait_for_server(rospy.Duration(5))
        move_to(destination['x'], destination['y'], destination['z'], destination['w'])
    except rospy.ROSInterruptException:
        pass
