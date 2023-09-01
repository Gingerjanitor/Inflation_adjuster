import tkinter as tk

class RowManips:
    def add_row(self):
        #self.master=master
        #add the remove button if this is the first add:
        if self.rownumber==2:
            self.removebutton=tk.Button(self.master,text="Remove a year", command=self.remove_row)
            self.removebutton.grid(row=self.rowloc+96, column=2, columnspan=1, pady=5, padx=10, sticky="w")

        
        self.rownumber+=1
        self.rowloc+=1
        print(f"add {self.rownumber}")
        print(self.yearentryfields)

        ##new date field
        self.newdateentry=tk.Entry(self.master)
        self.yearentryfields[self.rownumber]=self.newdateentry
        self.newdateentry.grid(row=self.rowloc, column=0, columnspan=2, pady=5, padx=40)
        
        ##new pay field
        self.newpayentry=tk.Entry(self.master)
        self.payentryfields[self.rownumber]=self.newpayentry
        self.newpayentry.grid(row=self.rowloc, column=1, columnspan=2, pady=5, padx=60, sticky="e")
        
        #make teh remove button visible:
        
    
    def remove_row(self):
        print(f"try to remove {self.rownumber}")
        print(self.yearentryfields)
        if self.rownumber in self.yearentryfields.keys():
            print(self.rownumber)
            if self.rownumber>2:
                print("removing {self.rownumber}")
                
                ##delete the date field
                toremove=self.yearentryfields[self.rownumber]
                toremove.destroy()
                del self.yearentryfields[self.rownumber]
                
                ##delete the pay field
                toremove=self.payentryfields[self.rownumber]
                toremove.destroy()
                del self.payentryfields[self.rownumber]
               
                
                try:
                    #remove the stored data from the dictionaries and list
                    #print(self.cleandate)
                    #print(f'yearlist has {self.yearlist}, want to remove {self.cleandate[self.rownumber]}')
                    if self.cleandate[self.rownumber] in self.yearlist:
                        self.yearlist.remove(self.cleandate[self.rownumber])
                    if self.rownumber in self.cleandate.keys():
                        self.cleandate.pop(self.rownumber)
                    
                    #ditto for pay info
                    if self.rownumber in self.cleanpay.keys():
                        self.cleanpay.pop(self.rownumber)
                    if self.rownumber in self.payentryfields.keys():
                        self.payentryfields.pop(self.rownumber)
                
                except KeyError:
                    pass
                #allowing the key error through since it probably means they left a entry field blank, then deleted.
                #except KeyError:
                #    pass
                
                #decrement
                print(self.rownumber)
                self.rownumber-=1
                self.rowloc-=1
                print(self.rownumber)
                
            if self.rownumber==2:
                print(self.removebutton)
                print("want to remove the button")
                self.removebutton.destroy()
