#!/usr/bin/env python
import rospy
from rover_msgs.msg import WheelVelocity
from rover_msgs.msg import SC_task
from rover_msgs.msg import ArmAngle
from rover_msgs.msg import Power
from rover_msgs.msg import GPS

import sys
class GUIsubscriber():
    def __init__(self):
        self.data = 0
    def callback_wheel(self,data):

        txtfile = open("wheel_vel_l.txt","w")
        txtfile.write(str(round(data.left,2)))
        txtfile.close()
        txtfile = open("wheel_vel_r.txt","w")
        txtfile.write(str(round(data.right,2)))
        txtfile.close()
    def callback_science(self,data):
        txtfile = open("soil_temp.txt","w")
        txtfile.write(str(data.Soil_temp))
        txtfile.close()
        txtfile = open("humidity.txt","w")
        txtfile.write(str(data.Soil_humi))
        txtfile.close()
        """
        txtfile = open("atm_temp.txt","w")
        txtfile.write(str(data.Atm_temp))
        txtfile.close()
        """
        txtfile = open("altitude.txt","w")
        txtfile.write(str(data.Altitude))
        txtfile.close()
        txtfile = open("pressure.txt","w")
        txtfile.write(str(data.Atm_press))
        txtfile.close()
    def callback_gps(self,data):
        txtfile = open("gps_lat.txt","w")
        txtfile.write(str(data.inst_lat))
        txtfile.close()
        txtfile = open("gps_long.txt","w")
        txtfile.write(str(data.inst_lng))
        txtfile.close()
    def callback_battery(self,data):
        txtfile = open("battery1.txt","w")
        txtfile.write(str(data.power_1))
        txtfile.close()
        txtfile = open("battery2.txt","w")
        txtfile.write(str(data.power_2))
        txtfile.close()
        txtfile = open("battery3.txt","w")
        txtfile.write(str(data.power_3))
        txtfile.close()
        txtfile = open("signal_strength.txt","w")
        txtfile.write(str(data.power_4))
        txtfile.close()

    def callback_angle(self,data):
        txtfile = open("angle1.txt","w")
        txtfile.write(str(round(data.angle_1,2)))
        txtfile.close()
        txtfile = open("angle2.txt","w")
        txtfile.write(str(round(data.angle_2,2)))
        txtfile.close()
        txtfile = open("angle3.txt","w")
        txtfile.write(str(round(data.angle_3,2)))
        txtfile.close()


    def subscribe(self):
        rospy.init_node('data_subscriber', anonymous=True)
        rospy.Subscriber("gps_coords",GPS,self.callback_gps)
        rospy.Subscriber("wheel_vel",WheelVelocity,self.callback_wheel)
        rospy.Subscriber("science_readings",SC_task,self.callback_science)
        rospy.Subscriber("battery_levels",Power,self.callback_battery)
        rospy.Subscriber("arm_angles",ArmAngle,self.callback_angle)
        rospy.spin()
if(__name__ == "__main__"):
    ABC = GUIsubscriber()
    ABC.subscribe()
