from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from Selection_tree_window import Ui_Selection_tree
from Liquid_fuel_window import Ui_LIQUID_FUEL
from Gaseous_fuel_window import Ui_GASEOUS_FUEL
import sys

app = QtWidgets.QApplication(sys.argv)

Selection_tree = QtWidgets.QMainWindow()
ui = Ui_Selection_tree()
ui.setupUi(Selection_tree)
Selection_tree.show()
def open_Liquid():
    global LIQUID_FUEL
    LIQUID_FUEL = QtWidgets.QMainWindow()
    ui = Ui_LIQUID_FUEL()
    ui.setupUi(LIQUID_FUEL)
    Selection_tree.hide()
    LIQUID_FUEL.show()
    def Return_from_L():
        LIQUID_FUEL.hide()
        Selection_tree.show()
    ui.L_btn_back.clicked.connect(Return_from_L)

def open_Gaseous():
    global GASEOUS_FUEL
    GASEOUS_FUEL = QtWidgets.QMainWindow()
    ui = Ui_GASEOUS_FUEL()
    ui.setupUi(GASEOUS_FUEL)
    Selection_tree.hide()
    GASEOUS_FUEL.show()
    def Return_from_G():
        GASEOUS_FUEL.hide()
        Selection_tree.show()
    ui.G_btn_back.clicked.connect(Return_from_G)
def Close():
    Selection_tree.close()

ui.btn_To_zhidkoe.clicked.connect(open_Liquid)
ui.btn_To_gazoobraznoe.clicked.connect(open_Gaseous)
ui.btn_cancel.clicked.connect(Close)
sys.exit(app.exec_())
