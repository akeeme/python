import random
l1=[]
l2=[]
l3=[]
l4=[]
sizeLarge=int(input('Enter the size of the large list. Must be an integer '))
sizeSmall=int(input('Enter the size of the small list. Must be an integer and smaller than first '))
for size in range(sizeLarge):
    l1.append(random.randint(1,10))
for size2 in range(sizeSmall):
    l2.append(random.randint(1,10))
print('List 1 is',l1,'List 2 is',l2)
