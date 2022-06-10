# Conversion program.

def main():
    print('This program convert Farenheit temperature to Celcius')
    
    for i in range(5):
       Farenheit=eval(input('Enter value in Farenheit:'))
       cs=(Farenheit-32)/1.8
       print('The temperature in Celcius is:','{0:.2f}'.format(cs))
main()