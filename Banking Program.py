#Programmer: Akeeme Black
#Date: 2/21
#Problem 1

'''To ask the user for salary and years'''

salary=eval(input("Enter your annual salary"))
years=eval(input('Enter your years at current job: '))
if salary>=60000:
    if years>=2:
        print("Congratulations!!! Your Qualified")
    else:
        print("Sorry, you're not qualified, you do not have enough experience")
else:
    print("You're not qualified, your salary isn't enough")
