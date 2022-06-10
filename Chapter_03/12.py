# Sum of cubes of first N natural numbers

n=eval(input('Enter number upto which calcultion needs to be done: '))
total=0

for i in range(1,n+1,1):
    t=i*i*i
    total=total+t

print('Total sum: ',total)