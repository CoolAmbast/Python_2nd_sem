#set
'''
a sets is an ordered collection of items
every set element is unique and must be immutable.
however a set itself is mutable
'''
#characteristics
'''
an ordered
mutable
no duplicates
'''
#adding item
#deleting item
#sets operation
#frozen set
#sets comprehension

#creating sets

a= {1,2,3,4,5}
#a= {1,2,3,{1,2,3}} 2d set is not possible
print(a)
b = {"hello",1,2,3,True} #sets does not allow duplicate values
print(b)
l = set([1,2,3,4]) #converting list to set
print(l)
#a1= {1,2,3,4,[1,2,3]} #sets does not contain mutable items
#print(a1)

'''sets does not support positive & negative slicing and indexing'''



#editing items in a set is not possible but we can add and remove items from a set

#accessing items

for item in a:
    print(item)
#adding items
a.add(6)
print(a)
a.update([7,8,9]) #adding multiple items
print(a)
a.update({10,11,12})
print(a)
a.update((13,14,15))
print(a)
a.remove(6) #removing an item that does not exist will raise an error
print(a)
a.discard(20) #removing an item that does not exist will not raise an error
print(a)