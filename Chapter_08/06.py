import math as m
import pyinputplus as pip

def main():
    num = pip.inputInt(prompt= 'Enter a number: ', min=3)
    
    while num > 1:
        flag = True
        y = int(m.sqrt(num))
        i = 2

        while i <= y:
            if num % i == 0:
                flag = False
                break
            else:
                i += 1

        if flag :
            print(num)

        num = num - 1 

main()
