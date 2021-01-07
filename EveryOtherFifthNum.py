a=[]

for entry in range(-5,36,+5):
    a.append(entry)
print("My list is",a)

if 1 in a:
    count1+=1
    print("1 is in the list, there are",a.count(1),"1's in the list")
else:
    print("1 is not in the list.")
if 15 in a:
    print("15 is in the list, there are",a.count(15),",","15's in the list")
else:
    print("15 is not in the list.")
