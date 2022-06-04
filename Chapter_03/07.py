# program to calculate distance between two points.
from cmath import sqrt
import math                                                  #importing math library for sqaure root

x1,y1=eval(input('Enter two points separated by comma: '))         #simenteneous assignment
x2,y2=eval(input('Enter another two points separated by comma: '))

distance=sqrt((x2-x1)^2+(y2-y1)^2)

print('The distance respectively: ',round(distance,2))