# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 11:38:23 2017
@author: Emil Wåreus
"""



from time import sleep
from Monitor import Monitor
from CV_AHR import CV_AHR #Class for computer vision
from S_COM import S_COM #Class for serial Communication
#from GUI import GUI

from tkinter import*
#import pyserial



    
    


if __name__ == "__main__":
    
    #Make Threads

    CV_thread = CV_AHR(1, "Computer Vision Thread", monitor = Monitor)
    #COM_thread = S_COM(2, "Serial Communication Thread", monitor = Monitor)
    #Start Threads
    CV_thread.start()
    #COM_thread.start() #Function not properly impleentet
    
    #root = Tk()
    #GUI = GUI(root , monitor = Monitor)
    
    #sleep(20)

    #COM_thread.destroy()    
   

    