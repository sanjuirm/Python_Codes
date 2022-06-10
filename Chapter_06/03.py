import numpy as np

def sphereVolume(radius):
    return ((4/3)*np.pi*np.power(radius,3))

def sphereArea(radius):
    return 4*np.pi*np.power(radius,2)

def main():
    rad=eval(input('Enter radius: '))
    sv=sphereVolume(rad)
    sa=sphereArea(rad)
    print('Volume of the sphere is:',round(sv,2),'\nArea of the sphere is:',round(sa,2))

main()
