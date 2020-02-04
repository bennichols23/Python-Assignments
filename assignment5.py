import tkinter
import tkinter.messagebox

class GUI():
    def __init__(self):
        # Create Window
        self.main_window = tkinter.Tk()
        self.main_window.title("Services")

        # Define frames
        self.prices_frame = tkinter.Frame(self.main_window)
        self.quit_frame = tkinter.Frame(self.main_window)
        self.submit_frame = tkinter.Frame(self.main_window)

        # Create buttons
        self.oil = tkinter.IntVar()
        self.oilB = tkinter.Checkbutton(self.prices_frame, variable = self.oil, text="Oil change ---- $30.00")
        self.oilB.pack()

        self.rad = tkinter.IntVar()
        self.radB = tkinter.Checkbutton(self.prices_frame, variable = self.rad, text="Radiator flush ---- $40.00")
        self.radB.pack()

        self.tra = tkinter.IntVar()
        self.traB = tkinter.Checkbutton(self.prices_frame, variable = self.tra, text="Transmission flush ---- $100.00")
        self.traB.pack()

        self.ins = tkinter.IntVar()
        self.insB = tkinter.Checkbutton(self.prices_frame, variable = self.ins, text="Inspection ---- $35.00")
        self.insB.pack()

        self.muf = tkinter.IntVar()
        self.mufB = tkinter.Checkbutton(self.prices_frame, variable = self.muf, text="Muffler replacement ---- $200.00")
        self.mufB.pack()

        self.car = tkinter.IntVar()
        self.carB = tkinter.Checkbutton(self.prices_frame, variable = self.car, text="Carwash ---- $20.00")
        self.carB.pack()

        self.lub = tkinter.IntVar()
        self.lubB = tkinter.Checkbutton(self.prices_frame, variable = self.lub, text="Lube job ---- $20.00")
        self.lubB.pack()

        self.tir = tkinter.IntVar()
        self.tirB = tkinter.Checkbutton(self.prices_frame, variable = self.tir, text="Tire rotation ---- $20.00")
        self.tirB.pack()

        self.prices_frame.pack()

        self.quitB = tkinter.Button(self.quit_frame, text="Quit", command=self.main_window.destroy)
        self.quitB.pack()
        self.quit_frame.pack(side="left")

        self.submit = tkinter.Button(self.submit_frame, text="Submit", command=self.calcPrices)
        self.submit.pack()
        self.submit_frame.pack(side="right")

        tkinter.mainloop()

    def calcPrices(self):
        total = self.oil.get() * 30 + self.rad.get() * 40 + self.tra.get() * 100 + self.ins.get() * 35 + self.muf.get() * 200 + self.car.get() * 20 + self.lub.get() * 20 + self.tir.get() * 20
        tkinter.messagebox.showinfo('Total cost', 'Total Amount: $' + str(total) + '.00')

        if total >= 100:
            ask = tkinter.messagebox.askyesno("Apply a Discount", "You are eligible for a discount! Would you like to choose another discount service for free? If not, a $20 discount will be applied.")
            self.main_window.destroy
            if ask is True:
                print("oh hi")
                self.discounts_window = tkinter.Tk()
                self.discounts_window.title("Discount")
                self.discounts_frame = tkinter.Frame(self.discounts_window)
                self.submit_frame = tkinter.Frame(self.discounts_window)
                self.but = tkinter.IntVar()
                
                if(self.car.get() == 1):
                    self.lubB = tkinter.Radiobutton(self.discounts_frame, variable = self.but, value = 2, text="Lube job ---- $20.00")
                    self.lubB.pack()
                    self.tirB = tkinter.Radiobutton(self.discounts_frame, variable = self.but, value = 3, text="Tire rotation ---- $20.00")
                    self.tirB.pack()
                elif(self.lub.get() == 1):
                    self.carB = tkinter.Radiobutton(self.discounts_frame, variable = self.but, value = 1, text="Carwash ---- $20.00")
                    self.carB.pack()
                    self.tirB = tkinter.Radiobutton(self.discounts_frame, variable = self.but, value = 3, text="Tire rotation ---- $20.00")
                    self.tirB.pack()
                elif(self.tir.get() == 1):
                    self.carB = tkinter.Radiobutton(self.discounts_frame, variable = self.but, value = 1, text="Carwash ---- $20.00")
                    self.carB.pack()
                    self.lubB = tkinter.Radiobutton(self.discounts_frame, variable = self.but, value = 2, text="Lube job ---- $20.00")
                    self.lubB.pack()
                else:
                    self.carB = tkinter.Radiobutton(self.discounts_frame, variable = self.but, value = 1, text="Carwash ---- $20.00")
                    self.carB.pack()
                    self.lubB = tkinter.Radiobutton(self.discounts_frame, variable = self.but, value = 2, text="Lube job ---- $20.00")
                    self.lubB.pack()
                    self.tirB = tkinter.Radiobutton(self.discounts_frame, variable = self.but, value = 3, text="Tire rotation ---- $20.00")
                    self.tirB.pack()

                self.submit = tkinter.Button(self.submit_frame, text="Submit", command=self.discounts_window.destroy)
                self.submit.pack()
                self.submit_frame.pack(side="right")


                self.discounts_frame.pack()
                tkinter.mainloop()

            else:
                total=total-20
                tkinter.messagebox.showinfo('Total cost', 'Total Amount: $' + str(total) + '.00')

    
GUI()









