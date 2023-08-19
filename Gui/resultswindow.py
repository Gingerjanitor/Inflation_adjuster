# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 15:37:08 2023

@author: Matt0
"""
import tkinter as tk
import datetime

class mixin:
    def results_window(self, runit):
        second_window = tk.Toplevel(runit)
        second_window.title("Results")
        
        header=tk.Label(second_window,text="Are you getting paid your worth?\n",anchor="center", font=('',20))
        header.grid(row=0, column=0,columnspan=3)
        
        # Add text to the second window
        multiline_text = f"""\n Back in {self.paydata['date'][0].year} you earned ${self.paydata['pay'][0]}. If we converted that into {self.paydata['date'][len(self.paydata)-1].year} dollars,
you would be making ${self.paydata['adjusted'][len(self.paydata)-1]}! How's the ${self.paydata['pay'][len(self.paydata)-1]} that you're earning look now?\n
The graphs on the right show your pay over time. For the top line, if the orange line goes over the blue line, you're making more than when you were hired.
If it's below, you're making less.\n If they are on top of each other, you haven't actually been getting raises at all, just small inflation adjustments \n
For the second graph, values above 0 indicate a raise relative to your start pay, values below 0 indicate a reduction in buying power. """
        
#make a general summary of the results
        general=tk.Label(second_window, text=multiline_text,
                         #width=100,
                         wraplength=500)
        
        general.grid(row=1,column=1)                 
        
        #customize the feedback
        if self.paydata['delta'][len(self.paydata)-1]<0:
            tailored=tk.Label(second_window,text=f"Compared to when you were hired, you've taken what amounts to a ${self.paydata['delta'][len(self.paydata)-1].round(2)} or a %{self.paydata['deltapctstart'][len(self.paydata)-1].round(2)} reduction in your buying power compared to when you were hired. Are you sure this job is worth it? \n \n Would you like to generate a template letter asking for a raise?",
                              #width=100,
                              wraplength=500)
            tailored.grid(row=2,column=1)
        elif self.paydata['delta'][len(self.paydata)-1]>0:
            tailored=tk.Label(second_window,text=f"Compared to when you were hired, you've actually gotten a raise! Yay! \n You're making ${self.paydata['delta'][len(self.paydata)-1].round(2)} or %{self.paydata['deltapctstart'][len(self.paydata)-1]} more than when you were hired.\n Still, think how many years of experience you've got- is the increase you got reflective of your experience? Would you like to generate a template letter asking for a raise?",
                             # width=100,
                              wraplength=500)
            tailored.grid(row=2,column=1)
        
        sayok=tk.Button(second_window,text="OK",command=second_window.destroy)
        sayok.grid(row=5, column=1,columnspan=3, rowspan=2, padx=15, pady=15)
        return second_window