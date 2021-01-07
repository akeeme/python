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
    count=0
    m=1
    while count<50:
        n+=1
        pentNum=m(3*m-1)/2
        count+=1
