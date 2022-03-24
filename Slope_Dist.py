# program to calculate slope of two point and distace among them 
from cmath import sqrt
import math                                                  #importing math library for sqaure root

x1,y1=eval(input('Enter two points separated by comma: '))         #simenteneous assignment
x2,y2=eval(input('Enter another two points separated by comma: '))

slope=(y2-y1)/(x2-x1)
distance=sqrt((x2-x1)^2+(y2-y1)^2)

print('The slope and distance respectively is: ',slope, distance)