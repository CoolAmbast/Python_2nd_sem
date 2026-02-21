n = int(input("Enter a number: "))
if n == 0:
    print("Factorial of 0 is 1")
elif n < 0:
    print("Factorial does not exist for negative numbers")
else:
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    print("Factorial of", n, "is", factorial)