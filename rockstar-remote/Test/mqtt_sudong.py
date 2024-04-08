import paho.mqtt.client as mqtt
import rospy
from geometry_msgs.msg import Twist

rospy.init_node('mqtt_turtlebot_controller', anonymous=True)

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("rockstar")

def on_message(client, userdata, msg):
    message = msg.payload.decode("utf-8")
    print("Received message: " + message)
    cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    move_cmd = Twist()

    if message == 'w':
        # 전진
        move_cmd.linear.x = 0.04
        move_cmd.angular.z = 0.0
    elif message == 'a':
        # 좌회전
        move_cmd.linear.x = 0.0
        move_cmd.angular.z = 0.04
    elif message == 'd':
        # 우회전
        move_cmd.linear.x = 0.0
        move_cmd.angular.z = -0.04
    elif message == 'x':
        # 후진
        move_cmd.linear.x = -0.04
        move_cmd.angular.z = 0.0
    elif message == 's':
        # 정지
        move_cmd.linear.x = 0.0
        move_cmd.angular.z = 0.0

    cmd_vel_pub.publish(move_cmd)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect('192.168.100.88', 1883, 60)

# 노드가 종료될 때까지 실행
rospy.spin()
