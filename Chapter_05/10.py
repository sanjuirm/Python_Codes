# AvgWordCounts.py

def main():
    tmp=input('Enter Text: ')
    intStr=tmp.split()
    total=len(intStr)
    lth=0

    for i in range(total):
        tmp=intStr[i-1]
        length=len(tmp)
        lth=lth+length

    print('Average Words Count is:',lth/total)

main()