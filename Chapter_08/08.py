# GCD 
# Euclid's Algorithm

import pyinputplus as pip
def main():
    m = pip.inputInt('Enter A Number: ', min=1)
    n = pip.inputInt('Enter Another Number: ', min=1)

    while True :
        temp = m % n
        m = n 
        n = temp
        
        if m >= 0:
            print(n)
            break
        else: continue
main()
