# Easter date
import pyinputplus as pip

def main():
    year= pip.inputInt(prompt=' Enter Year: ', greaterThan=1982, lessThan=2099)
    excp= [1954, 1981, 2049, 2076]

    a= year % 19
    b = year % 4
    c = year % 7
    d = (19 * a + 24) % 30
    e = (2 * b + 4 * c + 6 * d + 5) % 7
    
    if year in excp:
        if (d + e) > 9:         
            print('\nEaster Date is April {}'.format((d + e -9)- 7) )  
        else:
            print('\nEaster Date is March {}'.format((22 + d + e)-7))
    
    else:
        if (d + e) > 9:          # it would be in April if more than 9
            print('\nEaster Date is April {}'.format(d + e -9))   
        else:
            print('\nEaster Date is March {}'.format(22 + d + e))

main()
