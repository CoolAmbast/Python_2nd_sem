s="Hello Class"
#editing strings
#strings are immutable, we cannot change the value of a string
del s
#print(s)
s1="Pranjal"
s2="Hello"
del s1
print(s2)
#s= "Hello Class"
#del s[-1:-5:2]
#print(s)
#operations on strings
    #arithmetic operations
    #relation operations
    #logical operations
    #loops on strings
    #membership operations on strings
#arithmetic operations
first_name= "Pranjal"
last_name= "Ambast"
#concetation on strings
print(first_name+last_name)
#multiplication on strings
print(first_name*5)
print('*'*50)
print('-'*50)

#relational operators
if first_name==last_name:
    print("Both names are same")
elif first_name!=last_name:
    print("Both names are different")
n1= "Pranjal"
n2= "Ambast"
if n1>n2:
    print("n1 is greater than n2")
elif n1<n2:
    print("n1 is less than n2")
    
#logical operators
if first_name=="Pranjal" and last_name=="Ambast":
    print("Both names are correct")
if first_name=="Pranjal" or last_name=="Ambast":
    print("At least one name is correct")
#loops on strings
#for i in first_name:
    #print(i)
while first_name:
    print(first_name[0])
    first_name=first_name[1:]