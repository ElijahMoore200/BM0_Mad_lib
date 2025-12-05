from tkinter import *
#need to install on all machines
from tkmacosx import Button
import tkinter as tk 
l = Label(root, text = "text box")
# Create the main window
root = Tk()
root.title("Enter Title Here")

#Set size of window
root.geometry("300x150")

# Create buttons
red_button = Button(root, text="Red", background='red')
yellow_button = Button(root,text="Yellow", background='yellow')
green_button= Button(root,text='Green',background='green')
#Add a label
label = Label(root, text = "This is a stoplight")
textarea = tk.Text(root, width = 50, height = 10, wrap="word")
# Place widgets in window (with pack function!)
T = Text(root, height = 5, width = 52)
red_button.pack()
yellow_button.pack()
green_button.pack()
label.pack()

# Start the GUI event loop
root.mainloop()
tk.mainloop()