#fibonacci without function
n = int(input("Enter the number of terms: "))
a, b = 0, 1
if n <= 0:
    print("0")
elif n == 1:
    print("1")
else:
    print("Fibonacci sequence :")
    for i in range(n):
        print(a)
        a, b = b, a + b