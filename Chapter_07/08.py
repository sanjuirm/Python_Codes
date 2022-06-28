import pyinputplus as pip

def main():
    age= pip.inputInt(prompt='Enter age: ', min=0)
    US_year= pip.inputInt(prompt='\nEnter US citizen year: ', min=0)

    if age >=30 and US_year >=9:
        print('\nYou are eligible for US Senator')
    elif age >=25 and US_year >=7:
        print('\nYou are eligible for US House Representative')
    else:
        print('Sorry, You are not eligible for anything')
main()
