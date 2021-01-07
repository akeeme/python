cookiesAte= int(input('Enter how many cookies you ate as an integer ')) #Recieves an integer, asks how much cookies were ate
total=40 #Remembers how much cookies are total
calorieserv=300 #Remembers how many calories one serving is
servings=10 #Remembers how much cookies are in one serving
oneServing=(total/servings) #Finds how much cookies are in one serving
oneCookieCal=(calorieserv/oneServing) #Calculates how many calories in one cookie
caloriesAte=(cookiesAte*oneCookieCal) #Calculates the calories based off the information

print (caloriesAte)
