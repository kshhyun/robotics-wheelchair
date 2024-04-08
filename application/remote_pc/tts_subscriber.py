import pyttsx3
import rospy
from std_msgs.msg import String


def text_to_speech(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)
    engine.say(text)
    engine.runAndWait()


def call_text_to_speech(msg):
    if msg.data == '0':
        des = '접수처'
        text = "목적지를 " + str(des) + "로 설정합니다."
    elif msg.data == '1':
        des = '응급의료센터'
        text = "목적지를 " + str(des) + "로 설정합니다."
    elif msg.data == '2':
        des = 'CT촬영실'
        text = "목적지를 " + str(des) + "로 설정합니다."
    elif msg.data == '3':
        des = '이비인후과'
        text = "목적지를 " + str(des) + "로 설정합니다."
    elif msg.data == 'end':
        text = "목적지에 도착했습니다."
    elif msg.data == 'emr':
        text = "위급상황입니다. 위급상황입니다."
    else:
        text = "목적지를 설정해주세요."
    print(text)
    text_to_speech(text)


rospy.init_node('tts_subscriber', anonymous=True)

if __name__ == '__main__':
    sub = rospy.Subscriber('/tts', String, call_text_to_speech, queue_size=1)
    rospy.spin()
