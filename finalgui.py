# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'finalgui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1005, 800)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../../../../../Desktop/background.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0)"))
        MainWindow.setTabShape(QtGui.QTabWidget.Rounded)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.run = QtGui.QPushButton(self.centralwidget)
        self.run.setGeometry(QtCore.QRect(30, 520, 151, 41))
        self.run.setMouseTracking(False)
        self.run.setStyleSheet(_fromUtf8("background: url();\n"
"font: 63 medium 11pt \"Ubuntu\";\n"
"background-color: rgba(38, 206, 203,200);\n"
"border-color: rgba(255, 85, 0,175);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;"))
        self.run.setDefault(False)
        self.run.setObjectName(_fromUtf8("run"))
        self.button2 = QtGui.QPushButton(self.centralwidget)
        self.button2.setGeometry(QtCore.QRect(30, 570, 151, 41))
        self.button2.setStyleSheet(_fromUtf8("background: url();\n"
"background-color: rgba(38, 206, 203,200);\n"
"border-color: rgba(255, 85, 0,175);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"font: 63 medium 11pt \"Ubuntu\";\n"
""))
        self.button2.setDefault(False)
        self.button2.setObjectName(_fromUtf8("button2"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(280, 10, 351, 391))
        self.frame.setStyleSheet(_fromUtf8("background:  url();\n"
"border: 1px solid grey;\n"
"border-radius: 5px;\n"
""))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.label_6 = QtGui.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(30, 10, 241, 31))
        self.label_6.setStyleSheet(_fromUtf8("color: rgb(255,255,255);\n"
"border: 1px solid black"))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.Wheel_Velocity_Left = QtGui.QPlainTextEdit(self.frame)
        self.Wheel_Velocity_Left.setGeometry(QtCore.QRect(20, 50, 151, 61))
        self.Wheel_Velocity_Left.setStyleSheet(_fromUtf8("background: url();\n"
"background-color: rgb(200, 200, 200);\n"
"border-radius: 5px;"))
        self.Wheel_Velocity_Left.setObjectName(_fromUtf8("Wheel_Velocity_Left"))
        self.label_4 = QtGui.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(30, 120, 201, 51))
        self.label_4.setStyleSheet(_fromUtf8("color: rgb(255,255,255);\n"
"border: 1px solid black"))
        self.label_4.setTextFormat(QtCore.Qt.AutoText)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.angle_1 = QtGui.QPlainTextEdit(self.frame)
        self.angle_1.setGeometry(QtCore.QRect(210, 170, 111, 61))
        self.angle_1.setStyleSheet(_fromUtf8("background-color: rgb(200, 200, 200);\n"
"border-radius: 5px;\n"
"border-color: rgb(84, 84, 84);"))
        self.angle_1.setPlainText(_fromUtf8(""))
        self.angle_1.setObjectName(_fromUtf8("angle_1"))
        self.angle_2 = QtGui.QPlainTextEdit(self.frame)
        self.angle_2.setGeometry(QtCore.QRect(210, 240, 111, 61))
        self.angle_2.setStyleSheet(_fromUtf8("background: url();\n"
"background-color: rgb(200, 200, 200);\n"
"border-radius: 5px;"))
        self.angle_2.setObjectName(_fromUtf8("angle_2"))
        self.angle_3 = QtGui.QPlainTextEdit(self.frame)
        self.angle_3.setGeometry(QtCore.QRect(210, 310, 111, 61))
        self.angle_3.setStyleSheet(_fromUtf8("background: url();\n"
"background-color: rgb(200, 200, 200);\n"
"border-radius: 5px;"))
        self.angle_3.setObjectName(_fromUtf8("angle_3"))
        self.label_18 = QtGui.QLabel(self.frame)
        self.label_18.setGeometry(QtCore.QRect(30, 170, 141, 31))
        self.label_18.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"border: 1px solid black"))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.label_19 = QtGui.QLabel(self.frame)
        self.label_19.setGeometry(QtCore.QRect(30, 240, 141, 31))
        self.label_19.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255) ;\n"
"border: 1px solid black\n"
""))
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.label_20 = QtGui.QLabel(self.frame)
        self.label_20.setGeometry(QtCore.QRect(30, 310, 141, 31))
        self.label_20.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255) ;\n"
