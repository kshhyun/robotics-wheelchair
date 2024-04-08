import time
import pyttsx3
import selDestination_ui


def assign_des(btn, btn_list):
    print(btn.text())
    global des, tts_des
    
    # 모든 버튼의 styleSheet를 초기화하는 코드 필요
    for other_btn_name in btn_list:
        other_btn = getattr(selDestination_ui.Ui_selDestination, other_btn_name)
        other_btn.setStyleSheet("""
                background-color: #cfe3ac;
                text-align: left;
                padding: 5px;
                padding-left: 20px;
                border: none;
            """)
    
    # 클릭한 버튼의 배경색상 변경
    btn.setStyleSheet("""
                        background-color: #a1c464;
                        text-align: left;
                        padding: 5px;
                        padding-left: 20px;
                        border: none;
    """)
    
#
#     # 목적지별 좌표를 저장할 publisher 전송
#     if btn.text() == "CT촬영실":
#         des = '2'
#         pub.publish(des)
#     elif btn.text() == "응급의료센터":
#         des = '1'
#         pub.publish(des)
#     elif btn.text() == "이비인후과":
#         des = '3'
#         pub.publish(des)
#     elif btn.text() == "접수처":
#         des = '0'
#         pub.publish(des)
#     elif btn.text() == "치과":
#         des = '4'
#         pub.publish(des)
#     elif btn.text() == "화장실":
#         des = '5'
#         pub.publish(des)
#     print(des)
#     tts_des = btn.text()
#
#
# def start_driving(btn):
#     global des, tts_des
#     msg = String()
#
#     if btn.text() == "주행시작":
#         # navigation 시작 토픽 생성 및 전송
#         pub = rospy.Publisher('start', String, queue_size=1)
#         msg.data = 'start'
#         pub.publish(msg)
#         # 탭 비활성화
#         # selDestination_ui.tabs.setDisabled(True)
#         # tts: 주행시작 알림
#         if des.data == '0':
#             tts_des='접수처'
#         elif des.data == '1':
#             tts_des='응급의료센터'
#         elif des == '2':
#             tts_des='CT촬영실'
#         elif des.data == '3':
#             tts_des='이비인후과'
#         elif des.data == '4':
#             tts_des='치과'
#         elif des.data == '5':
#             tts_des='화장실'
#         text_to_speech("목적지를 " + tts_des + "로 설정합니다.")
#         print(tts_des)
#         # 클릭 시 버튼 텍스트 전환
#         #btn.setText("정지")
#
#     elif btn.text() == "정지":
#         msg.data = 'end'
#         text_to_speech("목적지에 도착했습니다.")
#         # 정지 버튼 눌렸을 때 subscribe
#     else:
#         btn.setText("주행시작")
#

# tts
def text_to_speech(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)
    engine.say(text)
    engine.runAndWait()
