from tkinter import *

window = Tk()
window.title("My First GUI program")
window.wm_minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = Label(text="I am a label", font=("Arial", 24))
my_label.pack()

my_label["text"] = "New Text"
my_label.config(text="New Text")
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)


# Buttons
def button_clicked():
    print("I got clicked!")
    # my_label.config(text="Button Got Clicked")
    my_label.config(text=my_input.get())


my_button = Button(text="Click Me", command=button_clicked)
my_button.grid(column=1, row=1)

my_new_button = Button(text="New Button")
my_new_button.grid(column=3, row=0)

# Entry
my_input = Entry(width=10)
my_input.grid(column=4, row=3)

window.mainloop()
