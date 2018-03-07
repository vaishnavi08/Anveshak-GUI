#!/bin/bash
. ~/catkin_ws/src/rover-control-master/devel/setup.bash
rosnode kill rosout gps_coord_publisher
