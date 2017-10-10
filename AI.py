# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 08:51:15 2017

@author: Emil Wåreus
"""

class AI():
    
    #TODO
    def init_AI(self, max_y, max_x):
        
        self.max_y = max_y 
        self.max_x = max_x
        
        
    def follow_puck(self,xPuck ,yPuck, xPlayer, yPlayer):
        
        if((xPuck < 150) and (xPuck > 0)):
            set_x = xPuck
            set_y = yPuck
            
        else:
            set_x = 5
            set_y = int(self.max_y/2)
        
        print(" Y:",set_y, " X:",set_x, "xPuck", xPuck)
        return  set_y,set_x 
        