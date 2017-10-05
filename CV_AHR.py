# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 08:20:49 2017

@author: Emil Wåreus
"""


import cv2

import threading


# construct the argument parse and parse the arguments
class CV_AHR(threading.Thread):
    
    
    
    def __init__(self, threadID, name, monitor):
        
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.monitor = monitor
    
    
    def destroy(self):
        print(self.name , "Destroyed")
        self.run=False
        
        
    def run(self):
        
        print("Starting " + self.name)
        print("Press q to quit")
        self.run=True
        self.monitor.init_CV(self)
        
        cap = cv2.VideoCapture(2)  
          
        while(self.run): 
            
            key = cv2.waitKey(1) & 0xFF
            if key == ord("q"):
                self.destroy()
                
            if(cap.isOpened()):
                frame, xPuck, yPuck, xPuck, yPlayer = self.monitor.get_frame(self,cap=cap)
                cv2.imshow("Frame", frame)

        
        # cleanup the camera and close any open windows
        cap.release()
        cv2.destroyAllWindows()
 
