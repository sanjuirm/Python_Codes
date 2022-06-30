import math as m
import pyinputplus as pip

def main():
    num = pip.inputInt(prompt= 'Enter a number: ', min=3)
    
    y = int(m.sqrt(num))
    i = 2
     
    while i <= y:
        if num % i == 0:
            print('It\'s  not a Prime Number')
            break
        else:
            i += 1
    print('Prime Number')
main()
