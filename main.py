# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 11:38:23 2017

@author: Emil Wåreus
"""

from CV_AHR import CV_AHR

from time import sleep

if __name__ == "__main__":
    
    CV_thread = CV_AHR(1, "Computer Vision Thread")
	#monitor = Monitor(2, "Monitor Thread")
	#monitor.start()
    CV_thread.start()
    
    sleep(20) #To destroy the thread
    
    CV_thread.destroy()
    