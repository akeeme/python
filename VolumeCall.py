from myFunction import getAreaRectangle
from myFunction import calcVolRectPrism
l=eval(input("Enter the length of the rectangular prism "))
w=eval(input("Enter the width of the rectangular prism "))
h=eval(input("Enter the height of the rectangular prism "))

b=getAreaRectangle(l,w)

print("The volume of the prism is",calcVolRectPrism(b,h))
