def sumList(lst):
    sum=0
    for i in lst:
        sum=sum+i
    return sum

def main():
    lst=[]
    n=eval(input('Enter total nos:'))
    for i in range(n):
        num=eval(input('Enter nos:'))
        lst.insert(i,num)
    
    sumL=sumList(lst)
    print('Sum of the List is:',sumL)