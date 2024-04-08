#!/usr/bin/env python

import paho.mqtt.client as mqtt
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import String

rospy.init_node('turtlebot_controller2', anonymous=True)

cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
move_cmd = Twist()

# Broker 주소와 포트 설정
broker_address = "223.195.194.41"
broker_port = 1883

# Client 생성
client = mqtt.Client()

# Client 연결
client.connect(broker_address, broker_port)
print("연결완료")

# Topic 설정
topic = "rockstar"

# 전역 변수로 현재 메시지를 저장
current_message = ''

# Callback 함수 설정
def on_message(client, userdata, message):
    global current_message
    print(message.payload)
    current_message = message.payload

def control_robot():
    rate = rospy.Rate(10)  # 10Hz로 루프 실행

    # 메시지 수신 대기
    while not rospy.is_shutdown():
        
        if current_message == b'w':
            # 전진
            move_cmd.linear.x = 0.09
            move_cmd.angular.z = 0.0
        elif current_message == b'a':
            # 좌회전
            move_cmd.linear.x = 0.0
            move_cmd.angular.z = -0.09
        elif current_message == b'd':
            # 우회전
            move_cmd.linear.x = 0.0
            move_cmd.angular.z = 0.09
        elif current_message == b'x':
            # 좌회전
            move_cmd.linear.x = -0.09
            move_cmd.angular.z = 0.00
        elif current_message == b's':
            # 정지
            move_cmd.linear.x = 0.0
            move_cmd.angular.z = 0.0

        cmd_vel_pub.publish(move_cmd)
        rate.sleep()

if __name__ == '__main__':
    try:
        # Callback 함수 등록
        client.on_message = on_message

        # Subscribe
        client.subscribe(topic)
        
        client.loop_start()

        control_robot()

    except rospy.ROSInterruptException:
        pass