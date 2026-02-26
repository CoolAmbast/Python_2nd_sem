'''
len = find out the length of a string.
max = find out the maximum value.
min = find out the minimum value.
sorted = sort any string. In ascending order by default, or in descending order if specified.
these functions are also used in list,tuples,set and dictionaries.
'''
print(len('pranjal'))
print(max('pranjal'))
print(min('pranjal'))

#when we use the sorted function it will return a list of sorted characters in the string or output will be in the form of list.
print(sorted('pranjal'))
name = 'pranjal'
print(sorted(name))

#capitalized/title/upper/lower/swap functions
name = 'pranjal ambast'
print(name.capitalize())
print(name)
print(name.title())
print(name.upper())
print(name.lower())
print(name.swapcase())

#count/find/index functions
name = "my name is pranjal ambast"
print(name.count('a')) #it will count the number of times 'a' is present in the string.
print(name.find('is')) #it will return the index of the first occurence of 'is' in the string. If the substring is not found then it will return -1.
print(name.index('is')) #it will also return the index of the first occurence of 'is' in the string. If the substring is not found then it will raise an error.
# endwith/startswith functions
name = "pranjal ambast"
print(name.endswith('pranjal')) #it will return False if the string ends with 'ambast' otherwise it will return False.
print(name.startswith('pranjal')) #it will return True if the string starts with 'pranjal' otherwise it will return False.
#**format function**
name = 'pranjal'
gender = 'male'
s= "My name is {} and I am {}".format(name,gender) #it will replace the {} with the values of name and age respectively.
print(s)
s= "My name is {} and I am {}".format(gender,name) #it will replace the {} with the values of age and name respectively.Order matters in this case.
print(s)
