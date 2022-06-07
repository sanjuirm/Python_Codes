# WC.py

# Total words.
def main():    
    infile=open('_13_.txt','r')
    wc=0
    wl=0
    for line in infile:
        x=line.split()
        tmp=len(x)
        wc=wc+tmp
    print(wc)    

# Total Lines.
    infile=open('_13_.txt','r')
    count=0
    for line in infile.readlines():
        count=count+1
    print(count)
    
# Total character count.
    infile=open('_13_.txt','r')
    myline=infile.read()
    cnt=0
    for i in myline:
        cnt=cnt+1
    
    print('Total Available Word is:',wc)
    print('Total Line is:',count)
    print('Total Character present is:',cnt)

    infile.close()
main()

