"""
Creating strings in Python
accessing strings
adding characters to strings
editing strings
deleting strings
operations on strings
string functions
"""
single= 'This is a single quote string'
double= "This is a double quote string"
triple= '''This is a triple quote string'''
s= "Hello Class"
print(single)
print(double)
print(triple)
#accessing strings
print(single[0:10])
print(double[-5])
print(triple[10:-1])
print(s[0:5])
name = "Pranjal"
#positive indexing
print(name[0], name[6])
#negative indexing
print(name[-7])
#slicing
print(s[5:5])
print(s[6:])
#alternate letter printing of a string
print(s[0:11:2])
print(s[1:11:3])
#first step is always greater than the second step in reverse slicing
print(s[7:0:-1])
str = "Pranjal"
# Reverse the string using slicing
print(str[::-1])
print(s[:-6:-1])
#printing only hello in reverse
print(s[4::-1])