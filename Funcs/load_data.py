# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 21:47:21 2023

@author: Matt0
"""
import json
import tkinter as tk
class mixin:
    def load_data(self):
        ######clean space
        
        
        ##need to fully reset the row space and entries in case you load a new account that has fewer entries. 
        ###
        print("rownumber")
        print(self.rownumber)
        while self.rownumber>-1:
            ##delete the date field
            print(self.rownumber)
            toremove=self.yearentryfields[self.rownumber]
            toremove.destroy()
            del self.yearentryfields[self.rownumber]
            
            ##delete the pay field
            toremove=self.payentryfields[self.rownumber]
            toremove.destroy()
            del self.payentryfields[self.rownumber]
           
            
            try:
                #remove the stored data from the dictionaries and list
                #print(self.cleandate)
                #print(f'yearlist has {self.yearlist}, want to remove {self.cleandate[self.rownumber]}')
                if self.cleandate[self.rownumber] in self.yearlist:
                    self.yearlist.remove(self.cleandate[self.rownumber])
                if self.rownumber in self.cleandate.keys():
                    self.cleandate.pop(self.rownumber)
                
                #ditto for pay info
                if self.rownumber in self.cleanpay.keys():
                    self.cleanpay.pop(self.rownumber)
                if self.rownumber in self.payentryfields.keys():
                    self.payentryfields.pop(self.rownumber)
            
            except KeyError:
                pass
            #allowing the key error through since it probably means they left a entry field blank, then deleted.
            #except KeyError:
            #    pass
            
            #decrement
            print(self.rownumber)
            self.rownumber-=1
            self.rowloc-=1
            print(self.rownumber)
        
        
        
        ######laod it and prepare
        with open("userdata.json","r") as location:
            loaded=json.load(location)
            
        tempdate=loaded[self.username.get()][1]['date']
        #resetting keys to int form
        self.cleandate={int(index):values for (index,values) in tempdate.items()}
        #must reset the 2023, since it gets cleaned up a little bit.
        #self.cleandate[100]="2023"
        
        #doing same for pay data
        temppay=loaded[self.username.get()][0]['pay']
        self.cleanpay={int(index):values for (index,values) in temppay.items()}
        
        


        ########populate the rows
        # self.e1.delete(0,tk.END)
        # self.e1.insert(0, self.cleandate[0])
        # self.e2.delete(0,tk.END)
        # self.e2.insert(0, self.cleanpay[0])
        # self.e3.delete(0,tk.END)
        # self.e3.insert(0, self.cleanpay[100])
        # self.curryear.delete(0,tk.END)
        # self.curryear.insert(0, self.cleandate[100])
        # print("loaded")
        
        ##
        #self.rowloc=6
        #self.rownumber=-1
        
        for index,value in self.cleanpay.items():
            self.genpayrows(value)
            self.gendaterows(self.cleandate[index])
            if self.rownumber<len(self.cleanpay.items())-2:
                self.rownumber+=1
                self.rowloc+=1
        print("rownum after loading")
        print(self.rownumber)
    def genpayrows(self, value):
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

 


