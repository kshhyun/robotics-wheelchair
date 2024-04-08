import rospy
from std_msgs.msg import String

# 노드 초기화
rospy.init_node('manualDriving_publisher', anonymous=True)

# 'direction' 토픽으로 메시지를 발행할 Publisher 생성
pub = rospy.Publisher('direction', String, queue_size=1)
rate = rospy.Rate(1)
msg = String()


def move_straight(self):
    # publishing
    global msg
    msg = 'w'
    pub.publish(msg)


def turn_left(self):
    # publishing
    global msg
    msg = 'a'
    pub.publish(msg)


def move_back(self):
    # publishing
    global msg
    msg = 'x'
    pub.publish(msg)


def turn_right(self):
    # publishing
    global msg
    msg = 'd'
    pub.publish(msg)


def stop_run(self):
    # publishing
    global msg
    msg = 's'
    pub.publish(msg)
