# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 22:38:52 2023

@author: Matt0
"""
import pandas as pd
import requests
import numpy as np
import seaborn as sns
import datetime 
from fredapi import Fred
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from urllib.error import URLError



###Planned features:
#1) Allow a tick box for "use the current year", which, when unticked, will let you enter a custom end year
#2) Allow entry of multiple years, as many as you want
#3) Add an option for a person taking a pay cut to generate an email template.
#4) Get it to upen the window in the middle of the screen both times.
#5) Log and store data entries, present a summary of those results.

class inflation_app:
    ##when initialized, establish the GUI
    def __init__(self ,master):
        self.master=master
    #establish and place startup labels
        self.instruct=tk.Label(master,text="Please enter your relevant pay info",justify="center")
        self.instruct.grid(row=1,column=0, columnspan = 4)
        
        self.askdate=tk.Label(master, text="Starting year:")
        self.askdate.grid(row=2, column=1)
        
        self.askstartpay=tk.Label(master, text="Starting salary $")
        self.askstartpay.grid(row=3,column=1)
        
        self.askcurrpay=tk.Label(master, text="Current salary $")
        self.askcurrpay.grid(row=4,column=1)
        
        #Error labels for call later
        self.baddate=tk.Label(master,text="The year provided is invalid", justify="center", fg="red")
        self.worddate=tk.Label(master,text="The year entered has non-numeric characters",justify="center", fg="red")
        self.badpay=tk.Label(master,text="The pay values must be numeric", \
                 justify="center", fg="red")
        self.timeout=tk.Label(master,text="There was a server error. Try again.", justify="center", fg="red")

        
        #entry fields +their locations
        self.e1 = tk.Entry(master)
        self.e1.grid(row=2,column=2, columnspan = 2)
        self.e2 = tk.Entry(master)
        self.e2.grid(row=3,column=2, columnspan = 2)
        self.e3 = tk.Entry(master)
        self.e3.grid(row=4,column=2, columnspan = 2)
        
        #buttons
        self.submit=tk.Button(master, text="Submit", command=self.mainscript).grid(row=7,column=2, columnspan = 2,pady=15, padx=5, )
        
        self.endit=tk.Button(master,text="Quit", command=master.destroy,).grid(row=7,column=0, columnspan = 2,pady=15, padx=5,sticky="e")

    def showit(self):
        print(self.e1.get())
        
    def checkdate(self):
        self.timeout.grid_forget()
        self.badpay.grid_forget()
        self.worddate.grid_forget()
        self.baddate.grid_forget()
        try:
            self.badpay.grid_forget()
            self.worddate.grid_forget()
            self.baddate.grid_forget()
            
            self.startdate=int(self.e1.get())
            
        except ValueError:

            error=True
            return error
        else:
            self.worddate.grid_forget()
            if (1930>self.startdate) or (self.startdate>datetime.date.today().year):
                self.baddate.grid(row=6,column=0, columnspan = 4)
                error=True
                return error
            else:
                self.baddate.grid_forget()
                
    def checkpay(self):
        try:
            self.worddate.grid_forget()
            self.baddate.grid_forget()
            self.startpay=int(self.e2.get().replace('$',"").replace(',',""))
            self.currpay=int(self.e3.get().replace('$',"").replace(',',""))
            return self.startpay, self.currpay
        
        except (TypeError,ValueError):
            self.badpay.grid(row=6,column=0, columnspan = 4)
            return None, None

        else:
            self.badpay.grid_forget()
            return self.startpay,self.currpay
        
    def mainscript(self):
        error=self.checkdate()
        if error==True:
            return
        else:
            startpay, currpay=self.checkpay()
        if startpay==None:
            return
        else:
            print("it worked! Sending to the calculator")
            df,inflationadj,delta,deltapct=self.inflation_adj()
            
            self.report_results(inflationadj, delta,deltapct,df)
            
        
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

        try:
            currentinflation = fred.get_series('CPIAUCNS',monthprior,today)
        except URLError: 
            try:
                currentinflation = fred.get_series('CPIAUCNS',monthprior,today)
            except:
                self.timeout.grid(row=6,column=0, columnspan = 4)

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
    
        
    def report_results(self, inflationadj, delta,deltapct, df):
        second_window = tk.Toplevel(runit)
        second_window.title("Results")
        
        # Add text to the second window
        
        #header=tk.Label(second_window,text="RESULTS:")
        #header.grid(row=0,column=0,columnspan=5)
        
        #make a general summary of the results
        general=tk.Label(second_window, text=f"""\n\nBack in {self.startdate} you earned ${self.startpay}. If we converted that into {datetime.date.today().year} dollars, \n you would be making ${inflationadj} dollars! How's the ${self.currpay} that you're earning look now?""")
        
        general.grid(row=1,column=1, columnspan=3)                 
        
        #customize the feedback
        if delta<0:
            tailored=tk.Label(second_window,text=f"\n Compared to when you were hired, you've taken what amounts to a ${delta} or a %{deltapct} reduction in your buying power compared to when you were hired.")
            tailored.grid(row=2,column=1,columnspan=3)
        elif delta>0:
            tailored=tk.Label(second_window,text=f"\n Compared to when you were hired, you've actually gotten a raise! Yay! \n Compared to when you were hired,you're making ${delta} or %{deltapct} more than when you were hired.\n Still, think how many years of experience you've got- I hope it's commensurate!")
            tailored.grid(row=2,column=1,columnspan=3)
        
        sayok=tk.Button(second_window,text="OK",command=second_window.destroy)
        sayok.grid(row=5, column=1,columnspan=3, rowspan=2, padx=15, pady=15)
        
        
        ####Graph:
            
        sns.set_theme()
        
        plt.figure(figsize=(9, 5))
        
        #init the two plots
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
        
        canvas=FigureCanvasTkAgg(plt.gcf(), master=second_window)
        canvas.draw()
        canvas.get_tk_widget().grid(row=3,column=1,columnspan=3)

runit=tk.Tk()
gui=inflation_app(runit)
runit.mainloop()