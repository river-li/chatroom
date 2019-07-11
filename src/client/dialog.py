from PyQt5.QtWidgets import QWidget, QDesktopWidget
from startup import Ui_Form
from PyQt5.QtGui import QIcon

class Start_Dialog(QWidget, Ui_Form):
    def __init__(self):
        super(Start_Dialog, self).__init__()
        self.setupUi(self)
        self.center()
        self.setWindowTitle("登录")
        self.setWindowIcon(QIcon('../../img/icon.svg'))

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)

    def get_addr(self):
        host = self.lineEdit.text()

        port = self.lineEdit_2.text()
        try:
            port = int(port)
        except Exception as e:
            print(e)
        username = self.lineEdit_3.text()
        addr = (host, port)
        self.close()
        return addr,username