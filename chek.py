fee=9.99 #Base Fee
check=eval(input('Enter amount of checks:')) #Enter ammount of checks 
#x variable is total 
#Check is 0 pay $4.99
if check==0:
    x=fee+4.99
    print(x)
#Check is less than 5 pay $0.25
if check<5:
    x=fee+(.25*check)
    print(round(x,1))
#Check is between 5 and 19 pay $0.10
if 5 <= check <= 19:
    x=fee+(0.10*check)
    print(round(x,1))
#Check is between 20 and 39 pay $0.08
if 20 <= check <= 39:
    x=fee+(0.08*check)
    print(round(x,1))
#Check is between 40 and 59 pay $0.06
if 40 <= check <= 59:
    x=fee+(0.06*check)
    print(round(x,1))
#Check is between 60 and 100 pay $0.04
if 60 <= check <= 100:
    x=fee+(0.04*check)
    print(round(x,1))
#Check is 100 pay no extra cost ($0.00)
if check>=100:
    x=fee
    print(round(x,1))
