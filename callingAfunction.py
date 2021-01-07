#calling a local function

from myfunctions import maxNumbers #Module, imports functions locally, etc.

a,b=eval(input("Enter any number separated by a comma "))

print("The largest number is",maxNumbers(a,b))
