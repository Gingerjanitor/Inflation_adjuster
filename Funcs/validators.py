import datetime
import pandas as pd

class mixin:
    def checkdate(self):
        ##tick the submissioncount, since they pressed submit
        self.submissioncount+=1
        self.timeout.grid_forget()
        self.badpay.grid_forget()
        self.worddate.grid_forget()
        self.baddate.grid_forget()
        self.badacct.grid_forget()
        
        ##restart the cleaned entry of the year fields so a resubmission nukes the dictionary.
        
        self.cleandate={}
        
        for index, yearentry in self.yearentryfields.items():

            print(self.yearentryfields)
            yearentry=yearentry.get()
            ###CHECK THAT IT IS INT
            try:
                yearentry=int(yearentry)
                #if no, fly error
            except ValueError:
                error=True
                self.worddate.grid(row=98,column=0, columnspan = 4)
                return error
            else:
            ###CHECK THAT IT IS A REASONABLE DATE (non future, non pre 1930)
                
                if (1930>yearentry) or (yearentry>datetime.date.today().year):
                    self.baddate.grid(row=98,column=0, columnspan = 4)
                    error=True
                    return error
                else:
                    #hide the error if there was one
                    self.baddate.grid_forget()
                    self.yearlist.append(yearentry)
                    self.cleandate[index]=yearentry
            
            print("I GOT THROUGH A CHECK!")
            ############
            
        ###CHECK that dates are entered in linear sequence
        for year in self.yearlist:
            index=self.yearlist.index(year)
            if index!=0:
            #if the years are equal, or the current year is less than the prior 
            #year, we have a sequence entered out of order.
                print(self.yearlist[index-1])
                if year<=self.yearlist[index-1]:
                    self.outofsequence.grid(row=96,column=0,columnspan=4)
                    return
        ###everything passed!
        print("\nthese are the years entered\n")
        print(self.yearlist)
        print(self.cleandate)
                    
        
    def checkpay(self):
        print(self.payentryfields)
        for index, payentry in self.payentryfields.items():
            
            if index in self.cleanpay.keys():
            
                try: 
                    #the values match- no point checking further..
                    print(f"current value is {self.cleanpay[index]}, comparing to {int(payentry.get())}")
                    
                    if self.cleanpay[index]==int(payentry.get()):
                        continue
                    
                    else:
                        print(f"i wanna remove {self.cleanpay[index]} its different")
                        self.cleanpay.pop(index)
                        
                #the index was in there, but the value is different- it's either not int, or it's changed! Run the checks again.
                except:
                    #remove the value from the list tracker
                    print(f"i wanna revalidate {self.cleanpay[index]} its not int")
                    pass
            
            try:
                self.worddate.grid_forget()
                self.baddate.grid_forget()
                pay=int(payentry.get().replace('$',"").replace(',',""))
                
                ##This weeds out the final value/current year entry
               # if index==100:
               #     self.lastpay=pay
               # else:
                self.cleanpay[index]=pay
            except (TypeError,ValueError):
                self.badpay.grid(row=96,column=0, columnspan = 4)
                self.error=True
                
            else:
                self.badpay.grid_forget()
        #self.cleanpay[100]=self.lastpay
        print(self.cleanpay)