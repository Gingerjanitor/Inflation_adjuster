# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 21:47:21 2023

@author: Matt0
"""
import json
import tkinter as tk
class mixin:
    def load_data(self):
        with open("userdata.json","r") as location:
            loaded=json.load(location)
            
        tempdate=loaded[self.username.get()][1]['date']
        #resetting keys to int form
        self.cleandate={int(index):values for (index,values) in tempdate.items()}
        #must reset the 2023, since it gets cleaned up a little bit.
        self.cleandate[100]="2023"
        
        #doing same for pay data
        temppay=loaded[self.username.get()][0]['pay']
        self.cleanpay={int(index):values for (index,values) in temppay.items()}
        
        
        ##need to fully reset the row space and entries in case you load a new account that has fewer entries. 
        ###
        self.e1.delete(0,tk.END)
        self.e1.insert(0, self.cleandate[0])
        self.e2.delete(0,tk.END)
        self.e2.insert(0, self.cleanpay[0])
        self.e3.delete(0,tk.END)
        self.e3.insert(0, self.cleanpay[100])
        print("loaded")
        
        ##
        for index,value in self.cleanpay.items():
            if (index!=0) and (index!=100):
                self.genpayrows(value)
                self.gendaterows(self.cleandate[index])

    
    def genpayrows(self, value):
        self.rownumber+=1
        self.rowloc+=1
        
        self.newpayentry=tk.Entry(self.master)
        self.payentryfields[self.rownumber]=self.newpayentry
        self.newpayentry.grid(row=self.rowloc, column=1, columnspan=2, pady=5, padx=60, sticky="e")
        self.newpayentry.delete(0,tk.END)
        self.newpayentry.insert(0,value)
    
    def gendaterows(self,value):
        self.newdateentry=tk.Entry(self.master)
        self.yearentryfields[self.rownumber]=self.newdateentry
        self.newdateentry.grid(row=self.rowloc, column=0, columnspan=2, pady=5, padx=40)
        self.newdateentry.delete(0,tk.END)
        self.newdateentry.insert(0, value)

 


