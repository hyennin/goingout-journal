# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\python\외출일지\add.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        Form.setStyleSheet("background:rgb(252, 252, 252);")
        self.add_title = QtWidgets.QLabel(Form)
        self.add_title.setGeometry(QtCore.QRect(310, 110, 161, 41))
        font = QtGui.QFont()
        font.setFamily("궁서체")
        font.setPointSize(18)
        self.add_title.setFont(font)
        self.add_title.setObjectName("add_title")
        self.search_title_3 = QtWidgets.QLabel(Form)
        self.search_title_3.setGeometry(QtCore.QRect(260, 260, 111, 51))
        font = QtGui.QFont()
        font.setFamily("궁서체")
        font.setPointSize(16)
        self.search_title_3.setFont(font)
        self.search_title_3.setObjectName("search_title_3")
        self.btn_add_student = QtWidgets.QPushButton(Form)
        self.btn_add_student.setGeometry(QtCore.QRect(290, 370, 191, 71))
        font = QtGui.QFont()
        font.setFamily("궁서체")
        font.setPointSize(14)
        self.btn_add_student.setFont(font)
        self.btn_add_student.setStyleSheet("background:rgb(150, 150, 255);")
        self.btn_add_student.setObjectName("btn_add_student")
        self.add_room_number = QtWidgets.QPlainTextEdit(Form)
        self.add_room_number.setGeometry(QtCore.QRect(390, 190, 211, 50))
        font = QtGui.QFont()
        font.setFamily("궁서체")
        font.setPointSize(14)
        self.add_room_number.setFont(font)
        self.add_room_number.setObjectName("add_room_number")
        self.search_title_2 = QtWidgets.QLabel(Form)
        self.search_title_2.setGeometry(QtCore.QRect(210, 190, 161, 51))
        font = QtGui.QFont()
        font.setFamily("궁서체")
        font.setPointSize(16)
        self.search_title_2.setFont(font)
        self.search_title_2.setObjectName("search_title_2")
        self.add_name = QtWidgets.QPlainTextEdit(Form)
        self.add_name.setGeometry(QtCore.QRect(390, 260, 211, 50))
        font = QtGui.QFont()
        font.setFamily("궁서체")
        font.setPointSize(14)
        self.add_name.setFont(font)
        self.add_name.setObjectName("add_name")
        self.btn_back = QtWidgets.QPushButton(Form)
        self.btn_back.setGeometry(QtCore.QRect(290, 460, 191, 71))
        font = QtGui.QFont()
        font.setFamily("궁서체")
        font.setPointSize(14)
        self.btn_back.setFont(font)
        self.btn_back.setStyleSheet("background:rgb(200, 200, 200);")
        self.btn_back.setObjectName("btn_back")

        self.retranslateUi(Form)
        self.btn_back.clicked.connect(Form.btn_add_to_edit) # type: ignore
        self.btn_add_student.clicked.connect(Form.getAddInput) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.add_title.setText(_translate("Form", "기숙사생 추가"))
        self.search_title_3.setText(_translate("Form", "이름 입력:"))
        self.btn_add_student.setText(_translate("Form", "추가"))
        self.search_title_2.setText(_translate("Form", "호실 번호 입력:"))
        self.btn_back.setText(_translate("Form", "뒤로가기"))
