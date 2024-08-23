from tkinter import *


window = Tk()
window.title("Mile to km Converter")
window.minsize(width=300, height=100)
window.config(padx=50, pady=50)



#do the calcualtion
def convertMilesToKiloMeters():
    """converts miles to kilometers"""
    miles = float(input.get())
    # print(miles)
    result = miles * 1.609
    resultLabel.config(text=result)
#textfield
input = Entry()
input.config(text="0")
input.grid(column=1, row=0)

#miles label
milesLabel = Label()
milesLabel.config(text="Miles")
milesLabel.grid(column=2, row=0)

#isEqualToLabel
isEqualToLabel = Label()
isEqualToLabel.config(text="is equal to")
isEqualToLabel.grid(column=0, row=1)

#resultLabel
resultLabel = Label()
resultLabel.config(text="0")
resultLabel.grid(column=1, row=1)

#kiloMeterLabel
kiloMeterLabel = Label()
kiloMeterLabel.config(text="Km")
kiloMeterLabel.grid(column=2, row=1)

#button for calcuate
calculateButton = Button()
calculateButton.config(text="Calculate", command=convertMilesToKiloMeters)
calculateButton.grid(column=1, row=2)





window.mainloop()