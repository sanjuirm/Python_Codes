# Acronym2.py
lst=[]

def acronym(phrase):
    global lst
    a=phrase.split()
    for i in a:
        x=i[0]
        lst.append(x)
    accr=''.join(lst)
    return accr

def main():
    phrase=input('Enter a string:\n ')
    y=acronym(phrase)
    print('The Acronym of the string is:',y.upper())

main()

