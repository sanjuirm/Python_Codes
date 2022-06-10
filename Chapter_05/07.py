# CaesarCipher.py
from tkinter.tix import InputOnly


def main():
    decoded_Text=input('Enter Your Text: ')
    key=eval(input('Enter Key: '))
    encoded_Text=''

    for ch in decoded_Text:
        tmp=chr(ord(ch)+key)
        encoded_Text=encoded_Text+tmp
    print(encoded_Text)
main() 
