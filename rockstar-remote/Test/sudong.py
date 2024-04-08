#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Point, Twist

rospy.init_node('turtlebot_controller', anonymous=True)


def msg_callback(msg):
    cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    move_cmd = Twist()

    if command == 'w':
        # 전진
        move_cmd.linear.x = 0.04
        move_cmd.angular.z = 0.0
    elif command == 'a':
        # 좌회전
        move_cmd.linear.x = 0.0
        move_cmd.angular.z = 0.04
    elif command == 'd':
        # 우회전
        move_cmd.linear.x = 0.0
        move_cmd.angular.z = -0.04
    elif command == 'x':
        # 후진
        move_cmd.linear.x = -0.04
        move_cmd.angular.z = 0.0
    elif command == 's':
        # 정지
        move_cmd.linear.x = 0.0
        move_cmd.angular.z = 0.0

    cmd_vel_pub.publish(move_cmd)



if __name__ == '__main__':
    try:
        rospy.Subscriber('/direction', String, msg_callback, queue_size=1)

         # 노드가 종료될 때까지 실행
        rospy.spin()
    except rospy.ROSInterruptException:
        pass