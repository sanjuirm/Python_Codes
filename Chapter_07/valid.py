# Question 12
import pyinputplus as pip

def validity(date):
    months = ['Jan','Feb', 'March', 'April', 'May', 'June', 'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    m1 = ['Jan','March', 'May', 'July', 'Aug', 'Oct', 'Dec']
    m2 = ['April','June','Sep','Nov']

    spt_str = date.split('/')

    if months[int(spt_str[0])-1] in m1:
        if int(spt_str[1]) in range(1,32):
            print('Correct Format')
            return True
        else:
            print('Wrong Format')
            return False
    elif months[int(spt_str[0])-1] in m2:
        if int(spt_str[1]) in range(1,31):
            print('Correct Format')
            return True
        else:
            print('Wrong Format')
            return False
    elif months[int(spt_str[0])-1] == 'Feb':
        if int(spt_str[2]) % 4 == 0:
            if int(spt_str[1]) in range(1,30):
                print('Correct Format')
                return True
            else:
                print('Wrong Format')
                return False
        else:
            if int(spt_str[1]) in range(1,29):
                print('Correct Format')
                return True
            else:
                print('Wrong Format')
                return False

if __name__ == '__main__':
    validity()

def main():
    date= pip.inputStr(prompt = 'Enter Date(month/day/year): ')

    validity(date)

if __name__ == '__main__':
    main()