n=int(input())  # no upto which the series is to be printed
i1,i2=0,1 
while n>1:
    nth=i1+i2
    i1=i2       # exchange of i2 into i1
    i2=nth      # exchange of ans into i2
    print('\n',nth)
    n=n-1