"border: 1px solid black\n"
""))
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.Wheel_Velocity_Right = QtGui.QPlainTextEdit(self.frame)
        self.Wheel_Velocity_Right.setGeometry(QtCore.QRect(180, 50, 151, 61))
        self.Wheel_Velocity_Right.setStyleSheet(_fromUtf8("background: url();\n"
"background-color: rgb(200, 200, 200);\n"
"border-radius: 5px;"))
        self.Wheel_Velocity_Right.setObjectName(_fromUtf8("Wheel_Velocity_Right"))
        self.frame_2 = QtGui.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(650, 10, 321, 461))
        self.frame_2.setStyleSheet(_fromUtf8("background:  url();\n"
"border: 1px solid grey;\n"
"border-radius: 5px;\n"
""))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.label_11 = QtGui.QLabel(self.frame_2)
        self.label_11.setGeometry(QtCore.QRect(70, 10, 201, 51))
        self.label_11.setStyleSheet(_fromUtf8("color: rgb(255,255,255);\n"
"border: 1px solid black"))
        self.label_11.setScaledContents(False)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.Pressure = QtGui.QPlainTextEdit(self.frame_2)
        self.Pressure.setGeometry(QtCore.QRect(180, 60, 111, 71))
        self.Pressure.setStyleSheet(_fromUtf8("background: url();\n"
"background-color: rgb(200, 200, 200);\n"
"border-radius: 10px;"))
        self.Pressure.setObjectName(_fromUtf8("Pressure"))
        self.Altitude = QtGui.QPlainTextEdit(self.frame_2)
        self.Altitude.setGeometry(QtCore.QRect(180, 160, 111, 71))
        self.Altitude.setStyleSheet(_fromUtf8("background: url();\n"
"background-color: rgb(200, 200, 200);\n"
"border-radius: 5px;"))
        self.Altitude.setObjectName(_fromUtf8("Altitude"))
        self.Soil_temp = QtGui.QPlainTextEdit(self.frame_2)
        self.Soil_temp.setGeometry(QtCore.QRect(180, 250, 111, 71))
        self.Soil_temp.setStyleSheet(_fromUtf8("background: url();\n"
"background-color: rgb(200, 200, 200);\n"
"border-radius: 5px;"))
        self.Soil_temp.setObjectName(_fromUtf8("Soil_temp"))
        self.Humidity = QtGui.QPlainTextEdit(self.frame_2)
        self.Humidity.setGeometry(QtCore.QRect(180, 350, 111, 71))
        self.Humidity.setStyleSheet(_fromUtf8("background: url();\n"
"background-color: rgb(200, 200, 200);\n"
"border-radius: 5px;"))
        self.Humidity.setObjectName(_fromUtf8("Humidity"))
        self.label_16 = QtGui.QLabel(self.frame_2)
        self.label_16.setGeometry(QtCore.QRect(20, 70, 121, 31))
        self.label_16.setStyleSheet(_fromUtf8("color: rgb(255,255,255);\n"
"border: 1px solid black"))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.label_15 = QtGui.QLabel(self.frame_2)
        self.label_15.setGeometry(QtCore.QRect(20, 170, 91, 31))
        self.label_15.setStyleSheet(_fromUtf8("color: rgb(255,255,255);\n"
"border: 1px solid black"))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.label_14 = QtGui.QLabel(self.frame_2)
        self.label_14.setGeometry(QtCore.QRect(20, 270, 151, 31))
        self.label_14.setStyleSheet(_fromUtf8("color: rgb(255,255,255);\n"
"border: 1px solid black"))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.label_13 = QtGui.QLabel(self.frame_2)
        self.label_13.setGeometry(QtCore.QRect(20, 360, 131, 31))
        self.label_13.setStyleSheet(_fromUtf8("color: rgb(255,255,255);\n"
"border: 1px solid black"))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.frame_3 = QtGui.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(30, 10, 231, 211))
        self.frame_3.setStyleSheet(_fromUtf8("background:  url();\n"
"border: 1px solid grey;\n"
"border-radius: 5px;\n"
""))
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.Joystick = QtGui.QCheckBox(self.frame_3)
        self.Joystick.setGeometry(QtCore.QRect(10, 60, 99, 22))
        self.Joystick.setStyleSheet(_fromUtf8("color: rgb(255,255,255);\n"
"border: 1px solid black"))
        self.Joystick.setObjectName(_fromUtf8("Joystick"))
        self.Wheel_Locomotion = QtGui.QCheckBox(self.frame_3)
        self.Wheel_Locomotion.setGeometry(QtCore.QRect(10, 100, 161, 22))
        self.Wheel_Locomotion.setStyleSheet(_fromUtf8("color: rgb(255,255,255);\n"
"border: 1px solid black"))
        self.Wheel_Locomotion.setObjectName(_fromUtf8("Wheel_Locomotion"))
        self.Arm_Gripper = QtGui.QCheckBox(self.frame_3)
        self.Arm_Gripper.setGeometry(QtCore.QRect(10, 140, 131, 22))
        self.Arm_Gripper.setStyleSheet(_fromUtf8("color: rgb(255,255,255);\n"
"border: 1px solid black"))
        self.Arm_Gripper.setObjectName(_fromUtf8("Arm_Gripper"))
        self.Science_Task = QtGui.QCheckBox(self.frame_3)
        self.Science_Task.setGeometry(QtCore.QRect(10, 180, 131, 22))
        self.Science_Task.setStyleSheet(_fromUtf8("color: rgb(255,255,255);\n"
"border: 1px solid black"))
        self.Science_Task.setObjectName(_fromUtf8("Science_Task"))
        self.label_5 = QtGui.QLabel(self.frame_3)
        self.label_5.setGeometry(QtCore.QRect(40, 20, 101, 21))
        self.label_5.setStyleSheet(_fromUtf8("color: rgb(255,255,255);\n"
"border: 1px solid black"))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label = QtGui.QLabel(self.frame_3)
        self.label.setGeometry(QtCore.QRect(120, 40, 68, 17))
        self.label.setStyleSheet(_fromUtf8("border: 1px solid black\n"
""))
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.frame_5 = QtGui.QFrame(self.centralwidget)
        self.frame_5.setGeometry(QtCore.QRect(650, 590, 311, 101))
        self.frame_5.setStyleSheet(_fromUtf8("background:  url();\n"
"border-radius: 5px;\n"
"background: url(\"/home/vaishnavi/Desktop/Anveshak.png\")"))
        self.frame_5.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_5.setObjectName(_fromUtf8("frame_5"))
        self.frame_4 = QtGui.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(30, 240, 231, 251))
        self.frame_4.setStyleSheet(_fromUtf8("background:  url();\n"
"border: 1px solid grey;\n"
"border-radius: 5px;\n"
""))
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.label_12 = QtGui.QLabel(self.frame_4)
        self.label_12.setGeometry(QtCore.QRect(10, 10, 181, 31))
        self.label_12.setStyleSheet(_fromUtf8("color: rgb(255,255,255);\n"
"border: 1px solid black"))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.battery_level_1 = QtGui.QProgressBar(self.frame_4)
        self.battery_level_1.setGeometry(QtCore.QRect(10, 50, 211, 25))
        self.battery_level_1.setStyleSheet(_fromUtf8("horizontal {\n"
"border: 1px solid black;\n"
"border-radius: 100px;\n"
"background-color: black;\n"
"margin-right: 4ex;\n"
"}\n"
""))
        self.battery_level_1.setProperty("value", 70)
        self.battery_level_1.setAlignment(QtCore.Qt.AlignCenter)
        self.battery_level_1.setObjectName(_fromUtf8("battery_level_1"))
        self.battery_level_2 = QtGui.QProgressBar(self.frame_4)
        self.battery_level_2.setGeometry(QtCore.QRect(10, 90, 211, 25))
        self.battery_level_2.setStyleSheet(_fromUtf8("background-color: rgb(85, 255, 0)"))
        self.battery_level_2.setProperty("value", 84)
        self.battery_level_2.setAlignment(QtCore.Qt.AlignCenter)
        self.battery_level_2.setObjectName(_fromUtf8("battery_level_2"))
        self.battery_level_3 = QtGui.QProgressBar(self.frame_4)
        self.battery_level_3.setGeometry(QtCore.QRect(10, 130, 211, 25))
        self.battery_level_3.setStyleSheet(_fromUtf8("border: 1px solid black;\n"
"border-radius: 5px;"))
        self.battery_level_3.setProperty("value", 75)
        self.battery_level_3.setAlignment(QtCore.Qt.AlignCenter)
        self.battery_level_3.setOrientation(QtCore.Qt.Horizontal)
        self.battery_level_3.setInvertedAppearance(False)
        self.battery_level_3.setObjectName(_fromUtf8("battery_level_3"))
        self.label_17 = QtGui.QLabel(self.frame_4)
        self.label_17.setGeometry(QtCore.QRect(10, 170, 191, 31))
        self.label_17.setStyleSheet(_fromUtf8("color: rgb(255,255,255);\n"
"border: 1px solid black"))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.signal_strength = QtGui.QProgressBar(self.frame_4)
        self.signal_strength.setGeometry(QtCore.QRect(10, 210, 211, 25))
        self.signal_strength.setStyleSheet(_fromUtf8("horizontal {\n"
"border: 1px solid gray;\n"
"border-radius: 3px;\n"
"background: white;\n"
"padding: 1px;\n"
"text-align: right;\n"
"margin-right: 4ex;\n"
"}\n"
"QProgressBar::chunk:horizontal {\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 0, stop: 0 rgb(85, 255, 0), stop: 1 white);\n"
"margin-right: 4px; /* space */\n"
"width: 10px;\n"
"}"))
        self.signal_strength.setProperty("value", 70)
        self.signal_strength.setTextVisible(False)
        self.signal_strength.setObjectName(_fromUtf8("signal_strength"))
        self.frame_6 = QtGui.QFrame(self.centralwidget)
        self.frame_6.setGeometry(QtCore.QRect(280, 420, 351, 241))
        self.frame_6.setStyleSheet(_fromUtf8("background:  url();\n"
"border: 1px solid grey;\n"
"border-radius: 5px;\n"
""))
        self.frame_6.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_6.setObjectName(_fromUtf8("frame_6"))
        self.latitude = QtGui.QPlainTextEdit(self.frame_6)
        self.latitude.setGeometry(QtCore.QRect(140, 150, 171, 61))
        self.latitude.setStyleSheet(_fromUtf8("background: url();\n"
"background-color: rgb(200, 200, 200);\n"
"border-radius: 5px;"))
        self.latitude.setObjectName(_fromUtf8("latitude"))
        self.longitude = QtGui.QPlainTextEdit(self.frame_6)
        self.longitude.setGeometry(QtCore.QRect(140, 70, 171, 61))
        self.longitude.setStyleSheet(_fromUtf8("background: url();\n"
"background-color: rgb(200, 200, 200);\n"
"border-radius: 5px;"))
        self.longitude.setObjectName(_fromUtf8("longitude"))
        self.label_9 = QtGui.QLabel(self.frame_6)
        self.label_9.setGeometry(QtCore.QRect(40, 80, 81, 31))
        self.label_9.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255) ;\n"
