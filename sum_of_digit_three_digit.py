n = int(input("Enter a three-digit number: "))
sum = 0
for i in range(3):
    digit = n % 10
    sum += digit
    n //= 10
print(f"The sum of the digits is: {sum}")