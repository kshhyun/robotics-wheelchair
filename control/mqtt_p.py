import paho.mqtt.client as mqtt

# Client 생성
client = mqtt.Client()

# Client 연결
client.connect('223.195.194.41', 1883, 60)
#client.connect('broker.hivemq.com', 1883)
# 172.18.77.109
# 223.195.194.41
# 192.168.100.88
# Topic 설정
topic = "rockstar"

# 메시지 생성
message = "w"
message1 = "a"
message2 = "s" 
message3 = "d"
message4 = "x"

# publish 확인
def on_publish(client, userdata, mid):
    print("Publish success")

# publish callback 함수 등록
client.on_publish = on_publish

# QoS 0로 publish
client.publish(topic, message, qos=0)
client.publish(topic, message1, qos=0)
client.publish(topic, message2, qos=0)
client.publish(topic, message3, qos=0)
client.publish(topic, message4, qos=0)
# Client 종료
client.disconnect()