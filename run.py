# 启动UI界面
from UI import UiMainWindow
import sys  # PyQt5中使用的基本控件都在PyQt5.QtWidgets模块中
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget  # 导入designer工具生成的图窗模块


class MyMainForm(QMainWindow, UiMainWindow):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setup_ui(self)


if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)  # 初始化
    myWin = MyMainForm()  # 将窗口控件显示在屏幕上
    myWin.show()  # 程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())
