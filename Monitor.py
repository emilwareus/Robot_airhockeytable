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
    def init_CV(self, hsvL = (29, 86, 6), hsvU = (100, 255, 255), hsvLP = (100, 150, 30), hsvUP =(255, 255, 255)):
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
        
        self.HSVLowerPlayer = hsvLP
        self.HSVUpperPlayer = hsvUP
         
        self.pts = deque(maxlen=self.args["buffer"])
        self.ptsPlayer = deque(maxlen=self.args["buffer"])
        self.counter = 0
        self.direction = ""
        
        cv2.namedWindow("Frame")
        def get_mouse_click(event, x, y, flags, param):
            	if event == cv2.EVENT_LBUTTONDOWN:
                    self.xR = x
                    self.yR = y
                    
                    
        cv2.setMouseCallback("Frame", get_mouse_click)
        self.xR = 0
        self.yR = 0
        
        self.cap = cv2.VideoCapture(2) 
    
        self.xPuck = 0
        self.yPuck = 0
        self.xPlayer = 0
        self.yPlayer = 0
    	
  
    def draw_circle(event,x,y,flags,param):
        if event == cv2.EVENT_LBUTTONDBLCLK:
            cv2.circle(img,(x,y),100,(255,0,0),-1)
    
    def release_cap(self):
        self.cap.release()
        cv2.destroyAllWindows()
        
        
    def isOpen(self):
        return self.cap.isOpened()

    def get_frame(self):
        '''
        input: cap - cv2.VideoCapture object
        return: frame, xPuck, yPuck, xPlayer, yPlayer
        
        This method returns the image (frame) and the cordinates
        of the tracked object
        '''
        # Capture frame-by-frame
        self.ret, self.frame = self.cap.read()
        
    
        self.frame = imutils.resize(self.frame, width=600)
        self.blurred = cv2.GaussianBlur(self.frame, (11, 11), 0)
        self.hsv = cv2.cvtColor(self.frame, cv2.COLOR_BGR2HSV)
        
        # Our operations on the frame come here to find Puck
        self.mask = cv2.inRange(self.hsv, self.HSVLower, self.HSVUpper)
        self.mask = cv2.erode(self.mask, None, iterations=2)
        self.mask = cv2.dilate(self.mask, None, iterations=2)
         
        self.cnts = cv2.findContours(self.mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
        
        self.center = None
        self.xPuck, self.yPuck = 0, 0
        # only proceed if at least one contour was found 
        
        
        if len(self.cnts) > 0:
    		 # find the largest contour in the mask, then use
    		 # it to compute the minimum enclosing circle and
    		 # centroid
            self.c = max(self.cnts, key=cv2.contourArea)
            ((self.xPuck, self.yPuck), self.radius) = cv2.minEnclosingCircle(self.c)
            self.M = cv2.moments(self.c)
            
            self.center = (int(self.M["m10"] / self.M["m00"]), int(self.M["m01"] / self.M["m00"]))
     
    		 # only proceed if the radius meets a minimum size
            if self.radius > 10:
                 cv2.circle(self.frame, (int(self.xPuck), int(self.yPuck)), int(self.radius),(0, 255, 255), 2)
                 cv2.circle(self.frame, self.center, 5, (0, 0, 255), -1)
                 self.pts.appendleft(self.center) 
       
        
        for i in np.arange(1, len(self.pts)):
    
            if self.pts[i - 1] is None or self.pts[i] is None:
                continue
    
                 
            self.thickness = int(np.sqrt(self.args["buffer"] / float(i + 1)) * 2.5)
            cv2.line(self.frame, self.pts[i - 1], self.pts[i], (0, 0, 255), self.thickness)
     
        
        # Our operations on the frame come here to find Puck
        self.maskPlayer = cv2.inRange(self.hsv, self.HSVLowerPlayer, self.HSVUpperPlayer)
        self.maskPlayer = cv2.erode(self.maskPlayer, None, iterations=2)
        self.maskPlayer = cv2.dilate(self.maskPlayer, None, iterations=2)
         
        self.cntsPlayer = cv2.findContours(self.maskPlayer.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
        
        self.centerPlayer = None
        self.xPlayer, self.yPlayer = 0, 0
        # only proceed if at least one contour was found 
        
        
        if len(self.cntsPlayer) > 0:
    		 # find the largest contour in the mask, then use
    		 # it to compute the minimum enclosing circle and
    		 # centroid
            self.cP = max(self.cntsPlayer, key=cv2.contourArea)
            ((self.xPlayer, self.yPlayer), self.radiusPlayer) = cv2.minEnclosingCircle(self.cP)
            self.MP = cv2.moments(self.cP)
            
            self.centerPlayer = (int(self.MP["m10"] / self.MP["m00"]), int(self.MP["m01"] / self.MP["m00"]))
     
    		 # only proceed if the radius meets a minimum size
            if self.radiusPlayer > 10:
                 cv2.circle(self.frame, (int(self.xPlayer), int(self.yPlayer)), int(self.radiusPlayer),(0, 0, 255), 2)
                 cv2.circle(self.frame, self.centerPlayer, 5, (255, 0, 0), -1)
                 self.ptsPlayer.appendleft(self.centerPlayer) 
       
        
        for i in np.arange(1, len(self.ptsPlayer)):
    
            if self.ptsPlayer[i - 1] is None or self.ptsPlayer[i] is None:
                continue
    
                 
            self.thicknessPlayer = int(np.sqrt(self.args["buffer"] / float(i + 1)) * 2.5)
            cv2.line(self.frame, self.ptsPlayer[i - 1], self.ptsPlayer[i], (255, 0, 0), self.thicknessPlayer)
     
        
        
        
        #cv2.putText(self.frame, self.direction, (10, 30), cv2.FONT_HERSHEY_SIMPLEX,0.85, (0, 0, 255), 3)
        cv2.putText(self.frame, "Puck: X: {}, Y: {}".format(int(self.xPuck), int(self.yPuck)),
                    (10, self.frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX,
                    0.35, (0, 0, 255), 1)
        
        cv2.putText(self.frame, "Player: X: {}, Y: {}".format(int(self.xPlayer), int(self.yPlayer)),
                    (int(self.frame.shape[1]/2), self.frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX,
                    0.35, (0, 0, 255), 1)
     
        
        cv2.putText(self.frame, "Wanted: X: {}, Y: {}".format(int( self.xR), int(self.yR)),
                    (int(self.frame.shape[1]/4)*3, self.frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX,
                    0.35, (0, 0, 255), 1)
     
    
            
    	 # show the frame to our screen and increment the frame counter
  
        
        return self.frame, self.xPuck, self.yPuck, self.xPlayer, self.yPlayer 
    
    def init_serial(self):
        self.xPuck = 0
        self.yPuck = 0
        self.xPlayer = 0
        self.yPlayer = 0
        print("Init Serial")
        #self.ser = serial.Serial('COM3',  9600 , timeout=.1)
    
    def try_serial(self):
        #sendPos = str(self.yPlayer) + ':' + str(self.yR)
        #self.ser.write(str.encode(sendPos))
        #data = self.ser.readline()
       
        print((self.xPuck))
        
        
        
    
