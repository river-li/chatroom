import socket
import sys
import json
from PyQt5.QtWidgets import  QMainWindow, QApplication, QMessageBox, QDesktopWidget
from PyQt5.QtGui import QIcon
from main_window import Ui_MainWindow
from dialog import Start_Dialog
from backen_thread import ListenThread

class Client(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Client, self).__init__()
        self.setupUi(self)
        self.center()
        self.isConnect = False
        self.dialog = Start_Dialog()
        self.dialog.pushButton.clicked.connect(self.login)
        self.pushButton.clicked.connect(self.send)
        self.pushButton_2.clicked.connect(self.refresh)
        self.setWindowTitle("聊天室Demo")
        self.setWindowIcon(QIcon('../../img/icon.svg'))

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)

    def __main__(self):
        self.listenThread = ListenThread(self.tcpCliSock, self)
        self.listenThread.start()
        self.refresh()

    def connect(self, ADDR):
        """连接服务器"""
        if not self.isConnect:
            self.tcpCliSock = socket.socket(socket.AF_INET,  socket.SOCK_STREAM)
            self.tcpCliSock.connect(ADDR)
            self.isConnect = True

    def show_error(self, msg):
        QMessageBox.warning(self, "Error", msg, QMessageBox.Yes, QMessageBox.Yes)

    def disConnect(self):
        """断开服务器"""
        self.tcpCliSock.close()

    def login(self):
        addr, username = self.dialog.get_addr()
        print(username)
        self.username = username
        data = {"type":"login", "username": username}
        json_data = json.dumps(data)
        json_data = bytes(json_data, 'utf8')
        try:
            self.connect(addr)
        except Exception as e:
            self.show_error("网络连接失败")
            print(e)
        else:
            self.tcpCliSock.send(json_data)
            recv_json_data = self.tcpCliSock.recv(1024)
            recv_data = json.loads(recv_json_data)
            if recv_data["type"] == "login" and recv_data["username"] == username and recv_data["status"] ==True:
                self.__main__()

    def send(self):
        if self.isConnect == False:
            self.show_error("Not Connected")
            return
        text = self.lineEdit.text()
        data = {"type":"chat", "msg":text, "from": self.username}
        json_data = json.dumps(data)
        json_data = bytes(json_data, 'utf8')
        try:
            self.tcpCliSock.send(json_data)
        except Exception as e:
            print(e)
            self.show_error("Send Failed!")
        self.lineEdit.clear()

    def refresh(self):
        data = {"type":"list"}
        json_data = json.dumps(data)
        json_data = bytes(json_data, 'utf8')
        self.tcpCliSock.send(json_data)


def main():
    app = QApplication(sys.argv)
    client = Client()
    client.show()
    client.dialog.show()
    app.exec_()

if __name__ == '__main__':
   main()
