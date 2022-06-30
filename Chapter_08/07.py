# Goldbach Conjecture
import math as m
import pyinputplus as pip

def main():
    lst = []
    num = pip.inputInt(prompt= 'Enter a number: ', min=3)
    temp = num

    if num %2 == 0:
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
                lst.append(num)
                # print(num)
            num = num - 1 

        for k in range(len(lst)):
            sum = 0
            for l in range(len(lst)):
                sum = lst[ k ] + lst[ l ]
                
                if sum == temp:
                    print(lst[ k ], lst[ l ])
                    break
                else:
                    continue

    else:
        print('Not An Even Number')
main()