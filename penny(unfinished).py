salary=0.00
sumInt=0
days=eval(input("Enter an amount of days as an integer: "))
while days<1:
    print("Try again")
    days=eval(input("Enter an amount of days as an integer: "))
while days>0:
    salary=salary*0.01
    days=days-1
    print(salary)

