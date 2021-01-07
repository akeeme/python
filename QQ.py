weight=int(input("Enter a weight in pounds "))
height=int(input("Enter a height in inches "))
kg=0.45359237
meter=0.0254
weightKg=weight*kg
print(weightKg)
heightMeter=height*meter
print(heightMeter)
heightSquare=heightMeter*heightMeter
print(heightSquare)
BM=weightKg/heightSquare
print(BM)
BMI=round(BM,1)
if BMI>18.5:
    print("You are underweight, your BMI is",BMI)
if BMI<=18.5 and BMI>=24.9:
    print("You are normal weight, your BMI is",BMI)
if BMI<=25.0 and BMI>=29.0:
    print("You are overweight, your BMI is",BMI)
if BMI<30.0:
    print("You are OBESE, your BMI is",BMI)
