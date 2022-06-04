# Calculation of Volume and surface area of a sphere
from numpy import *
radius=eval(input('Enter Radius: '))

vol=(4/3)*pi*power(radius,3)
area=4*pi*power(radius,2)

print('\nVolume of the Sphere is: {0:0.2f}'.format(vol),'\nArea of the Sphere is: {0:0.2f}'.format(area))