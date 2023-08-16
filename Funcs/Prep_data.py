# -*- coding: utf-8 -*-
import pandas as pd
import datetime

class mixin:
        def prep_data(self):
            for index,date in self.cleandate.items():
                if index==100:
                    self.cleandate[index]=str(datetime.date.today())
                else:
                    newdate=str(date)+"-01-01"
                    self.cleandate[index]=newdate
                    
            
            ##send them to PD
            self.cleanpay=pd.Series(self.cleanpay)
            self.cleandate=pd.Series(self.cleandate)
            self.paydata=pd.concat([self.cleanpay,self.cleandate],axis=1)
            self.paydata.columns=["pay","date"]
            
            self.paydata['date']=pd.to_datetime(self.paydata['date'])
            self.paydata['enddate']=self.paydata['date']-datetime.timedelta(weeks=28)
            self.paydata= self.paydata.set_index('date')
            self.paydata=self.paydata.sort_index()
            
            print(" \nIt's all ready to go captain\n")
            print(self.paydata.head())