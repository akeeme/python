'''Akeeme Black
March 28, 2018
MidTerm Question2 CST 1101'''

import random
count=0
countpos=0
countneg=0
while count<20:
    int1=random.randint(-100,100)
    print("The generated numbers",int1)
    count+=1
    if int1>0:
        countpos+=1
    if int1<0:
        countneg+=1
print("The number of positive numbers that were generated",countpos)
print("The number of negative numbers that were generated",countneg)
        
