# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 15:13:35 2023

@author: Matt0
"""
import tkinter as tk
class mixin:
    def data_entry(self, master): 
        self.master=master
        #establish and place startup labels
        self.instruct=tk.Label(master,text="Please enter your relevant pay info",justify="center")
        self.instruct.grid(row=1,column=0, columnspan = 4)
        
        self.askdate=tk.Label(master, text="Starting year:")
        self.askdate.grid(row=2, column=1)
        
        self.askstartpay=tk.Label(master, text="Starting salary $")
        self.askstartpay.grid(row=3,column=1)
        
        self.askcurrpay=tk.Label(master, text="Current salary $")
        self.askcurrpay.grid(row=4,column=1)
        
        #Error labels for call later
        self.baddate=tk.Label(master,text="The year provided is invalid", justify="center", fg="red")
        self.worddate=tk.Label(master,text="The year entered has non-numeric characters",justify="center", fg="red")
        self.badpay=tk.Label(master,text="The pay values must be numeric", \
                 justify="center", fg="red")
        self.timeout=tk.Label(master,text="There was a server error. Try again.", justify="center", fg="red")
    
    
        #entry fields +their locations
        self.e1 = tk.Entry(master)
        self.e1.grid(row=2,column=2, columnspan = 2)
        self.e2 = tk.Entry(master)
        self.e2.grid(row=3,column=2, columnspan = 2)
        self.e3 = tk.Entry(master)
        self.e3.grid(row=4,column=2, columnspan = 2)
        
        #buttons
        self.submit=tk.Button(master, text="Submit", command=self.mainscript).grid(row=7,column=2, columnspan = 2,pady=15, padx=5, )
        
        self.endit=tk.Button(master,text="Quit", command=master.destroy,).grid(row=7,column=0, columnspan = 2,pady=15, padx=5,sticky="e")
        