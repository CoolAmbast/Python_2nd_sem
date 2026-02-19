n = int(input("Enter a number: "))
sum_odd = 0
for i in range(1, n + 1):
    if i % 2 != 0:
        sum_odd += i
        print(i)
print("The sum of odd numbers from 1 to", n, "is:", sum_odd)