#take input from user in int and then reverse the number and print it
n = int(input("Enter a number: "))
rev = 0
while n > 0:
    last= n % 10
    rev = rev * 10 + last
    n = n // 10
print("Reversed number: ", rev)