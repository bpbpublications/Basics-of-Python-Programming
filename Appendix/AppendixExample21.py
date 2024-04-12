list1=[24,22,47,11,29,43]

# prebuilt max() and min() function to find smallest and largest number
if not list1:
    print("The list is empty.")
else:
    minimum = min(list1)
    maximum = max(list1)
    print(f"The minimum element in the list is: {minimum}")
    print(f"The maximum element in the list is: {maximum}")


