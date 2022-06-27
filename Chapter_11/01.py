import pyinputplus as pip

def main():
    rate=pip.inputNum(prompt='Enter Hourly Rate:')
    hours=pip.inputInt(prompt='\nEnter Total Work Hours:')

    if hours > 40:
        overtime= hours- 40
        total_money= (hours* rate)+ (overtime* rate/2)
    else:
        total_money= hours*rate

    print('\nTotal Money: ',total_money)
main()