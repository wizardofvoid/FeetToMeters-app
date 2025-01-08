from tkinter import *
from tkinter import ttk

class FeetToMeters:

    def __init__(self,root):
        root.title("Feet to Meter Converter")

        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(sticky=(N,E,S,W))

        self.feet = StringVar()
        FeetEntry = ttk.Entry(mainframe, textvariable=self.feet, width=10)
        FeetEntry.grid(column=2,row=1, sticky=S)

        ttk.Label(mainframe, text="feet").grid(column=3,row=1,sticky=S)
        ttk.Label(mainframe, text="is equivalent to:").grid(column=1, row=2, sticky=E)

        self.meters = StringVar()
        ttk.Label(mainframe, textvariable=self.meters).grid(column=2,row=2,sticky=N)
        ttk.Label(mainframe, text="meters").grid(column=3,row=2,sticky=W)

        ttk.Button(mainframe, text="Calculate", command=self.calculate).grid(column=3,row=3, sticky=E)
        for child in mainframe.winfo_children():
            child.grid(padx=10, pady=10)

        FeetEntry.focus()
        root.bind("<Return>",self.calculate)



    def calculate(self,*args):
        try:
            value = float(self.feet.get())
            self.meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
        except:
            pass

root = Tk()
FeetToMeters(root)
root.mainloop()