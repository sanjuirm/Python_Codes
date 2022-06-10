# Sum of first N natural numbers

n=eval(input('Enter number upto which calcultion needs to be done: '))
total=0

for i in range(1,n+1,1):
    total=total+i

print('Total sum: ',total)