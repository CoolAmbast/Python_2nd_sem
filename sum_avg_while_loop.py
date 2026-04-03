s = 0
c = 0
while True:
    n = int(input("Enter a number: "))
    if n == 0:
        break
    s+=n
    c+=1
print("Sum: ", s)
print("Average: ", s/c)