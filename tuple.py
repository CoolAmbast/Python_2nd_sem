# tuple
'''
a tuple in python is similar to a list
the difference between two is that we cannot change the element of a tuple once it is assigned,
whereas we can change the elememt of a list.
in short tuple is a immutable list
a tuple cannot be changed in any way once it is created
'''
#characteristics of tuple
'''
ordered
immutable
allows duplicates
'''
#creating a tuple
#indexing in tuple
#accessing items in tuple
#editing
#deleting
#operations on tuples


t= (1,2,3,4,5,6)

#accessing tuple
print(t[0])
print(t[1])
print(t[-1])
print(t[-2])

#slicing
print(t[0:5])

#stepping
print(t[0::2])

#reverse
print(t[::-1])

#T = (1,2,5,8,4)
#print(T)
#del T
#print(T)
#if you want to delete a whole tuple it is possible but deleting a single item in tuple is not possible

#operations on tuple

t1=(1,2,3,4,5)
t2=(5,4,3,2,1)

print(t1+t2)
print(t1*2)

#membership
print(2.in(t1))

#functions
'''
len
max
min
sorted
count
index
'''
print(len(t1))
print(max(t2))
print(min(t1))
print(sorted(t2))
print(t2.count(1))
print(t1.index(5))

'''
tuple unpacking
'''
#a,b,c= (2,3,4)
#print(a)
#print(b)
#print(c)

#a,b = (5,6,7)
#print(a,b)