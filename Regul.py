# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 08:49:34 2017

@author: Emil Wåreus
"""


import threading
from AI import AI

# construct the argument parse and parse the arguments
class Regul(threading.Thread):
    
    
    
    def __init__(self, threadID, name, monitor):
        
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.monitor = monitor
        self.AI = AI()
    
    
    def destroy(self):
        print(self.name , "Destroyed")
        self.run=False
        
        
    def run(self):
        
        print("Starting " + self.name)
        print("Press q to quit")
        self.run=True
        max_y, max_x = self.monitor.init_Regul()
        self.AI.init_AI(max_y, max_x)
        
        
         
          
        while(self.run & self.monitor.calibrated()): 
            xPuck ,yPuck, xPlayer, yPlayer = self.monitor.get_pos()
            set_y,set_x = self.AI.follow_puck(int(xPuck) ,int(yPuck), int(xPlayer), int(yPlayer))
            
            self.monitor.regulate(set_y,set_x)