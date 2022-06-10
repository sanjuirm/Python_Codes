import numpy as np
sum=0
sum_c=0

def sumN(n):
    global sum
    for i in range(1,n+1):
        sum=sum+i
    return sum

def sumNCubes(n):
    global sum_c
    for j in range(1,n+1):
        sum_c=sum_c+np.power(j,3)
    return sum_c

def main():
    num=eval(input('Enter:'))
    sumn=sumN(num)
    sum_Cube=sumNCubes(num)

    print('Sum of first ',num,'is:',sumn,'\nTheir cube root is:',sum_Cube)

main()

