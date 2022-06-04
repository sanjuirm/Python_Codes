# Conversion program.

def main():
    print('This program convert Celcius temperature to Farenheit')
    
    for i in range(5):
        celcius=eval(input('Enter value in Celcius:'))
        fr=1.8*celcius+32
        print('The temperature in farenheit is:','{0:.2f}'.format(fr))
main()

