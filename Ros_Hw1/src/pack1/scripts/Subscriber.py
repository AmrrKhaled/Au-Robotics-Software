#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32

num_1 = 0
num_2 = 0
state_1 = 0
state_2 = 0

def callback_1(data):
    global num_1, state_1
    num_1 = data.data
    state_1 = 1

def callback_2(data):
    global num_2, state_2
    num_2 = data.data
    state_2 = 2

def output():
    global num_1, num_2, state_1, state_2

    if num_1 != 0 and num_2 != 0:
        result = num_1 + num_2
        rospy.loginfo(rospy.get_caller_id() + ": %d", result)
        num_1 = 0
        num_2 = 0
    if num_2 != 0 and state_2 == 2:
        rospy.loginfo(rospy.get_caller_id() + ": %d", num_2)
        state_2 = 0
        num_2 = 0
    if num_1 != 0 and state_1 == 1:
        rospy.loginfo(rospy.get_caller_id() + ": %d", num_1)
        state_1 = 0
        num_1 = 0
    

def listener():
    rospy.init_node('listener', anonymous=True)

    # Subscribe both topics to the callback function
    rospy.Subscriber("Random_Number_1", Int32, callback_1)
    rospy.Subscriber("Random_Number_2", Int32, callback_2)

    rate = rospy.Rate(1) 

    while not rospy.is_shutdown():
        output()
        rate.sleep()

if __name__ == '__main__':
   listener()


