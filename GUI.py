# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 17:04:11 2017

@author: Emil Wåreus
"""



from tkinter import*

import matplotlib
matplotlib.use("TkAgg")
#from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg









class GUI():
    
    def __init__(self, root, monitor): 
        
        self._monitor = monitor
        self.root=root
       
        
        #Size of window
        root.geometry("1010x600+0+0") 
        #Window title
        root.title("Lets play!!")
  
        
   
    

class GUI_Thread():
    
    def __init__(self, monitor):
        #Init GUI Thread 
        self.root = Tk()
        self.gui = GUI(self.root, monitor = monitor)
        #self.gui.regul.setGUI(self.gui)
        #self.gui.updateGraph()
        self.gui.root.mainloop()
        
    def run(self): 
        print("Closed GUI")
