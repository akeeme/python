from myFunction import calcAverage
from myFunction import determineGrade

t1=int(input("Enter First Test Grade "))
t2=int(input("Enter Second Test Grade "))
t3=int(input("Enter Third Test Grade "))
t4=int(input("Enter Fourth Test Grade "))
t5=int(input("Enter Fifth Test Grade "))

average=calcAverage(t1,t2,t3,t4,t5)



print("Your average is",average,"Your grade is",determineGrade(average))

