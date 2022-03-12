# script to illustrate how swapping and simultenous assignment works in python 

x,y=eval(input('two nums: '))    # assigning initial values
temp=x                           # intrducing a new variable to store value temporarily
x=y                    
y=temp
print(x,y)                       # printing the new values