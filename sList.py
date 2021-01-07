sList=[]

length=int(input("Enter the length of your list: "))

for element in range(length):
    element=input("Enter a string ")
    sList.append(element)

print("The first element is",sList[0])
print("The original list is",sList)

print("The maximum value on the list is",max(sList))
print("The first element is",sList[0])

sList.sort()
print("The ascending order of the list is",sList)
print("The first element is",sList[0])

sList.reverse()
print("The descending order of the list is",sList)
print("The first element is",sList[0])
