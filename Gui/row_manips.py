import tkinter as tk

class RowManips:
    def add_row(self):
        #self.master=master
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
                self.rownumber-=1
                self.rowloc-=1