"border: 1px solid black\n"
""))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_7 = QtGui.QLabel(self.frame_6)
        self.label_7.setGeometry(QtCore.QRect(40, 10, 261, 31))
        self.label_7.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255) ;\n"
"border: 1px solid black\n"
""))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.frame_6)
        self.label_8.setGeometry(QtCore.QRect(40, 160, 61, 31))
        self.label_8.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255) ;\n"
"border: 1px solid black\n"
""))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1005, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Team Anveshak", None))
        self.run.setText(_translate("MainWindow", "RUN ROVER", None))
        self.button2.setText(_translate("MainWindow", "RUN LOGGER", None))
        self.label_6.setText(_translate("MainWindow", "W H E E L   V E L O C I T Y ", None))
        self.label_4.setText(_translate("MainWindow", "J O I N T  A N G L E S", None))
        self.label_18.setText(_translate("MainWindow", "Upper Link:", None))
        self.label_19.setText(_translate("MainWindow", "Shoulder Rotation:", None))
        self.label_20.setText(_translate("MainWindow", "Base Link:", None))
        self.label_11.setText(_translate("MainWindow", "S E N S O R   D A T A ", None))
        self.label_16.setText(_translate("MainWindow", "Radiation (CPS)", None))
        self.label_15.setText(_translate("MainWindow", "Altitude (m)", None))
        self.label_14.setText(_translate("MainWindow", "Temperature- Soil (K)", None))
        self.label_13.setText(_translate("MainWindow", "Soil Humidity (%)", None))
        self.Joystick.setText(_translate("MainWindow", "Joystick", None))
        self.Wheel_Locomotion.setText(_translate("MainWindow", "Locomotion", None))
        self.Arm_Gripper.setText(_translate("MainWindow", "Arm Gripper", None))
        self.Science_Task.setText(_translate("MainWindow", "Digger", None))
        self.label_5.setText(_translate("MainWindow", "N O D E S ", None))
        self.label_12.setText(_translate("MainWindow", "B A T T E R Y   L E V E L", None))
        self.label_17.setText(_translate("MainWindow", "S I G N A L   S T R E N G T H", None))
        self.label_9.setText(_translate("MainWindow", "Longitude:", None))
        self.label_7.setText(_translate("MainWindow", "G P S   C O O R D I N A T E S ", None))
        self.label_8.setText(_translate("MainWindow", "Latitude:", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

