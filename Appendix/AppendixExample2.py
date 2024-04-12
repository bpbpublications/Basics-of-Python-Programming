def findmaxmin(data):
    x = max(data)
    y = min(data)
    return(x,y)

data = (19, 98, 90, 9)

(maximum, minimum) = findmaxmin (data)
print("Maximum Marks = ", maximum)
print("Minimum Marks = ", minimum)
