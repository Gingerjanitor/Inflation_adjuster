# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 19:47:38 2023

@author: Matt0
"""
import pandas as pd
class mixin:
    def authenticate(self):
    
        
        #pwsalt=bcrypt.gensalt()
        #print("PWsalt")
        #print(pwsalt)
        #hashed_PW=bcrypt.hashpw(password.encode('utf-8'),pwsalt)
        #print(hashed_PW)
        self.badacct.grid_forget()
        self.logins=pd.read_csv("logins.csv")

        if self.username.get() in self.logins['account'].values:
            print("username matched")
            stored_password = self.logins['password'].loc[self.logins['account'] == self.username.get()].values[0]
            print(self.password.get())
            if str(self.password.get())==str(stored_password):
                print("Matched!")
                self.load_data()
        else:
            self.badacct.grid(row=98,column=0, columnspan = 4)
            print("The Username or Password does not match")
            return False