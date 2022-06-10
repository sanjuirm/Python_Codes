# Numeric value
def main():
    x=input('Name: ')
    y=x.lower()
    a=0
    
    for ch in y:
        a=a+(int(ord(ch))-96)
    
    print('Total Value:',a)

main()
