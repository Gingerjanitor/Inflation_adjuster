# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 22:26:27 2023

@author: Matt0
"""

import pandas as pd
import requests
import numpy as np
import matplotlib.pyplot as plt
import datetime 
from fredapi import Fred

def takevalue(pay):
    pay=pay.replace('$',"")
    pay=pay.replace(',',"")
    while pay.isnumeric()==False:
            pay=input("\nThe pay needs to be entered as just the number, no words or symbols.  ")
    return pay

startingyear=int(input("\nWhat year did you start working at your current employer?  "))
while (1930>startingyear) or (startingyear>datetime.date.today().year):
    startingyear=int(input("\nYou must enter your start year, between 1930 and 2023.  "))

startingpay=int(takevalue(input("\n What was your annual salary when you started?  ")))
endingpay=int(takevalue(input("\n What is your current annual salary?  ")))


startingdate=str(startingyear)+"/1/1"
startingdateend=str(startingyear)+"/3/1"

#how get the year of the current date?
today=datetime.date.today()
todayformat=today.strftime('%m/%d/%y')

monthprior=today-datetime.timedelta(weeks=16)

###########make the query

fred = Fred(api_key='APIGOESHERE')
initialinflation = fred.get_series('CPIAUCNS',startingdate,startingdateend)
currentinflation = fred.get_series('CPIAUCNS',monthprior,today)

##calculate changes
inflationadj=(startingpay*(currentinflation.mean()/initialinflation.mean())).round(2)
delta=(endingpay-inflationadj).round(2)
deltapct=(((endingpay/inflationadj)-1)*100).round(2)

print(f"""\n\nBack in {startingyear} you earned ${startingpay}. If we converted that into {datetime.date.today().year} dollars, you would be making ${inflationadj} dollars! How's the {endingpay} that you're earning look now?""")

if delta<0:
    print(f"\n Compared to when you were hired, you've taken what amounts to a ${delta} or %{deltapct} pay cut.")

elif delta>0:
    print(f"\n Compared to when you were hired, you've actually gotten a raise! Yay! Compared to when you were hired,you're making ${delta} or %{deltapct} more than when you were hired. Still, think how many years of experience you've got- I hope it's commensurate!")



###This pulls together inflation 3 months prior to the date and for january of the provided year.



#########take the query reply and put it into a graphy highlighting start date, end date, and difference.
#summarize what their starting pay was and what its buying power is now
#Illustrate if they are making more or less than previously in a variety of graphs.

######If they are at a substantial loss, as them if they want to email Clarkson's presient, and prefill an angry email.

