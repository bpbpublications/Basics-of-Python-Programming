def menu(choice):
    if choice == 1:
        return "Your choice is 1"
    elif choice == 2:
        return "Your choice is 2"
    elif choice == 3:
        return "Your choice is 3"
    else:
        return "You have entered invalid choice"

ch = int(input("Enter Your choice"))
output = menu(ch)
print(output)
