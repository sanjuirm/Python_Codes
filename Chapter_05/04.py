# Acronym.py
def main():
    x=input('Enter a string:\n ')
    b=[ ]
    
    for str in x.split():
        a=str[0].upper()
        b.append(a)
    accr=''.join(b)
    print(accr)

main()
