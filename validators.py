import datetime

class mixin:
    def checkdate(self):
        self.timeout.grid_forget()
        self.badpay.grid_forget()
        self.worddate.grid_forget()
        self.baddate.grid_forget()
        try:
            self.badpay.grid_forget()
            self.worddate.grid_forget()
            self.baddate.grid_forget()
            
            self.startdate=int(self.e1.get())
            
        except ValueError:

            error=True
            return error
        else:
            self.worddate.grid_forget()
            if (1930>self.startdate) or (self.startdate>datetime.date.today().year):
                self.baddate.grid(row=6,column=0, columnspan = 4)
                error=True
                return error
            else:
                self.baddate.grid_forget()
                
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