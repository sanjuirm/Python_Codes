# Doubling the MONEY

def main():
    amount = eval(input('Enter Initial Investment Amount: '))
    apr = eval(input('Enter Annual Interest Rate: '))
    
    x = 2*amount

    accumulated = 0
    interest = 0
    years = 0

    while accumulated != x :
        interest = (apr * 0.1) * amount
        accumulated = interest + amount
        amount = accumulated
        years = years + 1
    
    print('Money Will Be Doubled In {} Years'.format(years))
main()
