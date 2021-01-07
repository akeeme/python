#Programmer: Akeeme Black
#Date: 2/21
#Problem 1

grade=eval(input("Enter your test score: "))
if grade>=90:
    print("Congrats! You have an A")
else:
    if grade>=80:
        print("Congrats! You have a B")
    else:
        if grade>=70:
            print("Congrats! You have a C")
        else:
            if grade>=60:
                print("At least you passed...You have a D")
            else:
                print("Mission Failed...You'll get em next time")
