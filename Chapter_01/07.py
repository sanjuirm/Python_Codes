# A program showing Chaotic bheaviour.

def main():
    print('This program shows Chaotic function.')
    x=eval(input('Enter a number between 0 & 1: ')) 
    y=eval(input('Enter another number between 0 & 1: ')) 

    print('input:',x,y,'\n','----------------')
    for i in range(10):
        x=3.9*x*(1-x)
        y=3.9*y*(1-y)
        print('{0:.6f}'.format(x), '{0:.6f}'.format(y))
    
main()
