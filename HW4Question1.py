import math

def calcRadius(x,y):
    d=(x*x)+(y*y)
    r=math.sqrt(d)
    return r

def calcArea(r):
    area=math.pi*(r**2)
    return area

x=eval(input("Please enter the x coordinate as an integer "))
y=eval(input("Please enter the y coordinate as an integer "))
r=calcRadius(x,y)
r1=str(round(r,2))

area=calcArea(r)
a1=str(round(area,2))
print('The radius is',r1,'The area is',a1)
