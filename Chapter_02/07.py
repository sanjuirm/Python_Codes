# modifed_futval.py
# A program to compute value of an investment

def main():
    print('This program computes total future value of an investment')
    
    n=eval(input('Enter the total no of years for investment: '))
    principal=eval(input('Enter initial principal amount: '))
    amount=eval(input('Enter the amount to be invested each year: '))
    apr=eval(input('Enter annual interest rate: '))
    
    for i in range(n):
        principal=((principal*(1+(apr/100)))+amount)
        
    print('The total amount in',n,'years will be: ','{0:.3f}'.format(principal))

main()