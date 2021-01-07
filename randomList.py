'''Handout 14, Question 2... Write a program that randomly generates two lists
of a different size. Ask the user to determinesize of larger list and the size
a smaller list. Each list will contain only integers in the range from 1
through 100, inclusive. The program will display the generated lists and a list
that contains only the elements that are common to both randomly generated lists.
Your outcome list should not contain duplicates.
'''

import random
a=[]
b=[]
size1=eval(input("Enter the size of List1 as an integer. This list must be larger than the second "))
size2=eval(input("Enter the size of List2 as an integer. This list must be smaller than List1 "))
for size in range(size1):
    a.append(random.randint(1,100))
for sizee in range (size2):
    b.append(random.randint(1,100))

c=[]

for element in a:
    if element in b and element not in c:
        c.append(element)
print("The first generated list is",a)
print("Your second generated list is",b)
print("Your common list is",c)
