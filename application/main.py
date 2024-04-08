import sys
from functools import partial

import emrCall
import manualDriving
import manualDriving_ui, mainPage_ui, emrCall_ui, selDestination_ui
import loading
import paho.mqtt.client as mqtt
from selDestination import assign_des, start_driving
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QTimer, QThread, pyqtSignal


class MqttThread(QThread):
    message_received = pyqtSignal(bytes)
    
    def run(self):
        try:
            # Broker 주소와 포트 설정
            broker_address = "172.18.77.109"
            broker_port = 1883
            
            # Client 생성
            client = mqtt.Client()
            
            # Client 연결
            client.connect(broker_address, broker_port)
            # client.connect('broker.hivemq.com', 1883)
            print("a")
            
            # Topic 설정
            topic = "alarm"
            
            # Callback 함수 설정
            def on_message(client, userdata, message):
                print(message.topic, message.payload)
                self.message_received.emit(message.payload)
            
            # Callback 함수 등록
            client.on_message = on_message
            
            # Subscribe
            client.subscribe(topic)
            
            # 메시지 수신 대기
            while True:
                client.loop()
        except Exception as e:
            print(e)

# 화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow):
    def __init__(self):
        super().__init__()

        # UI 페이지 전환을 위한 QStackedWidget 생성
        self.stacked_widget = QStackedWidget(self)
        self.stacked_widget.addWidget(mainPage_ui.Ui_MainPage())
        self.stacked_widget.addWidget(selDestination_ui.Ui_selDestination())
        self.stacked_widget.addWidget(manualDriving_ui.Ui_ManualDriving())
        self.stacked_widget.addWidget(emrCall_ui.Ui_EmrCall())
        # 현재 페이지 인덱스 기록
        self.current_page_index = 0
        # 초기 화면 설정
        self.setCentralWidget(self.stacked_widget)

        #############################################################
        # 버튼 변수 정의 -------------------------------------------------
        # mainPage_ui ------
        self.btn_selDes = mainPage_ui.Ui_MainPage.btn_selDes  # 메인페이지 - 목적지설정
        self.btn_manDriving = mainPage_ui.Ui_MainPage.btn_manDriving  # 메인페이지 - 수동주행
        self.btn_emrCall = mainPage_ui.Ui_MainPage.btn_emrCall  # 메인페이지 - 긴급호출
        # selDestination_ui ------
        self.btn_home_selDestination = selDestination_ui.Ui_selDestination.btn_home
        # 1층
        self.btn1_1f = selDestination_ui.Ui_selDestination.btn1_1f  # 목적지설정 - 1층-1
        self.btn2_1f = selDestination_ui.Ui_selDestination.btn2_1f  # 목적지설정 - 1층-2
        self.btn3_1f = selDestination_ui.Ui_selDestination.btn3_1f  # 목적지설정 - 1층-3
        self.btn4_1f = selDestination_ui.Ui_selDestination.btn4_1f  # 목적지설정 - 1층-4
        self.btn5_1f = selDestination_ui.Ui_selDestination.btn5_1f  # 목적지설정 - 1층-5
        self.btn6_1f = selDestination_ui.Ui_selDestination.btn6_1f  # 목적지설정 - 1층-6
        # # 2층
        # self.btn1_2f = selDestination_ui.Ui_selDestination.btn1_2f    # 목적지설정 - 1층-1
        # self.btn2_2f = selDestination_ui.Ui_selDestination.btn2_2f    # 목적지설정 - 1층-2
        # self.btn3_2f = selDestination_ui.Ui_selDestination.btn3_2f    # 목적지설정 - 1층-3
        # self.btn4_2f = selDestination_ui.Ui_selDestination.btn4_2f    # 목적지설정 - 1층-4
        # self.btn5_2f = selDestination_ui.Ui_selDestination.btn5_2f    # 목적지설정 - 1층-5
        # self.btn6_2f = selDestination_ui.Ui_selDestination.btn6_2f    # 목적지설정 - 1층-6
        # #3층
        # self.btn1_3f = selDestination_ui.Ui_selDestination.btn1_3f    # 목적지설정 - 1층-1
        # self.btn2_3f = selDestination_ui.Ui_selDestination.btn2_3f    # 목적지설정 - 1층-2
        # self.btn3_3f = selDestination_ui.Ui_selDestination.btn3_3f    # 목적지설정 - 1층-3
        # self.btn4_3f = selDestination_ui.Ui_selDestination.btn4_3f    # 목적지설정 - 1층-4
        # self.btn5_3f = selDestination_ui.Ui_selDestination.btn5_3f    # 목적지설정 - 1층-5
        # self.btn6_3f = selDestination_ui.Ui_selDestination.btn6_3f    # 목적지설정 - 1층-6
        # #4층
        # self.btn1_4f = selDestination_ui.Ui_selDestination.btn1_4f    # 목적지설정 - 1층-1
        # self.btn2_4f = selDestination_ui.Ui_selDestination.btn2_4f    # 목적지설정 - 1층-2
        # self.btn3_4f = selDestination_ui.Ui_selDestination.btn3_4f    # 목적지설정 - 1층-3
        # self.btn4_4f = selDestination_ui.Ui_selDestination.btn4_4f    # 목적지설정 - 1층-4
        # self.btn5_4f = selDestination_ui.Ui_selDestination.btn5_4f    # 목적지설정 - 1층-5
        # self.btn6_4f = selDestination_ui.Ui_selDestination.btn6_4f    # 목적지설정 - 1층-6
        # #5층
        # self.btn1_5f = selDestination_ui.Ui_selDestination.btn1_5f    # 목적지설정 - 1층-1
        # self.btn2_5f = selDestination_ui.Ui_selDestination.btn2_5f    # 목적지설정 - 1층-2
        # self.btn3_5f = selDestination_ui.Ui_selDestination.btn3_5f    # 목적지설정 - 1층-3
        # self.btn4_5f = selDestination_ui.Ui_selDestination.btn4_5f    # 목적지설정 - 1층-4
        # self.btn5_5f = selDestination_ui.Ui_selDestination.btn5_5f    # 목적지설정 - 1층-5
        # self.btn6_5f = selDestination_ui.Ui_selDestination.btn6_5f    # 목적지설정 - 1층-6
        # #6층
        # self.btn1_6f = selDestination_ui.Ui_selDestination.btn1_6f    # 목적지설정 - 1층-1
        # self.btn2_6f = selDestination_ui.Ui_selDestination.btn2_6f    # 목적지설정 - 1층-2
        # self.btn3_6f = selDestination_ui.Ui_selDestination.btn3_6f    # 목적지설정 - 1층-3
        # self.btn4_6f = selDestination_ui.Ui_selDestination.btn4_6f    # 목적지설정 - 1층-4
        # self.btn5_6f = selDestination_ui.Ui_selDestination.btn5_6f    # 목적지설정 - 1층-5
        # self.btn6_6f = selDestination_ui.Ui_selDestination.btn6_6f    # 목적지설정 - 1층-6
        self.btn_start = selDestination_ui.Ui_selDestination.btn_start
        self.btn_emrCall_selDestination = selDestination_ui.Ui_selDestination.btn_emrCall

        # 버튼 변수를 문자열 형태로 리스트에 추가
        self.btn_list = []
        for i in range(1, 7):
            var_name = f"btn{i}_1f"
            self.btn_list.append(var_name)
        # manualDriving_ui ------
        self.btn_home_manualDriving = manualDriving_ui.Ui_ManualDriving.btn_home  # 수동주행 - HOME
        self.btn_up = manualDriving_ui.Ui_ManualDriving.btn_up  # 수동주행 - 직진
        self.btn_left = manualDriving_ui.Ui_ManualDriving.btn_left  # 수동주행 - 좌회전
        self.btn_down = manualDriving_ui.Ui_ManualDriving.btn_down  # 수동주행 - 후진
        self.btn_right = manualDriving_ui.Ui_ManualDriving.btn_right  # 수동주행 - 우회전
        self.btn_stop = manualDriving_ui.Ui_ManualDriving.btn_stop
        self.btn_emrCall_manualDriving = manualDriving_ui.Ui_ManualDriving.btn_emrCall  # 수동주행 - 긴급호출
        # emrCall_ui ------
        self.btn_home_emrCall = emrCall_ui.Ui_EmrCall.btn_home

        # 버튼 이벤트 ------------------------------------------------------------
        # mainPage_ui ------
        self.btn_selDes.clicked.connect(self.show_selDestination)
        self.btn_manDriving.clicked.connect(self.show_manualDriving)
        self.btn_emrCall.clicked.connect(self.show_emrCall)
        # selDestination_ui ------
        self.btn_home_selDestination.clicked.connect(self.show_mainPage)
        self.btn1_1f.clicked.connect(partial(self.call_assign_des, btn=self.btn1_1f, btn_list=self.btn_list))
        self.btn2_1f.clicked.connect(partial(self.call_assign_des, btn=self.btn2_1f, btn_list=self.btn_list))
        self.btn3_1f.clicked.connect(partial(self.call_assign_des, btn=self.btn3_1f, btn_list=self.btn_list))
        self.btn4_1f.clicked.connect(partial(self.call_assign_des, btn=self.btn4_1f, btn_list=self.btn_list))
        self.btn5_1f.clicked.connect(partial(self.call_assign_des, btn=self.btn5_1f, btn_list=self.btn_list))
        self.btn6_1f.clicked.connect(partial(self.call_assign_des, btn=self.btn6_1f, btn_list=self.btn_list))
        self.btn_start.clicked.connect(lambda: self.call_start_driving(self.btn_start))
        self.btn_emrCall_selDestination.clicked.connect(self.show_emrCall)
        # manualDriving_ui ------
        # 수동주행 객체 생성
        sudong_pub = manualDriving.sudong_pub()
        self.btn_home_manualDriving.clicked.connect(self.show_mainPage)

        self.btn_up.clicked.connect(sudong_pub.move_straight)
        self.btn_left.clicked.connect(sudong_pub.turn_left)
        self.btn_down.clicked.connect(sudong_pub.move_back)
        self.btn_right.clicked.connect(sudong_pub.turn_right)
        self.btn_stop.clicked.connect(sudong_pub.stop_run)

        self.btn_emrCall_manualDriving.clicked.connect(self.show_emrCall)
        # emrCall_ui ------
        self.btn_home_emrCall.clicked.connect(self.show_mainPage)
    
        self.mqtt_subscriber()

    def show_mainPage(self):
        # selDestination 페이지로 전환
        print("HOME")
        # 인덱스 전환
        self.stacked_widget.setCurrentIndex(0)
        self.current_page_index = 0

    def show_selDestination(self):
        # selDestination 페이지로 전환
        print("목적지 설정")
        # 인덱스 전환
        self.stacked_widget.setCurrentIndex(1)
        self.current_page_index = 1

    def show_manualDriving(self):
        # manualDriving 페이지로 전환
        print("수동주행")
        # 인덱스 전환
        self.stacked_widget.setCurrentIndex(2)
        self.current_page_index = 2

    def show_emrCall(self):
        # emrCall 페이지로 전환
        print("긴급호출")
        # 인덱스 전환
        self.stacked_widget.setCurrentIndex(3)
        self.current_page_index = 3
        
        # tts & mqtt 호출
        emrCall.delayed_sound()
        manualDriving.stop_run()
        emrCall.emr_mqtt()

    def call_assign_des(self, btn, btn_list):
        print("call_assign_des")
        assign_des(btn, btn_list)

    def call_start_driving(self, btn):
        print("call_start_driving")
        start_driving(btn)
        
    #  test: 1 누르면 모달창 보이기
    # def keyPressEvent(self, event):
    #     if event.key() == Qt.Key_1:
    #         loading.show_loading_dialog(self)  # loading.py의 메서드를 호출합니다.
    
    
    # mqtt 관제 제어 시작/종료 수신
    def mqtt_subscriber(self):
        self.mqtt_thread = MqttThread()
        self.mqtt_thread.message_received.connect(self.handle_message)
        self.mqtt_thread.start()
    
    def handle_message(self, payload):
        if payload == b"start":  # byte로 비교
            self.show_loading_dialog()  # self를 사용하여 호출
            self.loading_flag = True
        elif payload == b"stop":  # byte로 비교
            if self.loading_flag:
                self.hide_loading_dialog()  # self를 사용하여 호출
                self.loading_flag = False
    
    def show_loading_dialog(self):
        global loading_dialog
        print("2")
        loading_dialog = loading.LoadingDialog(self)
        loading_dialog.setWindowModality(Qt.ApplicationModal)
        loading_dialog.show()
        QApplication.processEvents()
        
        # 메인 윈도우 비활성화
        self.setEnabled(False)
    
    # 이전 코드에서 수정된 부분
    def hide_loading_dialog(self):
        global loading_dialog
        loading_dialog.close()
        loading_dialog.deleteLater()  # 참조 삭제
        # 메인 윈도우 다시 활성화
        self.setEnabled(True)
    
    # def call_position(self):
    #     self.timer = QTimer(self)
    #     self.timer.timeout.connect(tf_publishing.check_position)
    #     self.timer.start(5000)  # milliseconds

if __name__ == "__main__":
    # QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    # WindowClass의 인스턴스 생성
    myWindow = WindowClass()

    # 프로그램 화면을 보여주는 코드
    myWindow.show()

    # 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    sys.exit(app.exec_())
