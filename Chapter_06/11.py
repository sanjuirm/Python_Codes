import numpy as np

def squareEach(lst):
    new_lst=[]
    for i in range(len(lst)):
        y=lst[i]
        a=np.power(y,2)
        new_lst.insert(i,a)
    return new_lst


def main():
    lst=[]
    n=eval(input('Enter total nos:'))
    for i in range(n):
        num=eval(input('Enter nos:'))
        lst.insert(i,num)
    print(lst)
    sq_t=squareEach(lst)
    print(sq_t)

main()
