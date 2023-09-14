#!/usr/bin/env python
import rospy
import random
from std_msgs.msg import Int32

def talker():
    pub = rospy.Publisher("Random_Number_2", Int32, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(1) # 10hz
    while not rospy.is_shutdown():
        number = random.randint(1, 100)
        number = 5
        rospy.loginfo(number)
        pub.publish(number)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
