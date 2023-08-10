# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 15:37:08 2023

@author: Matt0
"""
import tkinter as tk
import datetime

class mixin:
    def results_window(self, runit, inflationadj, delta, deltapct):
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
        return second_window