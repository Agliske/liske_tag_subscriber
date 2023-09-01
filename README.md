# liske_tag_subscriber
ROS node to subscribe to the tag detection data and save it to CSV


Build Steps
1. follow the procedure to build a catkin workspace
2. download this repository, and put it in the "src" folder of the workspace. This repository is essentially a complete catkin package
3. in a terminal, cd to the python script and execute the command chmod +x * to change the mode of the python script to executable.
4. 

Execution Steps

1. start a roscore on voxl
2. start the voxl's liske_tag_subscriber ROS node
3. use the command export ROS_MASTER_URI=http://192.168.8.102:11311/ to add the ros master's IP address to the computer's environment (verify that it is the correct ip)
4. on PC rosrun liske_tag_subscriber tag_subscriber_source.py
