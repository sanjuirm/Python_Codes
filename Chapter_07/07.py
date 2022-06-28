# Babysitter bill
import pyinputplus as pip

def main():
    start_time= pip.inputStr(prompt='\nEnter Starting Time(HH:MM):') # 8:00
    end_time= pip.inputStr(prompt='\nEnter Starting Time(HH:MM):')   # 23:00

    start_hr= start_time[ : 1]
    end_hr= end_time[ : 2]
    start_min= start_time[2 :]
    end_min= end_time[3 : ]
    
    # converting into hours
    st= int(start_hr) +1/(60/ int(start_min))
    et= int(end_hr) +1/(60/ int(end_min))
    
    if et < 21:
        pay= (et - st)*2.50 
        print('\nTotal Pay: ' + '$' + str(round(pay,2)))
    else:
        xtra_time= et - 21
        pay=  ((et - st)- xtra_time) *2.50 + xtra_time*1.75
        print('\nTotal Pay: ' + '$' + str(round(pay,2)))
   
main()