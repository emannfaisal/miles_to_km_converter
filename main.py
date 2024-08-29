from tkinter import *

def miles_to_km():
 miles = float(miles_input.get())
 km = miles * 1.60934
 kilometer_result_label.config(text=f"{km}")

window = Tk()
window.title("Mile to kilometer convertor")
window.config(padx = 25, pady=20,bg='lightblue')

miles_input = Entry(width= 10)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles",bg='blue')
miles_label.grid(column=2, row=0)

is_equal = Label(text="Is equal to: ",bg='lightblue')
is_equal.grid(column=0, row=1)

kilometer_result_label = Label(text = "0",bg='lightblue')
kilometer_result_label.grid(column=1, row=1)

kilometer_label = Label(text="Km",bg='blue')
kilometer_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate" , command=miles_to_km)
calculate_button.grid(column = 1, row = 2)
window.mainloop()