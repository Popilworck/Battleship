# Python program to
# Illustrate Separator
# widget


# Import required modules
from tkinter import *
from tkinter import ttk


# Main tkinter window
x = Tk()
x.geometry("400x300")


# Label Widget
b = Label(x, bg="#f5f5f5", bd=4, relief=RAISED, text="With Separator")
b.place(relx=0.03, rely=0.1, relheight=0.8, relwidth=0.4)


# Separator object
separator = ttk.Separator(x, orient='vertical')
separator.place(relx=0.47, rely=0, relwidth=0.2, relheight=1)


# Label Widget
a = Label(x, bg="#f5f5f5", bd=4, relief=RAISED, text="With Separator")
a.place(relx=0.5, rely=0.1, relheight=0.8, relwidth=0.4)


mainloop()
