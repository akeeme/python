def maxNumbers(n1,n2):
    if n1>n2:
        answer=n1
    elif n2>n1:
            answer=n2
    else:
            answer=n1=n2
    return answer

def aveNumbers(n1,n2,n3,n4,n5):
    avg=(n1+n2+n3+n4+n5)/5
    return avg

def getPentagonalNumber(n):
    for n in range(1,n+1):
        n=n*(3*n-1)//2
        print(n,' ',end='')

def displayPattern(n):
    for i in range(n+1):
        for j in range(1,i):
            print(j, end='')
        print()

def myInfo():
    print("Akeeme Black")
    print("Pathways Into Technology Early College High School")
    print("Sophmore, 10th Grade")
    print("150 Albany Avenue")
    print("akeemeblack@students.ptechnyc.org")

def getAreaRectangle(length,width):
    area=(length*width)
    return area

def calcVolRectPrism(base,height):
    volume=(base*height)
    return volume

def calcAverage(ts1,ts2,ts3,ts4,ts5):
    average=(ts1+ts2+ts3+ts4+ts5)/(5)

def determineGrade(avr):
    if avr<60:
        grade="F"
    if avr>=60 and avr<70:
        grade="D"
    if avr>=70 and avr<77:
        grade="C"
    if avr>=77 and avr<80:
        grade="C+"
    if avr>=80 and avr<83:
        grade="B-"
    if avr>=83 and avr<87:
        grade="B"
    if avr>=87 and avr<90:
        grade="B+"
    if avr>=90 and avr<93:
        grade="A-"
    if avr>=93 and avr<=100:
        grade="A"
    return grade
