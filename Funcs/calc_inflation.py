# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 07:56:23 2023

@author: Matt0
"""

import datetime 
from fredapi import Fred
import pandas as pd
from urllib.error import URLError
import requests
import Funcs.config as config
import time

class mixin: 
    def inflation_adj(self):
        self.timeout.grid_forget()
        
        fredkey=config.set_key()
        fred = Fred(api_key=fredkey)
        retry=0
        #inflation=pd.DataFrame()

        print("pinging API")
        while retry<=5:
            try:
                self.inflation=fred.get_series('CPIAUCNS', self.paydata.index[0], self.paydata.index[len(self.paydata)-1],name="inflation")
                break
            except URLError:
                print(retry)
                if retry>=5:
                    self.timeout.grid(row=96,column=0, columnspan = 4)
                    print("no connection happened")
                    break
                print("failed, trying again")
                time.sleep(2)
                retry+=1
                
        self.inflationadjstart=pd.DataFrame(self.paydata['pay'][0]*(self.inflation/self.inflation[0])).round(2)
        self.inflationadjstart=self.inflationadjstart.rename(columns={0:"adjusted"})
        #merge in the adjusted pay values when the value has a pay match.
        self.paydata=pd.merge(self.paydata, self.inflationadjstart, 
                              left_on=self.paydata.index, 
                              right_on=self.inflationadjstart.index)
        
        self.paydata=self.paydata.rename(columns={'key_0':"date" , 0:"adjusted"})
        self.paydata.set_index('date')
        
        #difference between pay at the time and the starting pay inflation adjusted. positive values= a raise. negative= a pay cut.
        self.paydata['delta']=self.paydata['pay']-self.paydata['adjusted']
        self.paydata['deltapctstart']=((self.paydata['pay']/self.paydata['adjusted']-1)*100).round(2)
        self.paydata.set_index('date')
        
        #convert to hourly pay assuming 40hrs a week 50 a year. 
        self.paydata['hourlyraw']=(self.paydata['pay']/50/40).round(2)
        self.paydata['hourlyadj']=(self.paydata['adjusted']/50/40).round(2)
        print(self.paydata)
        
        print("Yippee!")
        