import datetime

class mixin:
    def checkdate(self):
        ##tick the submissioncount, since they pressed submit
        self.submissioncount+=1
        self.timeout.grid_forget()
        self.badpay.grid_forget()
        self.worddate.grid_forget()
        self.baddate.grid_forget()
        for index, yearentry in self.yearentryfields.items():
            #checking for if it was already entered by first atching index and then
            if index in self.cleandate.keys(): 
                try: 
                    #the values match- no point checking further..
                    print(f"current value is {self.cleandate[index]}, comparing to {int(yearentry.get())}")
                    if self.cleandate[index]==int(yearentry.get()):
                        continue
                    else:
                        print(f"i wanna remove {self.cleandate[index]} its different")
                        del self.yearlist[index]
                #the index was in there, but the value is different- it's either not int, or it's changed! Run the checks again.
                except:
                    #remove the value from the list tracker
                    print(f"i wanna remove {self.cleandate[index]} its not int")
                    #this manages the chance that you added a new row, caused an error, and then corrected
                    if len(self.yearlist)<=index:
                        del self.yearlist[index]
                    pass
            #this detects the current date, which alwys shows up in the 2nd slot of the dictionary, but must
            #appear at the end of the list later.
            if yearentry==datetime.date.today().year:
                continue
            #If they entered values, then added a row and more values, it would break.
            #This fixes it.

            
            if yearentry!=datetime.date.today().year:

                yearentry=yearentry.get()
                ###CHECK THAT IT IS INT
                try:
                    self.badpay.grid_forget()
                    self.worddate.grid_forget()
                    self.baddate.grid_forget()
                    
                    yearentry=int(yearentry)
                    
                except ValueError:
        
                    error=True
                    return error
                else:
                    ###CHECK THAT IT IS A REASONABLE DATE (non future, non pre 1930)
                    self.worddate.grid_forget()
                    if (1930>yearentry) or (yearentry>datetime.date.today().year):
                        self.baddate.grid(row=96,column=0, columnspan = 4)
                        error=True
                        return error
                    else:
                        #hide the error if there was one
                        self.baddate.grid_forget()
                        
                        if self.submissioncount==0:
                            #add the year value to a list to later check if they were entered sequentially)
                            self.yearlist.append(yearentry)
                            #update the dict to include the year of the tk stuff
                            self.cleandate[index]=yearentry
                            print(self.yearlist)
                        #these next two checks if it's not the first submission, as the ordering must be different.
                        #It also checks if the current year is in the list, since that can get broken if a person enters an invalid year.
                        
                        if self.submissioncount>0 & (datetime.date.today().year in self.yearlist):
                            #if they press submit a second time the stuff needs to go into the second to last slot.
                            self.yearlist.insert(index,yearentry)
                            
                            self.cleandate[index]=yearentry
                        #if they've hit submit, but they never got current year in the list.# fringe case.
                        elif self.submissioncount>0 & (datetime.date.today().year not in self.yearlist):
                            print("trying to fix this thing")
                            self.yearlist.insert(index,yearentry)
                            self.yearlist.append(datetime.date.today().year)
                            
        ##tack on the current date at the end of the list if it's not there.
        if datetime.date.today().year not in self.yearlist:
            self.yearlist.append(datetime.date.today().year)

            
        ###CHECK that dates are entered in linear sequence
        for year in self.yearlist:
            index=self.yearlist.index(year)
            if index!=0:
            #if the years are equal, or the current year is less than the prior 
            #year, we have a sequence entered out of order.
            
                if year<=self.yearlist[index-1]:
                    self.outofsequence.grid(row=96,column=0,columnspan=4)
                    return
        ###everything passed!
        print(self.yearentryfields)
                    
        
    def checkpay(self):
        for index, payentry in self.payentryfields.items():
            if index in self.cleanpay.keys():
                continue
            try:
                self.worddate.grid_forget()
                self.baddate.grid_forget()
                pay=int(payentry.get().replace('$',"").replace(',',""))
                self.payentryfields[index]=pay
            except (TypeError,ValueError):
                self.badpay.grid(row=6,column=0, columnspan = 4)
                self.error=True
                
            else:
                self.badpay.grid_forget()
        print(self.payentryfields)