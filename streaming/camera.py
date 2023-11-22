from imutils.video import VideoStream
import imutils
import cv2, os, urllib.request
import numpy as np
from django.conf import settings

class RtspCam(object):
    def __init__(self):
        self.url = cv2.VideoCapture("rtsp://192.168.1.61:30000/../../CAM/001.mp4")
        self.frame_cnt = 0
        
    def __del__(self):
        cv2.destroyAllWindows()
        
    
    def get_frame(self):
        success, image = self.url.read()
        self.frame_cnt += 1
        if self.frame_cnt % 10 == 0:
            ret, jpeg = cv2.imencode('.jpg', image)
            self.frame_cnt = 0
            return jpeg.tobytes()
    '''
    def get_frame(self):
        success, image = self.url.read()
        resize = cv2.resize(image, (640, 480), interpolation=cv2.INTER_LINEAR)
        ret, jpeg = cv2.imencode('.jpg', resize)
        return jpeg.tobytes()
    '''