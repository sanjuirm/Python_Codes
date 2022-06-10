# Fibbonacci2.py
i1,i2=0,1 
def fibonacci(n):
    global i1,i2
    while n>2:
        nth=i1+i2
        i1=i2       
        i2=nth 
        n=n-1
    return nth

def main():
    n=int(input('no upto which the series is to be printed:'))  
    fib=fibonacci(n)
    
    print('The nth fibonacci number is:',fib)

main()