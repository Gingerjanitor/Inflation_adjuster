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
       
        #self.paydata, self.inflationadjstart
        second_window=self.results_window(self.master)
              
        
        ####Graph:
            
        sns.set_theme()
        fig,axes=plt.subplots(2,1, figsize=(8,5))
        
        #init the two plots
        line1=sns.lineplot(self.inflationadjstart,
                           x=self.inflationadjstart.index, 
                           y=self.inflationadjstart['adjusted'], 
                           label="What your starting pay is now worth",
                           ax=axes[0])     
        line1.set(title="What you've been paid vs where you started")
        line1.set_ylabel("Pay in $")
        line1.xaxis.set_visible(False)
        
        line2=sns.lineplot(self.paydata,x=self.paydata['date'],
                           y=self.paydata['pay'], 
                           label="What you've been getting paid",
                           ax=axes[0],
                           marker="o")
        line2.legend(loc="lower right", bbox_to_anchor=(1,-.25))

        line3=sns.lineplot(self.paydata,x=self.paydata['date'],
                           y=self.paydata['deltapctstart'], 
                           #Title="How much your pay has changed since hiring, inflation adjusted (%)",
                           marker="o",
                           label='The % your pay has changed since 2016',
                           ax=axes[1])
        line3.set_ylabel("% change since 2016")
        line3.legend(loc="lower right")
        
        canvas=FigureCanvasTkAgg(plt.gcf(), master=second_window)
        canvas.draw()
        canvas.get_tk_widget().grid(row=1,column=2,rowspan=2)
