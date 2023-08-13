# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 15:13:35 2023

@author: Matt0
"""

import tkinter as tk
import datetime
import Gui.row_manips as row_manips

class mixin(row_manips.RowManips):
    def data_entry(self, master): 
        self.master=master
        
        ###setting this row tracker, which marks where the button stuff starts
        self.rowloc=3
        self.rownumber=0
        
        #establish and place startup labels
        self.instruct=tk.Label(master,text="Please enter your pay history. ",justify="center")
        self.instruct.grid(row=1,column=0, columnspan = 4)
        
        self.askdate=tk.Label(master, text="Year:")
        self.askdate.grid(row=2, column=0)
        
        self.askstartpay=tk.Label(master, text="Salary $")
        self.askstartpay.grid(row=2,column=2)
        
        self.curryear=tk.Label(master,text=f"{datetime.date.today().year}")
        self.curryear.grid(row=self.rowloc+25,column=0, pady=3)
        
        #self.askcurrpay=tk.Label(master, text="Current salary $")
        #self.askcurrpay.grid(row=4,column=2)
        
        #Error labels for call later
        self.baddate=tk.Label(master,text="The year provided is invalid", justify="center", fg="red")
        self.worddate=tk.Label(master,text="The year entered has non-numeric characters",justify="center", fg="red")
        self.badpay=tk.Label(master,text="The pay values must be numeric", \
                 justify="center", fg="red")
        self.timeout=tk.Label(master,text="There was a server error. Try again.", justify="center", fg="red")
    
        
        #####A tracker for the locations for both:
        self.payentryfields={}
        self.yearentryfields={}
            
        
        #entry fields +their locations
        #year entry
        self.e1 = tk.Entry(master)
        self.e1.insert(0, "(--Start year--)")
        self.e1.grid(row=3,column=0,pady=3)
        self.yearentryfields[self.rownumber]=self.e1
        
        #start pay entry
        self.e2 = tk.Entry(master)
        self.e2.insert(0,"(--Starting pay--)")
        self.e2.grid(row=3,column=2,pady=3)
        self.payentryfields[self.rownumber]=self.e2
        
        #current pay entry
        self.e3 = tk.Entry(master)
        self.e3.insert(0,"(--Current pay--)")
        self.e3.grid(row=self.rowloc+25,column=2, pady=3)
        
        #setting the rownumber absurdly high so that it doesn't get overwritten by new rows
        self.payentryfields[self.rownumber+100]=self.e3
        
        #this is for logging the current year
        self.yearentryfields[self.rownumber+100]=datetime.date.today().year
        
        #buttons
        self.submit=tk.Button(master, text="Submit", command=self.mainscript).grid(row=self.rowloc+99,column=0, columnspan=2)
        
        self.endit=tk.Button(master,text="Quit", command=master.destroy,).grid(row=self.rowloc+99,column=2,columnspan=2)
        
        self.rowadd=tk.Button(master,text="Add another year", command=self.add_row).grid(row=self.rowloc+98, column=0, columnspan=1, pady=15)
        
        ###maybe make this only show up if row number >0?
        self.rowadd=tk.Button(master,text="Remove a year", command=self.remove_row).grid(row=self.rowloc+98, column=2, columnspan=1, pady=15)
        
    
    # def add_row(self, master):
    #     #self.master=master
    #     self.rownumber+=1
    #     self.rowloc+=1
    #     self.newentry=tk.Entry(master)
    #     self.payentryfields[self.rownumber]=self.newentry
    #     self.newentry.grid(row=1)
        
