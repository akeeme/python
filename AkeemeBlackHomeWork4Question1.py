#Akeeme Black
#HomeWork4 Question1
#CST 1101
#May 19 2018

import math

def calcRadius(xcoor,ycoor):
    distance=xcoor**2+ycoor**2
    radius=math.sqrt(distance)
    return radius


def calcArea(radius):
    pi=math.pi
    area=pi*(radius**2)
    return area
#-------------------------------------------------------------------------------
xcoor=eval(input("Enter x coordinate as integer: "))
ycoor=eval(input("Enter y coordinate as integer: "))

calcRadius(xcoor,ycoor)
calcArea(calcRadius)
print(calcRadius,calcArea)
