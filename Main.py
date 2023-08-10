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

import Funcs.validators as validators
import Funcs.calc_inflation as calc_inflation
import Funcs.report_results as report_results
import Gui.initialentry as initialentry
import Gui.resultswindow as resultswindow

###Planned features:
#1) Allow a tick box for "use the current year", which, when unticked, will let you enter a custom end year
#2) Allow entry of multiple years, as many as you want
#3) Add an option for a person taking a pay cut to generate an email template.
#4) Get it to upen the window in the middle of the screen both times.
#5) Log and store data entries, present a summary of those results.

class inflation_app(validators.mixin,calc_inflation.mixin, report_results.mixin, initialentry.mixin, resultswindow.mixin):
    ##when initialized, establish the GUI
    def __init__(self ,master):
        self.master=master
        self.data_entry(master)
                

    def mainscript(self):
        error=self.checkdate()
        if error==True:
            return
        else:
            startpay, currpay=self.checkpay()
        if startpay==None:
            return
        else:
            print("it worked! Sending to the calculator")
            df,inflationadj,delta,deltapct=self.inflation_adj()
            
            self.report_results(inflationadj, delta,deltapct,df, self.master)


runit=tk.Tk()
gui=inflation_app(runit)
runit.mainloop()