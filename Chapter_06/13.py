def toNumbers(lst):
    lstf=[]
    for str in lst:
        for i in range(len(str)):
            vk=ord(str[i])
            lstf.insert(i,vk)
    return lstf


def main():
    lst=[]
    strList=[]
    n=eval(input('Enter total no of string:'))
    for j in range(n):
        strL=input('Enter String')
        lst.insert(j,strL)
    
    strList=toNumbers(lst)
    print(strList)

main()
