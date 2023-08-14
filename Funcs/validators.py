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
            print(f" my index is {index}")
            print(self.indexlog)
            if index in self.indexlog:
                print(self.indexlog)
                print(f"{index} value caused break")
                continue
            #this detects the current date, which alwys shows up in the 2nd slot of the dictionary, but must
            #appear at the end of the list later.
            if yearentry==datetime.date.today().year:
                self.lastvalue=yearentry
                self.lastindex=index
            #If they entered values, then added a row and more values, it would break.
            #This fixes it.

            
            if yearentry!=datetime.date.today().year:

                yearentry=yearentry.get()
                print(yearentry)
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
                        #add the intext to the list of indices
                        self.indexlog.append(index)
                        print(self.indexlog)
                        
                        if self.submissioncount==0:
                            #add the year value to a list to later check if they were entered sequentially)
                            self.yearlist.append(yearentry)
                            #update the dict to include the year of the tk stuff
                            self.yearentryfields[index]=yearentry
                            print(self.yearlist)
                            
                        if self.submissioncount>0:
                            #if they press submit a second time the stuff needs to go into the second to last slot.
                            print(self.yearlist)
                            self.yearlist.insert(len(self.yearlist)-1,yearentry)
                            
                            self.yearentryfields[index]=yearentry
                            print(f"after adding new thing {self.yearlist}")
                            
        ##tack on the current date at the end of the list, only for the first click.
        if self.submissioncount==0:
            self.yearlist.append(self.lastvalue)
            self.indexlog.append(self.lastindex)
            
        ###CHECK that dates are entered in linear sequence
        for year in self.yearlist:
            index=self.yearlist.index(year)
            if index!=0:
            #if the years are equal, or the current year is less than the prior 
            #year, we have a sequence entered out of order.
            
                if year<=self.yearlist[index-1]:
                    print("fuck they are out of sequence, abort!!!!")
                    self.outofsequence.grid(row=96,column=0,columnspan=4)
                    return
        ###everything passed!
        print(self.yearentryfields)
                    
        
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