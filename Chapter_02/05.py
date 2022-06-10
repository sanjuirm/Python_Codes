# Conversion program.

def main():
    print('This program convert Celcius tempearture to Farenheit for every 10 degree increment')
    
    celcius=0
    print('Celcius','Farenheit')
    for i in range(11):
        fr=1.8*celcius+32
        print(celcius,'\t',fr)
        celcius=celcius+10
main()

