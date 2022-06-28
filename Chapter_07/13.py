from valid import validity
import pyinputplus as pip

def main():
    mnths = ['Jan','Feb','March', 'April', 'May', 'June', 'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    mon_lk= ['March', 'April', 'May', 'June', 'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    date= pip.inputStr(prompt = 'Enter Date(month/day/year): ')
    
    mon,day,yr = date.split('/')

    res = validity(date)

    if res == True:
        if mon in mon_lk:
            if (yr % 4)!= 0:
                dayNum= (31* (mon-1) + day) - (4* (mon) + 23) //10
                print('Day Number is {}'.format(dayNum))
            else:
                dayNum =  ((31* (mon-1) + day) - (4* (mon) + 23) //10) + 1
                print('Day Number is {}'.format(dayNum))
        else:
            dayNum = (31* (mon-1) + day)
            print('Day Number is {}'.format(dayNum))
    else:
        print('Error!!!')

main()