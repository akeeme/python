row=8
count=0
space=8
space=' '
for i in range(1,9):
    row=row-1
    print('',row)
    count+=1
    for j in range(1,row+1):
        for k in range(1,1):           
            print('',row,count, end='')
