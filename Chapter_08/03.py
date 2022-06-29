# Doubling the MONEY

def main():
    amount = eval(input('Enter Initial Investment Amount: '))
    apr = eval(input('Enter Annual Interest Rate: '))
    
    flag = 0
    x = 0
    cont = 0
    while flag != 2*amount:
        x = amount * (1 + (apr * 0.1))
        amount = x
        flag = x
        cont += 1
        #amount = amount + x
    
    print('Money Will Be Doubled In {} Years'.format(cont))
main()
