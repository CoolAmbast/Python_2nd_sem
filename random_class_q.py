for i in 'Delhi':
    print('Pune') #output will be 'Pune' 5 times because there are 5 characters in the string 'Delhi'.

#question 1: print all letters except 'k' and 'u' in the string 'kaushikkumar'.
name = "kaushikkumar"
for i in name:
    if i == 'k' or i == 'u':
        continue
    print(i)
# same solution using while loop
name = "kaushikkumar"
i = 0
while i < len(name):
    if name[i] == 'k' or name[i] == 'u':
        i += 1
        continue
    print(name[i])
    i += 1