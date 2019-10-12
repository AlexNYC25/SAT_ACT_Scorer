# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SAT_Page.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.EnglishLabel = QtWidgets.QLabel(Dialog)
        self.EnglishLabel.setGeometry(QtCore.QRect(40, 40, 221, 16))
        self.EnglishLabel.setObjectName("EnglishLabel")
        self.InputEng = QtWidgets.QLineEdit(Dialog)
        self.InputEng.setGeometry(QtCore.QRect(40, 60, 41, 21))
        self.InputEng.setObjectName("InputEng")
        self.MathLabel = QtWidgets.QLabel(Dialog)
        self.MathLabel.setGeometry(QtCore.QRect(40, 90, 161, 16))
        self.MathLabel.setObjectName("MathLabel")
        self.InputMath = QtWidgets.QLineEdit(Dialog)
        self.InputMath.setGeometry(QtCore.QRect(40, 110, 41, 21))
        self.InputMath.setObjectName("InputMath")
        self.WritingLabel = QtWidgets.QLabel(Dialog)
        self.WritingLabel.setGeometry(QtCore.QRect(40, 140, 241, 16))
        self.WritingLabel.setObjectName("WritingLabel")
        self.InputWrite = QtWidgets.QLineEdit(Dialog)
        self.InputWrite.setGeometry(QtCore.QRect(40, 160, 41, 21))
        self.InputWrite.setObjectName("InputWrite")
        self.TitleLabel = QtWidgets.QLabel(Dialog)
        self.TitleLabel.setGeometry(QtCore.QRect(40, 10, 321, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.TitleLabel.setFont(font)
        self.TitleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.TitleLabel.setObjectName("TitleLabel")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.EnglishLabel.setText(_translate("Dialog", "Enter Raw English Score:"))
        self.MathLabel.setText(_translate("Dialog", "Enter Raw Math Score:"))
        self.WritingLabel.setText(_translate("Dialog", "Enter Raw Writing and Language Score:"))
        self.TitleLabel.setText(_translate("Dialog", "Enter Your SAT Score"))
