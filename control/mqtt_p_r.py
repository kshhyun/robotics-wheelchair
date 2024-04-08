import paho.mqtt.client as mqtt

# Client 생성
client = mqtt.Client()

# Client 연결
client.connect('223.195.194.41', 1883)
#client.connect('broker.hivemq.com', 1883)

# Topic 설정
topic = "alarm"

# 메시지 생성
message = "start"
message1 = "stop"

# publish 확인
def on_publish(client, userdata, mid):
    print("Publish success")

# publish callback 함수 등록
client.on_publish = on_publish

# QoS 2로 publish
client.publish(topic, message, qos=0)
client.publish(topic, message1, qos=0)

# Client 종료
client.disconnect()