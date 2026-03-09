#isalnum/alpha/digit/space/ functions
name = "pranjal123"
print(name.isalnum()) #it will return True if all characters in the string are alphanumeric (letters and numbers)
#and there is at least one character, otherwise it will return False.
name = "pranjal"
print(name.isalpha()) #it will return True if all characters in the string are alphabetic (letters) 
#and there is at least one character, otherwise it will return False.
name = "12345"
print(name.isdigit()) #it will return True if all characters in the string are digits 
#and there is at least one character, otherwise it will return False.
name = "   "
print(name.isspace()) #it will return True if all characters in the string are whitespace 
#and there is at least one character, otherwise it will return False.
'''is identifier functions'''
name = "pranjal"
print(name.isidentifier()) #it will return True if the string is a valid identifier
#(a name that can be used for variables, functions, etc.)
name = "123pranjal"
print(name.isidentifier()) #it will return False because it starts with a digit, which is not allowed in identifiers.
name = "pranjal_123"
print(name.isidentifier()) #it will return True because it is a valid identifier
#(it starts with a letter and contains letters, digits, and underscores). 
#split and join functions
name = "my name is pranjal ambast"
print(name.split()) #it will split the string into a list of words.
print(name.split('a')) #it will split the string into a list of words, splitting at 'a'.
name = "pranjal_ambast"
print(name.split('_')) #it will split the string into a list of words, splitting at '_'.
name = ['pranjal', 'ambast']
print('_'.join(name)) #it will join the list of strings with '_' as separator.
#replace function
name = "pranjal ambast"
print(name.replace('a', 'x')) #it will replace all occurrences of 'a' with 'x' in the string.
#strip/lstrip/rstrip functions
name = "   pranjal ambast   "
print(name.strip()) #it will remove leading and trailing whitespace from the string.
print(name.lstrip()) #it will remove leading whitespace from the string.
print(name.rstrip()) #it will remove trailing whitespace from the string.