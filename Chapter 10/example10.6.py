# Example of a Button click event 

#Here tkinter is imported
import tkinter as tk

def btnclick():
    label.config(text="You have clicked a button")
#root is a variable used in tkinter for main application window i.e.root window
root = tk.Tk()
# Main window is created
root.title("Example of a button click event")
# Label widget is created
label = tk.Label(root, text="Example of Button Click Event")
label.pack(pady=10)
# Button widget is created and a function btnclick is called
#command is used with widgets and for interacting when button is clicked etc.
button = tk.Button(root, text="Click Me", command=btnclick)
#pack() is used to place a widget in a block
button.pack()
#mainloop() is a method that runs an infinite loop and keeps the GUI running
#until the user closes the main window.
#it keeps the application responsive to the user actions.
root.mainloop()
