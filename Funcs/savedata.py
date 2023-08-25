
import pandas as pd

class mixin:
    def save_user(self):
        print("trying to save?")
        tickvalue=self.pleasesave.get()
        if tickvalue==1:
            print("you want to save")
            account= self.username.get()
            password=self.password.get()
            newlogs=pd.DataFrame()
            password=pd.Series(password, name="password")
            account=pd.Series(account, name="account")
            newlogs=pd.concat([account,password], axis=1)

            #self.pd
            
            #self.logins[password][len(self.logins)]=password
            self.logins=pd.concat([self.logins,newlogs],axis=0)
            self.logins=self.logins.reset_index(drop=True)        
            self.logins.to_csv("logins.csv")
            print("GO TO BED")
#    def save_data(self):
 #   