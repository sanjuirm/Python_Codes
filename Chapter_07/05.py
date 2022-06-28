import pyinputplus as pip
import numpy as np

def main():
    weight= pip.inputNum(prompt='Enter Weight(in pounds):', min=1)
    height= pip.inputNum(prompt='\nEnter Height(in inches):', min=1)

    bmi= (weight* 720)/ np.power(height,2)

    if bmi < 19:
        print(round(bmi,2), 'Thin')
    if bmi >=19 and bmi <=25:
        print(round(bmi,2), 'Healthy')
    else:
        print(round(bmi,2), 'Overweight')
main()

        