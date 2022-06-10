# guess2.py
import math as m
j=0

def Guess(x,n):
    sqRt=m.sqrt(x)
    guess_num=x/2
    global j
    for i in range(1,n+1):
        guess_val=(guess_num+(x/guess_num))/2
        j=j+guess_val
    
    return j

def main():
    x=eval(input('Enter no whose sqaure root is to be calcualted:'))
    n=eval(input('Enter no of times for guessing:'))
    
    guess=Guess(x,n)

    print('Final value of guess is:',guess)

main()


