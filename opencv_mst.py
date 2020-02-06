import cv2
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError




def gstreamer_pipeline (capture_width=1280, capture_height=720, display_width=640, display_height=480, framerate=30, flip_method=2) :   
	return ('nvarguscamerasrc auto-exposure=0 wbmode=5  ! ' 
	'video/x-raw(memory:NVMM), '
	'width=(int)%d, height=(int)%d, '
	'format=(string)NV12, framerate=(fraction)%d/1 ! '
	'nvvidconv flip-method=%d ! '
	'video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! '
	'videoconvert ! '
	'video/x-raw, format=(string)BGR ! appsink'  % (capture_width,capture_height,framerate,flip_method,display_width,display_height))

def show_camera():
	# To flip the image, modify the flip_method parameter (0 and 2 are the most common)
	print gstreamer_pipeline(flip_method=2)
	rospy.init_node('video_csi', anonymous=True)
	pub = rospy.Publisher('line', Image, queue_size=100)
	rate = rospy.Rate(30)
	bridge = CvBridge()
	cap = cv2.VideoCapture(gstreamer_pipeline(flip_method=0), cv2.CAP_GSTREAMER)
	if cap.isOpened():	
		
		while not rospy.is_shutdown():
			ret_val, img = cap.read();
			gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
			image_ros = bridge.cv2_to_imgmsg(gray, encoding="mono8")
                        pub.publish(image_ros)			
			
		cap.release()
		cv2.destroyAllWindows()
	else:
	        print 'kamera acilamadi ! opecv_mst dosyasina bak'


if __name__ == '__main__':
    show_camera()




