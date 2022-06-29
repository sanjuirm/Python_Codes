# Syracuse sequence
import pyinputplus as pip

def seq( x ):
    if x % 2 == 0:
        return x/2
    else:
        return (3 * x) + 1 


def main():
    x = pip.inputInt(prompt= 'Enter a Natural Number: ', min= 1)

    while x > 1:
        temp = seq(x)
        x = temp
        print(temp)
main()
