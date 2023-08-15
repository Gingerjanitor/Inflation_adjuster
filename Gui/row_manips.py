import tkinter as tk

class RowManips:
    def add_row(self):
        #self.master=master
        #add the remove button if this is the first add:
        if self.rownumber==0:
            self.removebutton=tk.Button(self.master,text="Remove a year", command=self.remove_row)
            self.removebutton.grid(row=self.rowloc+98, column=2, columnspan=1, pady=15)

        
        self.rownumber+=1
        self.rowloc+=1
        print(f"add {self.rownumber}")
        print(self.yearentryfields)

        ##new date field
        self.newdateentry=tk.Entry(self.master)
        self.yearentryfields[self.rownumber]=self.newdateentry
        self.newdateentry.grid(row=self.rowloc, column=0,pady=3)
        
        ##new pay field
        self.newpayentry=tk.Entry(self.master)
        self.payentryfields[self.rownumber]=self.newpayentry
        self.newpayentry.grid(row=self.rowloc, column=2,pady=3)
        
        #make teh remove button visible:
        
    
    def remove_row(self):
        print(f"try to remove {self.rownumber}")
        print(self.yearentryfields)
        if self.rownumber in self.yearentryfields.keys():
            if self.rownumber>0:
                print("removing {self.rownumber}")
                
                
                               
                
                ##delete the date field
                toremove=self.yearentryfields[self.rownumber]
                toremove.destroy()
                del self.yearentryfields[self.rownumber]
                
                ##delete the pay field
                toremove=self.payentryfields[self.rownumber]
                toremove.destroy()
                del self.payentryfields[self.rownumber]
               
                
                #remove the stored data from the dictionaries and list

                print(f'yearlist has {self.yearlist}, want to remote {self.cleandate[self.rownumber]}')
                if self.cleandate[self.rownumber] in self.yearlist:
                    self.yearlist.remove(self.cleandate[self.rownumber])
                if self.rownumber in self.cleandate.keys():
                    self.cleandate.pop(self.rownumber)
                
                #ditto for pay info
                if self.rownumber in self.cleanpay.keys():
                    self.cleanpay.pop(self.rownumber)
                if self.rownumber in self.payentryfields.keys():
                    self.payentryfields.pop(self.rownumber)
                #allowing the key error through since it probably means they left a entry field blank, then deleted.
                #except KeyError:
                #    pass
                
                #decrement
                self.rownumber-=1
                self.rowloc-=1
                
            if self.rownumber==0:
                print(self.removebutton)
                print("want to remove the button")
                self.removebutton.destroy()