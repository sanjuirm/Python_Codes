# futval.py
# A program to compute value of an investment

def main():
    print('This program computes future value of an investment')
    
    n=eval(input('Enter the time period for calculation: '))
    principal=eval(input('Enter the invested amount: '))
    apr=eval(input('Enter annual interest rate: '))
    

    for i in range(n):
        principal=principal*(1+(apr/100))

    print('The value in',n,'years will be: ','{0:.3f}'.format(principal))

main()