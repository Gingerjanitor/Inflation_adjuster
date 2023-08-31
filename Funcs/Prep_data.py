# -*- coding: utf-8 -*-
import pandas as pd
import datetime

class mixin:
        def prep_data(self):
            print(self.cleandate)
            for index,date in self.cleandate.items():
                if len(str(date))>=5:
                    continue
                #if index==100:
                #    self.cleandate[index]=str(f"{datetime.date.today().year}"+"-1-1")
                else:
                    newdate=str(date)+"-1-1"
                    self.cleandate[index]=newdate
                    
            print(self.cleandate)
            ##send them to PD
            self.temppay=pd.Series(self.cleanpay)
            self.tempdate=pd.Series(self.cleandate)
            self.paydata=pd.concat([self.temppay,self.tempdate],axis=1)
            self.paydata.columns=["pay","date"]
            
            self.paydata['date']=pd.to_datetime(self.paydata['date'])
                                                                       
            self.paydata=self.paydata.sort_index()
            
            print(" \nIt's all ready to go captain\n")
            self.paydata= self.paydata.set_index('date')

            print(self.paydata.head())