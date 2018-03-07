from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import QObject, pyqtSignal, QThread
from finalgui import Ui_MainWindow
import sys
import os
import subprocess

actualData01 = [0,0,0]
actualData02 = [0,0,0]
actualData03 = [0,0,0]
actualData04 = [0,0,0]
actualData05 = [0,0,0]
actualData06 = [0,0,0]
actualData07 = [0,0,0]
actualData08 = [0,0,0]
actualData09 = [0,0,0]
actualData10 = [0,0,0]
actualData11 = [0,0,0]
actualData12 = [0,0,0]

class exampleApp(Ui_MainWindow):
    def __init__(self,MainWindow):
        self.setupUi(MainWindow)
        self.val =0
        self.Joystick.stateChanged.connect(self.Node_Joystick)
        self.Wheel_Locomotion.stateChanged.connect(self.Node_Wheel_Locomotion)
        self.Arm_Gripper.stateChanged.connect(self.Node_Arm_Gripper)
        self.Science_Task.stateChanged.connect(self.Node_Science_Task)
        #self.GPS.stateChanged.connect(self.Node_GPS)
        #self.Battery.stateChanged.connect(self.Node_Battery)
        self.run.clicked.connect(self.Run_Rover)

    def Run_Rover(self):
        # p = subprocess.Popen(['roscore'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        os.system("gnome-terminal")
        os.system("roscore")
    def Node_Joystick(self):
        if self.Joystick.isChecked():
            self.label.setText("J+")
            p = subprocess.Popen(['bash Run_Joystick.sh'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        else:
            self.label.setText("J-")
            p = subprocess.Popen(['bash Stop_Joystick.sh'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    def Node_Wheel_Locomotion(self):
        if self.Wheel_Locomotion.isChecked():
            self.label.setText("W+")
            p = subprocess.Popen(['bash Run_Wheel_Locomotion.sh'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        else:
            self.label.setText("W-")
            p = subprocess.Popen(['bash Stop_Wheel_Locomotion.sh'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    def Node_Arm_Gripper(self):
        if self.Arm_Gripper.isChecked():
            self.label.setText("A+")
            p = subprocess.Popen(['bash Run_Arm_Gripper.sh'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        else:
            self.label.setText("A-")
            p = subprocess.Popen(['bash Stop_Arm_Gripper.sh'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    def Node_Science_Task(self):
        if self.Science_Task.isChecked():
            self.label.setText("S+")
            p = subprocess.Popen(['bash Run_Science_Task.sh'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        else:
            self.label.setText("S-")
            p = subprocess.Popen(['bash Stop_Science_Task.sh'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    def Node_GPS(self):
        # if self.GPS.isChecked():
        #     self.label.setText("G+")
        #     p = subprocess.Popen(['bash Run_GPS.sh'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        # else:
        #     self.label.setText("G-")
        #     p = subprocess.Popen(['bash Stop_GPS.sh'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
         p = subprocess.Popen(['bash Run_GPS.sh'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    def Node_Battery(self):
        # if self.Battery.isChecked():
        #     self.label.setText("B+")
        #     p = subprocess.Popen(['bash Run_Battery.sh'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        # else:
        #     self.label.setText("B-")
        #     p = subprocess.Popen(['bash Stop_Battery.sh'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        p = subprocess.Popen(['bash Run_Battery.sh'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)



    def actualSearch(self):
        self.val = 0

def Wheel_velocities():
    data = open("wheel_vel_l.txt","r")
    actualData01[2] = actualData01[1]
    actualData01[1] = actualData01[0]
    actualData01[0] = data.readline()
    data.close()
    gui.Wheel_Velocity_Left.setPlainText(str(actualData01[2]))
    gui.Wheel_Velocity_Left.insertPlainText(str(actualData01[1]))
    gui.Wheel_Velocity_Left.insertPlainText("\n")
    gui.Wheel_Velocity_Left.insertPlainText(str(actualData01[0]))
    gui.Wheel_Velocity_Left.insertPlainText("\n")

    data2 = open("wheel_vel_r.txt","r")
    actualData02[2] = actualData02[1]
    actualData02[1] = actualData02[0]
    actualData02[0] = data2.readline()
    data2.close()
    gui.Wheel_Velocity_Right.setPlainText(str(actualData02[2]))
    gui.Wheel_Velocity_Right.insertPlainText(str(actualData02[1]))
    gui.Wheel_Velocity_Right.insertPlainText("\n")
    gui.Wheel_Velocity_Right.insertPlainText(str(actualData02[0]))
    gui.Wheel_Velocity_Right.insertPlainText("\n")

def Science_tasks():
    data = open("soil_temp.txt","r")
    actualData03[2] = actualData03[1]
    actualData03[1] = actualData03[0]
    actualData03[0] = data.readline()
    data.close()
    gui.Soil_temp.setPlainText(str(actualData03[2]))
    gui.Soil_temp.insertPlainText(str(actualData03[1]))
    gui.Soil_temp.insertPlainText("\n")
    gui.Soil_temp.insertPlainText(str(actualData03[0]))
    gui.Soil_temp.insertPlainText("\n")

    data2 = open("humidity.txt","r")
    actualData04[2] = actualData04[1]
    actualData04[1] = actualData04[0]
    actualData04[0] = data2.readline()
    data2.close()
    gui.Humidity.setPlainText(str(actualData04[2]))
    gui.Humidity.insertPlainText(str(actualData04[1]))
    gui.Humidity.insertPlainText("\n")
    gui.Humidity.insertPlainText(str(actualData04[0]))
    gui.Humidity.insertPlainText("\n")
    """
    data3 = open("atm_temp.txt","r")
    actualData05[2] = actualData05[1]
    actualData05[1] = actualData05[0]
    actualData05[0] = data3.readline()
    data3.close()
    gui.Atm_temp.setPlainText(str(actualData05[2]))
    gui.Atm_temp.insertPlainText(str(actualData05[1]))
    gui.Atm_temp.insertPlainText("\n")
    gui.Atm_temp.insertPlainText(str(actualData05[0]))
    gui.Atm_temp.insertPlainText("\n")
    """
    data4 = open("altitude.txt","r")
    actualData06[2] = actualData06[1]
    actualData06[1] = actualData06[0]
    actualData06[0] = data4.readline()
    data4.close()
    gui.Altitude.setPlainText(str(actualData06[2]))
    gui.Altitude.insertPlainText(str(actualData06[1]))
    gui.Altitude.insertPlainText("\n")
    gui.Altitude.insertPlainText(str(actualData06[0]))
    gui.Altitude.insertPlainText("\n")

    data5 = open("pressure.txt","r")
    actualData07[2] = actualData07[1]
    actualData07[1] = actualData07[0]
    actualData07[0] = data5.readline()
    data5.close()
    gui.Pressure.setPlainText(str(actualData07[2]))
    gui.Pressure.insertPlainText(str(actualData07[1]))
    gui.Pressure.insertPlainText("\n")
    gui.Pressure.insertPlainText(str(actualData07[0]))
    gui.Pressure.insertPlainText("\n")

def GPS_coords():
    data = open("gps_lat.txt","r")
    actualData08[2] = actualData08[1]
    actualData08[1] = actualData08[0]
    actualData08[0] = data.readline()
    data.close()
    gui.latitude.setPlainText(str(actualData08[2]))
    gui.latitude.insertPlainText(str(actualData08[1]))
    gui.latitude.insertPlainText("\n")
    gui.latitude.insertPlainText(str(actualData08[0]))
    gui.latitude.insertPlainText("\n")

    data2 = open("gps_long.txt","r")
    actualData09[2] = actualData09[1]
    actualData09[1] = actualData09[0]
    actualData09[0] = data2.readline()
    data2.close()
    gui.longitude.setPlainText(str(actualData09[2]))
    gui.longitude.insertPlainText(str(actualData09[1]))
    gui.longitude.insertPlainText("\n")
    gui.longitude.insertPlainText(str(actualData09[0]))
    gui.longitude.insertPlainText("\n")

def Battery():
    # data = open("battery1.txt","r")
    # bat1 = data.readline()
    # data.close()
    gui.battery_level_1.setValue(93)

    # data2 = open("battery2.txt","r")
    # bat2 = data2.readline()
    # data2.close()
    gui.battery_level_2.setValue(91)

    # data3 = open("battery3.txt","r")
    # bat3 = data3.readline()
    # data3.close()
    gui.battery_level_3.setValue(86)

    data4 = open("signal_strength.txt","r")
    bat4 = data4.readline()
    data4.close()
    gui.signal_strength.setValue(int(float(bat4)))

def Joint_Angles():
    data = open("angle1.txt","r")
    actualData10[2] = actualData10[1]
    actualData10[1] = actualData10[0]
    actualData10[0] = data.readline()
    data.close()
    gui.angle_1.setPlainText(str(actualData10[2]))
    gui.angle_1.insertPlainText(str(actualData10[1]))
    gui.angle_1.insertPlainText("\n")
    gui.angle_1.insertPlainText(str(actualData10[0]))
    gui.angle_1.insertPlainText("\n")

    data2 = open("angle2.txt","r")
    actualData11[2] = actualData11[1]
    actualData11[1] = actualData11[0]
    actualData11[0] = data2.readline()
    data2.close()
    gui.angle_2.setPlainText(str(actualData11[2]))
    gui.angle_2.insertPlainText(str(actualData11[1]))
    gui.angle_2.insertPlainText("\n")
    gui.angle_2.insertPlainText(str(actualData11[0]))
    gui.angle_2.insertPlainText("\n")

    data3 = open("angle3.txt","r")
    actualData12[2] = actualData12[1]
    actualData12[1] = actualData12[0]
    actualData12[0] = data3.readline()
    data3.close()
    gui.angle_3.setPlainText(str(actualData12[2]))
    gui.angle_3.insertPlainText(str(actualData12[1]))
    gui.angle_3.insertPlainText("\n")
    gui.angle_3.insertPlainText(str(actualData12[0]))
    gui.angle_3.insertPlainText("\n")

if(__name__ == "__main__"):
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    gui = exampleApp(MainWindow)
    MainWindow.show()
    gui.Node_GPS()
    gui.Node_Battery()
    def update_label():
        Wheel_velocities()
        Science_tasks()
        Joint_Angles()
        GPS_coords()
    def update_label2():
        Battery()
    timer = QtCore.QTimer()
    timer.timeout.connect(update_label)
    timer.start(100)
    timer1 = QtCore.QTimer()
    timer1.timeout.connect(update_label2)
    timer1.start(500)

    sys.exit(app.exec_())
