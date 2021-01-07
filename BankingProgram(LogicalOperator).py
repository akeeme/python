#Programmer: Akeeme Black
#Date: 2/21
#Problem 1

'''To ask the user for salary and years'''

salary=eval(input("Enter your annual salary "))
years=eval(input('Enter your year(s) at current job: '))
if salary>=60000 and years>=2:
     print("Congratulations!!! Your Qualified")
else:
    print("You do not qualify")
