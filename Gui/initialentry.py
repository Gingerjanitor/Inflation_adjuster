# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 15:13:35 2023

@author: Matt0
"""

import tkinter as tk
import datetime
import Gui.row_manips as row_manips
import Funcs.authentication as authentication

class mixin(row_manips.RowManips):
    def data_entry(self, master): 
        self.master=master
        self.master.geometry("+480-250")
        
        ###setting this row tracker, which marks where the button stuff starts
        self.rowloc=6
        self.rownumber=0
        
        #establish and place startup labels
        #username
        self.getname=tk.Label(master,text="Username:",justify="left",anchor="w")
        self.getname.grid(row=1, column=0)
        
        #password
        self.getpass=tk.Label(master,text="Password:",justify="left")
        self.getpass.grid(row=2, column=0)
        
        #solicit UN/Pass
        self.introduction=tk.Label(master,text="Please enter your name and password load your info or save it for the future",justify="center")
        self.introduction.grid(row=0,column=0, columnspan = 3)
        
        #solicit pay info
        self.instruct=tk.Label(master,text="Or, please enter your pay history anew.",justify="center")
        self.instruct.grid(row=4,column=0, columnspan = 3)
        
        #solicit year
        self.askdate=tk.Label(master, text="Year:")
        self.askdate.grid(row=5, column=0, columnspan=2,pady=5, padx=5, )
        
        #solicit salary
        self.askstartpay=tk.Label(master, text="Salary $")
        self.askstartpay.grid(row=5,column=2, columnspan=2, pady=5, padx=20, sticky="w")
        
        
        
        #self.askcurrpay=tk.Label(master, text="Current salary $")
        #self.askcurrpay.grid(row=4,column=2)
        
        #Error labels for call later
        self.badacct=tk.Label(master,text="User/password combo invalid", justify="center",fg="red")
        self.baddate=tk.Label(master,text="The year provided is invalid", justify="center", fg="red")
        self.worddate=tk.Label(master,text="The year entered has non-numeric characters",justify="center", fg="red")
        self.badpay=tk.Label(master,text="The pay values must be numeric", \
                 justify="center", fg="red")
        self.timeout=tk.Label(master,text="There was a server error. Try again.", justify="center", fg="red")
        self.outofsequence=tk.Label(master,text="The years must be in order", \
             justify="center", fg="red")
        
        ###entry fields
        #UN+Pass
        self.username=tk.Entry(master, justify="left",)
        self.username.grid(row=1,column=1,sticky="w")
        
        self.password=tk.Entry(master)
        self.password.grid(row=2,column=1, sticky="w")
        
        
        #year entry
        self.e1 = tk.Entry(master)
        self.e1.insert(0, "(--Start year--)")
        self.e1.grid(row=6,column=0, columnspan=2,)
        #establish behavior when clicked on, auto wipe contents
        self.e1.bind('<FocusIn>', lambda event: self.remove_initial_text(self.e1))
        self.yearentryfields[self.rownumber]=self.e1
        
        
        #autofill current date slot
        self.curryear=tk.Entry(master) 
        self.curryear.insert(0, f"{datetime.date.today().year}")
        self.curryear.grid(row=self.rowloc+25, columnspan=2, column=0, pady=5, padx=5,)
    
        #start pay entry
        self.e2 = tk.Entry(master)
        self.e2.insert(0,"(--Starting pay--)")
        self.e2.grid(row=6,column=1, columnspan=2, pady=5, padx=60, sticky="e")
        self.e2.bind('<FocusIn>', lambda event: self.remove_initial_text(self.e2))

        self.payentryfields[self.rownumber]=self.e2
        
        #current pay entry
        self.e3 = tk.Entry(master)
        self.e3.insert(0,"(--Current pay--)")
        self.e3.grid(row=self.rowloc+25,column=1, columnspan=2, pady=5, padx=60, sticky="e")
        self.e3.bind('<FocusIn>', lambda event: self.remove_initial_text(self.e3))

        #final pay entry field
        #setting the rownumber absurdly high so that it doesn't get overwritten by new rows
        self.payentryfields[self.rownumber+100]=self.e3
        
        #final year entry field
        #this is for logging the current year
        self.yearentryfields[self.rownumber+100]=self.curryear
        
        #buttons
        #this still needs a command so it does something.
        self.loadit=tk.Button(master, text="Load",command= self.authenticate)
        self.loadit.grid(row=2,column=2,sticky="nsew", padx=5, pady=3)
        
        self.saveit=tk.Checkbutton(master,text="Check to save entries", variable=self.pleasesave)
        self.saveit.grid(row=1,column=2, sticky="nsew", padx=5, pady=3)
        
        self.submit=tk.Button(master, text="Submit", command=self.mainscript).grid(row=self.rowloc+99,column=0, columnspan=2)
        
        self.endit=tk.Button(master,text="Quit", command=master.destroy,).grid(row=self.rowloc+99,column=1,columnspan=2, pady=5, padx=100, sticky="e")
        
        self.rowadd=tk.Button(master,text="Add another year", command=self.add_row).grid(row=self.rowloc+98, column=0, columnspan=2, pady=5, padx=60,)
        
        ###maybe make this only show up if row number >0?
        #self.rowadd=tk.Button(master,text="Remove a year", command=self.remove_row).grid(row=self.rowloc+98, column=2, columnspan=1, pady=15)
        
    def remove_initial_text(self, activated):
        if activated.get() == "(--Start year--)":
            activated.delete(0, tk.END)
        if activated.get() == "(--Starting pay--)":
            activated.delete(0, tk.END)
        if activated.get() == "(--Current pay--)":
            activated.delete(0, tk.END)
            

    # def add_row(self, master):
    #     #self.master=master
    #     self.rownumber+=1
    #     self.rowloc+=1
    #     self.newentry=tk.Entry(master)
    #     self.payentryfields[self.rownumber]=self.newentry
    #     self.newentry.grid(row=1)
        
