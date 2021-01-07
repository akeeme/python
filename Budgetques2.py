#Davaughn Evans
#October 20, 2018
#HomeWork 2 Question 2

budget=eval(input("What is you're budget for this month? "))
expense=0
expenseCost=0
remainder=0

if budget>=1000:
    while expense<=7:
        expenseCost=eval(input("Enter your expense "))
        remainder=remainder+expenseCost
        print("You spent", remainder, "dollars")
        expense+=1
        remainder2=budget-remainder
        if remainder<0:
            print("You over budgeted",remainder)
        else:
            print("You haven't overbudgeted, you have",remainder2,"dollars")
elif budget<1000:
    print("You're budget must be 1000 or over")
