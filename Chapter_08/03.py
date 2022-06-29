# Doubling the MONEY

def main():
    amount = eval(input('Enter Initial Investment Amount: '))
    apr = eval(input('Enter Annual Interest Rate: '))
    
    x = 2*amount
    flag = True
    accumulated = 0
    interest = 0
    years = 0

    while flag:
        interest = (apr * 0.01) * amount
        accumulated = interest + amount
        amount = accumulated
        years += 1

        if accumulated > x:
            flag = False
        else:
            continue
    
    print('Money Will Be Doubled In Almost {} Years'.format(years))
main()
