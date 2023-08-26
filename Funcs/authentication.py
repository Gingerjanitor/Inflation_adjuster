# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 19:47:38 2023

@author: Matt0
"""
import pandas as pd
import bcrypt

class mixin:
    def authenticate(self):
    
        
        #pwsalt=bcrypt.gensalt()
        #print("PWsalt")
        #print(pwsalt)
        #hashed_PW=bcrypt.hashpw(password.encode('utf-8'),pwsalt)
        #print(hashed_PW)
        self.badacct.grid_forget()

        if self.username.get() in self.logins['account'].values:
            print("username matched")
            stored_password = self.logins['password'].loc[self.logins['account'] == self.username.get()].values[0]

            if str(self.password.get())==str(stored_password):
                print("Matched!")
                #initiate a loading of the prior person's data
        else:
            self.badacct.grid(row=96,column=0, columnspan = 4)
            print("The Username or Password does not match")
            return False
    
    
    def register(username,password):
        pwsalt=bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), pwsalt)
       # pd.DataFrame([username,hashed_password, pwsalt],)
