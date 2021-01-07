#Akeeme Black
#CST 1101
#May 20, 2018
#HomeWork4 Question2

import random
a=[]
b=[]

size1=eval(input("Enter the size of List1 as an integer. This must be larger than second list "))
size2=eval(input("Enter the size of List2 as an integer. Must be smaller than first "))

for size in range(size1):
    a.append(random.randint(1,10))
for sizee in range (size2):
    b.append(random.randint(1,10))

c=[]

for element in a:
    if element in b and element not in c:
        c.append(element)
print("The first generated list is",a)
print("Your second generated list is",b)
print("Your common list is",c)
