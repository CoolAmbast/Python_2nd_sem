#list comprehension
#disadvantage of python list

L = [1,"apple",3]
#print(L)
#print(id(L))
print(id(L[0]))
print(id(L[1]))
print(id(L[2]))
print(id(1))
print(id("apple"))
print(id(3))
#what are list?
'''
list is a data type where we can store multiple items under one name.Technically list act like dynamic array
which means we can add more item on the fly/go.
e.g:
L= [1,"apple", 3]
speed of execution == slow, reason being it stores data in non-contiguous memory location,
which means it has to store the reference of the data in the list and then access the data using the reference. 
This is why it is slower than array which stores data in contiguous memory location.
'''
#characteristics of a list
'''
ordered
changable/mutable
heterogeneous
can have duplicate items
list are dynamic
can be nested
item can accessed
'''
l1 = [1,2,3,4,5]
l2 = [2,1,3,4,5]
print(l1 == l2) #false
l = [1,1,2,3,4,5]
print(l)

#how to create a list
s1= []
print(s1)
#1-D list
l1 = [1,2,3,4,5] #homogeneous list
print(l1)
ll1 = [1,"apple",3.14,True] #heterogeneous list
print(ll1)
#2-D list
l2 = [[1,2,3],[4,5,6],[7,8,9]] #is a heterogeneous list because it contains list as an item
print(l2)
#3-D list
l3 = [[[1,2,3],[4,5,6]],[[10,11,12],[13,14,15]]] #is a homogeneous list
print(l3)

#type conversion
print(list('hello')) #list of characters

#accessing item from a list
a1 = [1,2,3,4,5,6,7,8]
#indexing
  #positive indexing
print(a1[0]) #access first item
print(a1[4]) #access fifth item
    #negative indexing
print(a1[-1]) #access last item

a2 = [1,2,3,[4,5]]
print(a2[3][1]) #access the list 5
#we have to access two element from 3-D list next
a4 = [[[1,2,3],[4,5,6]],[[10,11,12],[13,14,15]]]
print(a4[1][0][2]) #access the list 12

#slicing of list
a3 = [1,2,3,4,5,6,7,8]
print(a3[2:6]) 
# print and skipping item
print(a3[::2])
#reversing a list withing using reverse function
print(a3[::-1])

#adding item in a list
l4 = [1,2,3]
#append() function
l4.append(4) #add item at the end of the list and single item insertion is possible with append() function
print(l4)
#extend() function
l4.extend([5,6]) #add multiple item at the end of the list
print(l4)
#insert() function
l4.insert(1,'hello') #add item at the specified index
print(l4)

#editing item in a list
list1 = [1,2,3,4,5]
list1[1:4] = [200, 300, 400] #change the value of the item at the given index
print(list1)

#deleting item from a list
list2 = [1,2,3,4,5]
#del statement
#del list2[1:3] #delete item at the specified index
#print(list2)
#remove() function
#list2.remove(3) #delete the first occurrence of the specified value
#print(list2)
#clear() function
#list2.clear() #delete all items from the list
#print(list2)

#pop()
print(list2.pop())

#operations on list
list3 = [1,2,3,4,5]
list4 = [6,7,8,9,10]
#arithematic operations
print(list3 + list4) #concatenation of two list
print(list3 * 2) #repetition of list

#membership operations
print(3 in list3) #check if item is in the list
print(6 not in list3) #check if item is not in the list

#loop operations
for i in list3:
    print(i)
    
#list in functions
  #len()
  #min()
  #max()
  #sorted()
unsorted = [325,235234,241243,5325,324,235,23,42]
print(len(unsorted))
print(min(unsorted))
print(max(unsorted))
print(sorted(unsorted))
print(unsorted)

#count()
print(unsorted.count(23))

#index()
print(unsorted.index(23))

#reverse()
unsorted.reverse()
print(unsorted)
print(unsorted)

#sort()
unsorted.sort()
print(unsorted)
print(unsorted)