# 说明：这个文件是pyqt5的ui界面的代码，用于显示界面和交互
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtGui import QPainter, QColor, QBrush, QFont
import numpy as np
from calculate import Ann
import os
import csv
import time
import math
import matplotlib.pyplot as plt

if_con = True


def color_set(num):
    # 该函数用于根据数值大小返回颜色，目前为蓝色和紫色
    # 如果数值大于0，返回蓝色，否则返回紫色
    # 数值的绝对值越大，颜色越深
    if num > 0:
        return int((1 - math.tanh(0.5 * num)) * 255), 255, 255
    else:
        return 255, int((1 - math.tanh(-0.5 * num)) * 255), 255


class UiMainWindow(object):
    global if_con

    def setup_ui(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 615)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 10, 271, 331))
        self.groupBox.setObjectName("groupBox")
        self.textEdit_7 = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_7.setGeometry(QtCore.QRect(100, 265, 91, 16))
        self.textEdit_7.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_7.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_7.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.textEdit_7.setObjectName("textEdit_7")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 15, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 165, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(80, 165, 71, 16))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.textEdit_5 = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_5.setGeometry(QtCore.QRect(80, 215, 91, 16))
        self.textEdit_5.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_5.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_5.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.textEdit_5.setObjectName("textEdit_5")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 75, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(10, 190, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 290, 61, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(10, 240, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(10, 215, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 105, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_2.setGeometry(QtCore.QRect(80, 190, 71, 16))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.textEdit_6 = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_6.setGeometry(QtCore.QRect(80, 240, 91, 16))
        self.textEdit_6.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_6.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_6.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.textEdit_6.setObjectName("textEdit_6")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(10, 265, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(220, 25, 41, 31))
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit.setGeometry(QtCore.QRect(120, 15, 91, 21))
        self.textEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.textEdit.setObjectName("textEdit")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(10, 45, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setTextFormat(QtCore.Qt.PlainText)
        self.label_9.setWordWrap(False)
        self.label_9.setObjectName("label_9")
        self.textEdit_2 = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_2.setGeometry(QtCore.QRect(120, 45, 91, 21))
        self.textEdit_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_2.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(80, 75, 61, 20))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_4.setGeometry(QtCore.QRect(80, 105, 61, 20))
        self.pushButton_4.setObjectName("pushButton_4")
        self.textEdit_3 = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_3.setGeometry(QtCore.QRect(150, 75, 91, 20))
        self.textEdit_3.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_3.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_3.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.textEdit_3.setReadOnly(True)
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_4 = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_4.setGeometry(QtCore.QRect(150, 105, 91, 20))
        self.textEdit_4.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_4.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_4.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.textEdit_4.setReadOnly(True)
        self.textEdit_4.setObjectName("textEdit_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_5.setGeometry(QtCore.QRect(80, 290, 61, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setGeometry(QtCore.QRect(10, 135, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_6.setGeometry(QtCore.QRect(80, 135, 61, 20))
        self.pushButton_6.setObjectName("pushButton_6")
        self.textEdit_10 = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_10.setGeometry(QtCore.QRect(150, 135, 91, 20))
        self.textEdit_10.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_10.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_10.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.textEdit_10.setReadOnly(True)
        self.textEdit_10.setObjectName("textEdit_10")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(280, 10, 511, 311))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(490, 320, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.textEdit_8 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_8.setGeometry(QtCore.QRect(550, 320, 91, 20))
        self.textEdit_8.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_8.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_8.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.textEdit_8.setReadOnly(True)
        self.textEdit_8.setObjectName("textEdit_8")

        self.textEdit_8.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.textEdit_8.customContextMenuRequested[QtCore.QPoint].connect(self.text8click)

        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(280, 320, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.textEdit_9 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_9.setGeometry(QtCore.QRect(360, 320, 41, 20))
        self.textEdit_9.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_9.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_9.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.textEdit_9.setReadOnly(True)
        self.textEdit_9.setObjectName("textEdit_9")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "参数设置"))
        self.label.setText(_translate("MainWindow", "输入网络结构:"))
        self.label_4.setText(_translate("MainWindow", "损失函数:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "mse"))
        self.comboBox.setItemText(1, _translate("MainWindow", "mae"))
        self.comboBox.setItemText(2, _translate("MainWindow", "cross_entropy_error"))
        self.label_2.setText(_translate("MainWindow", "输入数据:"))
        self.label_5.setText(_translate("MainWindow", "优化器:"))
        self.pushButton_2.setText(_translate("MainWindow", "开始训练"))
        self.label_7.setText(_translate("MainWindow", "epochs:"))
        self.label_6.setText(_translate("MainWindow", "学习率:"))
        self.label_3.setText(_translate("MainWindow", "输出数据:"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "SGD"))
        self.label_8.setText(_translate("MainWindow", "batchsize:"))
        self.pushButton.setText(_translate("MainWindow", "确定"))
        self.label_9.setText(_translate("MainWindow", "输入激活函数:"))
        self.pushButton_3.setText(_translate("MainWindow", "上传"))
        self.pushButton_4.setText(_translate("MainWindow", "上传"))
        self.pushButton_5.setText(_translate("MainWindow", "暂停训练"))
        self.label_12.setText(_translate("MainWindow", "测试数据:"))
        self.pushButton_6.setText(_translate("MainWindow", "上传"))
        self.groupBox_2.setTitle(_translate("MainWindow", "网络示意图"))
        self.label_10.setText(_translate("MainWindow", "损失值："))
        self.label_11.setText(_translate("MainWindow", "当前次数："))
        """
        上述代码由工具生成，用于生成ui界面
        """

        self.flag = False
        self.pushButton.clicked.connect(self.on_click1)
        self.pushButton_2.clicked.connect(self.on_click2)
        self.pushButton_3.clicked.connect(self.on_click3)
        self.pushButton_4.clicked.connect(self.on_click4)
        self.pushButton_5.clicked.connect(self.on_click5)
        self.trainer = Ann()
        self.datain = []
        self.dataout = []
        self.structure = []
        self.active = []
        self.lossvalue = []
        # self.comboBox.currentIndexChanged.connect(self.indexchange)

    # 自定义右键按钮
    def text8click(self):
        popMenu = QMenu()
        popMenu.addAction(QAction(u'绘制图像', self))
        popMenu.triggered[QAction].connect(self.processtrigger8)
        popMenu.exec_(QCursor.pos())

    # 右键按钮事件
    def processtrigger8(self):
        plt.figure()
        plt.plot(self.lossvalue)
        plt.title('Model loss')
        plt.ylabel('Loss')
        plt.xlabel('Epoch')
        plt.legend(['Train'], loc='upper left')
        plt.show()

    def indexchange(self):
        sel = self.comboBox_3.currentText()
        # print(self.comboBox_3.currentText())
        for i in range(len(self.structure) - 1):
            self.centralwidget.findChild(QtWidgets.QTableWidget, "table" + str(i)).setVisible(False)
        self.centralwidget.findChild(QtWidgets.QTableWidget, "table" + sel[5:]).show()

    def on_click5(self):
        global if_con
        if_con = False

    def on_click3(self):
        filename = QFileDialog.getOpenFileNames(self, '选择图像', os.getcwd(), "All Files(*);;Text Files(*.csv)")
        if filename[0] != []:
            outname = filename[0][0]
            self.textEdit_3.setText(outname)
            self.datain = []
            with open(outname, encoding="utf-8") as f:
                reader = csv.reader(f)
                for row in reader:
                    data = np.array(row)
                    data = data.astype(np.float32)
                    self.datain.append(data)
            self.datain = np.array(self.datain)

    def on_click4(self):
        filename = QFileDialog.getOpenFileNames(self, '选择图像', os.getcwd(), "All Files(*);;Text Files(*.csv)")
        if filename[0] != []:
            outname = filename[0][0]
            self.textEdit_4.setText(outname)
            self.dataout = []
            with open(outname, encoding="utf-8") as f:
                reader = csv.reader(f)
                for row in reader:
                    data = np.array(row)
                    data = data.astype(np.float32)
                    self.dataout.append(data)
            self.dataout = np.array(self.dataout)

    def on_click2(self):
        batchsize = int(self.textEdit_7.toPlainText())
        epochs = int(self.textEdit_6.toPlainText())
        learnrate = float(self.textEdit_5.toPlainText())
        lossmod = self.comboBox.currentText()
        gradmod = self.comboBox_2.currentText()
        self.trainw = [[] for i in range(len(self.structure) - 1)]
        self.trainb = [[] for i in range(len(self.structure) - 1)]
        for i in range(len(self.structure) - 1):
            for k in range(self.structure[i + 1]):
                for l in range(self.structure[i]):
                    self.trainer.grad[i][k][l] = float(
                        self.centralwidget.findChild(QtWidgets.QTableWidget, "table" + str(i)).item(k, l).text())
            self.trainer.bias[i] = float(
                self.centralwidget.findChild(QtWidgets.QTableWidget, "table" + str(i)).item(0, l + 1).text())

            self.trainw[i].append(self.trainer.grad[i])
            self.trainb[i].append(self.trainer.bias[i])
        self.lossvalue = []
        self.trainbegin = TrainThread()
        self.trainbegin.send_signal.connect(self.update_table)
        self.trainbegin.setdata(inp=self.datain, expe=self.dataout, stru=self.structure, activemod=self.active,
                                epoch=epochs,
                                batchsize=batchsize, lossmod=lossmod, learnrate=learnrate, gradmod=gradmod,
                                trainer=self.trainer)
        self.trainbegin.start()
        # self.trainer.train(inp=self.datain,expe=self.dataout,stru=self.structure,activemod=self.active,epoch=epochs,
        #                   batchsize=batchsize,lossmod=lossmod,learnrate=learnrate,gradmod=gradmod)
        # print(self.trainer.grad)

    def update_table(self, text1, text2):
        # print(text1,text2)
        self.textEdit_9.setPlainText(str(text1))
        self.textEdit_8.setPlainText(str(text2))
        self.lossvalue.append(text2)

        for i in range(len(self.structure) - 1):
            table_widget = self.centralwidget.findChild(QtWidgets.QTableWidget, "table" + str(i))
            for k in range(self.structure[i + 1]):
                for l in range(self.structure[i]):
                    itemvalue = float(self.trainer.grad[i][k][l])
                    item = QTableWidgetItem(str(itemvalue))
                    itemcolor = color_set(itemvalue)
                    item.setBackground(QBrush(QColor(itemcolor[0], itemcolor[1], itemcolor[2])))
                    table_widget.setItem(k, l, item)
            itemvalue = float(self.trainer.bias[i])
            item = QTableWidgetItem(str(itemvalue))
            itemcolor = color_set(itemvalue)
            item.setBackground(QBrush(QColor(itemcolor[0], itemcolor[1], itemcolor[2])))
            table_widget.setItem(0, l + 1, item)
            self.trainw[i].append(self.trainer.grad[i])
            self.trainb[i].append(self.trainer.bias[i])

    def on_click1(self):
        if self.flag:
            for i in range(len(self.structure) - 1):
                self.centralwidget.findChild(QtWidgets.QTableWidget, "table" + str(i)).deleteLater()
        textread = self.textEdit.toPlainText()
        textread2 = self.textEdit_2.toPlainText()
        if textread == "" or textread2 == "":
            QtWidgets.QMessageBox.warning(self, '警告', '输入不能为空')
        else:
            try:
                textread = textread.split(",")
                self.structure = []
                for i in textread:
                    self.structure.append(int(i))
                print(self.structure)
                textread = textread2.split(",")
                self.active = []
                for i in textread:
                    self.active.append(i.lower())
                print(self.active)
                self.flag = True
                self.update()


            except:
                QtWidgets.QMessageBox.warning(self, '警告', '输入用逗号隔开!，例如：1,2,3')
            self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
            self.comboBox_3.setGeometry(QtCore.QRect(10, 340, 67, 20))
            self.comboBox_3.setObjectName("comboBox_2")
            self.trainer.initial(self.structure)
            self.trainw = [[] for i in range(len(self.structure) - 1)]
            self.trainb = [[] for i in range(len(self.structure) - 1)]
            for i in range(len(self.structure) - 1):
                self.comboBox_3.addItem("Layer" + str(i))
                table_widget = QtWidgets.QTableWidget(self.centralwidget)
                # 创建一个4行3列的表格
                table_widget.setRowCount(self.structure[i + 1])
                table_widget.setColumnCount(self.structure[i] + 1)
                table_widget.setGeometry(0, 360, 791, 211)
                table_widget.setObjectName("table" + str(i))
                table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

                # table widget 右键菜单 放在主窗口__init__(self):下
                table_widget.setContextMenuPolicy(Qt.CustomContextMenu)  # 允许右键产生子菜单
                table_widget.customContextMenuRequested.connect(self.tableclick)  # 右键菜单

                data = []
                for k in range(1, self.structure[i] + 1):
                    data.append("w" + str(k))
                data.append("b")
                table_widget.setHorizontalHeaderLabels(data)
                data = []
                for k in range(1, self.structure[i + 1] + 1):
                    data.append("w" + str(k))
                table_widget.setVerticalHeaderLabels(data)
                for k in range(self.structure[i + 1]):
                    for l in range(self.structure[i]):
                        itemvalue = float(self.trainer.grad[i][k][l])
                        item = QTableWidgetItem(str(itemvalue))
                        itemcolor = color_set(itemvalue)
                        print(itemcolor)
                        item.setBackground(QBrush(QColor(itemcolor[0], itemcolor[1], itemcolor[2])))
                        table_widget.setItem(k, l, item)
                itemvalue = float(self.trainer.bias[i])
                item = QTableWidgetItem(str(itemvalue))
                itemcolor = color_set(itemvalue)
                item.setBackground(QBrush(QColor(itemcolor[0], itemcolor[1], itemcolor[2])))
                table_widget.setItem(0, l + 1, item)
                # table_widget.show()

                self.trainw[i].append(self.trainer.grad[i])
                self.trainb[i].append(self.trainer.bias[i])

            self.centralwidget.findChild(QtWidgets.QTableWidget, "table0").show()
            self.comboBox_3.currentIndexChanged.connect(self.indexchange)
            self.comboBox_3.show()
            '''
            self.stackedLayout = QtWidgets.QStackedLayout(self.centralwidget)
            #self.stackedLayout.setGeometry(QtCore.QRect(0,360,791,211))
            frame = QtWidgets.QWidget(self.centralwidget)
            table = QtWidgets.QTableWidget(frame)
            table.setRowCount(4)
            table.setColumnCount(3)
            table.setGeometry(0,360,791,211)
            self.stackedLayout.addWidget(frame)
            '''

    def processtable(self):
        index = self.comboBox_3.currentText()[5:]
        tablecurrent = self.centralwidget.findChild(QtWidgets.QTableWidget, "table" + index)
        index = int(index)
        row = tablecurrent.currentIndex().row()
        colum = tablecurrent.currentIndex().column()
        print(index, row, colum)
        if colum == self.structure[index]:
            plt.figure()
            plt.plot(self.trainb[index])
            plt.title('b')
            plt.ylabel('value')
            plt.xlabel('Epoch')
            plt.legend(['Train'], loc='upper left')
            plt.show()
        else:
            plt.figure()
            plt.plot(np.array(self.trainw[index])[:, row, colum])
            plt.title('w' + str(row) + str(colum))
            plt.ylabel('value')
            plt.xlabel('Epoch')
            plt.legend(['Train'], loc='upper left')
            plt.show()

    def tableclick(self):
        """
        :return:
        """

        popMenu = QMenu()
        popMenu.addAction(QAction(u'绘制图像', self))
        popMenu.triggered[QAction].connect(self.processtable)
        popMenu.exec_(QCursor.pos())
        '''
        menu = QMenu() #实例化菜单
        item1 = menu.addAction(u"清除")
        item2 = menu.addAction(u"拷贝")
        action = menu.exec_(self.tableWidget_VTest.mapToGlobal(pos))

        if action == item1:
            print("清除")
        elif action == item2:
            print("拷贝")
        '''

    def paintEvent(self, event):
        if self.flag:
            painter = QPainter()
            painter.begin(self)
            painter.setBrush(QColor(25, 0, 90, 200))
            painter.setFont(QFont('SimSun', 10))
            startx = 500 + 20 - 20 * len(self.structure)
            starty = 180
            datapoint = [[] for i in range(len(self.structure))]
            for i in range(len(self.structure)):
                if i == 0:
                    if self.structure[i] <= 4:
                        painter.drawText(startx + i * 50 - 5, starty + 15 * self.structure[i], "input")
                        painter.setFont(QFont('SimSun', 10))
                        painter.drawText(startx + i * 50 + 8 - len(str(self.structure[i])),
                                         starty - 15 * self.structure[i] - 5, str(self.structure[i]))
                    else:
                        painter.drawText(startx + i * 50 - 5, starty + 65, "input")
                        painter.setFont(QFont('SimSun', 10))
                        painter.drawText(startx + i * 50 + 8 - len(str(self.structure[i])), starty - 70,
                                         str(self.structure[i]))
                else:
                    if self.structure[i] <= 4:
                        painter.setFont(QFont('SimSun', 15 - len(self.active[i - 1])))
                        painter.drawText(startx + i * 50 - len(self.active[i - 1]), starty + 15 * self.structure[i],
                                         self.active[i - 1])
                        painter.setFont(QFont('SimSun', 10))
                        painter.drawText(startx + i * 50 + 8 - len(str(self.structure[i])),
                                         starty - 15 * self.structure[i] - 5, str(self.structure[i]))
                    else:
                        painter.setFont(QFont('SimSun', 15 - len(self.active[i - 1])))
                        painter.drawText(startx + i * 50 - len(self.active[i - 1]), starty + 65, self.active[i - 1])
                        painter.setFont(QFont('SimSun', 10))
                        painter.drawText(startx + i * 50 + 8 - len(str(self.structure[i])), starty - 70,
                                         str(self.structure[i]))
                if self.structure[i] > 4:
                    painter.drawEllipse(startx + i * 50, starty - 65, 20, 20)
                    datapoint[i].append((startx + i * 50 + 10, starty - 55))
                    painter.drawEllipse(startx + i * 50, starty - 35, 20, 20)
                    datapoint[i].append((startx + i * 50 + 10, starty - 25))
                    painter.drawEllipse(startx + i * 50 + 9, starty, 2, 2)
                    painter.drawEllipse(startx + i * 50 + 9, starty + 5, 2, 2)
                    painter.drawEllipse(startx + i * 50 + 9, starty + 10, 2, 2)
                    painter.drawEllipse(startx + i * 50 + 9, starty + 15, 2, 2)
                    painter.drawEllipse(startx + i * 50 + 9, starty + 20, 2, 2)
                    painter.drawEllipse(startx + i * 50, starty + 35, 20, 20)
                    datapoint[i].append((startx + i * 50 + 10, starty + 45))
                else:
                    for k in range(self.structure[i]):
                        painter.drawEllipse(startx + i * 50, starty - 15 * self.structure[i] + 30 * k, 20, 20)
                        datapoint[i].append((startx + i * 50 + 10, starty - 15 * self.structure[i] + 30 * k + 10))
            for i in range(len(self.structure) - 1):
                for j in datapoint[i]:
                    for k in datapoint[i + 1]:
                        painter.drawLine(j[0], j[1], k[0], k[1])
            painter.end()


# 继承QThread
class TrainThread(QThread):  # 线程1
    global if_con
    send_signal = pyqtSignal(int, float)

    def __init__(self):
        super().__init__()

    def setdata(self, inp, expe, stru, activemod, epoch, batchsize, lossmod, learnrate, gradmod,
                trainer):  # 专门定义一个方法将主线程的参数传给子线程
        self.inp = inp
        self.expe = expe
        self.stru = stru
        self.activemod = activemod
        self.epoch = epoch
        self.batchsize = batchsize
        self.lossmod = lossmod
        self.learnrate = learnrate
        self.gradmod = gradmod
        self.trainer = trainer

    def run(self):
        global if_con
        num = 0
        for i in self.trainer.train(inp=self.inp, expe=self.expe, stru=self.stru, activemod=self.activemod,
                                    epoch=self.epoch,
                                    batchsize=self.batchsize, lossmod=self.lossmod, learnrate=self.learnrate,
                                    gradmod=self.gradmod):
            if if_con:
                num = num + 1
                self.send_signal.emit(num, i)
                time.sleep(0.5)  # 休眠
            else:
                if_con = True
                break
