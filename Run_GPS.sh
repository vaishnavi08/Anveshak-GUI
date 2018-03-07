#!/bin/bash
. ~/catkin_ws/src/rover-control-master/devel/setup.bash
rosrun  fake_gps_coords publisher.py
