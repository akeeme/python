a=[1,4,9,16,25,36,49,64,81,100]
aEven=[]
aOdd=[]

for integer in a:
    if integer%2==0:
        aEven.append(integer)
    else:
        aOdd.append(integer)

print("Your original list is",a)
print("Your even list is",aEven)
print("Your odd list is",aOdd)

print('')#-----------------------------------------------------------------------

aEven=[]
aOdd=[]

for i in range(len((a))):
    if a[i]%2==0:
        aEven.append(a[i])
    else:
        aOdd.append(a[i])
print("Your original list is",a)
print("Your even list is",aEven)
print("Your odd list is",aOdd)
