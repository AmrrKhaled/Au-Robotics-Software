!#/bin/bash

echo -n "Enter Workspace Path: "
read workspace_path
echo -n "Enter Workspace Name: "
read workspace_name
echo -n "Enter Package Name: "
read pack_name
mkdir -p "$HOME/$workspace_path/$workspace_name/src"
cd "$HOME/$workspace_path/$workspace_name/src"
catkin_init_workspace
cd ..
catkin_make
source devel/setup.bash
cd src
catkin_create_pkg $pack_name rospy std_msgs


