# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 15:37:08 2023

@author: Matt0
"""
import tkinter as tk
import datetime
import Funcs.gen_letter
import Funcs.gen_letter as gen_letter



class mixin:
    def results_window(self, runit):
        second_window = tk.Toplevel(runit)
        second_window.title("Results")
        
        header=tk.Label(second_window,text="Are you getting paid your worth?\n",anchor="center", font=('',20))
        header.grid(row=0, column=0,columnspan=3)
        
        # Add text to the second window
        summarytxt = f"""\n Back in {self.paydata['date'][0].year} you earned ${self.paydata['pay'][0]}. If we converted that into {self.paydata['date'][len(self.paydata)-1].year} dollars, you would be making ${self.paydata['adjusted'][len(self.paydata)-1]}! How's the ${self.paydata['pay'][len(self.paydata)-1]} that you're earning look now?\n \n The graphs on the right show your pay over time. For the top graph, if the orange line goes over the blue line, you're making more than when you were hired. If it's below, you're making less. If they are on top of each other, you haven't actually been getting raises at all, just small inflation adjustments \n\n For the second graph, values above 0 indicate a raise relative to your start pay, values below 0 indicate a reduction in buying power."""
        

        
        #customize the feedback
        if self.paydata['delta'][len(self.paydata)-1]<0:
            tailored=f"""\n \n Compared to when you were hired, you've taken what amounts to a ${self.paydata['delta'][len(self.paydata)-1].round(2)} or a %{self.paydata['deltapctstart'][len(self.paydata)-1].round(2)} reduction in your buying power compared to when you were hired. Are you sure this job is worth it? \n \n Would you like to save a template letter asking for a raise?"""
            
        elif self.paydata['delta'][len(self.paydata)-1]>0:
            tailored=f"""\n\nCompared to when you were hired, you've actually gotten a raise! Yay! \n You're making ${self.paydata['delta'][len(self.paydata)-1].round(2)} or %{self.paydata['deltapctstart'][len(self.paydata)-1]} more than when you were hired.\n Still, think how many years of experience you've got- is the increase you got reflective of your experience?"""

        feedback=summarytxt+tailored

#make a general summary of the results
        summary=tk.Text(second_window,bg="#F0F0F0",bd=0, height=25, width=55,wrap=tk.WORD, font=("Calibri", 11)) 
        summary.insert(tk.END, feedback)
        
        summary.grid(row=1,column=1, rowspan=2, padx=5, pady=5)                 
        
        
        sayok=tk.Button(second_window,text="OK",command=second_window.destroy)
        sayok.grid(row=5, column=2,columnspan=1, rowspan=2, padx=15, pady=15)
        
        genletter=tk.Button(second_window, text="Click to save a letter", command=lambda: gen_letter.gen_letter(self.paydata)) 
        genletter.grid(row=5, column=1,columnspan=1, rowspan=2, padx=15, pady=15)
        
        return second_window