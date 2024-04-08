#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import String

rospy.init_node('turtlebot_controller', anonymous=True)

cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
move_cmd = Twist()
current_command = ''  # 현재 명령을 저장할 변수

def msg_callback(msg):
    global current_command

    if msg.data == 'w':
        # 전진 명령
        current_command = 'w'
    elif msg.data == 'a':
        # 좌회전 명령
        current_command = 'a'
    elif msg.data == 'd':
        # 우회전 명령
        current_command = 'd'
    elif msg.data == 'x':
        # 후진 명령
        current_command = 'x'
    elif msg.data == 's':
        # 정지 명령
        current_command = 's'

def control_robot():
    rate = rospy.Rate(10)  # 10Hz로 루프 실행

    while not rospy.is_shutdown():
        if current_command == 'w':
            # 전진
            move_cmd.linear.x = 0.09
            move_cmd.angular.z = 0.0
        elif current_command == 'a':
            # 좌회전
            move_cmd.linear.x = 0.0
            move_cmd.angular.z = -0.6
        elif current_command == 'd':
            # 우회전
            move_cmd.linear.x = 0.0
            move_cmd.angular.z = 0.6
        elif current_command == 'x':
            # 후진
            move_cmd.linear.x = -0.09
            move_cmd.angular.z = 0.0
        elif current_command == 's':
            # 정지
            move_cmd.linear.x = 0.0
            move_cmd.angular.z = 0.0

        cmd_vel_pub.publish(move_cmd)
        rate.sleep()

if __name__ == '__main__':
    try:
        rospy.Subscriber('/direction', String, msg_callback, queue_size=1)
        control_robot()
    except rospy.ROSInterruptException:
        pass
