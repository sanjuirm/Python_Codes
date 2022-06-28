# Leap year
import pyinputplus as pip

def main():
    year= pip.inputStr(prompt=' Enter Year: ')
    if year[2: ] == '00':
        if int(year) % 400 == 0:
            print('\n{} is a Leap Year'.format(year))
        else:
            print('\n{} is not a Leap Year'.format(year))
    else:

        if int(year) % 4 == 0:
            print('\n{} is a Leap Year'.format(year))
        else:
            print('\n{} is not a Leap Year'.format(year))
main()