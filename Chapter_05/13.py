def main():
# Total words.
    infile=open('_13_.txt','r')
    wc=0
    wl=0
    for line in infile:
        x=line.split()
        tmp=len(x)
        wc=wc+tmp
    print(wc)    
    
# Average word length calculation.
    infile=open('_13_.txt','r')
    for str in infile:
        x=str.split()
        total=len(x)
        for i in range(total):
            tmp=x[i-1]
            length=len(tmp)
            wl=wl+length
    print('Average word length is:',round(wl/wc,2))

    infile.close()
main()

