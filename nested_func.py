def g(x):
    def h(x):
        x+=1
        print(x)
    x+=1
    print(x)
    h(x)
    return x
x = 3
z = g(x)
print(x)
print(z)