#AKeeme Black
#Final CST1101
#Question 1

def prof(numShare,priceShare,comRate,sPrice,comRatePaid): #defines and creates functions
    comRate=comRate/100
    comRatePaid=comRatePaid/100
    profit=((priceShare*numShare)-comRate)-((sPrice*numShare)+comRatePaid) #formula for profit
    return profit

numShare=eval(input("Enter the number of shares must be over 100 "))#validation loop
while numShare<100:
    numShare=eval(input("Enter the number of shares must be over 100 "))

priceShare=eval(input("Enter the price per share in dollars "))
comRate=eval(input("Enter the commision rate paid on the amount purchased in percent "))
sPrice=eval(input("Enter the sale price per share in dollars "))
comRatePaid=eval(input("Enter the commision rate paid on the amount sold in percent "))


profit=prof(numShare,priceShare,comRate,sPrice,comRatePaid)
if profit>0: #if profit is over 0 then it prints profit
    print("Your profit is",profit)
elif profit<0:
    print("Your loss is",profit)#if profit is under it prints loss
