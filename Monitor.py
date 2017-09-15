# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 17:17:22 2017

@author: Emil Wåreus
"""



from collections import deque
import numpy as np
import argparse
import imutils
import cv2
import serial

class Monitor():
     
    
    
    
    #These are the methods for the CV:
    def init_CV(self, hsvL = (29, 86, 6), hsvU = (64, 255, 255)):
        '''
        This method initializes the Computer Vision variables
        '''
        self.ap = argparse.ArgumentParser()
        self.ap.add_argument("-v", "--video",
                             help="path to the (optional) video file")
        self.ap.add_argument("-b", "--buffer", type=int, default=32,
                             help="max buffer size")
        self.args = vars(self.ap.parse_args())
        
        self.HSVLower = hsvL
        self.HSVUpper = hsvU
         
        self.pts = deque(maxlen=self.args["buffer"])
        self.counter = 0
        self.direction = ""
        
        
    def get_frame(self, cap):
        '''
        input: cap - cv2.VideoCapture object
        return: frame, x and y
        
        This method returns the image (frame) and the cordinates
        of the tracked object
        '''
        # Capture frame-by-frame
        self.ret, self.frame = cap.read()
        
    
        self.frame = imutils.resize(self.frame, width=600)
        self.blurred = cv2.GaussianBlur(self.frame, (11, 11), 0)
        self.hsv = cv2.cvtColor(self.frame, cv2.COLOR_BGR2HSV)
        # Our operations on the frame come here
        self.mask = cv2.inRange(self.hsv, self.HSVLower, self.HSVUpper)
        self.mask = cv2.erode(self.mask, None, iterations=2)
        self.mask = cv2.dilate(self.mask, None, iterations=2)
         
        self.cnts = cv2.findContours(self.mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
        
        self.center = None
        self.x, self.y = 0, 0
        # only proceed if at least one contour was found
    	 # only proceed if at least one contour was found
        if len(self.cnts) > 0:
    		 # find the largest contour in the mask, then use
    		 # it to compute the minimum enclosing circle and
    		 # centroid
            self.c = max(self.cnts, key=cv2.contourArea)
            ((self.x, self.y), self.radius) = cv2.minEnclosingCircle(self.c)
            self.M = cv2.moments(self.c)
            
            self.center = (int(self.M["m10"] / self.M["m00"]), int(self.M["m01"] / self.M["m00"]))
     
    		 # only proceed if the radius meets a minimum size
            if self.radius > 10:
                 cv2.circle(self.frame, (int(self.x), int(self.y)), int(self.radius),(0, 255, 255), 2)
                 cv2.circle(self.frame, self.center, 5, (0, 0, 255), -1)
                 self.pts.appendleft(self.center) 
       
        
        for i in np.arange(1, len(self.pts)):
    
            if self.pts[i - 1] is None or self.pts[i] is None:
                continue
    
                 
            self.thickness = int(np.sqrt(self.args["buffer"] / float(i + 1)) * 2.5)
            cv2.line(self.frame, self.pts[i - 1], self.pts[i], (0, 0, 255), self.thickness)
     
        
        
        cv2.putText(self.frame, self.direction, (10, 30), cv2.FONT_HERSHEY_SIMPLEX,0.85, (0, 0, 255), 3)
        cv2.putText(self.frame, "X: {}, Y: {}".format(int(self.x), int(self.y)),
                    (10, self.frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX,
                    0.35, (0, 0, 255), 1)
     
    	# show the frame to our screen and increment the frame counter

        return self.frame, self.x, self.y
    
    def init_serial(self):
    
        self.ser = serial.Serial('COM6',  9600 , timeout=.1)
    
    def try_serial(self):
        
        self.ser.write(b'F')
        data = self.ser.readline()
        print(data)
        
        
        
    
