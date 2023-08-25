# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 19:47:38 2023

@author: Matt0
"""
import pandas as pd
import bcrypt


def authenticate(logins, username,password):

    
    #pwsalt=bcrypt.gensalt()
    #print("PWsalt")
    #print(pwsalt)
    #hashed_PW=bcrypt.hashpw(password.encode('utf-8'),pwsalt)
    #print(hashed_PW)
    
    if username in logins['account'].values:
        print("username matched")
        stored_password = logins['password'].loc[logins['account'] == username].values[0]
        print(password)
        print(stored_password)
        if str(password)==str(stored_password):
            print("Matched!")
            #initiate a loading of the prior person's data
    else:
        print("The Username or Password does not match")
        return False


def register(username,password):
    pwsalt=bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), pwsalt)
   # pd.DataFrame([username,hashed_password, pwsalt],)
