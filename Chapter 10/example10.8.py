import tkinter as tk #Import a library
def arithmetic_operations(choice): #function is defined here
    try:    # Exception handling is used here
        number_1 = int(num_1.get())#user input is taken here
        number_2 = int(num_2.get())#user input is taken here
        if choice == "Addition":
            output.set(f"Output is: {number_1+number_2}")
        elif choice == "Subtraction":
            output.set(f"Output is: {number_1-number_2}")
        elif choice == "Multiplication":
            output.set(f"Output is: {number_1*number_2}")
        elif choice == "Division":
            output.set(f"Output is: {number_1/number_2}")
    except ValueError:
            output.set("Entered value is not valid")
#main window is created here and its title is set
root = tk.Tk()
root.geometry("400x400")
root.title("********Arithmetic Operations*********")
#Label1 is set here
num_1=tk.Label(root,text="Enter First Number",bg="pink",fg="blue")
# Pack() is used for arranging widgets within the window and places widgets in a block 
num_1.pack()
# entry field1 for user input is created here
num_1 = tk.Entry(root,width=20)
num_1.pack()
#Label2 is set here
num_2=tk.Label(root,text="Enter Second Number",bg="pink",fg="blue")
num_2.pack()
# entry field2 for user input is created here
num_2 = tk.Entry(root,width=20)
num_2.pack()
# 4 buttons are created for addition,subtraction,division and multiplication.A function arithmetic_operations() is called here
addition = tk.Button(root, text="Addition", command=lambda: arithmetic_operations("Addition"),width =20)
subtraction = tk.Button(root, text="Subtraction", command=lambda: arithmetic_operations("Subtraction"),width =20)
multiplication = tk.Button(root, text="Multiplication", command=lambda: arithmetic_operations("Multiplication"),width =20)
division = tk.Button(root, text="Division", command=lambda: arithmetic_operations("Division"),width =20)
addition.pack()
subtraction.pack()
multiplication.pack()
division.pack()
# Label created to display the output
output = tk.StringVar()
output_label = tk.Label(root,textvariable=output)
output_label.pack()
#mainloop() is a method and runs infinite loop.#mainloop() keeps the application running until the user closes the main window.
root.mainloop()
