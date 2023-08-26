
import pandas as pd
import random as random
import json as json

class mixin:
    def save_user(self):
        print("trying to save?")
        tickvalue=self.pleasesave.get()
        if tickvalue==1:
            print("you want to save")
            #save new username
            if self.username.get() not in self.logins['account'].values:
                print("new user entered")
                account= self.username.get()
                password=self.password.get()
                #gen random ID that will be used as linkage point.
                
                newlogs=pd.DataFrame()
                password=pd.Series(password, name="password")
                account=pd.Series(account, name="account")
                
                newlogs=pd.concat([account,password], axis=1)
                
                self.logins=pd.concat([self.logins,newlogs],axis=0)
                self.logins=pd.concat([self.logins], axis=1)
                self.logins=self.logins.reset_index(drop=True)        
                self.logins.to_csv("logins.csv")
                
                ##Save the data
                newdata={}
                payentry={}
                dateentry={}
                payentry["pay"]=self.cleanpay
                dateentry["date"]=self.cleandate
                
                ##append the data in
                with open("userdata.json","r") as location: 
                    userdata=json.load(location)
                
                userdata[self.username.get()]=[payentry,dateentry]
                
                with open("userdata.json","w") as location:
                    json.dump(userdata,location)
                
                print("I think I saved the entries!")
            #append the entered login info, replace old data if it exists.

##          account exists, therefore we must confirm password permission to replace the old data.
            else:
                print("this username exists, demand password before changing")
                stored_password = self.logins['password'].loc[self.logins['account'] == self.username.get()].values[0]

                if str(self.password.get())==str(stored_password):
                    print("Matched!")
                    newdata={}
                    payentry={}
                    dateentry={}
                    payentry["pay"]=self.cleanpay
                    dateentry["date"]=self.cleandate
                    
                    ##append the data in
                    with open("userdata.json","r") as location: 
                        userdata=json.load(location)
                    
                    userdata[self.username.get()]=[payentry,dateentry]
                    
                    with open("userdata.json","w") as location:
                        json.dump(userdata,location)
                    
                    print("I think I saved the entries!")
                else:
                    self.badacct.grid(row=96,column=0, columnspan = 4)
                    return

            ##store the data
            

#    def save_data(self):
 #   