import pyinputplus as pip

def main():
    score= pip.inputInt( prompt='Enter Marks Obtained(0-5)', min=0, lessThan=5)

    if score == 5:
        print('\nA')
    elif score == 4:
        print('\nB')
    elif score == 3:
        print('\nC')
    elif score == 2:
        print('\nD')
    elif score == 1:
        print('\n')
    elif score == 0:
        print('\nF')
main()