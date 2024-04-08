#!/usr/bin/env python

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from geometry_msgs.msg import Pose
from std_msgs.msg import String

# 노드 초기화
rospy.init_node('map_navigation', anonymous=False)
ac = actionlib.SimpleActionClient("move_base", MoveBaseAction)

def msg_callback(msg):
  # 목적지 좌표를 딕셔너리에 저장
  if  msg=='A':
        destination = {
        'x': 1.4,
        'y': -0.5,
        'z': 0.0,
        'w': 1.0
        }
        move_to(destination['x'], destination['y'], destination['z'], destination['w'])

  

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



if __name__ == "__main__":
    try:
        ac.wait_for_server(rospy.Duration(5))
        rospy.init_node('hello_subscriber')
        sub = rospy.Subscriber('/test', String, msg_callback, queue_size=1)
        rospy.spin()
    except rospy.ROSInterruptException:
        pass




  
 