'''
1. Find the length of a given string(user input string) without using len() function.
'''
#using for loop
string = input("Enter a string: ")
length = 0
for char in string:
    length += 1
print("Length of the string is:", length)

#using while loop
string = input("Enter a string: ")
length = 0
while string[length:]:
    length += 1
print("Length of the string is:", length)

'''
2. example: pranjambast2401@gmail.com
 extract everything before @ and output it
 the mail id should be user input instead of hard coded
'''
email = input("Enter your email id: ")
username = email.split('@')[0]
print("Username is:", username)

'''
3. Find the sum of digits of a three-digit number. (user input)
'''
n = int(input("Enter a three-digit number: "))
sum = 0
for i in range(3):
    digit = n % 10
    sum += digit
    n //= 10
print(f"The sum of the digits is: {sum}")

'''
4. Find palindrome or not. (user input)
'''
number = input("Enter a number: ")
reversed_number = number[::-1]
if number == reversed_number:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")
