# triangle2.py
import numpy as np

def area(a,b,c):
    S=(a+b+c)/2
    area=np.sqrt(S*(S-a)*(S-b)*(S-c))
    return area

def main():
    a,b,c=eval(input('enter length of three sides(separated by comma):'))
    ta=area(a,b,c)
    
    print('the area of the trainmgle is: ',round(ta,2))

main()
