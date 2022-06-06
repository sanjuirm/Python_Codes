# Numeric(Whole Name) value

def main():
    x=input('Name: ')
    y=x.lower()
    a=0
    
    for ch in y:
        if ch!=' ':
          a=a+(int(ord(ch))-96)
        else:
            continue
    
    print('Total Value:',a)

main()
