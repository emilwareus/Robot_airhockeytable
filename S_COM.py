# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 07:09:03 2017

@author: Emil Wåreus
"""


import threading
import time

import serial

class S_COM(threading.Thread):
    
     def __init__(self, threadID, name, monitor):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.monitor = monitor
        
        
        
     def destroy(self):
         print(self.name, "Destryed")
         self.run = False
    
     def run(self):
         print("Starting ", self.name)
         self.run = True
         #self.monitor.INIT_COM(self) #TODO
         self.monitor.init_serial(self)
         
         while(self.run):
              #TODO
              self.monitor.try_serial(self)
              time.sleep(3)
         
            
    
  
        