# Pizza per sq. inch calculaion
from numpy import *

diameter=eval(input('Enter Diameter: '))
Price=eval(input('Enter price of the pizza: '))
radius=diameter/2

area=(22/7)*power(radius,2)
print('\nCost per sqaure inch of the pizza is: {0:0.2f}'.format(Price/area))
