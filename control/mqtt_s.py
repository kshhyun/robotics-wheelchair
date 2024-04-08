import paho.mqtt.client as mqtt

# Broker 주소와 포트 설정
broker_address = "223.195.194.41"
broker_port = 1883

# Client 생성
client = mqtt.Client()

# Client 연결
client.connect(broker_address, broker_port)
# client.connect('broker.hivemq.com', 1883)
print("a")

# Topic 설정
topic = "present_position"

# Callback 함수 설정
def on_message(client, userdata, message):
    print(message.topic, message.payload)

# Callback 함수 등록
client.on_message = on_message

# Subscribe
client.subscribe(topic)

# 메시지 수신 대기
while True:
    client.loop()