# Average of N numbers

from audioop import avg


n=eval(input('Enter total no of times: '))
total=0

for i in range(1,n+1,1):
    v=eval(input('Enter no: '))
    total=total+v
avg=float(total/n)

print('Total sum: ',round(avg,2))