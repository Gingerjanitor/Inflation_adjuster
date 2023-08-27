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
            
        tempdate=loaded["newperson2"][1]['date']
        #resetting keys to int form
        self.cleandate={int(index):values for (index,values) in tempdate.items()}
        #must reset the 2023, since it gets cleaned up a little bit.
        self.cleandate[100]="2023"
        
        #doing same for pay data
        temppay=loaded["newperson2"][0]['pay']
        self.cleanpay={int(index):values for (index,values) in temppay.items()}
        
        ###
        self.e1.delete(0,tk.END)
        self.e1.insert(0, self.cleandate[0])
        self.e2.delete(0,tk.END)
        self.e2.insert(0, self.cleanpay[0])
        self.e3.delete(0,tk.END)
        self.e3.insert(0, self.cleanpay[100])
        print("loaded")

    
# =============================================================================
#     def genrows():
#         self.rownumber+=1
#         self.rowloc+=1
#         self.newpayentry=tk.Entry(self.master)
#         self.payentryfields[self.rownumber]=self.newpayentry
#         self.newpayentry.grid(row=self.rowloc, column=1, columnspan=2, pady=5, padx=60, sticky="e")
#         
# 
# =============================================================================


