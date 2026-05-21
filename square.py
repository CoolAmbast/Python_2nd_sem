def square(x):
    return x ** 2

y= int(input("Enter a number: "))
y= square(y)
print("The square of the number is: ",y)
#gives the reference of the function to y, so now y is a function
print(square)