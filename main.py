# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 11:38:23 2017
@author: Emil Wåreus
"""



from time import sleep
from Monitor import Monitor
from CV_AHR import CV_AHR #Class for computer vision
from S_COM import S_COM #Class for serial Communication
<<<<<<< HEAD
from Regul import Regul
=======
import time
>>>>>>> 49c6cb4e28a67970cdfcd0c881fdff0134dd3242
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
    sleep(5)

    CV_thread.start()
    sleep(2)
    COM_thread.start() #Function not properly impleentet
    
    Regul_thread.start()
    
    #root = Tk()
    #GUI = GUI(root , monitor = Monitor)
    
<<<<<<< HEAD
    sleep(60)
=======
    sleep(30)
>>>>>>> 49c6cb4e28a67970cdfcd0c881fdff0134dd3242

    COM_thread.destroy()    
    Regul_thread.destroy()

    