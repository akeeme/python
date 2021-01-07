#Akeeme Black
#March/20/2018
#Homework 2 Question 1

base=9.99 #The Base Fee
fee=0 #To make the program easier I'm going to setup an algorithm
checks=eval(input("Enter the amount of check(s) this month as an integer ")) #Stores  the amount of checks that month
total=base+checks+fee #A math problem to make solving easier, total holds an algorithm to check how much the amount will be
if checks==0:
    total=4.99+base
    print("You're total is",total)
#this checks if the amount of checks are exactly equal to 0 then follows through with the procedures
if 1<=checks<=4:
    fee=0.25 #uses the algorithm to make this code so much easier
    print("You're total is",total)
if 5<=checks<=19: #the rest is self explanatory
    fee=0.10
    print("You're total is", total)
if 20<=checks<=39:
    fee=0.08
    print("You're total is", total)
if 40<=checks<=59:
    fee=0.06
    print("You're total is", total)
if 60<=checks<=100:
    fee=0.04
    print("You're total is", total)
if checks>100:
    print("You're total is", total)
