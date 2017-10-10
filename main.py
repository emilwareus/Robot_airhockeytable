# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 11:38:23 2017
@author: Emil Wåreus
"""



from time import sleep
from Monitor import Monitor
from CV_AHR import CV_AHR #Class for computer vision
from S_COM import S_COM #Class for serial Communication

from Regul import Regul

import time

#from GUI import GUI

from tkinter import*
#import pyserial



    
    


if __name__ == "__main__":
    
    #Make Threads
    monitor = Monitor()
    
    CV_thread = CV_AHR(1, "Computer Vision Thread", monitor = monitor)
    COM_thread = S_COM(2, "Serial Communication Thread", monitor = monitor)
    Regul_thread = Regul(3, "Regulator Thread", monitor = monitor)
    
    #Start Threads
    sleep(2)

    CV_thread.start()
    sleep(10)
    COM_thread.start() #Function not properly impleentet
    
    Regul_thread.start()
    
    #root = Tk()
    #GUI = GUI(root , monitor = Monitor)
    
    while(CV_thread.is_open()):
        sleep(5)


    COM_thread.destroy()    
    Regul_thread.destroy()

    