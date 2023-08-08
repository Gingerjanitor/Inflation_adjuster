# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 10:51:28 2023

@author: Matt0
"""
import datetime
import tkinter as tk
startdate="shit"

def checkdate():
    badpay.grid_forget()
    worddate.grid_forget()
    baddate.grid_forget()
    try:
        badpay.grid_forget()
        worddate.grid_forget()
        baddate.grid_forget()
        
        startdate=int(e1.get())
        
    except ValueError:
        worddate.grid(row=6,column=0, columnspan = 4)
        error=True
        return error
    else:
        worddate.grid_forget()
        if (1930>startdate) or (startdate>datetime.date.today().year):
            baddate.grid(row=6,column=0, columnspan = 4)
            error=True
            return error
        else:
            baddate.grid_forget()
            
def checkpay():

    try:
        worddate.grid_forget()
        baddate.grid_forget()
        startpay=int(e2.get().replace('$',"").replace(',',""))
        currpay=int(e3.get().replace('$',"").replace(',',""))
    
    except (TypeError,ValueError):
        badpay.grid(row=6,column=0, columnspan = 4)
        return None, None

    else:
        badpay.grid_forget()
        return startpay,currpay

def validate():
    error=checkdate()
    if error==True:
        return
    else:
        startpay, currpay=checkpay()
    if startpay==None:
        print("The pay values are busted")
    
    
##INTERFACE##


master = tk.Tk()
#master.geometry("300x150")

tk.Label(master,text="Please enter your relevant pay info",justify="center").grid(row=1,column=0, columnspan = 4)
tk.Label(master, text="Starting year:").grid(row=2, column=1)
tk.Label(master, text="Starting salary $").grid(row=3,column=1)
tk.Label(master, text="Current salary $").grid(row=4,column=1)

baddate=tk.Label(master,text="The year provided is invalid", justify="center", fg="red")
worddate=tk.Label(master,text="The year entered has non-numeric characters",justify="center", fg="red")
badpay=tk.Label(master,text="The pay values must be numeric", \
         justify="center", fg="red")

e1 = tk.Entry(master)
e1.grid(row=2,column=2, columnspan = 2)
e2 = tk.Entry(master)
e2.grid(row=3,column=2, columnspan = 2)
e3 = tk.Entry(master)
e3.grid(row=4,column=2, columnspan = 2)

submit=tk.Button(master, text="Submit", command=validate).grid(row=7,column=0, columnspan = 2,pady=15, padx=5, )
#submit.grid(row=4,column=1)

endit=tk.Button(master,text="Quit", command=master.destroy,).grid(row=7,column=2, columnspan = 2,pady=15, padx=5,sticky="e")
#endit.grid(row=4,column=0)
#e1.grid(row=0, column=1)
#e2.grid(row=1, column=1)
#e3.grid(row=2, column=1)


master.mainloop()

