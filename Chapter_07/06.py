# Podunksville fine
import pyinputplus as pip

def main():
    speed_limit= pip.inputNum(prompt='Enter Speed Limit(mph): ', min=1)
    cloaked_speed= pip.inputNum(prompt='\nEnter Speed Achieved(mph): ', min=1)

    if cloaked_speed < speed_limit:
        print('\nYou are JUST Fine') 
    
    else:
        if cloaked_speed >= 90:
            fine= (cloaked_speed - speed_limit)*5+250
            print('\nFine amount:',str(fine) + '$')
        else:
            fine= (cloaked_speed -speed_limit)*5+ 50
            print('\nFine amount:',str(fine) + '$')
main()