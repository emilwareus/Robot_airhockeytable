# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 08:20:49 2017

@author: Emil Wåreus
"""

from collections import deque
import numpy as np
import cv2
import argparse
import imutils

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video",
	help="path to the (optional) video file")
ap.add_argument("-b", "--buffer", type=int, default=32,
	help="max buffer size")
args = vars(ap.parse_args())

cap = cv2.VideoCapture(1)


greenLower = (29, 86, 6)
greenUpper = (64, 255, 255)
 
pts = deque(maxlen=args["buffer"])
counter = 0
direction = ""


def get_fram():
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    

    frame = imutils.resize(frame, width=600)
    blurred = cv2.GaussianBlur(frame, (11, 11), 0)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # Our operations on the frame come here
    mask = cv2.inRange(hsv, greenLower, greenUpper)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)
     
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    
    center = None
    x, y = 0, 0
    # only proceed if at least one contour was found
	 # only proceed if at least one contour was found
    if len(cnts) > 0:
		 # find the largest contour in the mask, then use
		 # it to compute the minimum enclosing circle and
		 # centroid
        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
 
		 # only proceed if the radius meets a minimum size
        if radius > 10:
             cv2.circle(frame, (int(x), int(y)), int(radius),(0, 255, 255), 2)
             cv2.circle(frame, center, 5, (0, 0, 255), -1)
             pts.appendleft(center) 
   
    
    for i in np.arange(1, len(pts)):

        if pts[i - 1] is None or pts[i] is None:
            continue

             
        thickness = int(np.sqrt(args["buffer"] / float(i + 1)) * 2.5)
        cv2.line(frame, pts[i - 1], pts[i], (0, 0, 255), thickness)
 
    
    
    cv2.putText(frame, direction, (10, 30), cv2.FONT_HERSHEY_SIMPLEX,0.85, (0, 0, 255), 3)
    cv2.putText(frame, "X: {}, Y: {}".format(int(x), int(y)),
                (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX,
                0.35, (0, 0, 255), 1)
 
	# show the frame to our screen and increment the frame counter
    
    
    
    
    return frame, x, y
 
    # if the 'q' key is pressed, stop the loop
    
while(True):
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
    frame, x, y = get_fram()
    cv2.imshow("Frame", frame)
 
# cleanup the camera and close any open windows
cap.release()
cv2.destroyAllWindows()
 
'''
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

'''