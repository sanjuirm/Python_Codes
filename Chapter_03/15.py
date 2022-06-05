# Pi value calculation.

def main():
    n=eval(input('Enter total no of times: '))
    j=0
    pi_val=0
    for i in range(1,n+1,1):
         if i%2==0:
            pi_val=pi_val-(4/i+j)
         else:
            pi_val=pi_val+(4/i+j)
         j=+1
    
    print('Total sum: ',pi_val)

main()