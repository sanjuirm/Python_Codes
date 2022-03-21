# python program for calculating the real roots of a quadratic equation
import math                                       #importing math libray

print('python program for calculating the real roots of a quadratic equation')
a=int(input('Coefficient a: '))
b=int(input('Coefficient b: '))
c=int(input('Coefficient c: '))

discRoot=math.sqrt((b*b)-(4*a*c))                      # calculating discontinous root
a1=(-b+discRoot)/(2*a)
a2=(-b-discRoot)/(2*a)

print('The roots are: ',int(a1), int(a2))              # taking output as integer value
