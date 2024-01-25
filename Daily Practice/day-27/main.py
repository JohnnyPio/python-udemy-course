from tkinter import *

window = Tk()
window.title("My First GUI program")
window.wm_minsize(width=500, height=300)

# Label
my_label = Label(text="I am a label", font=("Arial", 24))
my_label.pack()

my_label["text"] = "New Text"
my_label.config(text="New Text")


# Buttons
def button_clicked():
    print("I got clicked!")
    # my_label.config(text="Button Got Clicked")
    my_label.config(text=my_input.get())


# Entry
my_input = Entry(width=10)
my_input.pack()

button = Button(text="Click Me", command=button_clicked)
button.pack()

window.mainloop()
