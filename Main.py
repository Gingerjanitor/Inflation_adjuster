# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 22:38:52 2023

@author: Matt0
"""
import pandas as pd
import requests
import numpy as np
import seaborn as sns
import datetime 
from fredapi import Fred
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from urllib.error import URLError

import Funcs.Prep_data as prep_data
import Funcs.validators as validators
import Funcs.calc_inflation as calc_inflation
import Funcs.report_results as report_results
import Gui.initialentry as initialentry
import Gui.resultswindow as resultswindow

###Planned features:
    
#2) Allow entry of multiple years, as many as you want
#3) Add an option for a person taking a pay cut to generate an email template.
#4) Get it to upen the window in the middle of the screen both times.
#5) Log and store data entries, present a summary of those results.
#6) a reset all button that restarts main

class inflation_app(validators.mixin, 
                    calc_inflation.mixin, 
                    report_results.mixin, 
                    initialentry.mixin, 
                    resultswindow.mixin,
                    prep_data.mixin):
    ##when initialized, establish the GUI
    def __init__(self ,master):
        self.master=master
        self.data_entry(master)
        self.yearlist=[]
        self.submissioncount=-1
        self.error=False
        self.cleanpay={}
        self.cleandate={}
        self.inflation=pd.DataFrame()
        
    def mainscript(self):
        error=self.checkdate()
        #janky, but this ensures lastvalue is always added at the very end of everything.
        #self.yearlist.append(self.lastvalue)
        #self.indexlog.append(self.lastindex)
        print(self.yearlist)
        if error==True:
            return
        else:
             self.checkpay()
        if self.error==True:
            return
        else:
            self.prep_data()
            self.inflation_adj()
            
            self.report_results()


runit=tk.Tk()
runit.eval('tk::PlaceWindow . center')
gui=inflation_app(runit)
runit.mainloop()