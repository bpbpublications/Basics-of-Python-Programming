import tkinter as tk
# function is defined here
def get_input():
    user = var2.get()
    var4.config(text=f"Welcome: {user}")
    
#root is a variable used in tkinter for main application window i.e. root window
#Tk() is a class and is a container for all the widgets 
root = tk.Tk()
# Main window is created
root.title("Example of taking input from a user")
var1 = tk.Label(root, text="Enter Your Name")
var1.pack(pady=5)
# Entry is also one of the widget and is used for input fields
var2 = tk.Entry(root, width=40)
# Pack() is used for arranging widgets within the window and places widgets in a block 
var2.pack(pady=5)
#Label is a widget and is used for displaying text or images
var3 = tk.Label(root, text="")
#pack() is used to place widgets in a block
var3.pack()
# Here function get_input() is called on button click event using command option and no parentheses are required
#Button is the widget and used for firing event
var4 = tk.Button(root, text="Click Button", command=get_input)
var4.pack()
#mainloop() is a method and runs infinite loop.
#mainloop() keeps the application running until the user closes the main window.
root.mainloop()

