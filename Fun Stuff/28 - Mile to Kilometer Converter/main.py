from tkinter import *

window = Tk()
window.title("28 - Mile to Kilometer Converter")
window_width = 500
window_height = 100
window.wm_minsize(width=window_height, height=window_height)
window.config(padx=50, pady=50)


# Button
def convert_mile_to_km():
    miles_input_float = float(miles_input.get())
    km_conversion = miles_input_float * 1.60934
    km_calc.config(text=f"{km_conversion}")


# Miles
miles_row = 0
miles_input = Entry()
miles_input.insert(END, string="Type your miles here...")


def temp_text(e):
    miles_input.delete(0, "end")


miles_input.bind("<FocusIn>", temp_text)
miles_input.grid(column=1, row=miles_row)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=miles_row)

# Kilometers
kilometers_row = 1
is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=kilometers_row)
km_label = Label(text="Km")
km_label.grid(column=2, row=kilometers_row)

km_calc = Label(text="0")
km_calc.grid(column=1, row=kilometers_row)

my_button = Button(text="Calculate", command=convert_mile_to_km)
my_button.grid(column=1, row=2)

window.mainloop()
