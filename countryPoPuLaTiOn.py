country=["China","India","USA","Russia","UK","Canada","Australia"]
population=[1379,1324,323.1,144.3,65.64,36.29,24.13]

for i in range(len(country)):
    print(country[i],'-',population[i],'million')

print("The country with the largest population is",country[0],population[0])
print("The country with the smallest population is",country[-1],population[-1])
