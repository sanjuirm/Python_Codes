# program to calculate slope of two point 

x1,y1=eval(input('Enter two points separated by comma: '))         
x2,y2=eval(input('Enter another two points separated by comma: '))

slope=(y2-y1)/(x2-x1)

print('The slope is: ',round(slope,2))