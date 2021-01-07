myList=[]

length=int(input("Enter the length of your list: "))

for element in range(length):
    element=int(input("Enter an integer on your list: "))
    myList.append(element)

print("My original list is", myList)
print("First element of my original list is",myList[0])

myList.sort()
print("My list is ascending in order is",myList)
print("First element of my list in ascending order is",myList[0])

myList.reverse()
print("My list in descending order is",myList)
print("First element of my original list in descending order",myList[0])
