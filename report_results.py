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


class mixin:
    def report_results(self, inflationadj, delta,deltapct, df, runit):
        second_window = tk.Toplevel(runit)
        second_window.title("Results")
        
        # Add text to the second window
        
        #make a general summary of the results
        general=tk.Label(second_window, text=f"""\n\nBack in {self.startdate} you earned ${self.startpay}. If we converted that into {datetime.date.today().year} dollars, \n you would be making ${inflationadj} dollars! How's the ${self.currpay} that you're earning look now?""")
        
        general.grid(row=1,column=1, columnspan=3)                 
        
        #customize the feedback
        if delta<0:
            tailored=tk.Label(second_window,text=f"\n Compared to when you were hired, you've taken what amounts to a ${delta} or a %{deltapct} reduction in your buying power compared to when you were hired.")
            tailored.grid(row=2,column=1,columnspan=3)
        elif delta>0:
            tailored=tk.Label(second_window,text=f"\n Compared to when you were hired, you've actually gotten a raise! Yay! \n Compared to when you were hired,you're making ${delta} or %{deltapct} more than when you were hired.\n Still, think how many years of experience you've got- I hope it's commensurate!")
            tailored.grid(row=2,column=1,columnspan=3)
        
        sayok=tk.Button(second_window,text="OK",command=second_window.destroy)
        sayok.grid(row=5, column=1,columnspan=3, rowspan=2, padx=15, pady=15)
        
        
        ####Graph:
            
        sns.set_theme()
        
        plt.figure(figsize=(9, 5))
        
        #init the two plots
        line1=sns.lineplot(df,x=df.index,
                           y=df['adjusted'], 
                           label="What your starting pay is now worth")
        
        line2=sns.lineplot(df,x=df.index,
                           y=df['unadjusted'], 
                           label="What you're currently being paid")
        
        line1.set_ylabel("pay")
        for x, y in zip(df.index, df['unadjusted']):
         # the position of the data label relative to the data point can be adjusted by adding/subtracting a value from the x &/ y coordinates
         plt.text(x = x, # x-coordinate position of data label
         y = y-800, # y-coordinate position of data label, adjusted to be 150 below the data point
         s = '${:.0f}'.format(y), # data label, formatted to ignore decimals
         color = 'black') # set colour of line
        
        for x, y in zip(df.index, df['adjusted']):
         # the position of the data label relative to the data point can be adjusted by adding/subtracting a value from the x &/ y coordinates
         plt.text(x = x, # x-coordinate position of data label
         y = y-800, # y-coordinate position of data label, adjusted to be 150 below the data point
         s = '${:.0f}'.format(y), # data label, formatted to ignore decimals
         color = 'black') # set colour of line
        
        canvas=FigureCanvasTkAgg(plt.gcf(), master=second_window)
        canvas.draw()
        canvas.get_tk_widget().grid(row=3,column=1,columnspan=3)
