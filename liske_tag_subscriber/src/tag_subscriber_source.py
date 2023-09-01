#!/usr/bin/env python
import rospy
from liske_tag_subscriber.msg import tag_detection_msg
import rospy.numpy_msg
import csv
import numpy as np
import os

#-----------------------------------USER Defined Variables-------------------------------------------------

export_filepath = "/home/user/Desktop"
export_filename = "rpy_data.csv"

#----------------------------------------------------------------------------------------------------------

path = os.path.join(export_filepath,export_filename)

print("Node Started")


def callback(msg, args):
    print('tag detected')
    
    


    rollPitchYaw = msg.rpy_to_cam                   #importing data into rollpitchyaw variable
    
    list(rollPitchYaw)                              #converting it to list
    string_rpy = [str(i) for i in rollPitchYaw]     #turning all list entries into strings
    
    print('rpy = ', string_rpy)

    string_rpy = [string_rpy]                       #putting the list of strings into another list so it's appended correctly in the writer

    file = open(path,"a+")                          #opening the file at with the information specified above
    with file:
        write = csv.writer(file)        
        write.writerows(string_rpy)                 #writing our data to be appended at the bottom of the CSV


    

def listener():

    context1 = "any context you want to pass to the callback"
    context2 = "you can add more than 1 arg entry into the tuple"

    rospy.init_node('liske_tag_subscriber', anonymous=True)
    rospy.Subscriber('tag_detection_t', tag_detection_msg, callback, (context1,context2))
    rospy.spin()

if __name__ == '__main__':
    
    listener()


