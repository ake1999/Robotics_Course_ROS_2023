#!/usr/bin/ python3
import roslib
import sys
import rospy
import cv2
import numpy as np
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError


class objectPosition:
    def __init__(self):
        self.bridge = CvBridge()
        self.image_pub = rospy.Publisher("/cv_edged_image", Image, queue_size=10)
        self.image_sub = rospy.Subscriber(
            "/camera/image", Image, self.objectDetection)

    def objectDetection(self, data):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
        except CvBridgeError as e:
            print(e)

        gray = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (11, 11), 0)

        edged = cv2.Canny(blurred, 30, 150)

        (cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE)
        cv_image_edged = cv_image.copy()
        cv2.drawContours(cv_image_edged, cnts, -1, (0, 255, 0), 2)
#        cv2.imshow("cv_image_edged", cv_image_edged)
#        cv2.waitKey(0)
        
        try:
            self.image_pub.publish(self.bridge.cv2_to_imgmsg(cv_image_edged, "bgr8"))
        except CvBridgeError as e:
            print(e)


def main(args):
    ob_po = objectPosition()
    rospy.init_node('object_detection', anonymous=True)
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")
        cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)
