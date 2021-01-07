#Akeeme Black
#HomeWork Assignment #3, Question 2
#May 1, 2018


import random
numOfStudents=eval(input("Enter the number of students in your class "))
numTest=eval(input("Enter the number of tests per student "))
for numOfStudents in range(1,numOfStudents+1):
    for numTest in range(1,numTest+1):
        testscore=random.randint(0,100)
avgTest=testscore/numTest
print("The number of students are",numOfStudents,"the average test score is",avgTest)
again=input("Do you want to repeat? Enter Yes or No ")
while again=="Yes":
    numOfStudents=eval(input("Enter the number of students in your class "))
    numTest=eval(input("Enter the number of tests per student "))
    for numOfStudents in range(1,numOfStudents+1):
            for numTest in range(1,numTest+1):
                testscore=random.randint(0,100)
    avgTest=testscore/numTest
    print("The number of students are",numOfStudents,"the average test score is",avgTest)
    again=input("Do you want to repeat? Enter Yes or No ")
if again== "No":
    print("End of Program")
    
