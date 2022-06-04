# Calculation of area of a traingle.
from numpy import *

a,b,c=eval(input('enter length of three sides(separated by comma):'))

S=(a+b+c)/2
area=sqrt(S*(S-a)*(S-b)*(S-c))

print('the area of the trainmgle is: ',round(area,2))
