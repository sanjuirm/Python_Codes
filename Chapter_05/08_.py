# CaesarCipher.py(Circular)

def main():
    decoded_Text=input('Enter Your Text: ')
    key=eval(input('Enter Key: '))
    encoded_Text=''

    for ch in decoded_Text:
        if ch!='z' or ch!='Z':
            tmp=chr(ord(ch)+key)
            encoded_Text=encoded_Text+tmp
        if ch=='z':
            tmp1=chr((ord(ch)-25)+(key-1))
            encoded_Text=encoded_Text+tmp1
        if ch=='Z':
            tmp2=chr((ord(ch)-25)+(key-1))
            encoded_Text=encoded_Text+tmp2
                   
    print(encoded_Text)
main() 
