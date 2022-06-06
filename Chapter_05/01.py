# Dateconvert.py
def main():
    dateStr=input('Enter Date(mm/dd/yyyy): ')
    monthStr,datStr,yearStr=dateStr.split('/')

    months=["January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"]

    monthStr=months[int(monthStr)-1]     # turning the str into int first. 

    print('The Month is {0}, The Date is {1}, The Year is {2}'.format(monthStr,datStr,yearStr))

main()