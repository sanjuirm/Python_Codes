# Conversion program.

def main():
    print('This program convert Kms into Miles')
    kms=eval(input('Distance in Kms:'))

    miles=kms*0.621

    print('Distance in miles is:','{0:.3f}'.format(miles))
main()

