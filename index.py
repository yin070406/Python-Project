from tkinter import *
from tkinter import messagebox

def click():
    while True:
        messagebox.showwarning(title="WARNING", message="Get Ratted By YinVIRUS")

window = Tk()

button = Button(window, command=click, text="click me")
button.pack()

window.mainloop()