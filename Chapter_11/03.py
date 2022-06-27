import pyinputplus as pip

def main():
    n=pip.inputNum(prompt='Enter Marks Obtained\n', min=0, lessThan=100)
    if n>=90 and n<=100:
        print('Grade: A')
        
    elif n>=80 and n<=89:
        print('Grade: B')
       
    elif n>=70 and n<=79:
        print('Grade: C')
        
    elif n>60 and n<=69:
        print('Grade: D')
        
    elif  n<=60:
        print('Grade: F')      
main()
        