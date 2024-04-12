import tkinter as tk

#Main window is created using tk.Tk()
root = tk.Tk()
root.title("Example of button click")
# A Label widget is created
# Label widget is a Python object
label = tk.Label(root, text="Label Widget")
# pack() method is used to arrange the widgets.
label.pack(pady=10)
# A button widget is created
# Button widget is a Python Object
button = tk.Button(root, text="Click Here")
button.pack()
root.mainloop()



