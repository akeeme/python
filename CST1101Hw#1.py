row=13
coloumn=8
count=0
for i in range(1,8):
    while row>7:
        count+=1
    row-=1
    print('')
    for j in range(1,row-1):
            print(count, end='')


