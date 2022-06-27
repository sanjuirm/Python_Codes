import pyinputplus as pip

def main():
    credit=pip.inputNum(prompt='Enter Credits Obtained: ', min=1)
    
    if credit < 7:
        print('Freshman\n')
    elif credit >= 7 and credit < 16:
        print('Sophomore')
    elif credit >= 16 and credit < 26:
        print('Junior')
    else:
        print('You are a Senior now.')
main()