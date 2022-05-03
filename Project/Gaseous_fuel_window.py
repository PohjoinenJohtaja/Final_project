# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Gaseous_fuel_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GASEOUS_FUEL(object):
    def setupUi(self, GASEOUS_FUEL):
        GASEOUS_FUEL.setObjectName("GASEOUS_FUEL")
        GASEOUS_FUEL.resize(400, 620)
        GASEOUS_FUEL.setStyleSheet("background-color: rgb(55,179,74);")
        self.centralwidget = QtWidgets.QWidget(GASEOUS_FUEL)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 20, 400, 40))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setIndent(25)
        self.label.setObjectName("label")
        self.radio_Volumetric = QtWidgets.QRadioButton(self.centralwidget)
        self.radio_Volumetric.setGeometry(QtCore.QRect(90, 200, 110, 20))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.radio_Volumetric.setFont(font)
        self.radio_Volumetric.setStyleSheet("color: rgb(255, 255, 255);")
        self.radio_Volumetric.setObjectName("radio_Volumetric")
        self.radio_Mass = QtWidgets.QRadioButton(self.centralwidget)
        self.radio_Mass.setGeometry(QtCore.QRect(210, 200, 110, 20))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.radio_Mass.setFont(font)
        self.radio_Mass.setStyleSheet("color: rgb(255, 255, 255);")
        self.radio_Mass.setObjectName("radio_Mass")
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
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 250, 351, 40))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.G_btn_calc_V = QtWidgets.QPushButton(self.centralwidget)
        self.G_btn_calc_V.setGeometry(QtCore.QRect(220, 300, 151, 40))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.G_btn_calc_V.setFont(font)
        self.G_btn_calc_V.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: #00f500;\n"
"}")
        self.G_btn_calc_V.setObjectName("G_btn_calc_V")
        self.G_Volumetric_result = QtWidgets.QLabel(self.centralwidget)
        self.G_Volumetric_result.setGeometry(QtCore.QRect(30, 300, 181, 40))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.G_Volumetric_result.setFont(font)
        self.G_Volumetric_result.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.G_Volumetric_result.setText("")
        self.G_Volumetric_result.setObjectName("G_Volumetric_result")
        self.Mass_result = QtWidgets.QLabel(self.centralwidget)
        self.Mass_result.setGeometry(QtCore.QRect(30, 350, 351, 40))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(12)
        self.Mass_result.setFont(font)
        self.Mass_result.setStyleSheet("color: rgb(255, 255, 255);")
        self.Mass_result.setObjectName("Mass_result")
        self.G_Mass_result = QtWidgets.QLabel(self.centralwidget)
        self.G_Mass_result.setGeometry(QtCore.QRect(30, 400, 181, 40))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.G_Mass_result.setFont(font)
        self.G_Mass_result.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.G_Mass_result.setText("")
        self.G_Mass_result.setObjectName("G_Mass_result")
        self.G_btn_calc_M = QtWidgets.QPushButton(self.centralwidget)
        self.G_btn_calc_M.setGeometry(QtCore.QRect(220, 400, 151, 40))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.G_btn_calc_M.setFont(font)
        self.G_btn_calc_M.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: #00f500;\n"
"}")
        self.G_btn_calc_M.setObjectName("G_btn_calc_M")
        self.Stoichiometric_result = QtWidgets.QLabel(self.centralwidget)
        self.Stoichiometric_result.setGeometry(QtCore.QRect(30, 450, 301, 40))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(12)
        self.Stoichiometric_result.setFont(font)
        self.Stoichiometric_result.setStyleSheet("color: rgb(255, 255, 255);")
        self.Stoichiometric_result.setObjectName("Stoichiometric_result")
        self.G_Stoichiometric_result = QtWidgets.QLabel(self.centralwidget)
        self.G_Stoichiometric_result.setGeometry(QtCore.QRect(30, 500, 181, 40))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.G_Stoichiometric_result.setFont(font)
        self.G_Stoichiometric_result.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.G_Stoichiometric_result.setText("")
        self.G_Stoichiometric_result.setObjectName("G_Stoichiometric_result")
        self.G_btn_calc_Stoich = QtWidgets.QPushButton(self.centralwidget)
        self.G_btn_calc_Stoich.setGeometry(QtCore.QRect(220, 500, 151, 40))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.G_btn_calc_Stoich.setFont(font)
        self.G_btn_calc_Stoich.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: #00f500;\n"
"}")
        self.G_btn_calc_Stoich.setObjectName("G_btn_calc_Stoich")
        self.G_btn_back = QtWidgets.QPushButton(self.centralwidget)
        self.G_btn_back.setGeometry(QtCore.QRect(30, 560, 341, 40))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.G_btn_back.setFont(font)
        self.G_btn_back.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: #00f500;\n"
"}")
        self.G_btn_back.setObjectName("G_btn_back")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(180, 90, 201, 40))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 90, 151, 40))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        GASEOUS_FUEL.setCentralWidget(self.centralwidget)

        self.retranslateUi(GASEOUS_FUEL)
        QtCore.QMetaObject.connectSlotsByName(GASEOUS_FUEL)
        def calc_V_cal_value():
            pass
        def calc_M_cal_value():
            pass
        def calc_Stoich_ratio():
            pass
        self.G_btn_calc_V.clicked.connect(calc_V_cal_value)
        self.G_btn_calc_M.clicked.connect(calc_M_cal_value)
        self.G_btn_calc_Stoich.clicked.connect(calc_Stoich_ratio)

    def retranslateUi(self, GASEOUS_FUEL):
        _translate = QtCore.QCoreApplication.translate
        GASEOUS_FUEL.setWindowTitle(_translate("GASEOUS_FUEL", "MainWindow"))
        self.label.setText(_translate("GASEOUS_FUEL", "Газообразное топливо"))
        self.radio_Volumetric.setText(_translate("GASEOUS_FUEL", "Объёмные"))
        self.radio_Mass.setText(_translate("GASEOUS_FUEL", "Массовые"))
        self.label_2.setText(_translate("GASEOUS_FUEL", "Доли компонентов топлива в таблице"))
        self.label_3.setText(_translate("GASEOUS_FUEL", "Объёмная теплотворная способность"))
        self.G_btn_calc_V.setText(_translate("GASEOUS_FUEL", "РАССЧИТАТЬ"))
        self.Mass_result.setText(_translate("GASEOUS_FUEL", "Массовая теплотворная способность"))
        self.G_btn_calc_M.setText(_translate("GASEOUS_FUEL", "РАССЧИТАТЬ"))
        self.Stoichiometric_result.setText(_translate("GASEOUS_FUEL", "Стехиометрическое отношение"))
        self.G_btn_calc_Stoich.setText(_translate("GASEOUS_FUEL", "РАССЧИТАТЬ"))
        self.G_btn_back.setText(_translate("GASEOUS_FUEL", "НАЗАД"))
        self.label_4.setText(_translate("GASEOUS_FUEL", "Месторождение"))



