# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Liquid_fuel_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LIQUID_FUEL(object):
    def setupUi(self, LIQUID_FUEL):
        LIQUID_FUEL.setObjectName("LIQUID_FUEL")
        LIQUID_FUEL.resize(400, 620)
        LIQUID_FUEL.setStyleSheet("background-color: rgb(55,179,74);")
        self.centralwidget = QtWidgets.QWidget(LIQUID_FUEL)
        self.centralwidget.setObjectName("centralwidget")
        self.Mass_result = QtWidgets.QLabel(self.centralwidget)
        self.Mass_result.setGeometry(QtCore.QRect(30, 350, 351, 40))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(12)
        self.Mass_result.setFont(font)
        self.Mass_result.setStyleSheet("color: rgb(255, 255, 255);")
        self.Mass_result.setObjectName("Mass_result")
        self.L_btn_calc_M = QtWidgets.QPushButton(self.centralwidget)
        self.L_btn_calc_M.setGeometry(QtCore.QRect(220, 400, 151, 40))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.L_btn_calc_M.setFont(font)
        self.L_btn_calc_M.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: #00f500;\n"
"}")
        self.L_btn_calc_M.setObjectName("L_btn_calc_M")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 250, 351, 40))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 150, 400, 40))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setIndent(25)
        self.label_2.setObjectName("label_2")
        self.L_Stoichiometric_result = QtWidgets.QLabel(self.centralwidget)
        self.L_Stoichiometric_result.setGeometry(QtCore.QRect(30, 500, 181, 40))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.L_Stoichiometric_result.setFont(font)
        self.L_Stoichiometric_result.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.L_Stoichiometric_result.setText("")
        self.L_Stoichiometric_result.setObjectName("L_Stoichiometric_result")
        self.L_radio_Mass = QtWidgets.QRadioButton(self.centralwidget)
        self.L_radio_Mass.setGeometry(QtCore.QRect(210, 200, 110, 20))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.L_radio_Mass.setFont(font)
        self.L_radio_Mass.setStyleSheet("color: rgb(255, 255, 255);")
        self.L_radio_Mass.setObjectName("L_radio_Mass")
        self.L_btn_back = QtWidgets.QPushButton(self.centralwidget)
        self.L_btn_back.setGeometry(QtCore.QRect(30, 560, 341, 40))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.L_btn_back.setFont(font)
        self.L_btn_back.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: #00f500;\n"
"}")
        self.L_btn_back.setObjectName("L_btn_back")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 20, 400, 40))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setScaledContents(False)
        self.label.setWordWrap(False)
        self.label.setIndent(75)
        self.label.setObjectName("label")
        self.L_radio_Volumetric = QtWidgets.QRadioButton(self.centralwidget)
        self.L_radio_Volumetric.setGeometry(QtCore.QRect(90, 200, 110, 20))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.L_radio_Volumetric.setFont(font)
        self.L_radio_Volumetric.setStyleSheet("color: rgb(255, 255, 255);")
        self.L_radio_Volumetric.setObjectName("L_radio_Volumetric")
        self.L_Volumetric_result = QtWidgets.QLabel(self.centralwidget)
        self.L_Volumetric_result.setGeometry(QtCore.QRect(30, 300, 181, 40))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.L_Volumetric_result.setFont(font)
        self.L_Volumetric_result.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.L_Volumetric_result.setText("")
        self.L_Volumetric_result.setObjectName("L_Volumetric_result")
        self.Stoichiometric_result = QtWidgets.QLabel(self.centralwidget)
        self.Stoichiometric_result.setGeometry(QtCore.QRect(30, 450, 301, 40))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(12)
        self.Stoichiometric_result.setFont(font)
        self.Stoichiometric_result.setStyleSheet("color: rgb(255, 255, 255);")
        self.Stoichiometric_result.setObjectName("Stoichiometric_result")
        self.L_Mass_result = QtWidgets.QLabel(self.centralwidget)
        self.L_Mass_result.setGeometry(QtCore.QRect(30, 400, 181, 40))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.L_Mass_result.setFont(font)
        self.L_Mass_result.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.L_Mass_result.setText("")
        self.L_Mass_result.setObjectName("L_Mass_result")
        self.L_btn_calc_V = QtWidgets.QPushButton(self.centralwidget)
        self.L_btn_calc_V.setGeometry(QtCore.QRect(220, 300, 151, 40))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.L_btn_calc_V.setFont(font)
        self.L_btn_calc_V.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: #00f500;\n"
"}")
        self.L_btn_calc_V.setObjectName("L_btn_calc_V")
        self.L_btn_calc_Stoich = QtWidgets.QPushButton(self.centralwidget)
        self.L_btn_calc_Stoich.setGeometry(QtCore.QRect(220, 500, 151, 40))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.L_btn_calc_Stoich.setFont(font)
        self.L_btn_calc_Stoich.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: #00f500;\n"
"}")
        self.L_btn_calc_Stoich.setObjectName("L_btn_calc_Stoich")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 80, 151, 40))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(180, 80, 201, 40))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        LIQUID_FUEL.setCentralWidget(self.centralwidget)

        self.retranslateUi(LIQUID_FUEL)
        QtCore.QMetaObject.connectSlotsByName(LIQUID_FUEL)
        def calc_V_cal_value():
            pass
        def calc_M_cal_value():
            pass
        def calc_Stoich_ratio():
            pass
        self.L_btn_calc_V.clicked.connect(calc_V_cal_value)
        self.L_btn_calc_M.clicked.connect(calc_M_cal_value)
        self.L_btn_calc_Stoich.clicked.connect(calc_Stoich_ratio)
    def retranslateUi(self, LIQUID_FUEL):
        _translate = QtCore.QCoreApplication.translate
        LIQUID_FUEL.setWindowTitle(_translate("LIQUID_FUEL", "MainWindow"))
        self.Mass_result.setText(_translate("LIQUID_FUEL", "Массовая теплотворная способность"))
        self.L_btn_calc_M.setText(_translate("LIQUID_FUEL", "РАССЧИТАТЬ"))
        self.label_3.setText(_translate("LIQUID_FUEL", "Объёмная теплотворная способность"))
        self.label_2.setText(_translate("LIQUID_FUEL", "Доли компонентов топлива в таблице"))
        self.L_radio_Mass.setText(_translate("LIQUID_FUEL", "Массовые"))
        self.L_btn_back.setText(_translate("LIQUID_FUEL", "НАЗАД"))
        self.label.setText(_translate("LIQUID_FUEL", "Жидкое топливо"))
        self.L_radio_Volumetric.setText(_translate("LIQUID_FUEL", "Объёмные"))
        self.Stoichiometric_result.setText(_translate("LIQUID_FUEL", "Стехиометрическое отношение"))
        self.L_btn_calc_V.setText(_translate("LIQUID_FUEL", "РАССЧИТАТЬ"))
        self.L_btn_calc_Stoich.setText(_translate("LIQUID_FUEL", "РАССЧИТАТЬ"))
        self.label_4.setText(_translate("LIQUID_FUEL", "Месторождение"))




