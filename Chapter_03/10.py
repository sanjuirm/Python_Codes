# Calculation for length of ladder.

from numpy import *

ang=(eval(input('Enter the angle of the ladder against the wall(in degrees): ')))
radians=(pi/180)*ang
height=eval(input('Enter the height of the wall: '))

length=height/sin(radians)

print('The length of the ladder is: ',round(length,2))
