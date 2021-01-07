'''Akeeme Black
March 28, 2018
MidTerm, CST 1101'''

weight=eval(input("Enter the weight of the package per pound as an integer "))
distance=eval(input("Enter the distance the package was shipped per mile "))
rate=1.10
rate2=0.95
if weight<=2 and distance<=500:
    distance=distance/50
    answer=distance*rate
    print("Your charges are", answer)
elif 2<weight<=10:
    rate=2.20
    distance=distance/50
    answer=distance*rate
    print("You're charges are $",answer)
elif weight>10:
    rate=3.80
    distance=distance/50
    answer=distance*rate
    print("You're charges are $",answer)
else:
    if weight<=2 and distance>500:
        distance=distance/50
        answer=distance*rate2
        print("You're charges are $",answer)
if 2<weight<=10 and distance>500:
    rate2=1.95
    distance=distance/50
    answer=distance*rate2
    print("You're charges are $",answer)
if weight>10 and distance>500:
    rate2=3.35
    distance=distance/50
    answer=distance*rate2
    print("You're charges are $",answer)
