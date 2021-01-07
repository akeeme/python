question = int(input("Enter a five-digit integer please: "))
##This prompts the user to enter a five-digit integer and makes sure that this is an integer
reverse = (str(question) [::-1])
##This turns the integer into a string which essentially makes it easier to reverse ::-1 is a slicing function
print (question)
##This prints the variable question
print (reverse)
##This prints the variable reverse
