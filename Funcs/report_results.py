# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 10:25:34 2023

@author: Matt0
"""
import seaborn as sns
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import numpy as np
import datetime

import Gui.resultswindow as resultswindow

class mixin(resultswindow.mixin):
    def report_results(self):
       
        
        second_window=self.results_window(self.master, self.paydata, self.inflationadjstart)
              
        
        ####Graph:
            
        sns.set_theme()
        
        plt.figure(figsize=(9, 5))
        
        #init the two plots
        line1=sns.lineplot(self.inflationadjstart,
                           x=self.inflationadjstart.index, 
                           y=self.inflationadjstart['adjusted'], 
                           label="What your starting pay is now worth")     
        
        line2=sns.lineplot(self.paydata,x=self.paydata.index,
                           y=self.paydata['pay'], 
                           label="What you've been getting paid",
                           marker="o")
        plt.show()
        
        line3=sns.lineplot(self.paydata,x=self.paydata.index,
                           y=self.paydata['deltapctstart'], 
                           #Title="How much your pay has changed since hiring, inflation adjusted (%)",
                           marker="o",)
        
        # line1.set_ylabel("pay")
        # for x, y in zip(self.inflationadjstart.index, self.inflationadjstart['unadjusted']):
        #  # the position of the data label relative to the data point can be adjusted by adding/subtracting a value from the x &/ y coordinates
        #  plt.text(x = x, # x-coordinate position of data label
        #  y = y-800, # y-coordinate position of data label, adjusted to be 150 below the data point
        #  s = '${:.0f}'.format(y), # data label, formatted to ignore decimals
        #  color = 'black') # set colour of line
        
        # for x, y in zip(df.index, df['adjusted']):
        #  # the position of the data label relative to the data point can be adjusted by adding/subtracting a value from the x &/ y coordinates
        #  plt.text(x = x, # x-coordinate position of data label
        #  y = y-800, # y-coordinate position of data label, adjusted to be 150 below the data point
        #  s = '${:.0f}'.format(y), # data label, formatted to ignore decimals
        #  color = 'black') # set colour of line
        
        canvas=FigureCanvasTkAgg(plt.gcf(), master=second_window)
        canvas.draw()
        canvas.get_tk_widget().grid(row=3,column=1,columnspan=3)
