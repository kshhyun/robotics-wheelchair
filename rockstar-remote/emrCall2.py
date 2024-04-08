import rospy
import pyttsx3
from PyQt5.QtCore import QTimer
import paho.mqtt.client as mqtt

import manualDriving

# 노드 초기화
# rospy.init_node('manualDriving_publisher', anonymous=True)

def emr_tts():
    # tts: 위급상황 알림
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)
    engine.say("위급상황입니다. 위급상황입니다.")
    engine.runAndWait()

    # 주행 정지
    pub = manualDriving.Pub()
    pub.stop_run()

def emr_mqtt():
    try:
        # Client 생성
        client = mqtt.Client()

        # Client 연결
        client.connect('172.18.77.109', 1883, 60)
        # client.connect('broker.hivemq.com', 1883)
        # 192.168.100.88
        # Topic 설정
        topic = "Emergency"

        # 메시지 생성
        message = "r"

        # publish 확인
        def on_publish(client, userdata, mid):
            print("Publish success")

        # publish callback 함수 등록
        client.on_publish = on_publish

        # QoS 0로 publish
        client.publish(topic, message, qos=0)
        
        # TTS 및 주행 정지 함수 호출
        emr_tts()

        # Client 종료
        client.disconnect()

    except Exception as e:
        print(e)

# QTimer를 이용한 소리 지연
def delayed_sound():
    # 1000 밀리초 (1초) 후에 delayed_sound 함수 호출
    QTimer.singleShot(500, emr_mqtt)
