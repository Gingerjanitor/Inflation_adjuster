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

class mixin: 
    def inflation_adj(self):
        ###derive appropriate years:
        startingdate=str(self.startdate)+"/1/1"
        startingdateend=str(self.startdate)+"/3/1"
        #Current date
        today=datetime.date.today()
        todayformat=today.strftime('%m/%d/%y')
        
        monthprior=today-datetime.timedelta(weeks=16)
    
        ###ping API
        fred = Fred(api_key='48cd97443a16478ab526b8c298b2d829')
        try:
            initialinflation = fred.get_series('CPIAUCNS',startingdate,startingdateend)
        except URLError:
            try: 
                initialinflation = fred.get_series('CPIAUCNS',startingdate,startingdateend)
            except URLError:
                self.timeout.grid(row=6,column=0, columnspan = 4)
                return
        try:
            currentinflation = fred.get_series('CPIAUCNS',monthprior,today)
        except URLError: 
            try:
                currentinflation = fred.get_series('CPIAUCNS',monthprior,today)
            except URLError:
                self.timeout.grid(row=6,column=0, columnspan = 4)
                return
        ##calculate changes
        ###This pulls together inflation 3 months prior to the date and for january of the provided year.
        inflationadj=(int(self.startpay)*(currentinflation.mean()/initialinflation.mean())).round(2)
        delta=(int(self.currpay)-inflationadj).round(2)
        deltapct=(((int(self.currpay)/inflationadj)-1)*100).round(2)
        
        #put into data frames: 
        dates=pd.to_datetime(pd.Series([startingdate, todayformat],name="dates"))
        adjusted=pd.Series([int(self.startpay),inflationadj], name="adjusted").astype(int)
        unadjusted=pd.Series([int(self.startpay), int(self.currpay)],name="unadjusted").astype(int)
        df=pd.concat([adjusted,unadjusted],axis=1).set_index(dates)
        pd.concat([dates,df],axis=1)
        
        print("Yippee!")
        return df,inflationadj,delta,deltapct