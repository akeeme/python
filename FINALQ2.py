import random

a=[]
b=[]
c=[]
d=[]
e=[]
countEven=0
countOdd=0
countPos=0
countNeg=0
listSize=int(input('Enter the size of the list '))

for s in range(listSize):
    a.append(random.randint(-10,10))
for element in a:
    if element % 2 == 0:
        countEven=countEven+1
        b.append(element)
for odd in a:
    if odd % 2 != 0:
        countOdd=countOdd+1
        c.append(odd)
for pos in a:
    if pos>0 and pos!=0:
        countPos=countPos+1
        d.append(pos)
for neg in a:
    if neg<0:
        countNeg=countNeg+1
        e.append(neg)
print('The original list is',a,'The amount of even numbers are',countEven,'This consists of',b,'The amount of Odd numbers are',countOdd,'This consists of',c,'The count of positive integers are',countPos,'These consists of',d,'The count of negative integers are',countNeg,'These consists of',e)
repeat=input("Would you like to repeat? Type yes or no ")
while repeat=='yes':
    a=[]
    b=[]
    c=[]
    d=[]
    e=[]
    countEven=0
    countOdd=0
    countPos=0
    countNeg=0
    listSize=int(input('Enter the size of the list '))

    for s in range(listSize):
        a.append(random.randint(-10,10))
    for element in a:
        if element % 2 == 0:
            countEven=countEven+1
            b.append(element)
    for odd in a:
        if odd % 2 != 0:
            countOdd=countOdd+1
            c.append(odd)
    for pos in a:
        if pos>0 and pos!=0:
            countPos=countPos+1
            d.append(pos)
    for neg in a:
        if neg<0:
            countNeg=countNeg+1
            e.append(neg)
    print('The original list is',a,'The amount of even numbers are',countEven,'This consists of',b,'The amount of Odd numbers are',countOdd,'This consists of',c,'The count of positive integers are',countPos,'These consists of',d,'The count of negative integers are',countNeg,'These consists of',e)
    repeat=input("Would you like to repeat? Type Yes or No ")
if repeat=='no':
    print('End of Program')
