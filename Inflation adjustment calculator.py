# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 22:26:27 2023

@author: Matt0
"""
import pandas as pd
import requests
import numpy as np
import seaborn as sns
import datetime 
from fredapi import Fred
import matplotlib.pyplot as plt


######FUNCTIONS AND CLASSES#############
def getdate():
    startingyear=int(input("\n What year did you start working at your current employer?"))
    while (1930>startingyear) or (startingyear>datetime.date.today().year):
        startingyear=int(input("\nYou must enter your start year, between 1930 and 2023.  "))
    return startingyear

    

def checkpay(pay):
    pay=pay.replace('$',"")
    pay=pay.replace(',',"")
    while pay.isnumeric()==False:
            pay=input("\nThe pay needs to be entered as just the number, no words or symbols.  ")
    return pay

def collectdata():
    startingpay=int(checkpay(input("\n What was your annual salary when you started?  ")))
    endingpay=int(checkpay(input("\n What is your current annual salary?  ")))
    return startingpay,endingpay



class pay:
    def __init__(self,startpay,startdate,currpay):
        self.startpay=startpay
        self.startdate=startdate
        self.currpay=currpay
    
    def inflationadj(self):
        ###derive appropriate years:
        startingdate=str(self.startdate)+"/1/1"
        startingdateend=str(self.startdate)+"/3/1"
        #Current date
        today=datetime.date.today()
        todayformat=today.strftime('%m/%d/%y')
        
        monthprior=today-datetime.timedelta(weeks=16)

        ###ping API
        print(f"{self.startdate}, {self.startpay}")
        fred = Fred(api_key='48cd97443a16478ab526b8c298b2d829')
        initialinflation = fred.get_series('CPIAUCNS',startingdate,startingdateend)
        currentinflation = fred.get_series('CPIAUCNS',monthprior,today)
        
        ##calculate changes
        ###This pulls together inflation 3 months prior to the date and for january of the provided year.
        inflationadj=(self.startpay*(currentinflation.mean()/initialinflation.mean())).round(2)
        delta=(self.currpay-inflationadj).round(2)
        deltapct=(((self.currpay/inflationadj)-1)*100).round(2)
        
        #put into data frames: 
        dates=pd.to_datetime(pd.Series([startingdate, todayformat],name="dates"))
        adjusted=pd.Series([startingpay,inflationadj], name="adjusted").astype(int)
        unadjusted=pd.Series([startingpay, endingpay],name="unadjusted").astype(int)
        df=pd.concat([adjusted,unadjusted],axis=1).set_index(dates)
        pd.concat([dates,df],axis=1)
        
        return df,inflationadj,delta,deltapct
        
    def interpret(self,inflationadj, delta,deltapct):
        print(f"""\n\nBack in {self.startdate} you earned ${self.startpay}. If we converted that into {datetime.date.today().year} dollars, you would be making ${inflationadj} dollars! How's the {self.currpay} that you're earning look now?""")
    
        if delta<0:
            print(f"\n Compared to when you were hired, you've taken what amounts to a ${delta} or %{deltapct} pay cut.")
    
        elif delta>0:
            print(f"\n Compared to when you were hired, you've actually gotten a raise! Yay! Compared to when you were hired,you're making ${delta} or %{deltapct} more than when you were hired. Still, think how many years of experience you've got- I hope it's commensurate!")

    def graph(self,df):
                
        sns.set_theme()
        
        plt.figure(figsize=(10, 6))
        
        line1=sns.lineplot(df,x=df.index,
                           y=df['adjusted'], 
                           label="What your starting pay is now worth")
        
        line2=sns.lineplot(df,x=df.index,
                           y=df['unadjusted'], 
                           label="What you're currently being paid")
        
        line1.set_ylabel("pay")
        for x, y in zip(df.index, df['unadjusted']):
         # the position of the data label relative to the data point can be adjusted by adding/subtracting a value from the x &/ y coordinates
         plt.text(x = x, # x-coordinate position of data label
         y = y-800, # y-coordinate position of data label, adjusted to be 150 below the data point
         s = '${:.0f}'.format(y), # data label, formatted to ignore decimals
         color = 'black') # set colour of line
        
        for x, y in zip(df.index, df['adjusted']):
         # the position of the data label relative to the data point can be adjusted by adding/subtracting a value from the x &/ y coordinates
         plt.text(x = x, # x-coordinate position of data label
         y = y-800, # y-coordinate position of data label, adjusted to be 150 below the data point
         s = '${:.0f}'.format(y), # data label, formatted to ignore decimals
         color = 'black') # set colour of line
        
        plt.show()
        


###



###eventually these will e outmodded by the GUI.
startingdate=getdate()

startingpay,endingpay=collectdata()

user=pay(startingpay,startingdate,endingpay)

data, inflationadj,delta,deltapct=user.inflationadj()

user.interpret(inflationadj,delta,deltapct)

user.graph(data)

