import numpy as np

def pizzaArea(radius):
    return (22/7)*np.power(radius,2)

def cost_SI(price,area):
    return price/area

def main():
    diameter=eval(input('Enter Diameter: '))
    price=eval(input('Enter price of the pizza: '))
    radius=diameter/2

    pa=pizzaArea(radius)
    psi=cost_SI(price,pa)
    print('\nCost per sqaure inch of the pizza is: {0:0.2f}'.format(psi))

main()
