import paho.mqtt.client as mqtt
### 관제 수동조작 publisher(최종) ###

# Client 생성
client = mqtt.Client()

# Client 연결
client.connect('223.195.194.41', 1883, 60)

# Topic 설정
topic = "rockstar"

# 메시지 생성
message = "w" #전진
message1 = "a" #좌회전
message2 = "s" #정지
message3 = "d" #우회전
message4 = "x" #후진

# publish 확인
def on_publish(client, userdata, mid):
    print("Publish success")

# publish callback 함수 등록
client.on_publish = on_publish

# QoS 0로 publish !!QOS 레벨은 변경 가능성 있음
client.publish(topic, message, qos=2)
client.publish(topic, message1, qos=2)
client.publish(topic, message2, qos=2)
client.publish(topic, message3, qos=2)
client.publish(topic, message4, qos=2)

# Client 종료
client.disconnect()