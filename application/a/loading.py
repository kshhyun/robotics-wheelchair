import sys
import time
from PyQt5.QtCore import Qt, QThread, pyqtSignal, QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QVBoxLayout, QLabel
from PyQt5 import QtGui, QtWidgets

import a.main


class LoadingDialog(QDialog):
    def __init__(self, parent=None):
        super(LoadingDialog, self).__init__(parent)
        self.setWindowTitle("")
        self.setWindowModality(Qt.ApplicationModal)
        self.setFixedSize(320, 200)
        
        self.label = QLabel("관리자가 권한 제어 중입니다.", self)
        self.label.setAlignment(Qt.AlignCenter)
        
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)
        
        # 창의 타이틀 바와 닫기 버튼을 숨깁니다.
        self.setWindowFlag(Qt.FramelessWindowHint)
        
        self.setupUi(self)
    
    def setupUi(self, LoadingDialog):
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        
        LoadingDialog.resize(400, 300)
        LoadingDialog.setStyleSheet("""background-color: #333333;
                                        color: white;""")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LoadingDialog.sizePolicy().hasHeightForWidth())
        LoadingDialog.setSizePolicy(sizePolicy)


# class Worker(QThread):
#     finished = pyqtSignal()
#
#     def run(self):
#         while True:
#             if massage.payload =="stop":
#                 break
#
#         # 작업이 끝나면 시그널을 보냅니다.
#         self.finished.emit()



def show_loading_dialog(window):
    print("2")
    loading_dialog = LoadingDialog(window)
    loading_dialog.setWindowModality(Qt.ApplicationModal)
    loading_dialog.show()
    QApplication.processEvents()
    
    # 메인 윈도우 비활성화
    window.setEnabled(False)
    
    # Worker 쓰레드를 생성하여 작업 시작
    # worker = Worker()
    # worker.finished.connect(lambda: hide_loading_dialog(loading_dialog, window))
    # worker.run()


# 이전 코드에서 수정된 부분
def hide_loading_dialog(loading_dialog, window):
    loading_dialog.close()
    loading_dialog.deleteLater()  # 참조 삭제
    # 메인 윈도우 다시 활성화
    window.setEnabled(True)


def handle_timeout(self):
    print("제어 요청이 거부되었습니다")
    self.hide_loading_dialog()

