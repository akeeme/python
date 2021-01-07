question = int(input ("Enter a Five-digit integer"))
reverse = 0
while(question>0):
    ui = question %10
    reverse = (reverse*10) + ui
    question = question //10
    print(reverse)
